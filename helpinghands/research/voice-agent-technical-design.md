# Voice Agent Technical Design -- Helping Hands Cleaning

**Date:** 2026-03-02
**Stack:** Twilio ConversationRelay + FastAPI + Claude tool_use + ElevenLabs TTS
**Status:** Design (pre-build)
**RAG Architecture:** See voice-agent-rag-architecture.md (Supabase pgvector, hybrid search, adapted from OD patterns)

---

## Architecture

```
Caller -> GHL Phone System
  -> Business hours: ring office, overflow to AI after 15s
  -> After hours: forward to Twilio number

Twilio Number -> TwiML webhook (POST /twiml)
  -> <Start><Recording />
  -> <Connect><ConversationRelay url="wss://server/ws" />

ConversationRelay (Twilio-managed):
  STT: Deepgram Nova-3 (transcribes caller speech to text)
  TTS: ElevenLabs Flash v2.5 (converts agent text to speech)

Your Python WebSocket Server (FastAPI):
  Receives: transcribed text from caller
  Sends: text responses (streamed token-by-token)
  LLM: Claude Sonnet via LiteLLM (tool_use for mid-call actions)
  Tools: check_pricing, create_ghl_contact, check_availability, transfer_call
  RAG: Supabase pgvector hybrid search -> relevant knowledge chunks
  Knowledge: sales script, pricing matrix, service descriptions (chunked + embedded)

Post-Call:
  WebSocket closes -> save transcript + extracted data
  -> Webhook to n8n/Make -> GHL contact creation
  -> Morning summary email to Gosia's team
```

---

## Cost Breakdown

| Component | Cost | Notes |
|-----------|------|-------|
| Twilio inbound voice | $0.0085/min | Standard US local |
| ConversationRelay | $0.07/min | Includes STT (Deepgram) + TTS (ElevenLabs) |
| LLM (Claude Haiku) | ~$0.003-0.008/min | Cheapest for structured flows |
| Twilio phone number | $1.00/mo | US local |
| **Total per minute** | **~$0.08-0.09** | |
| **Monthly (2,700 min)** | **~$216-243** | 30 calls/day x 3 min avg |

Compare: human answering service = $1-2/min = $2,700-5,400/mo.

---

## ConversationRelay TwiML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Recording
      recordingStatusCallback="https://server/recording-status"
      recordingStatusCallbackEvent="completed"
    />
  </Start>
  <Connect action="https://server/action">
    <ConversationRelay
      url="wss://server/ws"
      welcomeGreeting="Hi, thanks for calling Helping Hands Cleaning Services.
        How can I help you today?"
      ttsProvider="ElevenLabs"
      voice="[VOICE_ID]-flash_v2_5-1.1_0.7_0.8"
      elevenlabsTextNormalization="on"
      transcriptionProvider="Deepgram"
      speechModel="nova-3-general"
      language="en-US"
      interruptible="speech"
      interruptSensitivity="medium"
      dtmfDetection="true"
      hints="Helping Hands,Elmhurst,Naperville,DuPage,MaidCentral,Gosia"
    >
      <Language code="en-US" voice="[ENGLISH_VOICE_ID]" />
      <Language code="pl" voice="[POLISH_VOICE_ID]" />
    </ConversationRelay>
  </Connect>
</Response>
```

**Voice config format:** `[VoiceID]-[Model]-[Speed]_[Stability]_[Similarity]`
- Speed 1.1: slightly faster for phone (Twilio recommends 1.2, 1.1 is safer)
- Stability 0.7: natural variation without being too dramatic
- Similarity 0.8: close to original voice character

**ElevenLabs text normalization ON:** auto-converts "$150" to "one hundred fifty dollars", dates, etc. Adds slight latency but worth it for a cleaning quote agent.

---

## WebSocket Message Protocol

### Incoming (Twilio -> Server)

| Type | When | Key Fields |
|------|------|------------|
| `setup` | Call connects | `callSid`, `from`, `to`, `callerName`, `customParameters` |
| `prompt` | Caller finishes speaking | `voicePrompt` (transcribed text), `lang` |
| `interrupt` | Caller interrupts agent | `utteranceUntilInterrupt`, `durationUntilInterruptMs` |
| `dtmf` | Caller presses key | `digit` |
| `error` | Something broke | `description` |

### Outgoing (Server -> Twilio)

| Type | When | Key Fields |
|------|------|------------|
| `text` | Agent response | `token`, `last` (bool), `lang` (optional) |
| `play` | Play audio file | `source` (URL), `loop`, `preemptible` |
| `end` | End session | `handoffData` (JSON string for transfer context) |
| `language` | Switch language | `ttsLanguage`, `transcriptionLanguage` |

### Streaming Pattern

```python
# Stream LLM tokens directly to ConversationRelay
async for token in llm_stream:
    await ws.send_json({"type": "text", "token": token, "last": False})
