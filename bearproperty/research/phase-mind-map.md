# Bear Property - Full Mind Map: Phase 1 + Phase 2

---

## PHASE 1: Standalone Engine

### Data In

```
HOW DOES DATA GET INTO OUR SYSTEM?

Option A: CSV Export from RealPage
  - Does RealPage allow waiting list export? (ASK MARCH 4)
  - What fields come in the export?
  - Admin downloads CSV -> uploads to our dashboard

Option B: Manual Form Entry
  - Admin opens application in RealPage
  - Enters key fields into our web form:
    - Applicant name
    - Household size
    - Income source(s) + amounts
    - Pay type (hourly/salary)
    - Assets
    - Property applying to
  - Faster than hand-calculating, but still manual entry

Option C: Copy/Paste from RealPage Screen
  - Structured paste from RealPage application view
  - Our system parses it

Option D: Email Forwarding (if applications arrive via email)
  - Parse incoming application emails
  - Extract data automatically
  - NEED TO KNOW: do applications come in via email too, or only through RealPage online portal?
```

### Processing Engine

```
INCOME CALCULATION
  |
  |-- For each household member:
  |     |-- Employment income
  |     |     |-- Hourly: rate x 2080
  |     |     |-- Salary: annual figure
  |     |     |-- Part-time: rate x actual annual hours
  |     |     |-- Overtime: FLAG for employer verification
  |     |     |-- Tips: FLAG for employer verification
  |     |     |-- Commissions: FLAG for employer verification
  |     |     |-- Bonuses: FLAG for employer verification
  |     |
  |     |-- Other income
  |     |     |-- Social Security: annual benefit
  |     |     |-- Disability: annual benefit
  |     |     |-- Child support: court-ordered annual
  |     |     |-- Divorce decree income: annual
  |     |     |-- Self-employment: Schedule C net (2yr avg)
  |     |     |-- Seasonal: projected annual from actual period
  |     |     |-- Informal support: estimated annual
  |     |
  |     |-- Assets
  |           |-- Total < $5,000: self-cert OK (unless HOME layered)
  |           |-- Total > $5,000: verify + imputed income calc
  |           |-- HOME layered: verify regardless
  |           |-- Retirement accounts: only if actively drawing (HOTMA)
  |           |-- Disposed < FMV in last 2 years: add imputed value
  |
  |-- Aggregate all household members
  |-- Total = gross annual household income + imputed asset income
  |
  v
AMI BUCKET ASSIGNMENT
  |
  |-- Load HUD income limits for property county + year
  |-- Look up limit by household size
  |-- Compare total income to thresholds:
  |     40% -> 50% -> 60% -> 70% -> 80% -> OVER INCOME
  |-- Assign lowest qualifying bucket
  |
  v
FLAGGING
  |
  |-- Tips/commissions/bonuses: needs employer callback
  |-- Over income: deny
  |-- Under income for requested unit: suggest lower bucket
  |-- Missing information: flag for follow-up
  |-- HOME unit: needs student status verification
  |-- HOME unit: needs asset verification regardless of amount
  |-- Self-employed: needs tax returns
  |-- Seasonal: needs projection documentation
  |
  v
CONFIDENCE SCORE
  |
  |-- High: all standard income, no flags
  |-- Medium: some flags but likely qualifies
  |-- Low: tips/commissions/bonuses need verification, bucket could change
  |-- Denied: over income for all buckets
```

### Dashboard

```
VIEWS:
  - Application Inbox (all new, sorted by date)
  - AMI Sorted View (grouped by 40/50/60/70/80%)
  - Action Queue (flags needing human attention)
  - Waiting List (sorted by AMI, "next in line" per bucket)
  - Unit Availability (which AMI tiers have openings)
  - Denial Log (over-income, under-income, background fail)
  - Reports (denial rate, processing time, volume trends)

PER APPLICATION VIEW:
  - Applicant info
  - Household members
  - Income breakdown by source
  - Asset summary
  - Calculated gross annual income
  - Assigned AMI bucket
  - Confidence score
  - Flags / action items
  - Communication history
  - Status timeline
```

### Communication Layer (CRITICAL)

