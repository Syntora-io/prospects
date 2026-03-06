# Voice Agent RAG Architecture -- Helping Hands Cleaning

**Date:** 2026-03-02
**Status:** Draft plan (pre-build)
**Reference:** Open Decision RAG patterns (Supabase + pgvector + versioned embeddings)

---

## Why RAG for a Voice Agent

The system prompt approach hits a ceiling fast. Once Gosia sends the sales script, pricing matrix, service descriptions for 8+ types, 33 city details, objection handling playbooks, and FAQ content, you're looking at 10K+ tokens crammed into every LLM call. That burns money, slows TTFT, and makes updates require code changes.

RAG retrieves only what's relevant to the current caller turn. Caller asks about deep cleaning pricing in Naperville -- pull the deep cleaning price range and Naperville service details. Nothing else.

---

## Architecture (Adapted from Open Decision)

```
INGESTION (one-time + updates)
  Sales script, pricing, FAQs, service descriptions, city info
    -> Chunker (500 tokens, 50 overlap, paragraph-aware splits)
    -> Gemini embedding-001 (768 dims, RETRIEVAL_DOCUMENT task type)
    -> Supabase pgvector (HNSW indexed)
    -> Redis embedding cache (7-day TTL, SHA256 keys)

RUNTIME (per caller turn)
  Caller says: "How much does deep cleaning cost for a 2000 sq ft house?"
    -> Embed query (RETRIEVAL_QUERY task type, check Redis cache first)
    -> Hybrid search: pgvector cosine + full-text keyword (70/30 weight)
    -> Top 3-5 chunks returned (~1500 tokens of context)
    -> Inject into LLM prompt alongside system prompt + conversation history
    -> Claude Sonnet/Haiku generates response
    -> Stream tokens to ConversationRelay -> ElevenLabs TTS -> caller hears answer

SESSION CONTEXT CACHE
  First retrieval for "deep cleaning" topic cached in memory for call duration
    -> Follow-up questions on same topic skip the vector search
    -> New topic triggers fresh retrieval
    -> Cache cleared when WebSocket closes
```

---

## Stack (Mirrors Open Decision Patterns)

| Layer | OD Uses | Voice Agent Uses | Notes |
|-------|---------|-----------------|-------|
| Vector DB | Supabase pgvector | Supabase pgvector | Same project or dedicated |
| Embeddings | gemini-embedding-001 (768d) | gemini-embedding-001 (768d) | Same model, same cache strategy |
| Embedding cache | Redis (7-day TTL, SHA256 keys) | Redis (7-day TTL) | Critical for latency on repeated queries |
| Index | HNSW (cosine) | HNSW (cosine) | m=32, ef_construction=80 for knowledge base |
| Search | Hybrid (vector 70% + keyword 30%) | Hybrid (vector 70% + keyword 30%) | RPC function in Supabase |
| Chunking | 500 tokens, 50 overlap | 500 tokens, 50 overlap | Paragraph -> sentence -> line splits |
| LLM | Gemini 2.5 Flash | Claude Haiku (latency) / Sonnet (quality) | Via LiteLLM for provider flexibility |
| Server | Express (TypeScript) | FastAPI (Python) | Same DI patterns, different language |
| Versioning | embedding_v1_value columns | embedding_v1_value columns | Future-proof model migrations |

---

## Database Schema

### New Supabase project or existing Syntora project -- TBD.

