# Bear Property Management

## Status
- **Stage:** Presenting Solution -- March 4
- **First Contact:** 2026-02-23
- **Discovery Call:** 2026-02-23 (Sara only, Jenny couldn't make it)
- **Next Step:** Follow-up call -- TBD (Jenny OOO March 4-6, offered 9th/11th/12th, waiting on confirmation)
- **Original Date:** Wed March 4, 9:30-10:30am CT (Google Meet)
- **Call Agenda:** Present phased approach, get RealPage integration buy-in, scope pilot
- **Call Prep:** research/march-4-call-prep.md

## Company Info
- **Name:** Bear Property Management (part of Bear Real Estate Group)
- **Website:** bearpropertymanagement.com
- **Parent:** Bear Real Estate Group (bearreg.com) - family of companies since 1924
- **CEO:** S.R. Mills (referred us to Sara, ex-Silicon Valley tech background)
- **HQ:** Kenosha, WI (offices also in Chicago, Madison, Milwaukee, Jackson WY)
- **Owner (BPM):** Marti Mills, President & Owner
- **Footprint:** Active projects in 20+ states; PM focused on SE Wisconsin & Northern Illinois
- **Sister Companies:** Bear Development, Bear Commercial, Bear Homes, Bear Capital, CMA

## LIHTC Portfolio
- 26 LIHTC communities currently managed
- 4 in lease-up right now
- 7 more in pipeline
- Big growth year, especially Madison region
- Core List (Milwaukee): 576 units, coming online 72 at a time through 2026

## Contacts
| Name | Role | Email | Notes |
|------|------|-------|-------|
| Sara Luster | VP of Property & Portfolio Management | sluster@bearproperty.com | Primary contact, on both calls |
| Jenny Armor | Asset Manager | jarmer@bearreg.com | Bear REG (parent co), joining March 4 call |
| S.R. Mills | CEO, Bear Real Estate Group | - | Referred us to Sara, executive sponsor |
| Marti Mills | President & Owner, Bear Property Mgmt | - | Likely family of S.R. |
| Julie Neibarger | Director of Property Management | - | Operations |
| Dawn Parmelee | Director of Compliance | - | Compliance/LIHTC rules |

## Tech Stack
- **RealPage** -- ALL LIHTC properties (26+ communities). Compliance, PM, budgeting, waiting list.
- **AppFolio** -- Commercial side only. 3 legacy market-rate properties. NOT relevant.
- **Screening provider** -- Separate, handles credit/background. Already working well.
- Online leasing in RealPage is new for tax credit (post-COVID)

## Pain Points (Confirmed on Call)
1. **#1 Priority: Waiting list sorting into AMI buckets** -- RealPage can't auto-sort. Manual annotation.
2. **Manual income calculation** -- Every application opened by hand, income hand-calculated.
3. **Response time** -- Bad Google reviews about slow responses.
4. **Denial volume** -- 4-5 denials per acceptance. 80% of manual work is wasted.
5. **90-day waiting list expiration** -- Manual action required or applications expire.

## Staffing on Core List (576 units)
- 1 admin: 40+ hrs/week JUST opening, sorting, bucketing
- 2 leasing agents: following up with sorted leads, group tours
- 2 assistant managers: normal management duties
- 7 total, wasn't planned this early
- Madison: opposite problem -- not enough leads, staff need to do marketing

## Competitive Landscape
- Pay Score -- integrated with RealPage, income verification ($12/report), NOT AMI calculation
- Snappt -- integrated with Yardi, document fraud detection, NOT AMI calculation
- Neither competitor does LIHTC-specific income projection or AMI bucket sorting

## Sara's Magic Wand Answer
"The waiting list sorting."

## Our Proposed Solution
- **Phase 1:** Standalone Python engine (no RealPage dependency) -- immediate value in weeks
- **Phase 2:** RealPage API integration (Registered Vendor) -- full automation, run in parallel
- Details: research/technical-approach.md

## Action Items (Pre-March 4)
- [x] Research RealPage API and integration possibilities
- [x] Look at Pay Score and Snappt as competitive reference
- [x] Map Bear's full application process end-to-end
- [x] Draft RealPage Registered Vendor application
- [x] Build March 4 call agenda with phased approach
- [ ] March 4, 9:30am CT -- present to Sara + Jenny Armor

## Notes
- Referral came from CEO (S.R. Mills) down to Sara -- top-down interest
- Jenny Armor (Asset Management, parent co) signals executive-level buy-in
- Sara doesn't know what we have built -- she's evaluating if we can do this
- Online leasing for tax credit is new industry-wide -- emerging problem
- Sara said RealPage is "a pain in the butt" with integrations
- RealPage gates all API access -- must register as vendor, Bear must sponsor

## Folder Index
```
bearproperty/
  PROSPECT.md                                  <- You are here
  meetings/
    2025-02-23-discovery-call.md               <- Full call notes
  research/
    march-4-call-prep.md                       <- March 4 talk track + agenda
    phase-mind-map.md                          <- Full mind map: Phase 1 + Phase 2 + comms
    discovery-questions.md                     <- Call 2 questions (deep dive)
    application-process-map.md                 <- End-to-end process flow
    technical-approach.md                      <- Phase 1 + Phase 2 architecture + data model
    realpage-api-research.md                   <- API endpoints, auth, partner program
    realpage-vendor-application-draft.md       <- Draft vendor registration (every field)
    lihtc-application-process.md               <- LIHTC compliance background research
  notes/
```
