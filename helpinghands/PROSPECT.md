# Helping Hands Cleaning

## Status
- **Stage:** Discovery Complete
- **First Contact:** 2026-03-02
- **Discovery Call:** 2026-03-02 (Parker, Meghna, Gosia)
- **Next Step:** Send follow-up email with deliverables, wireframe voice agent, prepare quote
- **Source:** Former employer (Parker worked at Helping Hands)

## Company Info
- **Legal Name:** Helping Hands Maid Services, Inc.
- **DBA:** Helping Hands Cleaning Services
- **Type:** Residential cleaning service (also has commercial arm)
- **Website (Residential):** helpinghandscleaningservices.com
- **Website (Commercial):** helpinghandscommercialcleaning.com
- **Legacy site:** helpinghandscleaningservicesil.weebly.com (still live -- cleanup opportunity)
- **HQ:** 675 St Charles Rd, Elmhurst, IL 60126
- **Second Office:** 800 Roosevelt Rd, Bldg C, Ste 11, Glen Ellyn, IL 60137
- **Owner:** Gosia Baran (founded Nov 2001, immigrated from Poland 1999)
- **Co-owner:** Tony Baran (husband)
- **Revenue:** $7.5M target 2026 (~$5M two years ago, per Gosia on call)
- **Employees:** ~55
- **Founded:** November 2001
- **Service Area:** 33+ cities across DuPage, Cook, and Kane counties (western Chicago suburbs)
- **Awards:** ECCI Business of the Year 2022 (Elmhurst Chamber)
- **Certifications:** GBAC (ISSA), ISSA Residential, ARCSI, BSCAI
- **Charity:** Cleaning for a Reason partner -- 500+ free cleanings for women with cancer
- **Guarantee:** 200% satisfaction guarantee
- **Parker's history:** Former employee, deep knowledge of residential cleaning industry

## Contacts
| Name | Role | Notes |
|------|------|-------|
| Gosia Baran | Founder & Owner | ARCSI board member. LinkedIn: linkedin.com/in/gosia-baran-24024314/ |
| Tony Baran | Co-owner / Husband | Referenced in origin story |
| Dominika Wandachowicz | Business Development Manager | Per RocketReach |
| Jim Wilson | Business Development Manager | Commercial arm. LinkedIn: linkedin.com/in/jim-wilson-092228295/ |

## Tech Stack
| System | Platform | Notes |
|--------|----------|-------|
| CRM / Operations | **MaidCentral** | Cloud-based, cleaning-industry-specific. Client portal at `helpinghands.maidcentral.com`. REST API available. Zapier triggers for cancellations, lead closures, bookings, job completions. ~$450+/mo. |
| Marketing CRM | **GoHighLevel** | LeadConnector chat widget on residential site (Location ID: `lbXZx5ljWYY5fW1hXImV`). Likely used for lead capture / marketing automation. |
| Website (Residential) | **WordPress + Divi** | Hosted on A2 Hosting (LiteSpeed). Built by "Cleaning Company Websites" (niche agency). DNS at GoDaddy. 200+ blog posts, 25+ service area pages. |
| Website (Commercial) | **WordPress + Elementor** | Behind Cloudflare proxy. Different builder, different agency. Running MetaSync OTTO (Search Atlas automated SEO). Much lighter than residential site. |
- **SEO Agency:** Edge Digital (3-4 year relationship). Manages WordPress, GSC, GA, hosting (H2O). Meeting with them Friday 2026-03-07. Gosia will record and share transcript.
- **ChatGPT Business:** Integrated with website + social media ~6 months ago
- **Voice:** Already using 11 Labs

| SEO Plugin | **All in One SEO Pro v4.9.3** | Handles sitemap, schema, llms.txt on residential site |
| Analytics | **GTM (x2)** + Google Ads + Facebook Pixel | Two GTM containers (GTM-MCJDDMK, GTM-NPJ4FVM) -- agency manages one. Google Ads self-managed. |
| Schema (existing) | Organization, ProfessionalService, BreadcrumbList | On residential site via AIOSEO |
| Payments | Stripe or Authorize.net | Via MaidCentral |

**Key insight:** MaidCentral is backend-only (scheduling, dispatch, invoicing, CRM). It does NOT build or host websites. Any AEO/directory/website work is fully independent of their CRM. MaidCentral has a REST API and Zapier, so lead flow from AEO back into their CRM is feasible.

