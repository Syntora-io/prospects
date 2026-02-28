# Bear Property - Technical Approach

## Phase 1: Standalone Engine (No RealPage dependency)

### What It Is
Python-powered web application that Bear's team uses alongside RealPage. Handles all income calculations, AMI bucket assignment, waiting list sorting, and applicant notifications. Bear's admin feeds it data, gets sorted results back, updates RealPage manually.

### Architecture

```
DATA IN
  |
  |-- Option A: CSV upload (admin exports from RealPage)
  |-- Option B: Manual form entry (admin enters per applicant)
  |-- Option C: Bulk paste from spreadsheet
  |
  v
PYTHON ENGINE
  |
  |-- income_calculator/
  |     |-- hourly_income.py        (rate x 2080)
  |     |-- salary_income.py        (straight annual)
  |     |-- overtime_handler.py     (historical avg or employer projection)
  |     |-- tips_commissions.py     (flag for employer callback)
  |     |-- self_employment.py      (Schedule C net income)
  |     |-- social_security.py      (annual benefit amount)
  |     |-- child_support.py        (court-ordered amount annualized)
  |     |-- other_income.py         (disability, informal support, etc.)
  |     |-- income_aggregator.py    (sum all sources per household)
  |
  |-- asset_calculator/
  |     |-- asset_verification.py   (total assets, flag if > $5,000)
  |     |-- imputed_income.py       (passbook rate x total assets)
  |     |-- home_program_check.py   (verify assets regardless of amount)
  |     |-- disposed_assets.py      (FMV check on 2-year dispositions)
  |
  |-- ami_engine/
  |     |-- hud_income_limits.py    (load limits by county + household size)
  |     |-- bucket_assignment.py    (compare income to 40/50/60/70/80% thresholds)
  |     |-- over_under_flag.py      (flag if doesn't qualify for any bucket)
  |
  |-- notification_service/
  |     |-- application_received.py (auto-email on receipt)
  |     |-- qualification_status.py (preliminary AMI result)
  |     |-- waitlist_placement.py   (added to waitlist notification)
  |     |-- denial_notice.py        (over-income / under-income notice)
  |
  |-- flagging/
  |     |-- employer_callback.py    (tips/commissions/bonuses detected)
  |     |-- missing_docs.py         (required verifications not yet received)
  |     |-- student_status.py       (HOME units, financial aid check)
  |     |-- program_specific.py     (per-property layering rules)
  |
  v
DASHBOARD (Web UI)
  |
  |-- Application inbox: all new applications, sorted by date
  |-- AMI sorted view: applications grouped by 40/50/60/70/80%
  |-- Action queue: flags needing human attention (employer callbacks, missing docs)
  |-- Waiting list: sorted by AMI bucket, "next in line" per bucket
  |-- Unit matching: available units by AMI tier, match to waitlist
  |-- Export: sorted CSV to update RealPage manually
  |-- Reporting: denial rate, processing time, applications per week
  |
  v
DATA OUT
  |
  |-- Sorted waiting list (CSV export for RealPage update)
  |-- Applicant notifications (email/SMS)
  |-- Action items for staff (employer callbacks, doc requests)
```

### Tech Stack
- **Backend:** Python (FastAPI)
- **Database:** Supabase (Postgres)
- **Frontend:** Next.js or simple React dashboard
- **Email:** Resend or SendGrid
- **Hosting:** Vercel (frontend) + DigitalOcean or Railway (backend)
- **HUD Data:** Annual income limit tables loaded from HUD datasets

### Data Model (Core)

```
properties
  - id
  - name
  - county / MSA
  - ami_tiers (which buckets: 40, 50, 60, 70, 80)
  - program_layering (LIHTC only, LIHTC + HOME, etc.)
  - unit_count

units
  - id
  - property_id
  - unit_number
  - bedroom_count
  - ami_designation (40%, 50%, 60%, 70%, 80%)
  - status (available, occupied, pending)

applications
  - id
  - property_id
  - applicant_name
  - household_size
  - application_date
  - status (new, calculating, flagged, bucketed, waitlisted, assigned, denied)
  - assigned_ami_bucket
  - calculated_annual_income
  - realpage_id (for cross-reference)

income_sources
  - id
  - application_id
  - household_member
  - source_type (employment, overtime, tips, commissions, self_employment, social_security, child_support, disability, other)
  - pay_type (hourly, salary, annual)
  - rate
  - hours_per_year (default 2080 for full-time hourly)
  - annual_amount (calculated)
  - needs_employer_verification (boolean)
  - verified (boolean)

assets
  - id
  - application_id
  - asset_type
  - value
  - imputed_income (calculated if total > $5,000)

ami_limits
  - county
  - year
  - household_size
  - pct_40
  - pct_50
  - pct_60
  - pct_70
  - pct_80

flags
  - id
  - application_id
  - flag_type (employer_callback, missing_doc, student_status, over_income, under_income)
  - resolved (boolean)
```

### Key Calculation: AMI Bucket Assignment

