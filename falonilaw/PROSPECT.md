# Faloni Law

## Status
- **Stage:** Proposal Sent -- Awaiting Approval
- **First Contact:** 2026-02-18
- **Call 1:** 2026-02-18 (David + Darsh, Sean not present)
- **Call 2:** 2026-02-24 (David, Sean, Darsh, Trisha, Meghna, Parker)
- **Call 3:** 2026-03-03 (Proposal call)
- **Next Step:** David approves proposal, schedule kickoff call
- **Source:** Booked via older strategy call link (likely from website pages)

## Company Info
- **Name:** Faloni Law (Faloni Law Group LLC / Faloni & Associates LLC)
- **Type:** Debt collection law firm (NJ court system / E-Courts)
- **Owner:** David Faloni Jr. (Managing Partner)
- **Founded:** 1975 by David A. Faloni Sr. (branched into multiple entities)
- **HQ:** 425 Eagle Rock Ave, Suite 404, Roseland, NJ 07068
- **Offices:** Roseland NJ, Fairfield NJ, Atlantic Highlands NJ, King of Prussia PA, Flushing NY, Florida
- **Related entities:** Faloni & Associates LLC, Faloni & Wu LLP (NY/immigration, Louisa Wu)
- **Teams:** Local, Mexico, India, Africa (phone vendors)
- **Scale:** 1000+ court emails per day, mass filings (never one at a time)
- **Self-described:** "Top 3 collection firm in NJ, top 50 nationwide"
- **Est. Revenue:** $5M-$15M/year (likely $8-10M mid-range)
- **Est. Tech Budget:** $400K-$800K/year (industry benchmark 5-7% of revenue)
- **US Headcount:** ~15 (ZoomInfo), est. 40-80 total with offshore

## Contacts
| Name | Role | Notes |
|------|------|-------|
| David Faloni Jr. | Owner / Managing Partner | Primary contact. On calls 1, 2, 3. |
| Trisha | Programming Director | Higher-level direction alongside Chris. Security-conscious. On calls 2, 3. |
| Sean Barlisan | Programmer / Infrastructure | Technical lead for day-to-day scripting. Wrote most script structures. On calls 2, 3. |
| Darsh Patel | Programmer | Newer (started Sep, full-time Jan). Runs 3 scrapers. On calls 1, 2, 3. |
| Chris | Lead Programmer | Makes core programs (filers). Too busy. Target for discovery call. |
| Brian | Programmer | Also too busy. Not on calls. |
| David A. Faloni Sr. | Founding Partner / President | NJ Bar since 1969. Seton Hall. Founded firm 1975. |

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

## Accepted Approach (Post-Call 3)
**Land and expand. GitHub infrastructure first, automation/AI opportunities second.**

### Engagement: GitHub Infrastructure Setup -- $3,650 (fixed)

**Phase 1: Discovery (Week 1)**
- Kickoff call with David + Trisha
- Technical call with Sean
- Technical call with Darsh
- Technical call with Chris
- Audit all scripts, schedules, deployment processes across AWS Workspaces
- Map data flows, identify code touching sensitive data
- Identify automation/AI opportunities (documented for future engagement)

**Phase 2: Implementation (Weeks 2-3)**
- GitHub org + repo setup, folder structure mirroring team ownership
- Branch protection, CODEOWNERS, permissions model
- Import all existing scripts from each Workspace
- GitHub Actions pipeline (linting, deployment to Workspaces)
- 1-2 working sessions with Sean
- Handoff walkthrough with full team

**Calls:** Up to 7, 30-45 minutes each
**Timeline:** 3 weeks total
**Discovery is async where possible** -- they provide AWS access, we audit on our own time

### What's NOT Included
- Writing or modifying scripts
- AI or automation development
- Ongoing maintenance
- New script development from backlog

### They Provide
- AWS account access / workspace credentials
- Access to each developer's scripts
- Sean or Trisha as primary contact
- Each developer available for one 30-45 min call

### Strategy
- $3,650 is land-and-expand pricing. Less than 0.05% of their estimated revenue.
- Discovery surfaces automation opportunities. That list becomes the retainer conversation.
- All IP owned by Faloni Law (non-negotiable for them).

## Action Items (Post-Call 3)
- [x] Research GitHub licensing -- Team plan $4/user/mo, $28/mo for 7 users
- [x] Build proposal document -- v1 (`research/2026-03-03-proposal.html`)
- [x] Build internal call guide -- 14-slide wireframe (`research/2026-03-03-proposal-wireframe.html`)
- [x] Review Sean's code -- pagination bug, process gap not skill gap
- [x] Prepare Meghna feedback on Excalidraw deck
- [x] Correct GitHub pricing -- $4/user/mo flat (not $20/mo + $8/seat)
- [x] Port proposal to Syntora proposal builder
- [x] Research firm background -- revenue, entities, compliance history
- [ ] Send proposal to David via Syntora proposal builder (publish)
- [ ] Send Meghna feedback files
- [ ] Get Chris on a discovery call (David coordinating)
- [ ] Compile specific backlog items (need from Trisha/Chris)
- [ ] Confirm: do they have a PM tool?
- [ ] Schedule kickoff call once proposal approved

