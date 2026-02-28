# RealPage API Research

## Overview
RealPage supports both SOAP and REST APIs.
- SOAP: XML-based, SOAP 1.1 only
- REST: documented via Swagger
- All vendors need a RealPage-provided API key
- Developer Portal: https://developer.realpage.com
- API Explorer: https://developer.realpage.com/explore/api
- Vendor Registration: https://developer.realpage.com/get-started/vendor

## Authentication
Two methods available:
1. **UserAuthInfo**: Username, Password, SiteID, PmcID, InternalUser
2. **CallBackAuthInfo**: App, SessionID, SiteID, PmcID, EncryptionKey
- Transitioning to API Key-only auth (key in header)

## Partner Program (RealPage Exchange / RPX)
- **AppPartner**: Extensive review, vendor licenses APIs on client's behalf, listed in Integration Marketplace
- **Registered Vendor**: Lighter review, approved only for identified RealPage customers, client licenses APIs
- Certification required for both (infosec review, integration quality, scalability, security)
- Non-RPX vendors register at: https://developer.realpage.com/get-started/vendor
- RealPage charges extra fees for integrations (Sara confirmed this on call)

## Relevant API Endpoints Found

### 1. ApplyNow Web Service (CRITICAL)
**URL:** `https://onesite.realpage.com/webservices/residentservices/ApplyNow.asmx`

Key operations for Bear's use case:

| Operation | Description | Relevance |
|-----------|-------------|-----------|
| **FinalSaveWaitlistTaxCredits** | Save guestcard as waitlist for Tax Credits mixed use property | DIRECT HIT -- this is the waitlist endpoint for LIHTC |
| **FinalSaveAffordable** | Final save for affordable application | Affordable-specific save |
| **GetApplyNowWizardInitial** | Retrieves initial wizard data and object catalog | Get application structure/fields |
| **GetWaitlistWizardInitial** | Retrieves initial waitlist wizard data and object catalog | Get waitlist structure/fields |
| **GetEmployment** | Get employment information | Income data |
| **GetEmploymentJobTypes** | Get employment job type list | Job type classifications |
| **SaveWizardPageData** | Save wizard page information | Write data back to application |
| **GetWizardPageData** | Get wizard page information | Read application data |
| **GetApplyNowSummaryDetails** | Get the apply now summary | Full application summary |
| **GetFloorplanList** | Get floorplan preferences | Unit type matching |
| **GetUnitDetails** | Get additional unit details | AMI designation per unit |
| **FinalSaveWaitlistConventional** | Save guestcard as conventional waitlist | For comparison |
| **GetOnlineWaitlistDepositAndFee** | Get online waitlist fees | Fee structure |
| **GetRentalHistoryAddress** | Get rental history information | Verification data |
| **GetPetAndVehicle** | Get pet and vehicle information | Application data |
| **GetEmergencyContact** | Get emergency contact information | Application data |
| **GetQuoteDetails** | Get quote details | Pricing/rent data |

### 2. Prospect Management Service
**URL:** `https://onesite.realpage.com/WebServices/CrossFire/prospectmanagement/service.asmx`

| Operation | Description | Relevance |
|-----------|-------------|-----------|
| **InsertProspect** | Insert prospect | Create/update applicant records |
| **UpdateProspect** | Update prospect | Modify applicant data (e.g., AMI tag) |
| **ProspectSearch** | Search prospects | Query applicants |
| **GetUnitsByProperty** | Get units by property | Available units per property |
| **GetFloorPlanIDAndName** | Get floor plan ID and name | Unit type data |
| **GetAllProperties** | Get all properties | Property list |
| **GetLeasingAgentsByProperty** | Get leasing agents | Staff assignments |

InsertProspect request fields include:
- Name, email, address, phone
- Customer ID, relationship ID
- Move-in date, occupant count
- Floor plan preferences, desired rent, lease term
- Military fields, passport info
- Pet weight, prospect comments
- Lead source, leasing agent ID

Response statuses: NEW, DUPLICATE, EXISTING, ERROR

### 3. Pricing & Availability Service
**URL:** `https://onesite.realpage.com/WebServices/PricingAndAvailability/Service.asmx`

| Operation | Description |
|-----------|-------------|
| **GetUnitList** | List unit info including availability and pricing |
| **GetFloorPlanList** | Floor plan info including pricing |
| **GetRentMatrix** | Rent matrix data for apartments |
| **GetPickList** | Retrieve single pick list by type |
| **RetrieveLeaseEndingInfo** | Ending lease info |

## The Automation Opportunity (Mapped to APIs)

### Step 1: Read Application Data
- `GetApplyNowWizardInitial` -- get the application field structure
- `GetWizardPageData` -- read submitted application data
- `GetApplyNowSummaryDetails` -- get full application summary
- `GetEmployment` -- get employment/income data

### Step 2: Calculate Income & Determine AMI Bucket
- **This is our custom logic layer** (not in RealPage)
- Pull income data from application
- Apply LIHTC calculation rules:
  - Hourly x 2080 = annual
  - Aggregate all income sources
  - Asset imputation if > $5,000
  - Flag tips/commissions/bonuses for employer follow-up
