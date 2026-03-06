# Edge Acoustics

## Status
- **Stage:** Discovery Call Complete
- **First Contact:** 2026-03-05
- **Discovery Call:** 2026-03-05 (Parker, Branden)
- **Next Step:** Send discovery phase proposal to Branden
- **Source:** Google search

## Company Info
- **Name:** Edge Acoustics Ltd
- **Website:** TBD
- **HQ:** Vancouver, BC, Canada
- **Industry:** Commercial construction (specialty contractor -- acoustical ceilings and walls)
- **Size:** Small company, ~3 estimators + delivery fleet (3 trucks)
- **Primary Work:** Drop T-bar ceilings in offices and schools (commercial). Also acoustical walls. Minimal residential.

## Contacts
| Name | Role | Notes |
|------|------|-------|
| Branden West | Owner / Decision Maker | Primary contact. On discovery call. |
| (Head Estimator) | Lead Estimator | Name TBD -- key stakeholder for discovery phase |

## Tech Stack
| System | Platform | Notes |
|--------|----------|-------|
| Takeoff Software | **Plan Swift** | Quantity takeoff tool. Click corners on drawings, calculates distances/totals. Used ~10-15 years. Not locked in. |
| Pricing / Quoting | **Excel (Google Sheets)** | Manual entry from Plan Swift output. Contains pricing, markup, labor. Outputs basic PDF quote to customer. |
| Accounting / Invoicing | **QuickBooks** | Invoicing, inventory, pricing, payroll |
| Time Tracking | **TSheets** | Employee hour tracking via mobile app. Feeds into QuickBooks for payroll. |
| Environment | **Google Workspace** | Docs, Sheets, email. All Google. |

## Current Estimating Workflow
1. Customer sends drawings requesting a price
2. Estimator opens drawings in Plan Swift
3. Clicks through drawings page by page, identifying only acoustical scope (ignoring plumbing, lighting, etc.)
4. Plan Swift outputs quantities (e.g., 100ft of X, 500ft of Y, 1000ft of Z)
5. Estimator manually types quantities into Excel sheet with pricing, markup, labor
6. Excel calculates total cost
7. Estimator writes basic PDF quote and sends to customer
- **Average time per project:** ~1 hour
- **Range:** 20-30 min (small, e.g. 7-Eleven) to 8 hours (large, e.g. university)
- **Team:** 3 estimators

## Pain Points
1. **Missed items on takeoffs** -- flipping through pages to find only their scope is error-prone. Missing an area means standing behind a wrong quote.
2. **Time spent on manual takeoff review** -- bulk of time is scanning drawings page by page to find relevant scope
3. **DIY AI attempts failed** -- internal team tried to implement AI themselves, gave up ("it's not going to work")
4. **Manual data entry** -- Plan Swift output manually typed into Excel
5. **No route optimization** -- 3 delivery trucks planned manually each day
6. **Manual payroll flow** -- TSheets hours manually flow into QuickBooks

## Our Proposed Approach
### Phase 1: Discovery (Estimating) -- $485
- 3 calls total: 2 with head estimator (screen share of full workflow), 1 deliverable presentation
- Map automation opportunities across the estimating pipeline
- Architect solution for AI-assisted drawing review / takeoff verification
- Deliverables: process map, AI/automation opportunity map, implementation proposal

### Phase 2: Implementation (Estimating -- Post-Discovery)
- AI as safety net: reviews drawings, spot-checks takeoffs for missed items
- Goal: augment estimators, not replace them. Human always reviews.
- Potential integration with Plan Swift or alternative approach
- Scope depends on discovery findings

### Phase 3: Expand to Other Departments
- **Accounting:** Automate TSheets -> QuickBooks payroll data flow
- **Fleet:** Route optimization for 3 delivery trucks (daily planning)
- Each new department gets its own discovery phase

## Key Quotes
- "We don't have super basic redundant tasks... ours is less redundant" -- Branden on why DIY failed
- "We're not looking to reduce [headcount]. We're just looking to be more efficient and be more on the ball" -- Branden
- "If you miss an area, you do have to stand behind your quote" -- Branden on estimating risk
- Wants to be more efficient so estimators can spend time on growth, marketing, sales, and better job costing

## Action Items
### Parker (Syntora)
- [x] Discovery call -- 2026-03-05
- [ ] **Send discovery phase proposal to Branden** (committed to getting out today)
- [ ] Research Plan Swift integration capabilities (API, export formats, plugin ecosystem)
- [ ] Research AI-assisted construction takeoff tools / drawing analysis
- [ ] Scope discovery phase: 2 calls with head estimator + follow-up

### Branden (Edge Acoustics)
- [ ] Connect Parker with head estimator for discovery calls (screen share of workflow)
- [ ] Facilitate follow-up discussions for other departments (accounting, fleet) after estimating success

## Notes
- Branden is bought in on the partnership/consultancy model. Tried DIY, it failed, wants an expert.
- Company is growth-minded -- time savings reinvested into marketing, sales, job costing. Not cutting staff.
- Google environment is a plus for integration/automation.
- Plan Swift has been used 10-15 years but they're not locked in. Open to alternatives.
- Specialty contractor means they only care about a subset of items in any drawing set -- filtering signal from noise is the core challenge.
- Residential is minimal (theater rooms, etc.). Commercial is the bread and butter.
- Branden found Syntora through Google search.

## Folder Index
```
edgeacoustics/
  PROSPECT.md                                    <- You are here (source of truth)
  meetings/
    2026-03-05-discovery-call.md                 <- Full call notes + transcript summary
  notes/
  research/
    2026-03-05-discovery-proposal.html           <- Discovery phase proposal for Branden ($485)
```