```
Input:
  - All income sources for household (aggregated annual)
  - Imputed asset income (if applicable)
  - Household size
  - Property county/MSA

Process:
  1. Sum all annual income sources
  2. Add imputed asset income if total assets > $5,000
  3. Total = gross annual household income
  4. Look up AMI limits for county + household size
  5. Compare total to each threshold:
     - If income <= 40% AMI limit -> bucket = 40%
     - If income <= 50% AMI limit -> bucket = 50%
     - If income <= 60% AMI limit -> bucket = 60%
     - If income <= 70% AMI limit -> bucket = 70%
     - If income <= 80% AMI limit -> bucket = 80%
     - If income > 80% AMI limit -> OVER INCOME (deny)
  6. Assign lowest qualifying bucket (applicants want lowest rent)

Output:
  - AMI bucket assignment
  - Calculated gross annual income
  - Breakdown by income source
  - Flags for employer verification needed
  - Confidence level (high if all standard, lower if tips/commissions need verification)
```

### What This Solves Immediately
- Admin's 40+ hrs/week hand-calculating income -> batch upload, get results in seconds
- Manual AMI annotation next to names in RealPage -> sorted dashboard view
- 4-5 denials per acceptance -> pre-screen before full processing, save time on non-qualifiers
- Slow applicant response time -> auto-notifications on receipt
- No waiting list sorting in RealPage -> sorted export by AMI bucket


---


## Phase 2: RealPage Integration (If/When Approved)

### What Changes
Same Python engine from Phase 1. The only difference is how data gets in and out.

```
Phase 1:  CSV upload -> Engine -> CSV export (manual)
Phase 2:  RealPage API -> Engine -> RealPage API (automated)
```

### Integration Points

| Phase 1 (Manual) | Phase 2 (API) |
|-------------------|---------------|
| Admin uploads CSV | GetWizardPageData pulls application data |
| Admin enters applicant info | GetEmployment pulls income data |
| Engine calculates, dashboard shows results | Engine calculates (same logic) |
| Admin exports sorted CSV | UpdateProspect writes AMI tag back |
| Admin updates RealPage by hand | FinalSaveWaitlistTaxCredits sorts into correct bucket |
| Admin sends emails manually | SaveWizardPageData updates application record |

### API Endpoints We'd Use
**Read:**
- `GetApplyNowWizardInitial` -- application field structure
- `GetWizardPageData` -- submitted application data
- `GetApplyNowSummaryDetails` -- full application summary
- `GetEmployment` -- employment/income data
- `GetUnitList` -- available units by property
- `GetAllProperties` -- property list across portfolio

**Write:**
- `UpdateProspect` -- write AMI bucket tag to prospect record
- `SaveWizardPageData` -- save calculated data back to application
- `FinalSaveWaitlistTaxCredits` -- place into tax credit waitlist with correct bucket

### Webhook/Polling
- RealPage may not support webhooks (TBD during vendor registration)
- Fallback: poll for new applications on a schedule (every 15 min, hourly, etc.)
- Or: RealPage triggers on new application -> notifies our engine


---


## RealPage Developer Application Strategy

### Registration Path: Registered Vendor
- URL: https://developer.realpage.com/get-started/vendor
- Registered Vendor = approved for specific RealPage customer(s) only
- Bear sponsors the application (client-side licensing)
- Lighter review than full AppPartner

### What We Need From Bear
1. Willingness to sponsor our vendor registration
2. Their RealPage PMC ID and Site ID(s)
3. Confirmation their contract allows third-party API access
4. Introduction to their RealPage account rep (if possible)
5. Access to a test/sandbox environment (or a non-production property to test against)

### What RealPage Will Likely Require From Us
1. Company registration and contact info
2. Description of integration use case
3. Infosec review (how we handle data, encryption, storage)
4. Technical review of our API usage patterns
5. Certification testing before production access

### Timeline Estimate (Unknown, but educated guess)
- Registration + initial review: 2-4 weeks
- Infosec review: 2-4 weeks
- API key issuance + sandbox access: 1-2 weeks
- Integration development + testing: 4-6 weeks
- Certification: 2-4 weeks
- **Total: 3-5 months before production API access**

This is exactly why Phase 1 matters. Bear can't wait 3-5 months. The standalone tool delivers value in weeks while the integration process runs in parallel.

### Future: AppPartner (Optional, Long-Term)
If this works for Bear and we want to sell to other RealPage customers:
- Apply for AppPartner status (extensive review)
- Get listed in RealPage Integration Marketplace
- Vendor licenses APIs on client's behalf (simpler for clients)
- Opens up the entire RealPage affordable housing customer base
- This becomes a product, not a one-off project


---


## Summary: What to Present March 4

| | Phase 1: Standalone | Phase 2: RealPage Integration |
|---|---|---|
| **Dependency** | None | RealPage vendor approval |
| **Timeline to value** | Weeks | Months |
| **Manual steps** | Admin uploads data, exports sorted list | Fully automated |
| **Solves AMI sorting** | Yes (in our dashboard) | Yes (inside RealPage) |
| **Solves income calc** | Yes | Yes (same engine) |
| **Solves notifications** | Yes | Yes |
| **Risk** | Low | Medium (RealPage approval, fees, timeline) |
| **Recommendation** | Start here | Run in parallel |