## Current Online Presence
| Platform | Status | Notes |
|----------|--------|-------|
| Google Business Profile | Active | 1,000+ 5-star reviews (claimed) |
| Yelp | Active | 90 reviews, 43 photos |
| BBB | **Not accredited. B- rating.** | 1 unresolved complaint -- low-hanging fix |
| Angi | Active | 4.4/5 |
| HomeAdvisor | Active | Listed |
| Nextdoor | Active | 800+ 5-star reviews |
| Birdeye (aggregated) | 4.9 stars | 1,411 reviews |
| SoTellUs | 4.8 stars | 626 reviews |
| Apple Maps | Listed | |
| Elmhurst Chamber | Member | |
| Schaumburg Business Assoc. | Member | |
| Care.com | Listed | |
| Facebook | Active | /HelpingHandsCleaningServicesChicagoland |
| Instagram | @helpinghandscleans | 639 followers, 1,006 posts -- engagement gap |
| LinkedIn | Company page | 230 followers |
| X (Twitter) | @hhcleans | Listed |
| Groupon | Listed | |

**Not found on:** Thumbtack, Crunchbase, Wikidata, Trustpilot, Glassdoor, D&B, Bing Places (unverified), most data aggregators.

## Our Proposed Approach
### Phase 1: Voice Agent (After-Hours Sales)
- AI voice agent for evenings + weekends: Twilio ConversationRelay + FastAPI + Claude tool_use + ElevenLabs TTS
- RAG architecture: Supabase pgvector (hybrid search), Gemini embeddings, Redis cache (adapted from OD patterns)
- Knowledge base: sales script, pricing matrix, service descriptions, city info, FAQ (chunked + embedded)
- Gather: sq ft (or bedrooms/bathrooms/floors fallback), pets, service type
- Trained on Gosia's existing sales script + SOP
- Goal: capture missed leads outside business hours, provide dynamic quotes
- GHL native voice AI evaluated and rejected -- not good enough
- Details: research/voice-agent-technical-design.md, research/voice-agent-rag-architecture.md

### Phase 2: AEO Automation
- AI-generated pages targeting AI engine visibility (ChatGPT, Perplexity, Gemini)
- ~100 pages/day across service area cities, problem/solution Q&A format
- Hidden from human navigation, accessible via AI-specific sitemaps
- Complement (or replace) Edge Digital's traditional SEO
- Details: research/aeo-strategy.md, research/directory-strategy.md

### Phase 3: Commercial Calculator App
- On-site quoting tool for commercial BD walkthroughs
- Input walkthrough data -> instant quote generation

### Phase 4: Directory Saturation
- Get listed on unconventional directories (Crunchbase, Wikidata, Trustpilot, data aggregators)
- Build structured citations that AI models pull from

## Gaps & Opportunities (Pre-Call)
1. **BBB B- rating** -- not accredited, 1 unresolved complaint. Easy win to fix.
2. **Legacy Weebly site still live** -- brand consistency issue
3. **Instagram engagement gap** -- 1,006 posts but only 639 followers
4. **Missing from key AI-indexed directories** -- no Crunchbase, Wikidata, Trustpilot, Bing Places, data aggregators
5. **Schema exists but incomplete** -- has Organization, ProfessionalService, BreadcrumbList. Missing: Service (per-service), FAQ, AggregateRating, HowTo.
6. **Two separate websites built by different people** -- residential (Divi, "Cleaning Company Websites" agency) vs commercial (Elementor, different agency, MetaSync OTTO). Different builders, different toolchains, no cross-linking.
7. **llms.txt exists** -- auto-generated by AIOSEO Pro. Needs audit to see if it's actually useful or just boilerplate.
8. **Dual CRM** -- MaidCentral for ops + GHL for marketing. Need to understand if these are connected or siloed.
9. **Two GTM containers** -- suggests agency involvement. Need to know who manages what.
10. **Commercial site missing analytics/tracking** -- no visible GA/GTM/Pixel in source. No chat widget, no booking funnel.

