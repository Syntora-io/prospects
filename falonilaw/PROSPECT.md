# Filoni Law

## Status
- **Stage:** Proposal -- Call 3
- **First Contact:** 2026-02-18
- **Call 1:** 2026-02-18 (David + Darsh, Sean not present)
- **Call 2:** 2026-02-24 (David, Sean, Darsh, Trisha, Meghna, Parker)
- **Next Step:** Proposal call -- Tue Mar 3, 12:00 PM ET
- **Call Agenda:** Present proposal, pricing, formalize programming support plan. Chris may join.
- **Source:** Booked via older strategy call link (likely from website pages)

## Company Info
- **Name:** Filoni Law
- **Type:** Debt collection law firm (NJ court system / E-Courts)
- **Owner:** David Filoni Jr. (Managing Partner)
- **Founded by:** David's father (branched into multiple entities)
- **HQ:** New Jersey
- **Teams:** Local, Mexico, India, Africa (phone vendors)
- **Scale:** 1000+ court emails per day, mass filings (never one at a time)

## Contacts
| Name | Role | Notes |
|------|------|-------|
| David Filoni Jr. | Owner / Managing Partner | Primary contact, on calls 1 & 2 |
| Trisha | Programming Director | Higher-level direction alongside Chris. Security-conscious. On call 2. |
| Sean Barlisan | Programmer / Infrastructure | Technical lead for day-to-day scripting. Wrote most script structures. On call 2. |
| Darsh Patel | Programmer | Newer (started Sep, full-time Jan). Runs 3 scrapers. On calls 1 & 2. |
| Chris | Lead Programmer | Makes core programs (filers). Too busy. NOT on either call yet. Target for call 3. |
| Brian | Programmer | Also too busy. Not on calls. |

## Tech Stack
- **JST CollectMax** -- On-prem. Central database. Case management, court website interaction. ADS backend. NO REST API. File-based EDI only.
- **SQL Database** -- Separate DB where they pull JST data for custom reporting and cross-referencing (e.g. mapping court docket numbers + county to account numbers).
- **Python** -- Primary scripting language. Email scrapers, court website click-through automation, data import/export.
- **PowerShell Universal** -- Endpoints for FTP transfers, report generation, SQL queries.
- **Amazon Workspaces** -- Each programmer gets a designated AWS workspace. Scripts run there or on JST production server for heavier loads.
- **Okta** -- MFA for users (not dev stack).
- **BitBucket** -- Darsh has scrapers there, but not team-wide. Side project.
- **No centralized repo** -- Code is siloed per workspace. No GitHub, no shared repo, no version control.

## Current Workflow
1. NJ court system sends 1000+ emails/day to registered inboxes (Jeffers2, Jeffers3)
2. Python scrapers run hourly (12:01am-11:59pm) scanning for keywords (wage confirmation, court officer, goods & chattel, etc.)
3. Scrapers output Excel sheets for matching/verification against JST data
4. Data flows IN to JST from: court emails, data vendors, payment sites
5. Data flows OUT of JST to: mass court filings (bulk, never one at a time)
6. Some data pulled from JST into SQL for custom reporting beyond JST's limitations
7. PowerShell Universal handles FTP transfers, report generation, SQL queries
8. Chris builds core filer programs (may be broken), distributes raw files

## JST Import Limitations (Key Technical Detail)
- Blank fields: can bulk import via MaxUpdater
- Relational fields (e.g. place of employment): CANNOT bulk import. Must click dropdown to select existing record to avoid creating duplicates on the backend.
- This is why they need click-through Python automation (Selenium/similar) for certain data entry
- Court uses docket numbers (not unique alone), firm uses account numbers. Pairing docket + county = unique = account number. This mapping lives in the SQL database.

## Scripts Inventory
| Script | Owner | Function | Schedule |
|--------|-------|----------|----------|
| Wage confirmation scraper | Darsh | Scans Jeffers2 inbox for "wage application" keyword, outputs Excel | Hourly, 24/7 |
| Court officer scraper | Darsh | Scans for court officer assignments, docket numbers | Hourly, 24/7 |
| Goods & chattel scraper | Darsh | Same structure as wage, different keywords | Hourly, 24/7 |
| Jeffers3 email scrapers | Sean | Main E-Court contact scrapers. "Set in stone" per Sean. | Hourly |
| Court filer scripts | Chris | Click-through automation for court website filings (5 clicks). May be broken. | Unknown |
| Outlook calendar tool | Sean | Trial team calendar integration. Nearly done, needs trial team input. | In progress |
| Docket-to-account mapper | Resolved | Pairs county + docket number to get account number via SQL | Working |

## Pain Points (Updated After Call 2)
1. **Bottleneck on Chris (and Brian)** -- Lead programmers too busy, backlog growing
2. **JST import limitations** -- Relational fields require click-through automation, not bulk import
3. **No centralized code management** -- Scripts siloed across individual AWS workspaces
4. **No backlog list** -- "We need to get a list together of things that we really want" (David, call 2)
5. **Filer scripts may be broken** -- Chris owns them, nobody else touches them
6. **1000+ court emails/day** -- Must be processed into JST accurately and fast to keep database current

