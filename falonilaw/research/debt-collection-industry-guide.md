# Debt Collection Law Firms -- Complete Guide
## Operations, Software & AI Transformation

Covering: Operations, JST CollectMax & Accis, Process Automation, AI Automation, RAG Systems, Discovery Questions for AI Agencies

---

## PART ONE: Debt Collection Law Firms -- What They Are & How They Operate

### What Is a Debt Collection Law Firm?

A debt collection law firm is a specialized legal practice hired by creditors -- banks, hospitals, utility companies, landlords, auto lenders, or any business that is owed money -- to recover unpaid debts from individuals or businesses. Unlike general collection agencies, these firms carry the full weight of legal authority: they can file lawsuits, obtain court judgments, and enforce collection through wage garnishment, bank levies, and property liens.

They sit at the intersection of law and finance, operating at massive scale. A mid-sized firm might actively manage 30,000 to 100,000 accounts simultaneously across multiple creditor clients, multiple debt types, and multiple jurisdictions -- all at the same time.

### Types of Debt They Handle

- **Consumer Debt** -- Credit cards, personal loans, auto deficiencies, medical bills, student loans
- **Commercial Debt** -- Business-to-business unpaid invoices, lines of credit
- **Real Estate & HOA** -- Landlord-tenant unpaid rent, homeowner association dues
- **Subrogation** -- Insurance reimbursement claims after payouts
- **Government & Utility** -- Unpaid utility bills, municipal fines, tax liens

### The Day-to-Day Operations

#### 1. Account Intake & Onboarding
When a creditor client sends over a new batch of accounts, the firm must receive, validate, and set up each account before any collection activity begins. This involves importing account data (debtor name, address, SSN, balance, original creditor, account history), running each account through bankruptcy databases to check if the debtor has filed, checking death registries to flag deceased debtors, verifying the statute of limitations hasn't expired, and flagging accounts with legal barriers like active bankruptcy stays or represented debtors.

#### 2. Skip Tracing & Debtor Location
A significant portion of debtors have moved, changed phone numbers, or are otherwise difficult to locate. Skip tracing is the process of searching databases -- credit bureau address data, DMV records, utility records, social media, and public records -- to find a current, valid contact address or phone number. Without a good address, a demand letter cannot be sent and a lawsuit cannot be properly served.

#### 3. Pre-Litigation Collections
Before filing a lawsuit, the firm typically attempts to resolve the debt through written demand letters and phone contact. This includes sending a Reg F-compliant validation notice within five days of first contact, managing the 30-day dispute window, documenting all consumer responses, negotiating payment plans or settlements, and recording all contact attempts with time-stamps for compliance purposes.

#### 4. Litigation Authorization & Filing
When pre-litigation efforts fail, an attorney reviews the account and decides whether to recommend a lawsuit. This is a judgment call weighing the balance owed, the debtor's apparent ability to pay, the jurisdiction's filing costs, and the creditor client's instructions. If authorized, the firm prepares a complaint, calculates exact figures (principal, accrued interest, court costs, attorney fees), drafts an affidavit, and files with the correct court -- which varies by debt amount and jurisdiction.