```sql
-- Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- Knowledge base documents (sales script, pricing sheet, FAQ, etc.)
CREATE TABLE voice_documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID NOT NULL,              -- multi-tenant from day one
  title TEXT NOT NULL,
  doc_type TEXT NOT NULL,               -- 'sales_script', 'pricing', 'faq', 'service_desc', 'city_info'
  source_text TEXT,                     -- original full text
  metadata JSONB DEFAULT '{}',          -- flexible: city, service_type, version, etc.
  status TEXT DEFAULT 'pending',        -- 'pending', 'processing', 'completed', 'failed'
  chunk_count INTEGER DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Chunked content with embeddings
CREATE TABLE voice_document_chunks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  document_id UUID NOT NULL REFERENCES voice_documents(id) ON DELETE CASCADE,
  chunk_index INTEGER NOT NULL,
  content TEXT NOT NULL,
  token_count INTEGER,
  start_char INTEGER,
  end_char INTEGER,
  embedding_v1_value vector(768),
  embedding_v1_updated_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- HNSW index for fast approximate nearest neighbor
CREATE INDEX idx_voice_chunks_embedding_v1
  ON voice_document_chunks
  USING hnsw (embedding_v1_value vector_cosine_ops)
  WITH (m = 32, ef_construction = 80);

-- Full-text search index for hybrid search
CREATE INDEX idx_voice_chunks_fts
  ON voice_document_chunks
  USING gin (to_tsvector('english', content));

-- Call logs with transcripts
CREATE TABLE voice_calls (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID NOT NULL,
  call_sid TEXT UNIQUE,                 -- Twilio CallSid
  caller_phone TEXT,
  caller_name TEXT,
  started_at TIMESTAMPTZ DEFAULT now(),
  ended_at TIMESTAMPTZ,
  duration_seconds INTEGER,
  recording_url TEXT,
  transcript JSONB,                     -- [{role, content, timestamp}]
  extracted_data JSONB,                 -- {name, phone, email, service_type, sq_ft, etc.}
  ghl_contact_id TEXT,                  -- after sync to GoHighLevel
  transfer_reason TEXT,
  status TEXT DEFAULT 'active'          -- 'active', 'completed', 'transferred', 'failed'
);
```

---

## Hybrid Search RPC (from OD pattern)

```sql
CREATE OR REPLACE FUNCTION search_voice_knowledge(
  query_embedding vector(768),
  query_text TEXT DEFAULT NULL,
  client_filter UUID DEFAULT NULL,
  doc_type_filter TEXT DEFAULT NULL,    -- 'pricing', 'faq', 'sales_script', etc.
  match_threshold DOUBLE PRECISION DEFAULT 0.5,
  match_count INTEGER DEFAULT 5,
  vector_weight DOUBLE PRECISION DEFAULT 0.7,
  keyword_weight DOUBLE PRECISION DEFAULT 0.3
)
RETURNS TABLE (
  chunk_id UUID,
  document_id UUID,
  document_title TEXT,
  doc_type TEXT,
  content TEXT,
  chunk_index INTEGER,
  vector_similarity DOUBLE PRECISION,
  keyword_rank DOUBLE PRECISION,
  combined_score DOUBLE PRECISION,
  metadata JSONB
)
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = 'public', 'extensions'
AS $$
BEGIN
  SET LOCAL hnsw.ef_search = 100;

  RETURN QUERY
  SELECT
    vc.id AS chunk_id,
    vd.id AS document_id,
    vd.title AS document_title,
    vd.doc_type,
    vc.content,
    vc.chunk_index,
    (1 - (vc.embedding_v1_value <=> query_embedding)) AS vector_similarity,
    CASE
      WHEN query_text IS NOT NULL THEN
        ts_rank(to_tsvector('english', vc.content), plainto_tsquery('english', query_text))::DOUBLE PRECISION
      ELSE 0.0
    END AS keyword_rank,
    (
      (1 - (vc.embedding_v1_value <=> query_embedding)) * vector_weight
      + CASE
          WHEN query_text IS NOT NULL THEN
            ts_rank(to_tsvector('english', vc.content), plainto_tsquery('english', query_text))::DOUBLE PRECISION * keyword_weight
          ELSE 0.0
        END
    ) AS combined_score,
    vd.metadata
  FROM voice_document_chunks vc
  JOIN voice_documents vd ON vc.document_id = vd.id
  WHERE vc.embedding_v1_value IS NOT NULL
    AND (client_filter IS NULL OR vd.client_id = client_filter)
    AND (doc_type_filter IS NULL OR vd.doc_type = doc_type_filter)
    AND (1 - (vc.embedding_v1_value <=> query_embedding)) > match_threshold
  ORDER BY combined_score DESC
  LIMIT match_count;
END;
$$;
```

---

## Knowledge Base Structure

What gets ingested, how it's typed, and what metadata rides along.

| Doc Type | Source | Chunks Expected | Metadata |
|----------|--------|----------------|----------|
| `sales_script` | Gosia's SOP (blocker) | 10-20 | stage: greeting/qualifying/quoting/closing/objection |
| `pricing` | Rate card by sq ft + type (blocker) | 5-10 | service_type, size_range |
| `service_desc` | 8 service type descriptions | 8-16 | service_type |
| `city_info` | 33 cities with details | 33-66 | city, county, zip_codes |
| `faq` | Common caller questions | 15-30 | category |
| `policy` | Cancellation, guarantee, pets, eco | 5-10 | policy_type |
| `hours` | Business hours, holidays | 1-2 | -- |

