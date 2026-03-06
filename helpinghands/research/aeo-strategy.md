# AEO Strategy -- Helping Hands Cleaning

## How AI Engines Surface Cleaning Companies Today

| Engine | % of Locations Recommended | Primary Data Sources |
|--------|---------------------------|---------------------|
| ChatGPT | 1.2% | Website content (58%), Yelp reviews, aggregated directories |
| Perplexity | 7.4% | Yelp Fusion API (33% of searches), Angi, Thumbtack, HomeAdvisor, Expertise.com, Reddit, local media |
| Google AI Overviews | 7% of local searches | GBP, Facebook, YouTube, review sentiment, local media |
| Gemini | 11% | Google Maps data (100% profile accuracy) |
| Claude | No real-time local search | Influences brand perception in advisory queries |

Key stat: less than 50% of businesses ranking well in Google local results also appear in AI recommendations. Different algorithms, different signals.

## What Matters for AI Citations

### Technical Foundation
1. **NAP consistency** -- name, address, phone must be identical across every listing. One mismatch kills confidence.
2. **Schema markup** -- LocalBusiness, Service, FAQ, AggregateRating, Organization in JSON-LD on every page
3. **robots.txt must allow AI bots** -- GPTBot, PerplexityBot, ClaudeBot, GoogleBot
4. **Site speed** -- slow sites get skipped by AI processors
5. **llms.txt** at root -- business summary, service list, key page URLs in Markdown

### Content Structure
1. **Answer capsules** -- 2-3 sentence direct answers at top of every page (40% more citations)
2. **Front-load value** -- 44.2% of citations come from first 30% of content
3. **Clean H1/H2/H3 hierarchy** -- AI parses headings for topic understanding
4. **Bullet points and numbered lists** -- AI extractors prefer structured formats
5. **Conversational language** -- match how people talk to AI assistants

### Review Requirements
- Minimum 4.3 stars across platforms (ChatGPT's threshold)
- Volume matters -- more reviews = more data for AI to synthesize
- Recency matters -- fresh reviews signal active business
- Specific language in reviews matching search queries ("deep cleaning," "move-out cleaning") because AI extracts and paraphrases review language

### Content Freshness
- Pages updated within 2 months earn 28% more citations
- Quarterly audits of all service pages
- Visible publication and last-updated dates

## Content Strategy for Cleaning AEO

### Page Types That Get Cited

**Service + Location Pages:**
- "Residential Deep Cleaning in [City]" -- one per service per city
- Direct answer format: what it includes, how long it takes, price range, booking CTA
- FAQ schema on every page

**Comparison/Decision Content:**
- "House Cleaning vs. Maid Service: What's the Difference?"
- "How Often Should You Get Your House Professionally Cleaned?"
- "What to Expect from a Move-Out Cleaning Service"

**Cost/Pricing Transparency:**
- "How Much Does House Cleaning Cost in [City] in 2026?"
- AI engines love citing specific pricing data with context
- Pricing tables with schema markup

**Trust/Process Content:**
- "How We Vet and Train Our Cleaning Staff"
- "Our Green Cleaning Products and Why We Use Them"
- Builds E-E-A-T signals for recommendation confidence

### YouTube Strategy
YouTube has the highest correlation with AI visibility (0.737) -- higher than backlinks (0.218) or branded web mentions (0.664).

Ideas:
- "What a Professional Deep Clean Actually Looks Like" (walkthrough)
- "5 Things Your Cleaning Service Should Always Do"
- Before/after transformations
- Full transcripts and timestamps (AI parses these)

### Programmatic Scale
- 33+ service area cities x multiple service types = 200-500 location-specific pages
- Syntora's pipeline handles this: question mining, dedup, generation, publishing, IndexNow
- ~90 seconds per page, under $0.50/page generation cost

## Pitch Numbers

- AI search capturing 25%+ of search traffic by 2026 (Gartner)
- AI-referred traffic converts at 14.2% vs 2.8% for Google organic (5x)
- Brands cited in AI Overviews earn 35% more organic clicks and 91% more paid clicks
- First-mover advantage in home services AEO is massive -- the space is nearly empty
- Less than 50% of Google local pack businesses appear in AI results

## Call Learnings (2026-03-02)

### AI Visibility Test (Live on Call)
- Searched "best cleaning service Naperville" on ChatGPT -- **Helping Hands did not appear**
- Gosia confirmed: Jennifer (employee) ran this test 6 months ago across all service area cities -- not appearing anywhere
- This is the baseline. Zero AI visibility today.

### Lead Volume Problem
- Current: 50-60 leads/week (down 50% in Jan/Feb despite same Google Ads spend)
- Target: 100 leads/week to hit $7.5M residential revenue
- Google Ads managed in-house, not through Edge Digital
- Team is on gain/profit sharing -- financially motivated to grow

### Edge Digital (Current SEO Agency)
- 3-4 year relationship
- Parker's scrape found zero AEO pages on the site
- Gosia unsure if they're doing any AEO work
- Meeting Friday 2026-03-07 -- Gosia will record and share transcript
- Parker provided vetting questions PDF for Gosia to ask

### Gosia's Understanding
- Familiar with ChatGPT (has business account integrated with site + social)
- Went to a marketing conference ~6 months ago, learned about AI search
- Not deeply technical -- needs plain-English explanations
- Very open to being a first mover in the cleaning industry
- Wants to understand: what are the pages, who writes them, what's on them

### What Parker Explained on Call
- AEO pages are hidden from human navigation, accessible via AI-specific sitemaps
- Content is problem/solution Q&A format for AI extraction
- Can generate ~100 pages/day across all service area cities
- AI generation cost: ~$100/mo at their scale using Gemini
- Different from SEO -- targets AI engines, not human readers
- Complements (or eventually replaces) traditional SEO

## Syntora Delivery Model
- 4-week implementation
- Client owns 100% of content + full Python codebase in private GitHub repo
- Week 1: keyword validation, infra setup, baseline SoV report, WordPress API integration
- Weeks 2-4: generate and QA first 100 pages
- Week 5: deploy, verify structured data, monitor initial citations
- Week 6+: weekly SoV reports, Slack alerts, monthly reviews

### WordPress-Specific Delivery
- Python scripts publish via WordPress REST API (different from Syntora's Supabase pipeline)
- AIOSEO Pro handles sitemap + schema generation automatically
- robots.txt updated to allow GPTBot, PerplexityBot, ClaudeBot, GoogleOther
- Custom post type keeps AEO pages separate from existing blog/service pages
- Divi-compatible minimal template for AEO content (text-only, fast loading)
- Google Search Console API for sitemap submission and index monitoring
- Coordination with Edge Digital needed for hosting access and to avoid conflicts

### Cleaning-Specific AEO Targets
- 33+ service area cities x 8+ service types = 264+ base combinations
- Service types: recurring residential, deep cleaning, move-in/out, commercial, post-construction, disinfection, window washing, carpet cleaning
- Question categories: pricing ("How much does deep cleaning cost in Naperville?"), comparison ("House cleaning vs maid service"), process ("What to expect from move-out cleaning"), eco ("Green cleaning products safe for pets")
- Expand with: seasonal (spring cleaning, holiday prep), problem-specific (pet hair, allergens, marble care), FAQ from actual customer calls
