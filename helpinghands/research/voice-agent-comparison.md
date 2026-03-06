# Voice Agent Platform Comparison -- Helping Hands Cleaning

**Date:** 2026-03-02
**Use case:** After-hours inbound phone agent for residential cleaning sales
**Requirements:** Collect lead info, provide rough quotes, book callbacks, warm transfer if needed, push data to GoHighLevel, Polish language support (bonus)

---

## Platform Summary

| Platform | Type | All-In Cost/Min | Monthly Min | GHL Integration | After-Hours Routing | Polish | Voice Cloning | Latency |
|----------|------|----------------|-------------|-----------------|-------------------|--------|--------------|---------|
| **GHL Native** | Built-in | ~$0.08-0.10 | $0 (or $97 unlimited inbound) | Native | Native (IVR workflows) | Unknown | No | Unknown |
| **ElevenLabs** | End-to-end | ~$0.10 | $99 (1,100 min) | Webhook/Make | External (Twilio routing) | Yes (auto-detect) | Yes (Professional) | Sub-1s |
| **Retell AI** | End-to-end | ~$0.13-0.20 | $0 (pay-as-you-go) | Webhook/Make | Native (dashboard toggle) | Via ElevenLabs | Via ElevenLabs | ~600ms |
| **Vapi** | Orchestrator | ~$0.13-0.31 | $0 (pay-as-you-go) | Native (4 GHL tools) | External (GHL/Make) | Yes | Via providers | ~550-800ms |
| **Bland AI** | Full-stack | ~$0.11-0.14 | $0 (Start) / $299 (Build) | Webhook/Zapier | Pathway conditions | Unknown | Yes (single MP3) | ~800ms |
| **Twilio Custom** | DIY | ~$0.08-0.09 | $0 | Custom webhook | Custom code (trivial) | Via providers | Via ElevenLabs | p50: 491ms |

---

## Cost Estimates (Helping Hands Volume)

Assuming 30 after-hours calls/day, 3 min avg = ~2,700 min/month.

| Platform | Monthly Cost | Notes |
|----------|-------------|-------|
| **GHL Native** | ~$97 (unlimited inbound) | Cheapest if unlimited plan. $0.06/min + tokens if pay-per-use (~$216) |
| **ElevenLabs Pro** | ~$105 | $99/mo (1,100 min) + ~$6 Twilio. Would need Scale at $330 for 2,700 min |
| **Retell AI** | ~$352-540 | Pay-as-you-go, no monthly |
| **Vapi** | ~$351-837 | Varies heavily by provider stack chosen |
| **Bland AI** | ~$297-378 | Start plan ($0.14/min) or Build ($299 + $0.12/min) |
| **Twilio Custom** | ~$216-243 | ConversationRelay at ~$0.08-0.09/min |

---

## Platform Deep Dives

### 1. GHL Native Voice AI

**The surprise contender.** GHL shipped native voice AI in 2025. Since Helping Hands already uses GHL, this is the zero-integration option.

**Pros:**
- Native CRM sync -- contacts, appointments, pipelines, workflows, all automatic
- After-hours routing built into IVR workflows (time-based branching)
- Call recording, transcription, and post-call workflows native
- $97/mo unlimited inbound plan covers everything
- No middleware needed (no Make/n8n/Zapier)
- Lowest complexity -- everything in one platform

**Cons:**
- Outbound limited to 100 calls/day, 10AM-6PM (not relevant for inbound-only use case)
- Requires LC Phone numbers (not direct Twilio)
- Voice model options are limited vs. dedicated platforms
- Voice quality unproven vs. ElevenLabs
- No voice cloning
- Less control over conversation design than dedicated platforms
- Newer product -- less battle-tested

**Verdict:** If voice quality is "good enough" and the goal is speed to deploy, this is the fastest path. Test it first since it is already in their stack.

---

### 2. ElevenLabs Conversational AI (ElevenAgents)

**The strongest fit on paper.** Client already uses ElevenLabs. Best-in-class voice quality. Full agent platform now, not just TTS.

**Pros:**
- Client already has an ElevenLabs relationship
- Best voice quality in the market (industry consensus)
- Voice cloning -- can clone Gosia's voice for the phone agent
- Polish auto-detect built in (big differentiator for this client)
- Integrated STT (Scribe v2), LLM routing, and TTS in one pipeline = lower latency
- Knowledge base for pricing sheets and sales scripts
- Structured data extraction (name, phone, service type, sq ft)
- $99/mo Pro plan is competitive

**Cons:**
- No native phone numbers -- needs Twilio (~$1/mo + $0.0085/min)
- No native GHL integration -- needs Make/n8n webhook bridge
- No native after-hours routing -- Twilio or GHL must handle time-based logic
- 5 file / 300K char knowledge base limit on non-Enterprise plans
- Pro plan only includes 1,100 min -- need Scale ($330) for higher volume
- LLM markup of 10-30% on top of base pricing

**Verdict:** Best voice experience. The "wow factor" option for demos. Voice cloning + Polish = unique selling points for this specific client. Integration complexity is moderate (Twilio + Make).

---

### 3. Retell AI

**The most complete out-of-the-box solution.** Everything you need with minimal integration work.

**Pros:**
- Native after-hours routing in dashboard (business hours toggle, ring-then-AI fallback)
- Conversation Flow builder is purpose-built for intake/sales flows
- GHL integration well-documented (Make.com modules, live workshops)
- ElevenLabs voices supported (Flash v2, v2.5)
- Structured data extraction with post-call analysis
- Knowledge base supports files, URLs, spreadsheets (up to 1,000 rows)
- SOC2 Type II, HIPAA, GDPR compliant
- No monthly minimum -- pure pay-as-you-go
- 600ms latency is competitive