await ws.send_json({"type": "text", "token": "", "last": True})
```

ConversationRelay batches tokens internally and starts TTS as soon as it has enough text. No sentence-level buffering needed on our side.

---

## System Prompt (Draft)

```
You are the after-hours phone assistant for Helping Hands Cleaning Services,
a residential cleaning company based in Elmhurst, Illinois serving 33+ cities
across DuPage, Cook, and Kane counties.

PERSONALITY:
- Warm, professional, helpful
- You are not a robot -- speak naturally
- Use the caller's name once you have it
- If the caller speaks Polish, respond in Polish

YOUR JOB:
1. Greet the caller and find out what they need
2. Collect their information (name, phone, email, address)
3. Determine the service they need (standard cleaning, deep cleaning,
   move-in/move-out, post-construction, recurring)
4. Collect property details (square footage or bedrooms/bathrooms/floors)
5. Ask about pets and any special requests
6. Provide a rough price range using the pricing tool
7. Offer to schedule a callback from the team in the morning
8. If the caller has an urgent request or complex situation, transfer to
   the owner

RULES:
- NEVER make up pricing. Always use the check_pricing tool.
- NEVER guarantee exact pricing. Say "based on what you have described,
  the typical range is..." and explain final pricing depends on a walkthrough.
- If you do not know something, say "I will make sure the team gets back
  to you on that first thing in the morning."
- Spell out numbers when speaking (say "one hundred fifty" not "150")
- Do not use markdown, bullet points, or emojis in your responses
- Keep responses concise -- this is a phone call, not an email
- If the caller asks about commercial cleaning, let them know Helping Hands
  also has a commercial division and you will have someone reach out

BUSINESS HOURS:
Monday through Friday: 8 AM to 5 PM
Saturday: 10 AM to 3 PM
Sunday: Closed

You are answering because the office is currently closed. The team will
follow up first thing the next business day.

