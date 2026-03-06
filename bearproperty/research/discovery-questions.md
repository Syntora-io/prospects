# Bear Property - Call 1: Discovery (COMPLETED 2/23)

Answered. See meetings/2025-02-23-discovery-call.md


---


# Bear Property - Call 2: March 4, 9:30am CT

## Attendees
Parker Gawne, Meghna Shindhe, Sara Luster, Jenny Armor

## Agenda

### 1. Recap & Introductions (5 min)
- Introduce Jenny Armor
- Quick recap of discovery call findings for Jenny's context
- "We spent the last week researching RealPage's platform and your integration options"

### 2. Present What We Build (15 min)

**Product A: Communication Engine (standalone, no RealPage dependency)**
- Automated applicant notifications (receipt, missing docs, status updates, denial notices)
- Document completeness check before human review
- SMS + email follow-up for missing items (Day 0, Day 5, Day 10)
- 90-day waitlist expiration auto-warning
- Fixes response time and Google reviews immediately

**Product B: LIHTC Income Engine (standalone, no RealPage dependency)**
- Paste or upload application data, our engine calculates income and assigns AMI bucket
- Dashboard showing all applications pre-sorted by AMI
- Flagging for tips/commissions/employer callback
- No RealPage approval needed, no integration fees
- Your admin still updates RealPage manually, but the 40+ hours of hand calculations goes away

**RealPage Integration (end state, registration starts Day 1)**
- Direct API connection: reads applications, calculates income, writes AMI bucket back, sorts waiting list inside RealPage
- Connects both products to RealPage -- same engines, automated pipes
- Registration runs in background while Bear uses standalone products

### 3. Questions for Bear (15 min)

**RealPage Contract & Access**
- Does your RealPage contract allow third-party vendors to access APIs on your behalf?
- Who is your RealPage account rep? Have you worked with them on integrations before?
- Which OneSite modules do you have licensed? (Leasing, Affordable, Waitlist, Compliance?)
- Would Bear be willing to sponsor our Registered Vendor application with RealPage?

**Current Data Flow**
- When an applicant fills out the online application, what income fields are they entering? (Hourly rate? Employer name? Pay frequency?)
- Can you export waiting list data from RealPage right now? CSV, report, anything?
- How are AMI income limits configured in your system -- do you update them annually when HUD publishes new limits?
- Are the AMI buckets the same across all 26 communities or do they vary by property/county?

**Scope**
- Should we start with the Core List (576 units) as the pilot, or a different property?
- Would you want the automated notifications to come from Bear's email domain, or is a separate system fine?
- Besides Sara's team, would Dawn Parmelee's compliance team need to be involved in validating the calculation logic?

### 4. Deep Dive Questions (if time allows)

**Income Calculations**
- When your team is calculating gross annual income, are they pulling from pay stubs, VOEs from employers, or both?
- For applicants with multiple income sources -- W-2 employment plus child support plus Social Security -- is someone manually aggregating all of that on a worksheet?
- How are you handling self-employed applicants? Two years of tax returns and Schedule C?
- When you get seasonal or irregular employment, how does your team project forward to the anticipated 12-month income?

**Asset Verification**
- With the HOTMA changes moving the asset threshold to $50,000 -- has that changed your workflow?
- Are most applicants self-certifying under the threshold, or are you still doing a lot of asset verifications?
- How are you handling retirement accounts now that HOTMA says you only verify if actively drawing?

**Student Status**
- Are HOTMA student financial aid rules affecting your workflow?
- How often are student-status households in your applicant pool?

**TIC Completion**
- Once income and assets are calculated, who's completing the TIC?
- Are you populating TICs manually or does RealPage generate them?
- How long from completed application to signed TIC?
- Does Wisconsin HFA require pre-approval of initial TICs before move-in?

**Rent Calculation**
- Are you calculating max allowable rent manually -- 30% of AMI adjusted for household size, minus utility allowance?
- How often are utility allowances changing?

**Recertifications**
- Full annual recerts, or are any properties on the 100% LIHTC waiver?
- How far in advance do you start the recert process?
- Is recert workload comparable to initial certs?

**Document Management / Compliance**
- All digital in RealPage, or a mix of paper and digital?
- Confidence level when state does a file audit?
- XML reports to state HFA, or different format?

### 5. Next Steps & Timeline (5 min)
- Which products to start with (A, B, or both)
- Start RealPage registration Day 1 (need PMC ID, Site IDs)
- Define pilot scope (which property, which team)
- Identify next call / deliverable