**Cons:**
- More expensive per minute than GHL native or custom Twilio
- No native voice cloning (must clone in ElevenLabs first, then use in Retell)
- Multiple cost layers (infrastructure + TTS + LLM + telephony + KB)
- Phone numbers $2/mo (vs $1 Twilio)

**Verdict:** Best "ready to go" option. After-hours routing as a first-class feature, not a hack. GHL bridge is well-trodden path. Good middle ground between capability and complexity.

---

### 4. Vapi

**The developer's choice.** Maximum flexibility, steeper learning curve.

**Pros:**
- Native GHL integration with 4 built-in tools (contact create, contact get, check availability, create event)
- Mix-and-match any STT/LLM/TTS provider
- Workflow builder for structured flows
- Polish support via Deepgram Multi + ElevenLabs/Cartesia
- Warm transfer with AI-generated summary
- Structured data extraction via JSON Schema
- $10 free credit to test

**Cons:**
- No native after-hours routing -- needs GHL or Make to handle time logic
- Warm transfer requires Twilio (not free Vapi numbers)
- Pricing is opaque -- $0.05/min base + each provider adds cost
- Most expensive option at realistic all-in rates ($0.15-0.31/min)
- Developer-oriented -- more setup than Retell or ElevenLabs
- Multiple bills (Vapi + each provider API key)

**Verdict:** Best GHL integration of any external platform. But the pricing complexity and developer burden make it harder to justify vs. simpler options for a single-client deployment.

---

### 5. Bland AI

**The visual builder play.** Good conversation design tools, but priced for higher volume.

**Pros:**
- Visual Conversational Pathways builder (drag-and-drop nodes)
- Single-MP3 voice cloning
- Intelligent call routing (NLU-based, not IVR menus)
- Structured variable extraction with loop conditions
- $0.14/min Start plan has no monthly minimum

**Cons:**
- Build plan ($299/mo) needed for real features (5 clones, 2K calls/day, 50 concurrency)
- Knowledge base is text-only (no file upload, no PDF, no vector DB)
- No ElevenLabs voice integration (uses their own TTS engine)
- 800ms latency is the slowest of the group
- No native GHL integration -- webhooks only
- Compliance burden is on you (no built-in TCPA tooling)

**Verdict:** Good platform, but the $299/mo floor on Build plan and lack of ElevenLabs integration make it less attractive for this use case. Better suited for high-volume outbound campaigns.

---

### 6. Twilio Custom (ConversationRelay)

**The build-it-yourself option.** Cheapest per minute, reusable across clients, but requires engineering time.

**Pros:**
- Cheapest all-in cost (~$0.08-0.09/min with ConversationRelay)
- ElevenLabs is the DEFAULT TTS provider in ConversationRelay
- Lowest latency (p50: 491ms, p95: 713ms)
- Full LLM flexibility (Claude, GPT, Mistral, anything)
- Full control over conversation design, data flow, and integrations
- Data stays in your infrastructure
- Reusable across future Syntora clients -- becomes a product
- White-label (no "powered by" branding)

**Cons:**
- 1-2 week build (ConversationRelay approach)
- You own uptime, monitoring, and maintenance
- No dashboard -- build your own analytics/logging
- Edge cases (interruptions, noise, accents, disconnects) take time to handle well
- Compliance verification is on you
- ConversationRelay is still maturing (launched 2025)

**Verdict:** Best long-term play if Syntora plans to offer voice agents as a service line. The ConversationRelay approach is NOT the old "stitch raw audio streams together" nightmare -- Twilio handles STT/TTS orchestration, you just send/receive text over a WebSocket. Core server is ~100 lines of code.

---

## Decision (2026-03-02)

**GHL Native Voice AI: Rejected.** Voice quality and conversation capability not good enough.

**Selected: Twilio ConversationRelay (custom build)**
- Full Python/FastAPI control for robust automations
- RAG architecture with Supabase pgvector (adapted from Open Decision patterns)
- ElevenLabs TTS built into ConversationRelay
- ~$0.08-0.09/min, reusable across future Syntora clients
- Helping Hands is the pilot client

See: voice-agent-technical-design.md (stack + tools + prompts), voice-agent-rag-architecture.md (RAG pipeline + schema + ingestion)

---

## Final Architecture

```
Call Flow:
  Caller -> GHL Phone Number -> GHL IVR Workflow
    -> Business hours: ring office, overflow to AI
    -> After hours: forward to Twilio number -> ConversationRelay -> AI Agent

AI Agent Stack:
  STT: Deepgram Nova-3 (via ConversationRelay, ~$0.008/min)
  LLM: Claude Haiku/Sonnet via LiteLLM (~$0.005-0.01/min)
  TTS: ElevenLabs Flash v2.5 (via ConversationRelay, included)
  RAG: Supabase pgvector + Gemini embeddings + Redis cache
  Server: Python FastAPI WebSocket on Fly.io

Data Flow:
  Call ends -> post-call webhook -> n8n/Make -> GHL
    -> Create contact (name, phone, email, address)
    -> Create opportunity (service type, sq ft, preferred date)
    -> Trigger nurture workflow (confirmation SMS, follow-up sequence)
    -> Morning summary email to Gosia's team
```

---

## Sources

All source URLs documented in individual platform research files. Key sources:
- Vapi: vapi.ai/pricing, docs.vapi.ai
- ElevenLabs: elevenlabs.io/pricing, elevenlabs.io/docs
- Retell: retellai.com/pricing, docs.retellai.com
- Bland: bland.ai, docs.bland.ai
- GHL: help.gohighlevel.com (Voice AI, IVR, Workflows, Pricing articles)
- Twilio: twilio.com/docs/voice/twiml/connect/conversationrelay