**Total estimated chunks:** ~80-160
**Total estimated tokens:** ~40K-80K stored, but only ~1,500 retrieved per turn.

---

## Retrieval Strategy

### Per-Turn Flow

```python
async def retrieve_context(
    query: str,
    conversation_history: list[dict],
    session_cache: dict,
    client_id: str,
) -> str:
    """Retrieve relevant knowledge for the current caller turn."""

    # 1. Check session cache -- same topic, skip vector search
    cache_key = extract_topic_key(query)  # simple keyword extraction
    if cache_key in session_cache:
        return session_cache[cache_key]

    # 2. Embed the query (Redis cache hit = ~1ms, miss = ~50ms)
    query_embedding = await embed(query, task_type="RETRIEVAL_QUERY")

    # 3. Hybrid search via Supabase RPC
    chunks = await supabase.rpc("search_voice_knowledge", {
        "query_embedding": query_embedding,
        "query_text": query,
        "client_filter": client_id,
        "match_threshold": 0.5,
        "match_count": 5,
        "vector_weight": 0.7,
        "keyword_weight": 0.3,
    })

    # 4. Format context block
    context = format_chunks(chunks)

    # 5. Cache for this call session
    session_cache[cache_key] = context

    return context
```

### Context Injection

```python
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "system", "content": f"RELEVANT KNOWLEDGE:\n{retrieved_context}"},
    *conversation_history,
    {"role": "user", "content": caller_transcript},
]
```

The system prompt stays lean (~500 tokens): personality, rules, business hours, service area list. The retrieved context adds only what's relevant to this turn (~500-1500 tokens). Conversation history provides continuity.

---

## Latency Impact

| Stage | Without RAG | With RAG | Delta |
|-------|-------------|----------|-------|
| Query embedding | 0ms | ~5ms (cache hit) / ~50ms (miss) | +5-50ms |
| Vector search | 0ms | ~10-30ms (pgvector HNSW) | +10-30ms |
| Context in prompt | Baseline | +500-1500 tokens | +20-40ms TTFT |
| **Total added** | -- | -- | **+35-120ms** |

On a 600ms budget, RAG adds 35-120ms. Still under 800ms which feels natural on a phone call. The session cache eliminates the retrieval cost on follow-up turns about the same topic.

**Optimization levers:**
- Redis embedding cache: turns 50ms embedding into 5ms lookup
- Session-level context cache: zero retrieval cost on follow-ups
- HNSW ef_search tuning: trade recall for speed if needed
- Pre-warm embeddings: embed common queries at startup
- Supabase connection pooling: avoid cold connection overhead

---

## Python Server Structure (Updated with RAG)

```
voice-agent/
  server.py                <- FastAPI app (TwiML + WebSocket + action handlers)
  llm.py                   <- LLM streaming with tool_use (LiteLLM)
  rag.py                   <- Retrieval pipeline (embed, search, format, cache)
  tools.py                 <- Tool implementations (pricing, GHL, transfer)
  prompts.py               <- System prompt (lean) + context formatting
  chunker.py               <- Document chunking (500 tokens, 50 overlap)
  embeddings.py            <- Gemini embedding client + Redis cache
  ingest.py                <- CLI: load documents into Supabase (chunk + embed + store)
  config.py                <- Environment config (Twilio, LLM, Supabase, Redis)
  knowledge/
    sales-script.txt       <- Gosia's sales script (when she sends it)
    pricing-matrix.json    <- Pricing by sq ft + service type
    service-areas.json     <- 33 cities with zip codes
    services.json          <- 8 service type descriptions
    faq.txt                <- Common questions and answers
    policies.txt           <- Cancellation, guarantee, pets, eco
  requirements.txt
  fly.toml                 <- Fly.io deployment config
  .env.example
```

**New dependencies:**
```
supabase                   # Supabase Python client
google-genai               # Gemini embeddings
redis[hiredis]             # Embedding cache
tiktoken                   # Token counting (or approximation)
```

---

## Ingestion Pipeline