```
WHAT WE NEED TO KNOW (ASK MARCH 4):
  - What email system does Bear use? Gmail (Google Workspace) or Outlook (Microsoft 365)?
  - Do they want notifications sent FROM a Bear email domain (e.g., leasing@bearproperty.com)?
  - Or is a separate notification system acceptable (e.g., notifications@syntora.io)?
  - Do they also want SMS notifications?
  - Do they have existing email templates for applicant communication?
  - Are there compliance requirements around what can/can't be said in automated messages?

AUTOMATED MESSAGES:

1. Application Received
   - Trigger: new application enters system
   - To: applicant
   - Content: "We've received your application for [Property Name].
     Our team is reviewing your information and you'll hear from us
     within [X] business days."
   - Channel: email (+ SMS optional)

2. Preliminary Qualification
   - Trigger: engine completes calculation, no flags
   - To: applicant
   - Content: "Based on the information you provided, you may qualify
     for a [X]% AMI unit at [Property Name]. A team member will reach
     out to discuss next steps and schedule an appointment."
   - Channel: email

3. Additional Information Needed
   - Trigger: flags generated (missing docs, employer verification)
   - To: applicant
   - Content: "To continue processing your application, we need the
     following: [list of items]. Please provide these within [X] days."
   - Channel: email

4. Waitlist Placement
   - Trigger: qualified but no unit available
   - To: applicant
   - Content: "You've been placed on our waiting list for a [X]% AMI
     unit at [Property Name]. We'll contact you when a unit becomes
     available. Your position: [X]."
   - Channel: email

5. Unit Available
   - Trigger: unit opens + applicant is next in line
   - To: applicant
   - Content: "A unit matching your qualification is now available at
     [Property Name]. Please contact us within [X] days to schedule
     an appointment."
   - Channel: email + SMS

6. Denial Notice
   - Trigger: over-income, under-income, or background fail
   - To: applicant
   - Content: "After reviewing your application, we're unable to offer
     you a unit at [Property Name] at this time. Reason: [X]. You may
     reapply after [X] days."
   - Channel: email
   - NOTE: compliance team should review denial templates

7. 90-Day Waitlist Expiration Warning
   - Trigger: 75 days on waitlist (15-day warning)
   - To: applicant
   - Content: "Your application at [Property Name] will expire in 15
     days. Please confirm your continued interest by [date]."
   - Channel: email + SMS

8. Internal Staff Notifications
   - Trigger: various
   - To: Bear staff (leasing agents, admin)
   - Content: "New application bucketed: [Name] -> [X]% AMI"
     or "Action needed: employer callback for [Name]"
   - Channel: email or dashboard notification

IMPLEMENTATION OPTIONS:

Option A: Transactional Email Service (Resend, SendGrid, Postmark)
  - Send FROM a Bear domain (leasing@bearproperty.com)
  - Requires Bear to add DNS records (SPF, DKIM, DMARC)
  - Professional, branded, good deliverability
  - Bear controls the domain

Option B: Google Workspace / Outlook Integration
  - Send directly through Bear's existing email system
  - Gmail: Google Workspace API
  - Outlook: Microsoft Graph API
  - Messages appear in Bear's sent folder
  - Most seamless for their team
  - Requires Bear to grant API access to their email

Option C: Separate Notification System
  - Send FROM notifications@syntora.io or similar
  - No setup needed from Bear
  - Less branded, may look less professional to applicants
  - Fastest to implement

RECOMMENDED: Option A (transactional email from Bear's domain)
  - Professional, branded as Bear
  - Doesn't require access to their email system
  - Just DNS records
  - Can add SMS via Twilio if they want it
```

### Data Out

```
- Sorted waiting list (CSV export for RealPage manual update)
- Applicant notifications (email/SMS)
- Staff action items (employer callbacks, doc requests)
- Reports (exportable)
```

---

## PHASE 2: RealPage Integration

### What Changes from Phase 1

```
PHASE 1                          PHASE 2
---------                        ---------
Manual CSV upload           -->  API auto-pulls new applications
Manual form entry           -->  GetWizardPageData / GetEmployment
Same calculation engine     -->  Same calculation engine (no change)
Same dashboard              -->  Same dashboard (no change)
Same communication layer    -->  Same communication layer (no change)
CSV export for RealPage     -->  UpdateProspect writes AMI tag back
Manual waitlist update      -->  FinalSaveWaitlistTaxCredits auto-sorts
Staff checks dashboard      -->  Staff checks dashboard (no change)
```

### Integration Architecture

```
REALPAGE (Bear's system)
  |
  |-- [AUTO] Poll for new applications (every 15 min or webhook)
  |     |-- GetApplyNowWizardInitial (field structure)
  |     |-- GetWizardPageData (application data)
  |     |-- GetEmployment (income data)
  |     |-- GetApplyNowSummaryDetails (full summary)
  |
  v
SYNTORA ENGINE (same as Phase 1)
  |
  |-- Income calculation (same logic)
  |-- AMI bucket assignment (same logic)
  |-- Flagging (same logic)
  |-- Confidence scoring (same logic)
  |
  v
WRITE BACK TO REALPAGE
  |
  |-- UpdateProspect (write AMI bucket tag to prospect record)
  |-- SaveWizardPageData (save calculated data to application)
  |-- FinalSaveWaitlistTaxCredits (place into correct waitlist bucket)
  |
  v
COMMUNICATION (same as Phase 1)
  |
  |-- Auto-email applicant (same triggers, same templates)
  |-- Staff notifications (same)
  |
  v
DASHBOARD (same as Phase 1, plus)
  |
  |-- Real-time sync indicator (last poll time, sync status)
  |-- RealPage write-back confirmation (success/fail per application)
```

### What We Need for Phase 2

```
FROM BEAR:
  - RealPage PMC ID
  - RealPage Site ID(s)
  - Sponsorship of Registered Vendor application
  - Confirmation contract allows third-party API access
  - RealPage account rep intro (optional)
  - Test/sandbox property to develop against

FROM REALPAGE:
  - Vendor registration approval
  - API key
  - Sandbox environment
  - Documentation for specific endpoints
  - Infosec review completion
  - Certification sign-off

ESTIMATED TIMELINE:
  - Registration + review: 2-4 weeks
  - Infosec review: 2-4 weeks
  - API key + sandbox: 1-2 weeks
  - Development + testing: 4-6 weeks
  - Certification: 2-4 weeks
  - TOTAL: 3-5 months
```

---

## Questions to Add to March 4 Call

### Communication
- What email system does Bear use -- Google Workspace (Gmail) or Microsoft 365 (Outlook)?
- Do you want applicant notifications to come from a Bear email address (e.g., leasing@bearproperty.com)?
- Does your compliance team need to review notification templates before they go live?
- Do you want SMS notifications in addition to email?
- Do you have existing email templates your team uses for applicant communication?
- Who currently handles applicant communication -- the leasing agents, the admin, or both?