SERVICE AREA (33+ cities):
Elmhurst (HQ), Naperville, Glen Ellyn, Wheaton, Lombard, Hinsdale,
Downers Grove, Oak Park, La Grange, Western Springs, Clarendon Hills,
Villa Park, Addison, Bensenville, Wood Dale, Itasca, Roselle, Bloomingdale,
Glendale Heights, Carol Stream, Winfield, West Chicago, Warrenville,
Lisle, Woodridge, Darien, Willowbrook, Burr Ridge, Countryside,
Brookfield, Riverside, Forest Park, Oak Brook
```

---

## LLM Tools

### check_pricing

```python
{
    "name": "check_pricing",
    "description": "Look up estimated pricing for a cleaning service based on
        property size and service type",
    "parameters": {
        "type": "object",
        "properties": {
            "service_type": {
                "type": "string",
                "enum": ["standard", "deep_clean", "move_in_out",
                         "post_construction", "recurring_weekly",
                         "recurring_biweekly", "recurring_monthly"]
            },
            "square_footage": {
                "type": "integer",
                "description": "Property size in square feet"
            },
            "bedrooms": {
                "type": "integer",
                "description": "Number of bedrooms (fallback if sq ft unknown)"
            },
            "bathrooms": {
                "type": "integer",
                "description": "Number of bathrooms"
            }
        },
        "required": ["service_type"]
    }
}
```

Implementation: RAG retrieves relevant pricing chunks from Supabase pgvector, then tool validates and returns a structured price range. Not an exact quote.

### create_ghl_contact

```python
{
    "name": "save_caller_info",
    "description": "Save the caller's information for morning follow-up.
        Call this once you have collected name, phone, and service interest.",
    "parameters": {
        "type": "object",
        "properties": {
            "first_name": {"type": "string"},
            "last_name": {"type": "string"},
            "phone": {"type": "string"},
            "email": {"type": "string"},
            "address": {"type": "string"},
            "service_type": {"type": "string"},
            "square_footage": {"type": "integer"},
            "bedrooms": {"type": "integer"},
            "bathrooms": {"type": "integer"},
            "has_pets": {"type": "boolean"},
            "preferred_callback_time": {"type": "string"},
            "notes": {"type": "string"}
        },
        "required": ["first_name", "phone"]
    }
}
```

Implementation: POST to GHL API (or webhook to n8n -> GHL) to create contact + opportunity in pipeline.

### transfer_call

```python
{
    "name": "transfer_call",
    "description": "Transfer the caller to a live person. Use only if the
        caller has an urgent situation or explicitly requests to speak
        with someone.",
    "parameters": {
        "type": "object",
        "properties": {
            "reason": {"type": "string"},
            "destination": {
                "type": "string",
                "enum": ["owner", "emergency"]
            }
        },
        "required": ["reason", "destination"]
    }
}
```

Implementation: sends `type: end` message with handoffData. Action URL handles the `<Dial>` to Gosia's cell.

---

## Python Server Structure

```
voice-agent/
  server.py              <- FastAPI app (TwiML + WebSocket + action handlers)
  llm.py                 <- LLM streaming with tool_use (LiteLLM)
  rag.py                 <- Retrieval pipeline (embed, search, format, session cache)
  tools.py               <- Tool implementations (pricing, GHL, transfer)
  prompts.py             <- System prompt (lean ~500 tokens) + context formatting
  chunker.py             <- Document chunking (500 tokens, 50 overlap)
  embeddings.py          <- Gemini embedding client + Redis cache
  ingest.py              <- CLI: load documents into Supabase (chunk + embed + store)
  config.py              <- Environment config (Twilio, LLM, Supabase, Redis, GHL)
  knowledge/
    sales-script.txt     <- Gosia's sales script (when she sends it)
    pricing-matrix.json  <- Pricing by sq ft + service type
    service-areas.json   <- 33 cities with zip codes
    services.json        <- 8 service type descriptions
    faq.txt              <- Common questions and answers
    policies.txt         <- Cancellation, guarantee, pets, eco
  requirements.txt
  fly.toml               <- Fly.io deployment config
  .env.example
```

**Dependencies:**
```
fastapi
uvicorn[standard]
litellm
python-dotenv
httpx
supabase
google-genai
redis[hiredis]
```

---

## Call Transfer Flow

```python
# In tools.py
async def handle_transfer(ws, call_summary, destination):
    """End ConversationRelay session and pass to action URL for transfer."""
    await ws.send_json({
        "type": "text",
        "token": "Let me connect you with someone right now. One moment please.",
        "last": True
    })
    await ws.send_json({
        "type": "end",
        "handoffData": json.dumps({
            "reasonCode": "live-agent-handoff",
            "destination": destination,
            "callSummary": call_summary
        })
    })

