# Questions for Sean -- Feb 24 Call

## 1. CollectMax vs Accis
- Are you on CollectMax (on-prem) or have you migrated to Accis (cloud)?
- If CollectMax: are you considering the Accis migration? Has JST reached out?
- If Accis: are you using the API integrations (QuickBooks, PaymentVision) or still doing file-based exchange?

*Why: This changes everything. CollectMax = EDI/flat file only, no REST API. Accis = API-native on AWS. Our approach to building on top of their system depends entirely on this answer.*

## 2. How Data Gets Out of JST
- When your Python scripts pull data from JST, how are they accessing it? Direct database queries against ADS? MaxExtract exports to CSV/Excel? Something else?
- Are the scripts reading from the live production database or from exported flat files?
- Do you use MaxUpdater to push data back in, or is it one-way (read only)?

*Why: CollectMax uses Advantage Database Server. If they're querying ADS directly, we need to understand the schema. If they're working off MaxExtract exports, we're downstream of a batch process. This determines how real-time anything we build can be.*

## 3. Script Inventory and Architecture
- Roughly how many active scripts are running right now?
- Are they standalone .py files or is there a shared codebase/repo?
- Any version control (Git) or is it files on the server?
- What triggers them -- Windows Task Scheduler, manual execution, something else?
- Are there any scripts that interact with external services (court websites, skip trace vendors, credit bureaus)?

*Why: We need to know if we're inheriting spaghetti or something organized. Version control tells us their maturity. Court website scraping scripts are the most fragile and highest-maintenance.*

## 4. The Backlog
- What scripts or automations does the team want built but hasn't had time for?
- Is there a list somewhere, or is it all in Chris's head?
- What's the single most requested thing that keeps getting pushed back?

*Why: This is what we get hired to do. The backlog is the scope.*

## 5. Error Handling and Monitoring
- When a scheduled script fails, how do you find out? Alerts, logs, someone notices the output is missing?
- Have there been scripts that silently failed and caused downstream problems?
- Any logging or monitoring infrastructure, or is it just check-the-folder?

*Why: If there's no monitoring, that's a quick win we can deliver on day one -- and it builds trust before we touch anything critical.*

## 6. Server Environment
- Windows Server? What version?
- Python version?
- Any virtual environments or dependency management (pip, conda)?
- How do you handle deployments -- copy files to the shared folder?
- Any firewall/VPN considerations for remote access?

*Why: We need to know if we can work remotely or if this requires VPN/on-site. Also tells us if there's any DevOps maturity at all.*

## 7. Data Sensitivity and Access
- What compliance restrictions exist around debtor data (PCI, GLBA, state regs)?
- Can we get access to a test/dev environment or sanitized sample data?
- Would we need to sign a BAA or NDA before seeing any account data?
- Can we work remotely, or does the data need to stay on-prem?

*Why: This is a debt collection firm handling SSNs, financial data, and regulated debtor info. We cannot touch production data without knowing the compliance boundaries. Sets us apart as professionals who take this seriously.*

## 8. Chris's Role (Light Touch)
- When Chris builds a new program, what does that look like? Does he spec it out, write it, and hand off the raw files?
- Is there documentation on what he's built, or would we need a walkthrough?
- Would Chris be available for a handoff session, or are we reverse-engineering?

*Why: We're being brought in to relieve Chris. We need to understand his workflow without stepping on toes. Sean is the bridge here.*

## 9. AI Appetite (Only If It Comes Up Naturally)
- You mentioned you've been thinking about AI internally -- what use cases were you considering?
- What are the specific compliance concerns that held you back?
- Have you looked at using AI for any of the court website interactions or document processing?

*Why: Don't lead with this. But if Sean opens the door, these questions let us gauge whether there's a real AI project behind the Python work.*

---

## Call Flow Suggestion
1. Let Sean introduce himself and his role
2. Questions 1-2 (platform and data access -- foundational)
3. Questions 3-4 (scripts and backlog -- scope)
4. Questions 5-6 (environment and monitoring -- quick wins)
5. Question 7 (compliance/access -- professionalism)
6. Question 8 (Chris handoff -- relationship)
7. Question 9 only if natural
8. Summarize what you heard, propose discovery next steps
