# Feedback for Meghna -- Faloni Law Excalidraw Deck

**Date:** 2026-03-02

---

Meghna,

Good work on this. You built a real presentation structure from scratch and covered a lot of ground. Before I get into revisions, I want to walk through what you did well because the foundation here is solid.

## What You Nailed

**The framing is right.** "DevOps wraps around JST. It does not replace it." That single line is probably the most important sentence in the entire deck. David and Trisha need to hear that their core system isn't being disrupted. You understood the assignment -- position JST as the engine, position us as the team building the garage around it. That's exactly the message we need to lead with.

**The compliance section is strong.** FDCPA, TCPA, SOC 2 Type II, GLBA -- you went and researched what laws actually apply to a debt collection firm and laid them out cleanly. This matters because Trisha's primary concern is security and audit trails. When she sees that slide, she'll feel like we understand her world. That section stays as-is.

**The JST tools breakdown shows research depth.** MaxExtract, MaxUpdater, MaxSecurity, MaxPlans, Built-in Compliance -- you mapped out how JST's own tools plug into the DevOps system we're proposing. That tells the client we're not just throwing generic infrastructure at them. We actually looked at what their software can do and built around it.

**The 7-stage pipeline visual is clean.** The assembly line graphic with the icons is well-designed and easy to follow. The phase table underneath with owners, gate criteria, tooling, and status badges is a good format. The structure of that table is exactly right -- we're going to keep that format and adjust the content inside it.

**The staged rollout (Stages 1-5) is the right approach.** You didn't try to present everything as a single big bang. You broke it into phases that build on each other. That's important for a team that's never had centralized infrastructure before.

**"JST is the engine and DevOps is the garage" and "A pipeline is just a checklist that runs itself."** Both of these are great plain-language explanations. David is a managing partner at a law firm, not an engineer. These analogies land.

## Where to Adjust

The core issue is one thing: **too many new tools introduced at once.** Your instinct to show the full enterprise pipeline was right in terms of thinking big, and that's where we want them to end up. But for the call tomorrow, we need to show them that the first phase is one new platform (GitHub), not eleven.

Right now the deck introduces Jira, Confluence, SonarQube, Snyk, Terraform, Datadog, PagerDuty, DocuSign, Policy Engine, AWS CodeDeploy, and GitHub all in the same breath. For a team where Sean said adopting GitHub alone is "a big bridge to cross," seeing that list will create resistance instead of buy-in.

Here's the shift: **GitHub handles almost every stage of the pipeline natively.** Code, build, test, security, review, deploy, and monitoring all live inside GitHub and GitHub Actions. We don't need separate tools for each stage in Phase 1. We need one platform that scales with them, and we add specialized tools later when the volume justifies it.

### Specific changes:

**Pipeline table** -- Keep the format you built. Replace the tooling column so every stage maps to GitHub or something they already have. I put together a revised mapping in the detailed notes file (2026-03-02-excalidraw-feedback.md).

**Phase table owners** -- Swap out generic titles (Engineering Lead, Release Manager, On-Call Engineer) for their actual people. Sean, Darsh, Chris, Brian, Trisha. When they see their own names in the system, it stops being abstract and starts being real.

**GitHub section** -- This is the biggest addition. The deck currently gives GitHub one bullet in Stage 1. It needs its own section covering repo structure, branch strategy, permissions, and how migration works without downtime. I wrote out the full detail including a CODEOWNERS file and branch protection rules in the notes file. The key points:

- **Sean is the Admin.** He runs the GitHub workflow day-to-day. This matches how their team already operates.
- **Trisha is a Required Reviewer**, not an admin. She gets a compliance gate on any PR that touches debtor communication, letter templates, or filer scripts. She doesn't need to learn Git. She clicks Approve or Request Changes on a web page.
- **Each dev gets their own branch** (dev/sean, dev/darsh, etc.) that mirrors how they work today -- isolated, their code, their pace. The difference is it all flows into one place.

**Stages 4-5** -- Label Stage 5 as future state. Don't present Datadog/PagerDuty as part of the build. They're where we go after Stages 1-3 are stable.

**Stage 2** -- Replace Terraform with GitHub Actions deploying to their existing AWS Workspaces. Same outcome, no new tool to learn.

**Add a before/after slide.** Show the same scenario (Darsh writes a scraper) under the current workflow vs. after Phase 1 vs. after Phase 2. This is the simplest way to show value. Detail in the notes file.

**Project management** -- Remove Jira/Confluence. They likely already have something for tracking work. We'll ask on the call. Don't introduce PM tooling we haven't confirmed they need.

## Where to Find the Details

Everything above with full tables, code examples, and the revised stage breakdown is in:

`falonilaw/notes/2026-03-02-excalidraw-feedback.md`

Use that as the reference for revisions. The structure of your deck doesn't need to change. The content inside the pipeline table, the owners, and the tooling references are what we're updating.

The vision you built is where we're taking them. We're just adjusting the on-ramp so they don't see the full highway on day one.

Good work. Let's get this tightened up for tomorrow.

-- Parker