# March 4 Call Prep - Bear Property Management

**Date:** TBD -- Jenny OOO March 4-6, offered March 9, 11, or 12. Waiting on confirmation.
**Original Date:** Wednesday, March 4, 2026 -- 9:30-10:30am CT
**Attendees:** Parker Gawne, Meghna Shindhe, Sara Luster, Jenny Armor
**Platform:** Google Meet

---

## Before the Call
- Review PROSPECT.md for full context
- Have technical-approach.md open for reference
- Have realpage-vendor-application-draft.md ready to screen share if needed

---

## Talk Track

### 1. Open + Jenny Intro (5 min)

"Sara, great to see you again. Jenny, great to meet you -- Sara's told us a lot about the work you're doing on the asset management side. Before we dive in, quick recap for Jenny's context."

**Recap for Jenny:**
- We're looking at automating the LIHTC application review process
- Sara's team is spending 40+ hours/week manually opening applications, hand-calculating income, and sorting applicants into AMI buckets
- RealPage can't auto-sort the waiting list by AMI, so they're annotating names manually
- 4-5 denials for every acceptance -- most of that manual work is on people who won't qualify
- We researched RealPage's platform and API capabilities and want to walk through what we found

### 2. What We Found (10 min)

"We spent the last week going deep on RealPage's developer platform. Here's what we found."

**RealPage API access is real, but gated:**
- RealPage has public APIs for Prospect Management, Resident Management, Units, Pricing
- All access requires vendor registration through their developer portal
- Bear would sponsor our application as a Registered Vendor
- There's a review/certification process on RealPage's side

**The good news:**
- Pay Score and Snappt have already proven the integration path works
- RealPage has specific SOAP endpoints for tax credit waitlist operations (FinalSaveWaitlistTaxCredits)
- We can read application data, calculate income, and write AMI assignments back

**The reality:**
- RealPage vendor approval could take months
- Bear can't wait that long, especially with buildings coming online every few months on the Core List

### 3. Present the Phased Approach (10 min)

**Phase 1: Standalone Tool (start now)**

"We build a web application your team uses alongside RealPage. Your admin uploads application data -- CSV export, form entry, or paste from a spreadsheet. Our engine runs all the LIHTC income calculations instantly and sorts everyone into the right AMI bucket."

What it does:
- Calculates projected 12-month income from all source types (hourly x 2080, salary, Social Security, child support, disability, everything)
- Flags tips, commissions, and bonuses that need employer callback
- Assigns AMI bucket (40/50/60/70/80%) based on county income limits and household size
- Handles asset imputation if over $5,000
- Flags HOME program units that need extra student status and asset verification
- Dashboard showing all applications sorted by AMI bucket
- "Next in line" view per bucket when a unit opens
- Automated email notifications to applicants (receipt, preliminary qualification, waitlist placement)
- Exportable sorted waiting list to update RealPage

What it solves immediately:
- That admin doing 40+ hrs/week of hand calculations? Batch upload, results in seconds
- Pre-screens the 80% that get denied before your team spends time on full processing
- Applicant response time improves -- auto-emails go out immediately
- No RealPage dependency, no approval process, no integration fees

**Phase 2: RealPage Integration (run in parallel)**

"While your team is using the standalone tool, we register as a vendor with RealPage, sponsored by Bear. Once approved, we plug the same calculation engine directly into RealPage via API. No more manual data transfer -- applications flow in automatically, AMI buckets write back automatically, waiting list sorts itself."

Same engine, just automated pipes instead of manual upload/export.

### 4. Questions for Bear (15 min)

**RealPage:**
- Does your RealPage contract allow third-party vendors to access APIs on your behalf?
- Who is your RealPage account rep?
- Which OneSite modules do you have? (Leasing, Affordable, Waitlist, Compliance?)
- Would Bear sponsor our Registered Vendor application?
- Can you export waiting list data from RealPage today? CSV, report, anything?

**Communication:**
- What email system does Bear use -- Google Workspace or Microsoft 365?
- Do you want applicant notifications to come from a Bear email address (e.g., leasing@bearproperty.com)?
- Do you want SMS notifications in addition to email?
- Does your compliance team need to review notification templates before they go live?
- Do you have existing email templates your team uses for applicant communication?
- Who currently handles applicant communication -- the leasing agents, the admin, or both?

