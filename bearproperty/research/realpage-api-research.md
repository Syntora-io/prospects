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

## How This Fits Our Products

### Product A: Communication Engine (No RealPage dependency)
Does not need RealPage API access. Runs standalone with CSV-exported contact info.
- Automated applicant notifications (SMS + email)
- Document completeness checks
- Missing doc follow-up (Day 0, 5, 10)
- 90-day expiration warnings
- Denial notices (HUD/FCRA compliant)

### Product B: LIHTC Income Engine (No RealPage dependency)
Does not need RealPage API access. Runs standalone with CSV upload or manual entry.
- Income calculation with all LIHTC source types
- AMI bucket assignment by county + household size
- Asset imputation, flagging, confidence scoring
- Dashboard with sorted waiting list
- Exportable sorted CSV to update RealPage manually

### RealPage Integration (End State)
Connects both products directly to RealPage via API. Registration starts Day 1, runs in background while Bear uses standalone products.

**API endpoints we'd use:**
- Read: GetWizardPageData, GetEmployment, GetApplyNowSummaryDetails
- Write: UpdateProspect, SaveWizardPageData, FinalSaveWaitlistTaxCredits
- Reference: GetUnitList, GetAllProperties, GetFloorPlanList

**Path:** Register at developer.realpage.com -> Bear sponsors -> API key issued -> build integration -> certification review -> deploy

**Why it's the end state:** Bear runs 26 LIHTC communities in RealPage with 7 more coming. CSV doesn't scale to 37 properties. Both products work standalone today -- integration removes the manual handoff when registration clears.

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