## GitHub Pricing (Verified 2026-03-02)
- **Team plan:** $4/user/month flat. $28/mo for 7 users, $336/year.
- **Actions:** 3,000 min/month included. ~$0.008/min overage on Linux.
- **Included free:** Basic secret scanning, Dependabot alerts, branch protection, CODEOWNERS, required reviewers.
- **Paid add-ons (Stage 5+):** Advanced Secret Protection $19/active committer/mo, Advanced Code Security $30/active committer/mo.
- **Enterprise ($21/user/mo):** Overkill. They already have Okta for MFA. No need for SAML SSO or audit log API.

## GitHub Permissions Model
| Person | GitHub Role | Access |
|--------|------------|--------|
| David | Org Owner | Billing, org settings. No code access needed. |
| Sean | Admin | Repo settings, branch protection, merge authority. Day-to-day lead. |
| Trisha | Write + Required Reviewer | Compliance gate. Reviews and approves before merge to main. |
| Darsh, Chris, Brian | Write | Push to dev branches, open PRs. Cannot merge to main without review. |
| Syntora (us) | Outside Collaborator | Scoped to repos we're actively working on. Removed when done. |

## Sean Code Review Findings (2026-03-02)
Reviewed `agent_email_scraper_python.py` (one of Sean's Jeffers3 scrapers):
- **Critical:** No pagination -- `$top=100` but they get 1000+ emails/day. Missing 90% of daily emails on high-volume days.
- **Bug:** `cleanup_excel_file()` deletes from current directory, but file is saved to network share. Never hits the right file.
- **Bug:** `fetch_emails_and_create_excel()` always returns `None` instead of the output path.
- **Minor:** Bare `except: pass` clause swallows all errors during column width calculation.
- **Positive:** AWS Secrets Manager for credentials, Microsoft Graph API (modern), clean regex extraction, date-based folder organization.
- **Conclusion:** Sean writes solid code. The bugs are exactly what a single PR review would catch. This is a process gap, not a skill gap.

## Compliance History (Internal Only -- Never Mention on Calls)
- **2016 CFPB enforcement:** Faloni & Associates altered Citibank affidavits (dates/amounts after execution), filed in NJ courts. $15k penalty. Citibank hit for $11M refund + $34M forgiven + $3M penalty.
- **2024 reprimand (David Jr.):** RPC 1.4(c) + RPC 1.5(b) -- fee disclosure failures.
- **2025 admonition (David Jr.):** RPC 1.15(a) trust account commingling + RPC 1.15(d) recordkeeping + RPC 8.1(b) failure to cooperate with ethics investigation.
- **David Sr.** also on NJ Disciplinary Review Board's disciplined attorneys list.
- **Implication:** Audit trails, code review gates, and Trisha as required reviewer aren't just nice-to-haves. They're protection. Never position it this way to the client.

## Notes
- David came through an older/deprecated booking link -- source unclear but likely website
- Firm founded 1975. David Sr. admitted to NJ bar 1969. Seton Hall for BA + JD.
- Multiple entities: Faloni Law Group LLC, Faloni & Associates LLC, Faloni & Wu LLP
- Trisha has authority but is not deeply technical -- security is her concern
- Sean is the technical bridge -- code structure, mentorship, infrastructure knowledge
- Darsh started Sep 2025, full-time Jan 2026. Learning curve was manageable with Sean's mentorship.
- Chris has never been on a call. Must get him on a discovery call.
- "Our one job is to make sure we collect all the data coming in and put it into the system as fast and accurate as possible" -- Trisha (core mission statement)
- Vendors in India and Africa are on phones with debtors, need real-time accurate data from JST
- Sean on GitHub: "it's not my decision, it's something the whole team should go over because it's a big bridge to cross"
- BBB: A+ rated, not accredited, 50 years in business
- Websites: falonilaw.com (elder law/estate), falonilawfirm.com (debt collection)
- Minimal online presence: 4 LinkedIn followers, no significant review volume

## Folder Index
```
falonilaw/
  PROSPECT.md                                        <- You are here
  meetings/
    2026-02-18-discovery-call.md                     <- Call 1 notes + transcript
    2026-02-24-discovery-call-2.md                   <- Call 2 notes + transcript
  research/
    feb-24-call-prep.md                              <- Call 2 prep + questions for Sean
    sean-questions.md                                <- Technical questions for Sean
    debt-collection-industry-guide.md                <- Full industry/JST/AI reference guide
    sean-code-review.md                              <- Analysis of Sean's email scraper script
    2026-03-03-proposal-wireframe.html               <- Internal call guide (14 slides + presenter notes)
    2026-03-03-proposal.html                         <- Client-facing proposal v1 (original $16-25k scope)
    2026-03-03-proposal-v2.html                      <- Client-facing proposal v2 ($3,650 GitHub setup)
  notes/
    2026-02-24-post-call-strategy.md                 <- Strategic pivot: consulting > staff aug
    2026-03-02-excalidraw-feedback.md                <- Master technical reference (pipeline, GitHub, pricing)
    2026-03-02-excalidraw-feedback.html              <- HTML version of above
    2026-03-02-meghna-feedback.md                    <- Feedback letter for Meghna on her deck
    2026-03-02-meghna-feedback.html                  <- HTML version of above
```