**Scope:**
- Should we pilot on the Core List (576 units, Milwaukee) or a different property?
- Should Dawn Parmelee's compliance team validate our calculation logic before go-live?
- Are the AMI buckets the same across all 26 communities or do they vary by property/county?

**Data:**
- When an applicant fills out the online application, what income fields are they entering? (Hourly rate? Employer? Pay frequency?)
- How are AMI income limits configured in your system -- do you update annually when HUD publishes?
- Can you export waiting list data from RealPage right now? CSV, report, anything?

### 5. Deep Dive (if time allows)

Pull from discovery-questions.md -- income calculations, asset verification, HOTMA changes, TIC completion, recertifications. Only go here if we have time.

### 6. Close + Next Steps (5 min)

**Get agreement on:**
- Which approach (Phase 1 standalone, Phase 2 integration, or hybrid -- push for hybrid)
- Pilot property
- Who needs to be involved going forward (Dawn for compliance validation?)
- Next deliverable from us (scope doc? prototype? pricing?)
- Next meeting date

**If they say yes to sponsoring the vendor registration:**
- We need their PMC ID and Site ID(s)
- We'll submit the application after the call
- Set expectations: RealPage approval is on their timeline, not ours
- Phase 1 runs regardless

---

## Key Things to Remember

- **Jenny Armor is Asset Management (parent company).** She represents the CEO's interest. Speak to portfolio-level impact, not just one property.
- **Sara is evaluating whether we can actually do this.** Show the technical depth. Reference the specific API endpoints, the calculation logic, the data model.
- **Sara said RealPage is "a pain in the butt."** Don't oversell the integration timeline. Be honest about the process. That's why Phase 1 exists.
- **The CEO referred us.** This has top-down momentum. Don't let it stall.
- **Sara's magic wand answer was "the waiting list sorting."** Keep coming back to that. Everything we're building leads to that outcome.
- **Don't quote pricing on this call unless directly asked.** If asked, say we need to finalize the scope first and will follow up with a proposal.

---

## Credibility: API Integration Experience

**When to drop this:** When RealPage comes up as "a pain in the butt," when Jenny asks about our technical capabilities, or when anyone asks "have you done integrations like this before?"

**The line:**
"We've built financial API integrations with Plaid and Stripe -- banking data, payment processing, account linking. Those are some of the most security-intensive integrations you can do. PCI compliance, SOC 2 environments, token-based authentication, encrypted data at every layer. RealPage's vendor security review covers the same ground we've already cleared on those projects."

**Why it matters to Bear:**
- Plaid = reading sensitive financial data from bank accounts (income verification, account balances). Directly relevant to what we'd do with RealPage application data.
- Stripe = processing payments with zero tolerance for errors or data leaks. Speaks to reliability and accuracy.
- Both require infosec reviews, encrypted transport, secure token handling -- exactly what RealPage's vendor certification process tests for.
- This is not our first time navigating a gated API ecosystem with a review process.

**What NOT to do:**
- Don't lead with this. Let it come up naturally.
- Don't compare RealPage's security to Plaid/Stripe directly (don't diminish their process).
- Don't list every project. Two names is enough. Financial APIs carry weight on their own.

---

## Objection Handling

**"Can't you just plug directly into RealPage?"**
Not without their approval. RealPage gates all API access. That's why we're recommending the hybrid approach -- Phase 1 gives you immediate relief while we work through the vendor registration.

**"We already looked at Pay Score / Snappt."**
Those verify income. We calculate projected 12-month LIHTC income and assign AMI buckets. Different problem. Pay Score tells you what someone earned. We tell you which AMI bucket they belong in.

**"What if RealPage doesn't approve the integration?"**
Phase 1 works regardless. Your team gets the same calculation engine, same sorted waiting list, same time savings. The only difference is the admin updates RealPage manually instead of it happening automatically.

**"How much does this cost?"**
We need to finalize scope first -- which properties, what volume, what features. We'll follow up with a detailed proposal after this call.

**"How long until we see results?"**
Phase 1 can be built and deployed in weeks. Phase 2 depends on RealPage's review timeline.