#### 5. Case Management & Court Tracking
Once a lawsuit is filed, the firm tracks every court date, deadline, and procedural requirement. This includes monitoring for debtor responses (answers, counterclaims), scheduling hearings, managing default judgment timelines (if the debtor doesn't respond), and coordinating with process servers for service of process.

#### 6. Post-Judgment Enforcement
After a judgment is obtained, the real collection work begins. The firm can now pursue wage garnishment (requiring employer compliance), bank account levies (requiring bank compliance), property liens, and asset discovery proceedings. Each of these involves separate legal filings, compliance with state-specific exemption rules, and coordination with third parties.

#### 7. Payment Processing & Trust Accounting
Every payment received -- whether a lump sum, settlement, or installment -- must be logged accurately, applied to the correct debt components (principal vs. interest vs. fees), held in a client trust account (IOLTA), and remitted to the creditor client on schedule after deducting the firm's fee. Trust accounting is heavily regulated and errors create both compliance and client relationship problems.

#### 8. Compliance Monitoring
Collection activity is governed by the Fair Debt Collection Practices Act (FDCPA), the Telephone Consumer Protection Act (TCPA), the CFPB's Regulation F, and a patchwork of state laws. Every letter, phone call, and legal filing must comply. Firms must maintain logs of all consumer contacts, track opt-in/opt-out preferences for texting and email, honor dispute requests, and ensure their staff are trained on current rules.

#### 9. Client Reporting & Audits
Creditor clients -- especially banks and large institutions -- require regular reporting on portfolio performance: accounts placed, accounts resolved, amounts collected, accounts in litigation, recovery rates, and age of portfolio. Many institutional clients conduct formal audits of their collection law firms, requiring detailed documentation of compliance practices, security protocols, and operational procedures.

---

## PART TWO: JST CollectMax & Accis

### JST: Company Overview
JST (JS Technologies, Inc.) is a Richmond, Virginia-based software company founded in 1985. Since 1987 it has been building debt collection software exclusively for law firms. With over 1,000 installations nationwide, JST is the market leader in legal debt collection software -- serving more collection law firms than any other high-end provider in the space. Their current flagship product is CollectMax, and their next-generation platform is Accis.

JST is employee-owned (ESOP since 2007), which contributes to the company's notably stable, long-tenured team. More than half of their staff have been with the company for over 10 years.

### CollectMax: Structure & Features

CollectMax is an on-premise Windows application built on an ADS (Advantage Database Server) foundation, backed by a PHP/MySQL architecture for its web-facing components.

#### The Four Pillars of CollectMax

**COMPLY** -- Built-in compliance tools including integrated complaint/dispute tracking, automatic call-time blocking based on TCPA rules, document suppression for bankruptcies, represented debtors, and Do Not Contact accounts, and MaxSecurity for PCI-compliant audit trails and data masking.

**COMPARE** -- Competitive cost structure: starts at $260/month subscription or one-time purchase. Unlimited debtor and client accounts. Modular -- pay only for features you need. No volume-based licensing fees.

**CONNECT** -- Pre-built EDI interfaces to dialers, skip tracers, payment processors (including PaymentVision), and other industry vendors. Well-regarded for the quality of its vendor integration program.

**GROW** -- Scales from single-attorney shops to 200+ seat firms without architecture changes. Easy user onboarding. Flexible configuration without programming knowledge required.

#### Key Features In-Depth

**MaxPlans -- Workflow Automation Engine**
MaxPlans is the heart of CollectMax's automation. It allows firms to design account 'tracks' -- sequences of automated events triggered on a schedule without any user intervention. An account placed on a MaxPlan will automatically receive the right letter on day 1, a follow-up on day 30, a litigation referral on day 60, and so on. Conditions can be layered in (using MaxConditions) so that the plan adapts based on debtor responses, payment activity, or account status changes.

**MaxUpdater -- Bulk Data Import**
MaxUpdater allows firms to import data from external files (CSV, Excel, tab or pipe delimited) and bulk-update CollectMax account fields. It uses configurable templates so firms can map any incoming file format to the correct fields. Used heavily for creditor-provided data updates, commission rate changes, and vendor-returned skip tracing results.

**MaxExtract -- Data Export Engine**
MaxExtract is the counterpart to MaxUpdater -- it pulls structured data out of CollectMax into flat files using configurable templates. Used for client audit reports, custom analytics, and feeding data to external reporting tools. Reviewers consistently cite it as one of the most practically valuable features, though note a learning curve in template configuration.

**MaxSecurity -- Audit & Compliance Layer**
Tracks every user who accesses any account. Generates full audit reports. Supports PCI compliance standards. Allows account-level lockdown (supervisor access only). Masks sensitive data like SSNs and account numbers from standard user views. Controls printing with password requirements or print-button disabling.

**Document Generation & Suppression**
Generates all legal correspondence and collection documents from configurable templates using merge variables. Critically, it also automatically suppresses document generation for accounts that carry a Do Not Contact flag, an active bankruptcy, or a represented-debtor flag -- preventing inadvertent FDCPA violations.

#### Integration Approach: EDI, Not API
CollectMax's integration model is file-based (EDI) rather than real-time API. Vendors exchange flat files on a schedule -- imported via MaxUpdater, exported via MaxExtract. JST builds specific connector programs for approved vendors (dialers, skip tracers, payment processors). There is no self-serve REST API for custom integrations, though JST has a System Integration Consultant on staff for custom data integration projects.

### Accis: The Next-Generation Cloud Platform

Accis is JST's complete rebuild of CollectMax on a modern technology stack, developed in partnership with Codal, a digital product firm. It is now in active production -- JST converted its first CollectMax customer to Accis in 2024 and is actively onboarding the broader customer base.

#### Architecture & Infrastructure

- **Cloud Hosting:** Amazon Web Services (AWS) -- hosted in the USA
- **Database:** Amazon RDS with AES-256 encryption at rest (AWS KMS managed keys)
- **Transport Security:** AWS Certificate Manager (ACM) -- TLS encrypted in transit
- **Media Storage:** AWS S3 with SSE-S3 server-side encryption
- **Security Certification:** Penetration tested and certified by Secureworks
- **Deployment Options:** Cloud (AWS hosted by JST) or Self-Hosted (customer infrastructure)
- **Technology:** Modern web-based application -- accessible via browser, no desktop install

#### What's New in Accis vs. CollectMax

| Dimension | CollectMax | Accis |
|-----------|------------|-------|
| Architecture | On-premise Windows app | Cloud-native (AWS) or self-hosted web app |
| Access | Desktop client on local network | Browser-based from anywhere |
| Integration Model | File-based EDI (batch) | API-based real-time vendor integrations |
| Accounting | Limited -- external tools often needed | QuickBooks Online integration (live) |
| Payment Processing | PaymentVision (EDI) | PaymentVision API integration (live) |
| Security Certification | PCI compliance tools | Secureworks certified penetration tested |
| Scalability | Limited by local server | AWS auto-scaling infrastructure |
| Deployment | Single model (on-premise) | Cloud or self-hosted customer choice |

#### API Access in Accis

This is one of the most important developments in the Accis platform. CollectMax had no REST API -- everything was batch file exchange. Accis is being built from the ground up as an API-integrated platform.

- **Confirmed live integrations built on real-time APIs:** QuickBooks Online (accounting sync) and PaymentVision (digital payment processing).
- **Stated architecture goal:** 'Support integration with industry vendor APIs' -- vendor integrations (dialers, skip tracers, credit bureaus, e-filing systems) will communicate with Accis via API rather than file exchange.
- **No published developer portal or public REST API documentation exists yet** -- meaning firms cannot currently build custom third-party integrations on a self-serve basis.
- **Inbound API access** (allowing external systems to push/pull data into Accis programmatically) is not yet publicly available. Firms needing custom integration should contact JST directly to discuss custom connector development.
- The cloud-native AWS architecture makes future public API exposure technically straightforward -- the infrastructure is ready even if the product roadmap hasn't confirmed a timeline.
- For firms evaluating Accis with API-driven integration needs -- custom client portals, AI workflow layers, CRM connections, or proprietary creditor system interfaces -- the key conversation to have with JST is whether they will expose inbound/outbound REST endpoints, and on what timeline.

---

## PART THREE: Process Automation, AI & RAG

### Process Automation Solutions (Rule-Based, No AI Required)

| Task | Manual Overload | Solution |
|------|----------------|----------|
| Account Intake & Data Onboarding | Staff manually enter rows from creditor spreadsheets, run individual bankruptcy/death checks one-by-one. A batch of 500 accounts takes a full day per person. Data entry errors are common and compliance flags get missed. | API-based auto-import pulls data directly from creditor systems. Simultaneous multi-database scrubbing (bankruptcy, death, SOL, OFAC) runs automatically. Only flagged exception accounts require human review. |
| Skip Tracing | Staff manually log into 2-4 skip tracing services, search each debtor individually, read results, and manually update the account. At scale this consumes hours per day. | Automated skip trace orders trigger based on account status rules. Results return via API or EDI and automatically update debtor address and phone fields. |
| Demand Letters & Notices | Staff pull template letters, manually merge debtor info, generate documents one-by-one. Errors in merge fields or missing suppression checks create FDCPA exposure. | MaxPlans-style workflow automation generates the correct compliant letter for every account on the correct schedule, with automatic suppression for DNC/bankruptcy/represented accounts. |
| Follow-Up Diary & Account Ticklers | Staff maintain manual calendar reminders or spreadsheet trackers. Things fall through the cracks. Coverage gaps during PTO create backlogs. | Rules-based diary systems automatically advance accounts through each workflow stage on schedule. Accounts not actioned within SLA windows auto-escalate. |
| Payment Plans & ACH Processing | Setting up a payment plan requires manual entry of each installment, manual ACH debit initiation, manual application of each payment to principal/interest/fees. | Payment plan setup automatically generates the ACH schedule, debits on schedule, applies payments to the correct ledger fields, flags NSF returns for follow-up. |
| Client Reporting | Account managers manually pull multiple reports, reformat in Excel, check figures, email to clients. For firms with 50+ clients this can consume 2-3 days per month. | Automated reporting pipelines generate portfolio reports on schedule and deliver them directly to client portals or email. Live dashboards give clients self-serve visibility. |

### AI Automation Solutions (Requires ML/AI)

| Task | Manual Overload | Solution |
|------|----------------|----------|
| Litigation Scoring & Case Triage | Attorneys manually review every account to decide whether to recommend filing. Sub-optimal accounts get filed; recoverable accounts miss their window. | ML model trained on historical case outcomes scores each account for likelihood of successful recovery (0-100). Attorneys focus exclusively on high-value and borderline cases. |
| Settlement Propensity Prediction | Settlement offers are made based on intuition or flat policy ('we always offer 60 cents on the dollar'). No systematic way to know which debtors will settle, at what amount. | AI model predicts each debtor's settlement propensity and optimal settlement range based on historical outcomes for similar profiles. |
| Compliance Review of Communications | Compliance depends on staff training and supervisor spot-checks. Letter templates are reviewed periodically but individual variations create violation risk. | AI compliance layer reviews every outgoing letter and communication against current federal and state law before it is sent. Flags potential violations, suggests corrections, logs the review. |
| Call Analytics & Monitoring | Supervisors can only manually review a small fraction of collection calls. Compliance violations, negotiation opportunities, and coaching needs go undetected. | AI transcription and analysis processes 100% of calls automatically. Flags FDCPA/TCPA language, scores collector performance, auto-generates call summaries. |
| Debtor Communication Optimization | All debtors receive the same contact sequence regardless of their likely responsiveness -- same channel, same frequency, same tone. | AI contact optimization analyzes prior response patterns to determine the best channel (letter, SMS, email, call), timing, and tone for each debtor. |
| Anomaly Detection in Payments & Accounting | Payment errors caught only through manual reconciliation or by mistake. Trust accounting errors create regulatory exposure. | AI continuously monitors payment activity for anomalies: duplicate amounts, unusual timing patterns, balance inconsistencies, and potential fraud indicators. |

### RAG (Retrieval-Augmented Generation) Use Cases

Critical design requirement: accuracy and citation. A collection firm acting on a hallucinated legal answer faces regulatory sanctions, malpractice exposure, and client liability. Every RAG response must cite its source document, flag confidence levels, and clearly distinguish between what the system knows and what it does not.

| Task | Manual Overload | Solution |
|------|----------------|----------|
| Compliance & Legal Knowledge Base | FDCPA, TCPA, Reg F, GLBA, and 50 different state laws create a knowledge maintenance problem. Staff make compliance decisions from memory. | RAG system indexed over federal statutes, CFPB rules, state AG guidance, court opinions, and the firm's own compliance memos answers any compliance question in seconds with direct citations. |
| Document Drafting Assistance | Attorneys and paralegals start every non-standard document from scratch or hunt through a template library. Jurisdiction-specific requirements require manual lookup. | RAG over the firm's template library, court local rules, and prior successful filings generates jurisdiction-specific document drafts on demand. |
| Client & Account Inquiry Handling | Creditor clients frequently call or email asking about specific accounts. This consumes account manager time for questions that have factual, retrievable answers. | RAG layer over live account data and client agreements handles routine client inquiries automatically through a self-serve portal or chat interface. |
| Staff Training & Onboarding | Debt collection firms have high staff turnover. New collectors and paralegals rely on supervisors to answer procedural questions. Written procedure manuals are rarely consulted and quickly outdated. | RAG system over the firm's procedure manual, compliance policies, software documentation, and FAQ history becomes an always-on training assistant. |
| Commercial Debtor Asset Research | For commercial collections, attorneys need to assess a debtor entity's asset position before recommending litigation. Manual searches of UCC filings, SOS records, real estate records, litigation history. | RAG over structured integrations with public business databases, UCC filing systems, and court records aggregates a debtor entity profile on demand. |

---

## PART FOUR: Discovery Questions for AI Agencies

### Category A: Operations & Volume Understanding

**Q1:** How many active accounts are you managing right now, and how many new accounts come in per month?
*Scale of manual overhead. 5,000 accounts vs 80,000 = different ROI math.*

**Q2:** Walk me through what happens the moment a new batch of accounts arrives from a client. Who touches it, and how long does it take?
*Surfaces intake process. Listen for manual data entry, manual database checks, spreadsheet steps.*

**Q3:** How do you currently decide which accounts to prioritize for litigation versus pre-litigation collection work?
*Reveals whether they have a scoring system or rely on gut feel.*

### Category B: Manual Overhead & Staff Time

**Q4:** If you think about where your staff spend the most time on repetitive, non-judgment tasks -- what comes to mind first?
*Single best question for identifying automation targets. Let them answer without leading.*

**Q5:** How much of your team's day is spent on client reporting, and how do you currently produce those reports?
*Manual client reporting is almost universally a significant time sink.*

**Q6:** When you hire a new collector or paralegal, how long does it take before they can work independently? What breaks down most often in the first 90 days?
*Quantifies the training and knowledge management problem.*

### Category C: Compliance & Risk

**Q7:** How do you currently ensure that outgoing letters and communications comply with Reg F and your state-specific rules? What happens if something slips through?
*Answer is usually 'training and spot-checks.' Opens the door to AI compliance monitoring.*

**Q8:** Have you had any CFPB complaints, FDCPA demand letters, or regulatory inquiries in the past two years? What triggered them?
*Past incidents are the most compelling data points.*

**Q9:** When a new regulatory rule comes out, how does that change get communicated to every person who handles consumer accounts?
*Identifies the knowledge management gap that a RAG compliance system addresses.*

### Category D: Technology & Data

**Q10:** What software are you currently running, and are there integration points you wish existed but don't?
*Tells you the ecosystem and surfaces integration gaps.*

**Q11:** How accessible is your data? If you wanted to run an analysis on your last three years of cases -- recovery rates by debt type, jurisdiction, debtor profile -- could you do that today?
*Most firms will say this would take days or is practically impossible.*

**Q12:** Are you on CollectMax's legacy on-premise version or have you moved to Accis? And are there any other software tools your team uses that aren't connected to your collection system?
*Current integration state and data silos.*

### Category E: Strategy & AI Awareness

**Q13:** What does your current recovery rate look like on average across your portfolio, and what do you think is dragging it down?
*Recovery rate is the north star metric.*

**Q14:** Are any of your creditor clients pushing you to use AI or technology tools as part of their vendor requirements?
*Large institutional creditors are increasingly requiring technology from their law firm vendors.*

**Q15:** When you think about the next three years -- what's the operational problem that, if you solved it, would have the biggest impact on the firm's performance and profitability?
*Closing question. Surfaces their self-identified priority.*

### Key Listening Signals
- They mention **spreadsheets** in any operational context = immediate automation opportunity
- They describe a process as **'it depends on who you ask'** = knowledge management and RAG opportunity
- They reference a **compliance incident** in the past 2 years = AI compliance monitoring is a priority sale
- They say **'we can't easily pull that data'** = analytics infrastructure and AI reporting are the entry point
- They describe decisions made by **'feel' or 'experience'** = AI scoring and prediction models are the pitch
- They mention **high staff turnover or training time** = RAG training assistant has immediate operational ROI
- They say **'our clients are asking for more visibility'** = automated reporting and client portals open the door
