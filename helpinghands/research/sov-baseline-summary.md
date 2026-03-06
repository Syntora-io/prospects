# Share of Voice Baseline -- Helping Hands Cleaning Services
**Date:** 2026-03-02
**Target:** Helping Hands Cleaning Services (helpinghandscleaningservices.com)
**Engines tested:** ChatGPT (API, gpt-4o-search-preview), Perplexity (manual spot check)

---

## Headline Numbers

| Metric | Value |
|--------|-------|
| Total queries | 35 |
| ChatGPT mentions | 7/35 (20%) |
| Brand query mentions | 3/3 (100%) |
| Non-brand mentions | 4/32 (12.5%) |
| Featured (URL cited) | 4/35 (11.4%) |

## ChatGPT Results by Category

| Category | Queries | Mentioned | Rate | Notes |
|----------|---------|-----------|------|-------|
| Brand | 3 | 3 | 100% | Expected -- searching by name |
| Local (10 cities) | 10 | 2 | 20% | Only Wheaton + Oak Park. ABSENT from Elmhurst (HQ), Naperville, Glen Ellyn, Lombard, Hinsdale, Downers Grove, DuPage County, western suburbs |
| Service-specific | 6 | 1 | 16.7% | Only post-construction (commercial site cited). Absent from deep cleaning, move-out, recurring, eco, carpet |
| Question (conversational) | 4 | 1 | 25% | "best cleaning service near me in Elmhurst" worked. Other conversational queries absent. |
| Decision/comparison | 4 | 0 | 0% | Zero visibility on "how to choose" / "what to look for" content |
| Pricing | 4 | 0 | 0% | Zero visibility on cost/pricing queries |
| Trust/eco | 4 | 0 | 0% | Zero visibility despite green cleaning being core brand differentiator |

## Perplexity Spot Check

| Query | Result |
|-------|--------|
| "best house cleaning service in Elmhurst IL" | Helping Hands listed FIRST |

Perplexity surfaces them because it leans on Google Maps data and directory APIs (Yelp Fusion, Angi). Helping Hands has 1,000+ reviews at 4.9 stars on Google Maps -- that signal is strong enough for directory-driven engines.

## Why the Split Matters

| Engine | Primary Data Source | HH Strength | HH Visibility |
|--------|-------------------|-------------|---------------|
| Perplexity | Yelp API (33%), Angi, directories, Google Maps | 1,000+ reviews, 4.9 stars | Strong |
| Gemini | Google Maps (100% profile accuracy) | Same review strength | Likely strong (untested) |
| ChatGPT | Website content (58%), directories | Weak -- no AEO pages, only traditional SEO | Weak (20%) |
| Google AI Overviews | GBP, YouTube, review sentiment | Strong GBP, no YouTube | Mixed |

**The gap is website content.** Engines that rely on directories already find them. Engines that rely on crawling website content do not. AEO pages fix exactly this.

## Competitor Landscape (ChatGPT)

| Competitor | Mentions (out of 35) |
|-----------|---------------------|
| Maid Brigade | 4 |
| MaidPro | 3 |
| Molly Maid | 2 |
| Merry Maids | 2 |
| ServiceMaster | 1 |
| Helping Hands | 7 (but 3 are brand queries) |

Non-brand: Maid Brigade leads with 4 mentions. Helping Hands has 4 non-brand mentions. Essentially tied with national franchises despite being a single-location independent company with zero AI-specific content. Significant room to grow.

## Queries Where Helping Hands Was Mentioned

1. **"Helping Hands Cleaning Services Elmhurst IL"** -- FEATURED (URL cited)
2. **"Helping Hands Cleaning Services reviews"** -- MENTIONED (but ChatGPT confused them with other companies using same name nationally)
3. **"Is Helping Hands Cleaning Services good?"** -- MENTIONED (same name confusion)
4. **"best maid service in Wheaton IL"** -- FEATURED (Glen Ellyn service area page cited)
5. **"top rated cleaning service Oak Park IL"** -- FEATURED (homepage cited)
6. **"post construction cleaning DuPage County"** -- MENTIONED (commercial site cited)
7. **"what is the best cleaning service near me in Elmhurst"** -- FEATURED (homepage cited)

## Critical Gaps

1. **Absent from Elmhurst for non-brand queries** -- ChatGPT does not recommend them for "best house cleaning service in Elmhurst IL" despite HQ being in Elmhurst with 1,000+ reviews
2. **Zero pricing content** -- no cost/pricing queries surfaced them. AI engines cite specific pricing data.
3. **Zero decision content** -- "how to choose a cleaning service" queries go to competitors
4. **Zero eco/trust content** -- despite green cleaning being their core differentiator, none of that surfaces in AI responses
5. **Name confusion** -- ChatGPT confuses them with other "Helping Hands" cleaning companies nationally. AEO pages with location-specific structured data fix this.

## What AEO Fixes

- 33 cities x 8 service types = 264+ location-specific pages with direct answers
- Pricing transparency pages ("How much does deep cleaning cost in Naperville?")
- Decision content ("House cleaning vs maid service")
- Eco/trust content ("Green cleaning products safe for pets")
- FAQ schema on every page for AI extraction
- First two sentences directly answer the question (AI citation format)
- robots.txt updated to allow GPTBot, PerplexityBot, ClaudeBot

## Baseline for Measurement

This is a preliminary baseline from a 35-query sample. Full audit will test thousands of individual prompts across every city, service type, and question format. Ongoing tracking:
- Overall mention rate across full prompt set
- Non-brand mention rate (currently 12.5%)
- Category gap coverage (pricing, decision, trust currently at 0%)
- Competitor positioning relative to national franchises

---

*Full response data: sov-baseline-2026-03-02.json*
*Script: sov-baseline.py (reusable for monthly tracking)*