- Compare against AMI limits (by county, household size)
- Assign AMI bucket (40%, 50%, 60%, 70%, 80%)

### Step 3: Write Back to RealPage
- `UpdateProspect` -- update prospect with AMI bucket tag
- `SaveWizardPageData` -- save calculated data back to application
- `FinalSaveWaitlistTaxCredits` -- save to tax credit waitlist with correct bucket

### Step 4: Auto-Communication
- Trigger email/notification on application receipt
- Include preliminary AMI qualification
- Notify of waitlist placement or next steps

## Competitive Reference

### Pay Score (already integrated with RealPage)
- Automated income verification
- Connects to 99% of North American banking institutions
- Also connects to payroll providers
- API or dashboard, PDF reports
- Setup in < 5 minutes (code snippet)
- $12/report range
- Focus: income verification accuracy, fraud reduction

### Snappt (integrated with Yardi, unclear on RealPage)
- Document fraud detection (99.8% accuracy)
- Identity verification
- Trained on 16M+ documents
- Focus: fraud detection, not income calculation

### Key Differentiator for Syntora
Pay Score and Snappt verify income. They don't:
- Calculate projected 12-month income (LIHTC requirement)
- Determine AMI bucket assignment
- Sort waiting lists by AMI
- Handle the full affordable housing eligibility workflow
- Auto-communicate qualification status to applicants

**Our value is in the LIHTC-specific calculation and sorting layer, not just income verification.**

## API Access Reality
**RealPage gates all API access.** No external calls without a RealPage-issued API key. Every vendor must register through their developer portal. There is no way to just hit their endpoints from the outside.

## Two Approaches to Present

### Option 1: Standalone Tool (No RealPage dependency)
**How it works:** Separate web app that Bear's team uses alongside RealPage. Admin exports or copies application data into our tool, it runs calculations, outputs AMI bucket assignments. Team manually updates RealPage.

**Pros:**
- No RealPage approval process needed
- No integration fees from RealPage
- Can build and deploy immediately
- Zero dependency on RealPage cooperation
- If RealPage changes their API, we don't break

**Cons:**
- Still some manual steps (copy data in, update RealPage manually)
- Not fully automated end-to-end
- Doesn't auto-sort the waiting list inside RealPage

**Could include:**
- Web-based income calculator with LIHTC rules baked in
- AMI bucket assignment engine (by county, household size, income limits)
- Flag tips/commissions/bonuses that need employer follow-up
- Asset imputation calculator
- Dashboard showing all applications sorted by AMI bucket
- Automated applicant notifications (email/SMS on application receipt + preliminary status)
- Exportable sorted waiting list

**Best for:** Fast deployment, proving value, getting Bear a win now while exploring deeper integration later.

### Option 2: RealPage Integration (Registered Vendor)
**How it works:** Register as a Registered Vendor through RealPage Developer Portal, sponsored by Bear. Get API key, build direct integration that reads application data, calculates income, writes AMI bucket back, sorts waiting list automatically.

**Pros:**
- Fully automated end-to-end
- No manual data transfer
- Waiting list sorted inside RealPage automatically
- Scales across all 26+ LIHTC communities
- Professional, production-grade solution

**Cons:**
- Requires RealPage approval (certification, infosec review)
- Bear must sponsor the vendor application
- RealPage may charge integration fees
- Timeline depends on RealPage's review process (unknown)
- Sara said RealPage is "a pain in the butt" with integrations

**API endpoints we'd use:**
- Read: GetWizardPageData, GetEmployment, GetApplyNowSummaryDetails
- Write: UpdateProspect, SaveWizardPageData, FinalSaveWaitlistTaxCredits
- Reference: GetUnitList, GetAllProperties, GetFloorPlanList

**Path:** Register at developer.realpage.com -> Bear sponsors -> API key issued -> build integration -> certification review -> deploy

**Best for:** Long-term solution, full automation, scalable across portfolio.

### Option 3: Hybrid (Recommended to Present)
**Phase 1:** Build standalone tool immediately. Bear gets value in weeks, not months. Solves the income calculation and AMI sorting problem right away. Admin still updates RealPage manually, but the 40+ hrs/week of hand calculations drops dramatically.

**Phase 2:** In parallel, start the RealPage Registered Vendor process. Once approved, plug the same calculation engine directly into RealPage via API. Eliminate the manual transfer step. Full automation.

This de-risks the project -- Bear gets immediate relief while the integration process plays out.

## Open Questions for March 4 Call
- Does Bear's RealPage contract allow third-party API access?
- Which specific OneSite modules do they have licensed?
- Can we get a sandbox/test environment from RealPage?
- What data fields are populated when an applicant applies online?
- How are AMI limits currently configured in their system?
- Would Bear sponsor our Registered Vendor application with RealPage?
- What does their current data export capability look like? (CSV, reports, etc.)
- Who is their RealPage account rep?

## Next Steps
1. Prep March 4 presentation with both options
2. Build proof-of-concept income calculation engine
3. Research RealPage Registered Vendor registration process in detail
4. Map AMI income limits for Bear's counties (Kenosha, Milwaukee, Madison)
5. Draft standalone tool wireframe/spec
6. Identify notification system approach (email, SMS)