## Action Items
### Parker (Syntora)
- [x] Discovery call -- 2026-03-02
- [x] AEO vetting questions PDF for Edge Digital meeting
- [x] SoV baseline -- 35-query sample across ChatGPT + Perplexity spot check
- [x] SoV report PDF (client-facing, no guarantees, frames as preliminary sample)
- [x] Document sales cycle + voice agent routing design
- [x] Draft follow-up email to Gosia
- [x] Voice agent platform comparison (6 platforms evaluated, GHL rejected)
- [x] Voice agent technical design (Twilio ConversationRelay + FastAPI + Claude + ElevenLabs)
- [x] Voice agent RAG architecture plan (pgvector, hybrid search, adapted from OD)
- [ ] **Send follow-up email** with: call transcript, vetting questions PDF, SoV report PDF
- [ ] Build full SoV audit (thousands of prompts across all cities/services/question types)
- [ ] Wireframe voice agent (share with Meghna for feedback)
- [ ] Quote: voice agent setup + AEO automation pricing
- [ ] Review Edge Digital meeting transcript (when received after Friday 03/07)
- [ ] Audit website for schema markup and AI bot access (robots.txt)
- [ ] AEO vs SEO comparison doc for Gosia

### Gosia (Helping Hands)
- [ ] **Send sales script + SOP** for residential sales cycle (blocker for voice agent build)
- [ ] **Send pricing breakdown** by sq ft and service type (blocker for voice agent quotes)
- [ ] **Confirm phone system** -- GHL, separate provider, or regular phone line?
- [ ] Record Edge Digital meeting (Friday 03/07) and share transcript
- [ ] Use Parker's vetting questions during Edge Digital meeting
- [ ] Share referral contact (friend needing GHL setup for cleaning company)

## Notes
- Gosia Baran is active in the industry (ARCSI board) -- credibility is already there, just not surfaced digitally in the right places
- Commercial arm exists as separate entity (PCT Janitorial sister company in Atlanta)
- Services: recurring residential, deep cleaning, move-in/out, commercial, post-construction, disinfection, window washing, carpet cleaning
- Residential site built by "Cleaning Company Websites" -- niche agency that does WordPress + Divi for cleaning companies. Not a custom build.
- MaidCentral is the dominant CRM for high-growth cleaning companies. Every residential cleaning company on the 2025 Inc. 5000 runs it. $450+/mo starting. Has REST API + Zapier.
- GHL setup done by VA from Philippines. GHL used for marketing/nurture, Maid Central for ops. Confirmed on call these are the only two systems.
- Current leads: 50-60/week (down 50% Jan/Feb despite same ad spend). Need 100/week for $7.5M target.
- Google Ads managed in-house (not by Edge Digital)
- Team is on gain/profit sharing -- incentivized to grow
- Gosia wants to be "first in cleaning industry" with AI -- strong referral potential to ARCSI network
- Meghna feedback: simplify technical language for non-technical stakeholders, avoid name-dropping tools

## Folder Index
```
helpinghands/
  PROSPECT.md                                   <- You are here (source of truth)
  meetings/
    2026-03-02-discovery-call.md                <- Full call notes + action items
  notes/
    follow-up-email-draft.md                    <- Email to Gosia (ready to send)
    aeo-vetting-questions-edge-digital.md       <- 10 questions for Edge Digital meeting
    AEO-Vetting-Questions-Edge-Digital.pdf      <- PDF version (attach to email)
    generate-pdf.py                             <- Script that generates the vetting PDF
  research/
    aeo-strategy.md                             <- AEO approach + call learnings + WordPress delivery
    directory-strategy.md                       <- Full directory audit + prioritized list
    tech-stack.md                               <- Full stack + WP REST API integration architecture
    sales-cycle.md                              <- Sales cycle + voice agent design + routing + data flow
    sov-baseline-summary.md                     <- SoV results summary (20% overall, 12.5% non-brand)
    sov-baseline-2026-03-02.json                <- Raw SoV data (35 queries x ChatGPT)
    sov-baseline.py                             <- Reusable SoV tracking script (monthly)
    AI-Search-Visibility-Report.pdf             <- Client-facing SoV report (attach to email)
    generate-sov-pdf.py                         <- Script that generates the SoV PDF
    voice-agent-comparison.md                   <- 6-platform comparison (GHL, ElevenLabs, Retell, Vapi, Bland, Twilio custom)
    voice-agent-technical-design.md             <- Architecture, stack, tools, prompts, deployment plan
    voice-agent-rag-architecture.md             <- RAG design (pgvector, hybrid search, ingestion, adapted from OD)
```