# In server.py -- action URL handler
@app.post("/action")
async def action(request: Request):
    form = await request.form()
    handoff = form.get("HandoffData")
    if handoff:
        data = json.loads(handoff)
        if data.get("reasonCode") == "live-agent-handoff":
            phone = TRANSFER_NUMBERS[data["destination"]]
            xml = f"""<?xml version="1.0" encoding="UTF-8"?>
            <Response>
              <Say>Connecting you now.</Say>
              <Dial>{phone}</Dial>
            </Response>"""
            return Response(content=xml, media_type="text/xml")

    # Unexpected disconnect -- reconnect
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <Response>
      <Say>Sorry about that interruption.</Say>
      <Connect action="https://{DOMAIN}/action">
        <ConversationRelay url="{WS_URL}"
          welcomeGreeting="I am back. How can I continue helping you?" />
      </Connect>
    </Response>"""
    return Response(content=xml, media_type="text/xml")
```

---

## After-Hours Routing

GHL handles the time-based routing. No custom code needed for this part.

**GHL IVR Workflow:**
1. Inbound call to GHL LC Phone number
2. If/Else branch: check current time against business hours
3. Business hours path: ring office phone for 15 seconds
   - If no answer: forward to Twilio number (AI takes over)
4. After hours path: forward immediately to Twilio number

**Business hours:**
- Mon-Fri: 8:00 AM - 5:00 PM CT
- Saturday: 10:00 AM - 3:00 PM CT
- Sunday: closed (all calls to AI)
- Holidays: all calls to AI (manually toggle in GHL)

---

## Latency Budget

| Stage | Expected (ms) | Notes |
|-------|--------------|-------|
| Caller speech -> Twilio edge | ~40 | Network |
| Deepgram STT | ~150-350 | Nova-3 |
| WebSocket to server | ~10-20 | If colocated in us-east |
| LLM time-to-first-token | ~200-400 | Claude Haiku / GPT-4o-mini |
| Token streaming back | ~10-20 | WebSocket |
| ElevenLabs TTS first byte | ~75-100 | Flash v2.5 |
| **Total mouth-to-ear** | **~500-900ms** | p50 target: ~600ms |

Human conversation turn gap: 300-500ms. Under 800ms feels natural on a phone call.

**Optimization levers:**
- Use Claude Haiku or GPT-4o-mini (not Sonnet) for fastest TTFT
- Deploy server in us-east-1 (same region as Twilio media edge)
- Stream tokens (do not wait for full response)
- Set ElevenLabs text normalization to ON (avoids "$150" pronunciation issues)

---

## Voice Cloning Caveat

ConversationRelay uses Twilio-provisioned ElevenLabs capacity. No ElevenLabs API key required. This means:
- 1,000+ pre-built ElevenLabs voices available
- Custom/cloned voices are NOT confirmed to work through ConversationRelay
- If Gosia wants her voice cloned for the agent, we may need ElevenLabs' own Conversational AI product (import Twilio number into ElevenLabs instead)

**Recommendation:** Start with a pre-built voice. If Gosia wants cloning, evaluate ElevenLabs Conversational AI as an alternative to ConversationRelay. The server-side code (LLM + tools) is reusable either way.

---

## Multilingual (Polish)

ConversationRelay supports automatic language detection:

1. Set `transcriptionProvider="Deepgram"` + `speechModel="nova-3-general"`
2. Add `<Language code="pl" voice="[POLISH_VOICE_ID]" />` in TwiML
3. Deepgram returns detected language in `prompt` message (`"lang": "pl"`)
4. System prompt tells the LLM: "If the caller speaks Polish, respond in Polish"
5. ElevenLabs Flash v2.5 auto-detects language from text and renders Polish TTS

No code changes needed beyond the TwiML config and system prompt instruction.

---

## What We Need From Gosia (Blockers)

1. **Sales script + SOP** -- becomes the system prompt and knowledge base
2. **Pricing breakdown** -- becomes the pricing matrix for `check_pricing` tool
3. **Phone system confirmation** -- need to know if GHL LC Phone or external provider to set up forwarding
4. **Transfer number** -- who does the AI transfer to for urgent calls? Gosia's cell?
5. **Service type list** -- exact services and what each includes (for the enum in tools)

---

## Deployment Plan

1. **Local dev:** ngrok for wss:// tunnel, test with Twilio trial number
2. **Staging:** Fly.io (free tier with credit card), test number
3. **Production:** Fly.io or DO App Platform, production Twilio number, GHL forwarding configured

**Timeline estimate:** MVP in 1-2 weeks once we have Gosia's sales script and pricing data.

---

## Open Questions

1. Voice cloning: does Gosia want a cloned voice? If so, ConversationRelay may not support it -- need ElevenLabs direct.
2. Voicemail: if caller wants to leave a voicemail instead of talking to AI, how do we handle?
3. Spanish: any Spanish-speaking callers in the service area?
4. Existing phone number: does the current business number stay, or do we add a new one?
5. Call recording consent: Illinois is a two-party consent state. The greeting must disclose recording.

---

*Research sources: voice-agent-comparison.md, Twilio ConversationRelay docs, ElevenLabs docs, GHL help center*