```python
# ingest.py -- run once, then again when Gosia sends updates

async def ingest_document(file_path: str, doc_type: str, metadata: dict):
    """Chunk a knowledge file and store embeddings in Supabase."""

    # 1. Read source text
    text = Path(file_path).read_text()

    # 2. Create document record
    doc = await supabase.table("voice_documents").insert({
        "client_id": CLIENT_ID,
        "title": Path(file_path).stem,
        "doc_type": doc_type,
        "source_text": text,
        "metadata": metadata,
        "status": "processing",
    }).execute()

    # 3. Chunk (500 tokens, 50 overlap, paragraph-aware)
    chunks = chunk_text(text, max_tokens=500, overlap=50)

    # 4. Embed all chunks (batch, with Redis cache)
    embeddings = await batch_embed(
        [c.content for c in chunks],
        task_type="RETRIEVAL_DOCUMENT",
    )

    # 5. Store chunks with embeddings
    rows = [
        {
            "document_id": doc.data[0]["id"],
            "chunk_index": i,
            "content": c.content,
            "token_count": c.token_count,
            "start_char": c.start_char,
            "end_char": c.end_char,
            "embedding_v1_value": emb,
        }
        for i, (c, emb) in enumerate(zip(chunks, embeddings))
    ]
    await supabase.table("voice_document_chunks").insert(rows).execute()

    # 6. Update document status
    await supabase.table("voice_documents").update({
        "status": "completed",
        "chunk_count": len(chunks),
    }).eq("id", doc.data[0]["id"]).execute()
```

**CLI usage:**
```bash
python ingest.py --file knowledge/sales-script.txt --type sales_script --meta '{"version": "1.0"}'
python ingest.py --file knowledge/pricing-matrix.json --type pricing --meta '{"source": "gosia"}'
python ingest.py --dir knowledge/ --auto  # infer types from filenames
```

---

## Multi-Tenant Design

Built for Helping Hands first, reusable for every future Syntora voice agent client.

- `client_id` on every table scopes data per client
- Same Supabase project, same pgvector indexes, different client_id filter
- Onboarding a new client: upload their docs via `ingest.py`, set their client_id in config
- No code changes per client -- knowledge base is the differentiator

---

## Embedding Versioning (from OD)

Column naming: `embedding_v1_value`, `embedding_v1_updated_at`

When Gemini ships a better model or we switch to a different provider:
1. Add `embedding_v2_value` column
2. Dual-write during migration
3. Backfill existing chunks
4. Flip search RPC to v2
5. Drop v1 column

No downtime, no re-architecture. Same pattern OD uses.

---

## What Changes in the Existing Design

| Component | Before (system prompt only) | After (RAG) |
|-----------|---------------------------|-------------|
| System prompt | ~2000+ tokens (everything) | ~500 tokens (personality + rules only) |
| Pricing lookup | `check_pricing` tool with hardcoded JSON | Retrieved from vector store, tool still validates |
| Sales script | Crammed into prompt | Retrieved by conversation stage |
| City info | Listed in prompt | Retrieved when caller mentions location |
| FAQ | Not included (too long) | Retrieved by question similarity |
| Knowledge updates | Redeploy server | Run `ingest.py`, no restart |
| New client onboard | Rewrite prompt | Upload their docs, set client_id |
| Token cost per call | High (fat prompt every turn) | Low (lean prompt + targeted retrieval) |

---

## Blockers

Same as before, plus:
1. **Gosia's sales script + SOP** -- primary knowledge base content
2. **Gosia's pricing breakdown** -- pricing knowledge base
3. **Supabase project decision** -- new project or use existing Syntora project?
4. **Redis hosting** -- Fly.io Redis add-on, Upstash, or Railway?

---

## Open Questions

1. **Supabase project:** Dedicated project per client, or shared Syntora project with client_id isolation? Shared is simpler now, dedicated is cleaner long-term.
2. **Embedding model:** Gemini embedding-001 (free tier, 768d) or OpenAI text-embedding-3-small (1536d, $0.02/1M tokens)? Gemini matches OD. Cost is negligible at this scale.
3. **Pre-warming:** Should we embed the 50 most common cleaning questions at startup and cache them? Eliminates embedding latency for predictable queries.
4. **Conversation-aware retrieval:** Should we use the full conversation history (not just last turn) to build the retrieval query? Better context but more tokens to embed.
5. **Tool calls + RAG:** Keep `check_pricing` as a tool call that validates against retrieved pricing context, or replace it with pure RAG retrieval? Tool call gives structured output; RAG gives natural language. Probably both.

---

*Adapted from Open Decision RAG patterns. Reference: voice-agent-technical-design.md, voice-agent-comparison.md*