## What They Want
1. **More Python developers** -- extension of their team to unblock Chris/Sean/Brian
2. **New scripts for JST import workarounds** -- click-through automation for fields that can't be bulk imported
3. **Potentially: GitHub + CI/CD pipeline setup** -- Sean and Darsh already researching, team consensus needed
4. **They own all IP** -- David, Darsh, and Trisha all emphasized this multiple times
5. **NOT looking for AI yet** -- primary need is Python scripting capacity

## What They Don't Need (Yet)
- Existing scrapers are "set in stone" -- don't touch
- Chris's filers are his domain -- needs Chris on a call first
- Reporting is handled by JST + SQL -- not a pain point
- AI is not on the table for this engagement

## Our Proposed Approach (Revised Post-Call 2)
**Lead with consulting, not staff augmentation.**

The bottleneck is not headcount. They have 4-5 programmers. The bottleneck is that every programmer is siloed on a separate AWS Workspace with no shared repo, no CI/CD, no code visibility, and no onboarding path. Adding a 6th programmer into that environment creates a 6th silo.

Parker has built enterprise monorepo structures before. He knows how to set up a codebase where every developer has their own workspace/branch but everything flows into a single controlled repo with proper CI/CD. The key value: build the infrastructure around them while they keep running -- no downtime, no disruption to daily operations.

### Pricing Structure

**Phase 1: Discovery + Infrastructure Plan -- $3,500 - $5,000 (fixed)**
- Audit every workspace, script, schedule, deployment process
- Map full data flow: court emails -> scrapers -> JST -> SQL -> filings
- Deliver written infrastructure plan: repo structure, branching strategy, pipeline design, security model, migration path
- Low enough that David doesn't overthink it, high enough to signal expertise
- Also qualifies the client -- if they balk at $4k for a plan, they won't pay for implementation

**Phase 2: Implementation -- $12,000 - $20,000 (fixed)**
- Enterprise monorepo setup with per-developer branching (Sean, Darsh, Chris, Brian each have space but everything unifies)
- GitHub Actions pipelines for automated script deployment and scheduling
- Incremental script migration from siloed workspaces (no downtime, no disruption)
- Security model implementation (Trisha's primary concern)
- Onboarding documentation so any new dev can ramp in days, not months
- Fixed fee removes client risk -- they know exactly what they're paying

**Phase 3: Ongoing Support -- $2,000 - $4,000/mo (retainer, optional)**
- New script development (JST click-through automation, backlog items)
- Pipeline maintenance and updates
- Onboarding support for future devs
- Start lower to get them in, increase as scope grows

**Total first engagement: ~$16k - $25k, then recurring monthly.**

### ROI Argument for David
- He's paying 4-5 programmer salaries ($60-80k+ each = $300-400k/yr in dev payroll)
- If infrastructure work makes those people 30% more productive, that's equivalent to adding 1.5 headcount without a single new hire
- Entire engagement pays for itself in a couple months
- They asked for a new programmer. We're giving them the equivalent of 1-2 new programmers by unlocking their existing team.

### Pricing Presentation Notes
- David asked on call 1 about hourly vs fixed vs maintenance fees -- he thinks in those terms
- Present all three phases with fixed prices
- Frame retainer as optional
- Fixed feels safer to a law firm owner than open-ended hourly
- All IP owned by Filoni Law (non-negotiable for them)

## Action Items (Pre-Mar 3 Proposal Call)
- [ ] Research GitHub Pro vs Enterprise licensing for their team size
- [ ] Build proposal document with scope, pricing options, deliverables
- [ ] Prepare GitHub + pipeline implementation plan
- [ ] Get Chris on the call (David coordinating)
- [ ] Compile specific backlog items (need from Trisha/Chris)

## Notes
- David came through an older/deprecated booking link -- source unclear but likely website
- David's dad started the firm, branched into multiple entities
- Trisha has authority but is not deeply technical -- security is her concern
- Sean is the technical bridge -- code structure, mentorship, infrastructure knowledge
- Darsh started Sep 2025, full-time Jan 2026. Learning curve was manageable with Sean's mentorship.
- Chris has never been on a call. Getting him on call 3 is important.
- "Our one job is to make sure we collect all the data coming in and put it into the system as fast and accurate as possible" -- Trisha (core mission statement)
- Vendors in India and Africa are on phones with debtors, need real-time accurate data from JST
- Sean on GitHub: "it's not my decision, it's something the whole team should go over because it's a big bridge to cross"

## Folder Index
```
falonilaw/
  PROSPECT.md                              <- You are here
  meetings/
    2026-02-18-discovery-call.md           <- Call 1 notes + transcript
    2026-02-24-discovery-call-2.md         <- Call 2 notes + transcript
  research/
    feb-24-call-prep.md                    <- Call 2 prep + questions for Sean
    sean-questions.md                      <- Technical questions for Sean
    debt-collection-industry-guide.md      <- Full industry/JST/AI reference guide
  notes/
    2026-02-24-post-call-strategy.md       <- Strategic pivot: consulting > staff aug
```
