# Feb 24 Call Prep -- Filoni Law (Call 2)

## Context
- **When:** Tue Feb 24, 1:00 PM ET
- **Who:** David Filoni Jr., Darsh, Sean (new -- infrastructure/scripts lead)
- **Goal:** Get Sean's technical deep dive, define discovery scope, build trust

## JST / CollectMax Background
- Made by JST (est. 1987), product is **CollectMax**
- On-prem debt collection case management + accounting
- 900+ installations nationwide, serves solo to 200+ workstation firms
- EDI interfaces for court website interaction
- Handles all debt types: auto, credit card, medical, HOA, landlord-tenant, subrogation
- Also has **Accis** (next-gen cloud/self-hosted version) -- worth asking if they're on legacy CollectMax or Accis
- Subscription from $260/mo or permanent license

## What We Know (from Call 1)
- JST is the central DB, Python pulls keyword-based Excel sheets from it
- Scripts run on schedules (e.g. Monday 2pm), output distributed to Mexico/India/local teams
- PowerShell handles file number + account number reconciliation
- All scripts stored centrally on a shared server folder
- Chris built most core programs, Sean wrote most script code
- 60% automated, 40% manual
- Chris and Brian are bottlenecked -- that's why we're here

## Questions for Sean

### Infrastructure
1. Are you on CollectMax or Accis (the newer cloud version)?
2. How does JST/CollectMax expose data -- direct DB queries, API, CSV exports, or something else?
3. What does the server environment look like? Windows Server? What version of Python?
4. How are scripts triggered -- Task Scheduler, cron, manual, something else?
5. Any version control on the scripts (Git, or just files on the server)?

### Scripts + Workflow
6. Walk us through a typical script end-to-end (from trigger to team delivery)
7. How many active scripts are running right now? Ballpark.
8. What's the most painful script to maintain or the one that breaks the most?
9. What's in the backlog -- what scripts/automations does the team want but hasn't built?
10. How do you handle errors/failures when a script doesn't run? Alerts, logs, manual checks?

### Onboarding Us
11. How would we get access to a dev/test environment or sample data?
12. Any compliance restrictions on what data we can see or where we can work from?
13. What does Chris's handoff look like -- does he document the raw files he distributes?
14. Would we be working directly in the shared server folder, or submitting code for review?

### AI (Light Touch -- Don't Push)
15. Has Sean looked at any specific AI use cases internally?
16. Any repetitive decision-making in the workflow that could benefit from classification/sorting?

## Talk Track
1. **Open:** Introductions, let Sean talk. He's the technical authority -- give him the floor.
2. **Listen:** Let Sean walk through the infrastructure. Take notes. Ask follow-ups.
3. **Mirror back:** Summarize what we heard to confirm understanding.
4. **Propose discovery:** "Based on what Sean described, here's what we'd need to scope this properly..."
   - Access to sample scripts (read-only is fine)
   - Understanding of the JST data model
   - List of the backlog items / wishlist
   - 1-2 hours with Sean for a technical walkthrough
5. **Next steps:** Define what discovery deliverable looks like, timeline, and what we need from them.

## Things to Avoid
- Don't oversell AI -- they said compliance is a concern, respect that
- Don't promise pricing yet -- still in discovery
- Don't assume their scripts are messy -- Sean wrote most of them, treat his work with respect
- Don't talk over Sean -- he's the one we need to win over

## Positioning
- We are an **extension of their team**, not a replacement
- We take pressure off Chris and Brian
- We speak Python natively -- no learning curve
- Long-term: when they're ready for AI, we're already embedded and trusted
