# Note: The Applicant Side of the Problem

**Date:** 2026-02-23
**Context:** Thinking about Section 8 / LIHTC from the applicant's perspective, not just Bear's operations team.

---

## Core Insight

We've been focused on Bear's staff problem (sorting, calculations, time). But the applicant experience is just as broken. These are people who may not check email, may not understand what documents they need, may not know why they got rejected or that they could qualify somewhere else. The product needs to serve both sides.

## Applicant-Side Problems to Solve

### Document Completeness
- Applicants forget to turn in specific documents or don't know what's required
- Child support documentation, income verification, asset statements
- The system should check for completeness BEFORE the team ever reviews the application
- Only fully documented applications should reach human review
- Reduces wasted staff time on incomplete files

### Proactive Communication (SMS-First)
- These applicants may not check email frequently
- SMS is the right channel for critical notifications:
  - Missing documents: "You're missing X, submit by Y date or your application stalls"
  - Application expiration warnings: "Your application expires in 15 days, here's what you need to do"
  - Step-by-step status updates: tell them where they are in the process at every stage
  - Rejection with redirection: "Your income is above the AMI limit for this area, but you may qualify at [other property] where the AMI threshold is higher"
- Communication frequency matters. How often do we need to nudge people about missing docs?

### Rejection Redirection
- When someone is denied because their income exceeds the AMI for a specific area, don't just reject them
- Tell them: "The AMI here is X. Your income qualifies you for Y% AMI. Property Z in [other county] has a higher AMI limit and you would more likely qualify there."
- This is a portfolio-level play. Bear has 26 communities across different counties with different AMI limits.
- Cross-property matching based on income: if they don't fit here, where DO they fit?

### Full Process Understanding Needed
- We need to map the ENTIRE Section 8 / LIHTC application process from the applicant's perspective
- What are they doing manually?
- What calculations happen?
- What could staff be doing better with their time if the system handled document collection and qualification pre-screening?
- Human tendencies: what do applicants commonly miss, forget, or not understand?

## Product Implications

### Pre-Qualification Layer
- Before human review: system checks all required documents are present
- Credit check status, income docs, child support orders, asset statements
- Only passes to staff when the file is complete
- Staff reviews fully qualified, fully documented applications only

### Communication as a Core Feature (Not an Add-On)
- SMS should be primary, not optional
- Email as backup/formal record
- The communication layer reduces burden on staff AND improves applicant experience
- Every step communicated: received, missing docs, qualified, waitlisted, denied with alternatives, expiring

### Cross-Property Matching
- If denied at Property A due to AMI, auto-check against all 26 (and growing) communities
- "You don't qualify here, but you do qualify here"
- This is unique value. No competitor does this.

## Discovery Questions to Add (For the Call)

- What's the applicant experience like right now? How do they know where they stand?
- How often do applications stall because of missing documents?
- What percentage of applicants need to be contacted multiple times for docs?
- Do applicants have email? Do they check it? Is SMS more reliable for this population?
- When someone is denied at one property, does anyone check if they qualify at another Bear community?
- What's the most common reason an application sits incomplete?
- How does the team currently communicate with applicants -- phone calls, email, letters?

---

*This reframes the product from "staff efficiency tool" to "applicant experience platform that also makes staff more efficient." Both sides of the same coin.*
