# Excalidraw Deck Feedback for Meghna

**Date:** 2026-03-02
**Context:** Faloni Law proposal deck review. Call 3 is Mar 3, 12:00 PM ET.

---

## What's Working

- **"DevOps wraps around JST" framing.** Non-threatening, positions JST as the center. This is the right message for David and Trisha.
- **Compliance section** (FDCPA, TCPA, SOC 2, GLBA) speaks directly to Trisha and David's concerns. Keep as-is.
- **JST tool breakdowns** (MaxExtract, MaxUpdater, MaxSecurity, MaxPlans, Built-in Compliance) show we did our homework. Keep as-is.
- **"Assembly line" metaphor** for the pipeline is accessible for non-technical stakeholders.
- **"JST is the engine, DevOps is the garage"** is a strong analogy. Keep it.
- **Build in phases** is the right call. Stages 1-5 as a roadmap makes sense.

---

## Their Actual Tech Stack (From Calls 1 and 2)

This is everything confirmed on the calls. Nothing more, nothing less. The deck should reference only what they actually use, not what we assume they have.

| Tool | What it does | Where it runs |
|------|-------------|---------------|
| **JST CollectMax** | Central database. Case management, court filings, payments, compliance. ADS backend. File-based EDI only. No REST API. | On-prem production server |
| **SQL Database** | Separate DB for custom reporting, cross-referencing (docket + county = account number). Overcomes JST's reporting limitations. | Likely on-prem or same server |
| **Python** | Primary scripting language. Email scrapers, click-through court automation, data import/export. | AWS Workspaces (per dev) or JST production server for heavy loads |
| **PowerShell Universal** | Endpoints for FTP transfers, report generation, SQL queries. | Their server infra |
| **Amazon Workspaces** | Each dev gets a dedicated VM. Scripts run there. One workspace per programmer. | AWS |
| **Okta** | MFA for users. Not part of dev stack. | SaaS |
| **BitBucket** | Darsh's scrapers only. Side project, not team-wide. Not adopted. | Cloud |

### What They Don't Have

- **No centralized repo.** Code is siloed per AWS Workspace. No GitHub, no shared repo.
- **No CI/CD pipeline.** Scripts are run manually or on cron schedules per workspace.
- **No project management tool confirmed.** David said "we need to get a list together of things that we really want" on call 2, implying no formal backlog system. Ask on the call what they use to track work requests.
- **No version control (team-wide).** Darsh has BitBucket for his own scrapers. Nobody else uses it.
- **No formal code review process.** Sean mentors Darsh informally but there's no structured review.

### Scripts Inventory (Confirmed on Calls)

| Script | Owner | Function | Schedule |
|--------|-------|----------|----------|
| Wage confirmation scraper | Darsh | Scans Jeffers2 inbox for "wage application" keyword, outputs Excel | Hourly, 24/7 (12:01am-11:59pm) |
| Court officer scraper | Darsh | Scans for court officer assignments, docket numbers | Hourly, 24/7 |
| Goods & chattel scraper | Darsh | Same structure as wage, different keywords | Hourly, 24/7 |
| Jeffers3 email scrapers | Sean | Main E-Court contact scrapers. "Set in stone" per Sean. | Hourly |
| Court filer scripts | Chris | Click-through automation for court website filings (5 clicks). May be broken. | Unknown |
| Outlook calendar tool | Sean | Trial team calendar integration. Nearly done, needs trial team input. | In progress |
| Docket-to-account mapper | Resolved | Pairs county + docket number to get account number via SQL | Working |

---

## What Needs to Change

### 1. Pipeline Table: Remap Every Stage to GitHub or What They Already Have

The current table lists 11 separate tools (Jira, Confluence, SonarQube, Snyk, Terraform, Datadog, PagerDuty, DocuSign, Policy Engine, AWS CodeDeploy, GitHub). That's overwhelming for a team that doesn't have a shared repo yet. Sean said GitHub alone is "a big bridge to cross."

The fix isn't removing stages. It's showing that **GitHub handles most of them natively**. One platform, not eleven.

| # | Phase | What handles it today | What handles it in our system |
|---|-------|-----------------------|-------------------------------|
| 01 | Plan | No formal PM tool confirmed. Ask on call. | Whatever they already use. GitHub Issues available if they need it later. |
| 02 | Code | Siloed AWS Workspaces, no shared repo | **GitHub** -- shared repo, branches, PRs |
| 03 | Build | Manual -- devs run scripts locally | **GitHub Actions** -- comes free with GitHub |
| 04 | Test | Manual -- devs eyeball output | **GitHub Actions** -- linting, validation checks |
| 05 | Security | Nothing | **GitHub built-in** -- basic secret scanning, Dependabot alerts, branch protection (all included with Team, no add-on cost) |
| 06 | Legal Gate | Nothing formal | **GitHub PR approval** -- Trisha required as reviewer on anything touching debtor communication |
| 07 | Deploy | Manual copy to AWS Workspace | **GitHub Actions** -- auto-deploy to Workspaces on merge |
| 08 | Monitor | Manual -- check if scripts ran | **GitHub Actions logs** + basic alerting (email/Slack on failure) |

**One new tool. Eight pipeline stages covered.** That's the pitch.

SonarQube, Snyk, Terraform, Datadog, PagerDuty, DocuSign, Policy Engine, AWS CodeDeploy are all valid tools for a mature DevOps org. None are wrong long-term. But introducing them now is like handing someone who just got their driver's license the keys to a semi truck. They get added one at a time as the team matures and the volume justifies it.

### 2. Phase Table Owners Don't Map to Their People

The current table uses generic titles: Engineering Lead, Dev Team, Senior Dev + QA, Release Manager, On-Call Engineer, General Counsel. Faloni doesn't have these roles. The table should use their actual people or at minimum roles they recognize.

**Rewrite owners as:**

| # | Phase | Owner (current deck) | Owner (revised) |
|---|-------|---------------------|-----------------|
| 01 | Sprint Planning | Engineering Lead | Sean (coordinates with Trisha) |
| 02 | Development | Dev Team | Sean, Chris, Darsh, Brian |
| 03 | Code Review | Senior Dev + QA | Sean (approver) |
| 04 | Staging Deploy | DevOps | GitHub Actions (automated) |
| 05 | Legal / Compliance Review | General Counsel | Trisha (required reviewer) |
| 06 | Production Deploy | Release Manager | Sean (merge to main) |
| 07 | Post-Deploy Monitoring | On-Call Engineer | Automated alerts + on-call dev |

Show them **their team** in the new system, not generic org chart roles.

### 3. Remove Terraform From Stage 2

The current deck says "Build Terraform server and import to GitHub." Here's why that doesn't fit Phase 1:

**What Terraform does:** Provisions and manages cloud infrastructure as code -- spinning up servers, configuring VPCs, managing databases, replicating environments.

**What Faloni's infrastructure actually is:**
- An on-prem JST production server (Terraform can't touch on-prem)
- A handful of static AWS Workspaces, one per dev, that don't change
- A SQL database (likely on-prem)
- PowerShell Universal endpoints on their server infra

There's nothing dynamic here. They're not spinning environments up and down. They're not running containers or microservices. They have 5 static VMs and an on-prem server. Terraform manages infrastructure that changes frequently. Theirs doesn't.

**Replace with:** "Configure GitHub Actions to deploy to existing AWS Workspaces." Same outcome, no new tool, no new syntax to learn.

**When Terraform enters the picture (future state):**
- **Stage 3+** -- if we build the ETL pipeline on AWS (RDS, Lambda, S3), Terraform codifies that infra so it's reproducible
- **Onboarding** -- if they hire a 6th dev and need a new Workspace provisioned identically, Terraform makes that repeatable
- **Disaster recovery** -- if AWS Workspaces need rebuilding, Terraform recreates them from config

But none of those are Phase 1 problems. Phase 1 is getting code into a shared repo. The infrastructure underneath is stable and not the bottleneck.

### 4. Remove Jira/Confluence

No project management tool was confirmed on either call. David's "we need to get a list together" comment suggests they don't have a formal backlog system. Ask on the call what they currently use to track work requests. Could be email threads, a shared spreadsheet, JST's internal workflow, Microsoft Planner, or nothing at all.

Whatever it is, GitHub Issues can integrate with it later. Don't introduce PM tooling we haven't confirmed they need and don't solve that problem tomorrow.

### 5. Remove Snyk From Stage 4

The current deck says "Use Snyk for flagging security vulnerabilities." GitHub Team plan includes secret scanning and Dependabot for free. These cover:
- Detecting hardcoded credentials, API keys, tokens in code
- Flagging known vulnerabilities in dependencies
- Automated alerts when issues are found

Snyk is a future upgrade when they have enough code in the repo and enough dependency complexity to justify a dedicated scanner. For a team writing Python scrapers and PowerShell endpoints, GitHub's built-in tools cover it.

### 6. Other Stage Revisions

**Stage 1** -- Swap "Setup GitHub Organization" from a bullet to the headline. It's not one task among five. It's the entire point of Stage 1.

**Stage 5** -- Label as future state. "Stage 5 becomes available once Stages 1-4 are stable. This is where specialized monitoring tools enter the picture." Don't present it like it's part of the initial build.

### 7. Add a "Before and After" Slide

This is missing from the deck entirely. Easiest way to show the value without listing tools.

**Today:**
- Darsh writes a scraper on his AWS Workspace
- Nobody else can see it, test it, or recover it if his Workspace dies
- If Darsh leaves, the code leaves with him
- No record of what changed, when, or why

**After Phase 1 (GitHub only):**
- Darsh writes the same scraper, pushes to his branch
- Sean reviews and approves via PR
- Code merges to main, deployed automatically
- If Darsh leaves, the code is in the repo with full history
- Trisha can see every change and who approved it

**After Phase 2 (GitHub Actions):**
- Same workflow, but now checks run automatically before merge
- Failed scripts trigger an alert instead of someone noticing hours later
- Trisha gets a dashboard of every change and who approved it

**After Phase 3+ (Specialized tools as needed):**
- Security scanning catches vulnerabilities before deploy
- Dedicated monitoring catches production failures in real-time
- Infrastructure-as-code (Terraform) manages new AWS resources
- Each stage gets its own specialized tool when the volume justifies it

This shows the scale path without front-loading the complexity.

---

## GitHub Organization Detail (Add as a Section)

This is the most important addition to the deck. GitHub is the biggest behavioral change for their team and the current deck gives it one bullet. This section should sit between the intro and the stages.

### Org + Plan

- GitHub Organization: `filoni-law`
- **GitHub Team plan** -- $4/user/month.
- 7 users: David (Org Owner), Sean (Admin), Trisha (reviewer), Chris, Brian, Darsh (Write), Syntora (Admin, temporary) = **$28/month ($336/year)**.
- Includes: branch protection, required reviewers, CODEOWNERS enforcement, draft PRs, 3,000 GitHub Actions minutes/month, 2GB Packages storage, basic Dependabot alerts, basic secret scanning on private repos.
- **Enterprise ($21/user/month) is overkill.** Enterprise adds SAML SSO, SCIM provisioning, audit log API, 50k Actions minutes. They don't need any of that with 5 devs and Okta already handling MFA.
- **Note:** On call 2, Parker quoted Pro at "$20/mo + $8/seat." That's outdated. Team plan is $4/user/month flat -- significantly cheaper. Correct this on the call.

### GitHub Actions: Included and Sufficient

- 3,000 minutes/month included with Team plan (Linux runners).
- A typical lint + validation job takes 1-2 minutes. Even at 50 PRs/month, that's ~100 minutes used. They won't come close to the 3,000 limit.
- Overage (if ever needed): ~$0.008/minute for Linux runners.
- GitHub reduced hosted runner prices by ~39% as of Jan 2026. Cost is not a concern here.

### Security Features: What's Included vs. Paid Add-Ons

| Feature | Included with Team? | Paid add-on? |
|---------|---------------------|-------------|
| Dependabot alerts (vulnerable dependencies) | Yes, free | -- |
| Secret scanning on private repos (basic pattern detection) | Yes, free | -- |
| Branch protection, required reviewers | Yes, free | -- |
| Push protection bypass controls, AI scanning, validity checks | No | GitHub Secret Protection, $19/active committer/month |
| Copilot Autofix, dependency review, grouped updates | No | GitHub Code Security, $30/active committer/month |

**For Phase 1-2, the free features cover everything Faloni needs.** The paid add-ons ($19 and $30/committer/month) are Stage 5+ when code volume and security requirements justify them. Don't mention these on the call -- just say "GitHub includes built-in security scanning."

### Repo Strategy: Monorepo

One repo: `filoni-law/automation`

```
automation/
  scrapers/
    jeffers2/              <- Darsh's wage, court officer, goods & chattel
    jeffers3/              <- Sean's E-Court scrapers
  filers/                  <- Chris's court filing click-through scripts
  etl/                     <- MaxExtract/MaxUpdater wrapper scripts
  powershell/              <- PowerShell Universal endpoints (FTP, reports, SQL)
  shared/                  <- DB connections, config, common utilities
  .github/
    workflows/             <- GitHub Actions (linting, tests, deploy)
    CODEOWNERS             <- Auto-assigns reviewers per folder
```

**Why monorepo, not separate repos:** They have 5 devs. Separate repos means separate permission configs, separate CI pipelines, separate PR processes to learn. One repo = one set of rules, one place to look, one thing to learn. Lowest friction path from "code on my desktop" to "code in a shared system."

### Branch Strategy

| Branch | Purpose | Who pushes here |
|--------|---------|-----------------|
| `main` | Production. Protected. Deployed code. | Nobody directly. Merge only. |
| `staging` | Pre-production validation | Merges from feature/dev branches |
| `dev/sean` | Sean's working branch | Sean |
| `dev/darsh` | Darsh's working branch | Darsh |
| `dev/chris` | Chris's working branch | Chris |
| `dev/brian` | Brian's working branch | Brian |
| `feature/*` | New script or enhancement | Any dev |
| `hotfix/*` | Emergency production fix | Any dev (fast-track review) |

**This is the key slide for Sean.** Each dev gets their own branch that mirrors how they work today -- isolated workspace, their code, their pace. The difference is it all flows into one place. He already mentors Darsh; PR review formalizes what he's already doing informally.

### Permissions

| Person | GitHub Role | What they can do |
|--------|------------|------------------|
| David | Org Owner | Billing, org settings. Hands-off. |
| Sean | Admin | Repo settings, branch protection, merge authority, onboards devs |
| Trisha | Write + Required Reviewer | Pushes nothing, but **required approver** on any PR touching debtor communication, letter templates, or compliance logic. Full audit visibility. |
| Chris, Brian | Write | Push to personal/feature branches, open PRs |
| Darsh | Write | Push to personal/feature branches, open PRs |
| Syntora (us) | Admin | During engagement only. Setup, migration, pipeline config. Removed after handoff. |

**Sean runs the system day-to-day.** This is already how their team operates informally. We're putting structure around it.

**Trisha gets a gate, not a dashboard she has to manage.** Any PR that touches compliance-sensitive code requires her approval before it can merge. She doesn't need to learn Git. She clicks Approve or Request Changes on a web page.

**David gets visibility without overhead.** Org Owner means he controls billing and can see everything, but nothing requires his daily attention.

### Branch Protection Rules on `main`

- **Require a pull request** before merging (no direct push, ever)
- **Require 1 approval** (Sean or Trisha depending on scope)
- **Require status checks to pass** (linting first, tests later as they build them)
- **No force push** (nobody can rewrite history)
- **No branch deletion** (main is permanent)

**This is the key slide for Trisha.** Every change to production is reviewed, approved, and logged. GitHub keeps a permanent record of who changed what, when, and who approved it. That's her audit trail built into the platform -- no custom tooling required.

### CODEOWNERS File

GitHub supports a `CODEOWNERS` file that automatically assigns reviewers based on what files a PR touches.

```
# CODEOWNERS - filoni-law/automation

# Sean reviews everything by default
*                           @sean-barlisan

# Trisha must approve changes to debtor communication logic
/filers/                    @sean-barlisan @trisha
/etl/                       @sean-barlisan @trisha

# Darsh owns his scrapers, Sean still reviews
/scrapers/jeffers2/         @darsh-patel @sean-barlisan

# Sean owns his scrapers
/scrapers/jeffers3/         @sean-barlisan
```

This means:
- Darsh opens a PR changing a Jeffers2 scraper -- Sean is automatically tagged for review
- Chris opens a PR changing a filer script -- both Sean and Trisha are automatically tagged
- Nobody has to remember to tag the right person. The system enforces it.

### How Migration Actually Works (No Downtime)

1. We create the org, repo, and folder structure
2. Each dev's existing scripts get imported into their section (Sean's scrapers into `scrapers/jeffers3/`, Darsh's into `scrapers/jeffers2/`, etc.)
3. Scripts keep running on their current AWS Workspaces -- nothing changes day one
4. Devs start making changes in GitHub, pushing to their dev branch
5. Once comfortable, we wire GitHub Actions to deploy from `main` to the Workspaces
6. Old workflow dies naturally -- no forced cutover, no "migration day"

**Nobody's scripts stop running.** Nobody's daily work changes until they're ready. The repo wraps around their existing workflow the same way DevOps wraps around JST.

---

## Revised Stages (Suggested Rewrite)

### Stage 1: GitHub + Documentation
- Set up GitHub Organization (`filoni-law`, Team plan, ~$28/mo)
- Create monorepo (`automation`) with folder structure
- Import existing scripts from each dev's AWS Workspace
- Document the current JST setup, data flows, and script inventory
- Map compliance requirements (what code touches debtor data)
- Configure branch protection, permissions, CODEOWNERS

### Stage 2: GitHub Actions + Deployment Pipeline
- Configure GitHub Actions to run linting and basic validation on every PR
- Set up auto-deploy from `main` to AWS Workspaces (replaces manual copy)
- Create separate deploy targets: staging Workspace and production Workspace
- Set up AWS backups and test recovery process
- Enable GitHub secret scanning and Dependabot

### Stage 3: ETL Pipeline + Audit Trail
- Build MaxExtract/MaxUpdater wrapper scripts in the repo
- ETL pipeline: Python script at 2:00 AM EST extracts account data, validates, loads into secure database (AWS RDS)
- Extracted data feeds report generation, client portal, and audit logs
- Create append-only audit table logging all data access, pipeline runs, and changes
- All ETL code goes through the same PR/review process as everything else

### Stage 4: Compliance Gate + Security Hardening
- Implement CODEOWNERS so Trisha is required reviewer on compliance-sensitive paths
- GitHub Actions checks for SSN patterns, PII exposure, hardcoded credentials
- Flag any PR that touches debtor communication logic for compliance review
- Timestamp and log all approvals into the audit trail
- Evaluate specialized security tools (Snyk, SonarQube) based on actual needs at this point

### Stage 5: Infrastructure-as-Code + Observability (Future State)
- **Terraform enters here** -- codify any new AWS resources (RDS, Lambda, S3) built in Stage 3
- Terraform configs for reproducible Workspace provisioning (new dev onboarding)
- Add monitoring dashboards (evaluate Datadog, CloudWatch, or simpler options based on needs)
- Build runbooks for common failure scenarios
- Simulate system failures to test recovery process
- This stage activates after Stages 1-4 are stable and running

---

## Tool Introduction Timeline

To keep the deck clean, here's the explicit timeline for when each tool enters:

| Tool | When | Cost | Why then |
|------|------|------|----------|
| **GitHub Team** (repo, PRs, branches) | Stage 1 | $4/user/month ($28/mo for 7 users) | Core problem: code is siloed. This fixes it. |
| **GitHub Actions** (lint, test, deploy) | Stage 2 | Included -- 3,000 min/month with Team | Automated linting, testing, deployment. No additional cost. |
| **Basic Secret Scanning** | Stage 2 | Included with Team | Catches hardcoded credentials in private repos. No additional cost. |
| **Dependabot Alerts** | Stage 2 | Included with Team | Flags vulnerable dependencies. No additional cost. |
| **CODEOWNERS** | Stage 1 (config) / Stage 4 (enforcement) | Included with Team | Auto-assigns reviewers. Set up early, enforce when team is comfortable. |
| **GitHub Secret Protection** (advanced) | Stage 5+ | $19/active committer/month | Push protection bypass, AI scanning, validity checks. Not needed until code volume justifies it. |
| **GitHub Code Security** (advanced) | Stage 5+ | $30/active committer/month | Copilot Autofix, dependency review, grouped updates. Future state. |
| **Terraform** | Stage 5 | Free (open source) | New AWS resources from Stage 3 need to be codified. Not needed before that. |
| **Datadog / CloudWatch** | Stage 5+ | Varies | When pipeline volume justifies dedicated monitoring beyond GitHub Actions logs. |
| **PM tooling** | Only if needed | -- | Ask what they use first. GitHub Issues covers basics. Don't introduce without confirming a gap. |

**The message: GitHub is the platform. Everything else plugs in when it's earned.**

---

## Why This Matters Now -- The Bottleneck Argument

The deck needs to address their immediate pain head-on. Their dev team is already behind. Chris and Sean are bottlenecked. The backlog is growing. David said "we need to get a list together of things that we really want" -- they can't even enumerate the backlog, let alone work through it. They came to us asking for another programmer. The deck should explain why infrastructure solves the bottleneck faster than headcount -- and sets them up for what's next.

### Today: adding a new engineer is slow.

A new dev gets an AWS Workspace. They ask Sean where the code is. Sean points them to his Workspace, explains his folder structure, walks them through the scripts manually. There's no README, no repo to clone, no onboarding path. Darsh said the learning curve "wasn't too big" because he had Sean. But Sean's time is the bottleneck. Every hour Sean spends onboarding is an hour he's not writing code. Adding a 6th programmer into this environment creates a 6th silo and pulls Sean away from his own work even more.

### After GitHub: a new engineer clones the repo and starts.

They see the folder structure. They see the scripts. They see the commit history of every change. They see the CODEOWNERS file telling them who owns what. They read the PR history to understand why things were built the way they were. They open a PR, Sean reviews it in 10 minutes instead of spending a week walking someone through his Workspace, and they're contributing on day one. Sean's mentorship time drops from weeks to hours.

### After GitHub Actions: the team moves faster without more people.

Linting catches syntax errors before Sean ever sees the PR. Automated deployment means nobody manually copies files to a Workspace. Failed scripts alert the team instead of someone noticing hours later. The 4-5 devs they already have become significantly more productive -- equivalent to adding 1-2 headcount without a single new hire.

### ROI for David

He's paying 4-5 programmer salaries ($60-80k+ each = $300-400k/yr in dev payroll). If infrastructure makes those people 30% more productive, that's equivalent to adding 1.5 headcount without hiring. The entire engagement ($16-25k) pays for itself in a couple of months. They asked for a new programmer. We're giving them the equivalent of 1-2 new programmers by unlocking their existing team.

### The foundation for AI.

They said AI isn't on the table for this engagement. That's fine. But the infrastructure we're building is the prerequisite for when they're ready. AI agents need three things to work with a codebase:

1. **A structured repo to read from.** An AI can't navigate 5 separate AWS Workspaces with no folder conventions. It can navigate a monorepo with clear folder structure and commit history.
2. **A pipeline to deploy through.** An AI can't SSH into a Workspace and copy files. It can open a PR that triggers GitHub Actions to lint, test, and deploy.
3. **A review process to gate the output.** An AI shouldn't push code to production unchecked. It opens a PR, Sean reviews it, Trisha approves if it touches compliance code. Same process as any human dev.

Without GitHub, AI has nowhere to plug in. With it, the door is open. When they're ready -- whether that's 6 months or 2 years from now -- an AI agent could draft a new scraper, open a PR, Sean reviews it, and it deploys through the same pipeline as any human-written code. The repo structure makes that possible. Without it, AI is a non-starter.

**Don't sell AI on this call.** But plant the seed: "The infrastructure we're building doesn't just solve today's bottleneck. It's the foundation that lets you scale with both people and technology."

---

## Questions to Ask on the Call (Mar 3)

These gaps need to be filled before or during the proposal presentation:

1. **Project management:** "What do you currently use to track work requests and the backlog David mentioned? Spreadsheet, email, something in JST?" -- determines whether we mention PM tooling at all.
2. **Chris:** Is he on this call? If not, we're still missing context on the filer scripts and whether they're broken.
3. **AWS Workspace setup:** Are they provisioned manually through the AWS console? Who has AWS admin access? This informs whether Terraform has value for workspace management later.
4. **SQL database location:** On-prem alongside JST, or hosted separately? Affects the Stage 3 ETL pipeline design.
5. **Budget reaction:** David asked about hourly vs fixed vs maintenance on call 1. Present all three phases with fixed prices. Watch his reaction to the Phase 1 number ($3,500-$5,000) before going deeper on Phase 2.

---

## Summary of Changes for Meghna

1. **Rewrite the pipeline table** so every stage maps to GitHub or existing tools. One new platform, not eleven.
2. **Rewrite the phase owners** using Faloni names and roles, not generic enterprise titles.
3. **Add the GitHub deep-dive** (org, repo, branches, permissions, CODEOWNERS, migration plan) as its own major section between the intro and the stages.
4. **Add a before/after slide** showing the same developer workflow at each phase of adoption.
5. **Add the tech stack table** showing exactly what they confirmed on the calls -- anchor the deck in their reality.
6. **Add the tool timeline** showing when each tool enters and why. Sets up the scale story without front-loading.
7. **Add the bottleneck argument.** Address the immediate pain: their team is behind, adding headcount into the current setup is slow, GitHub infrastructure makes the existing team faster and makes onboarding instant. Include the ROI math for David.
8. **Plant the AI seed.** Don't sell AI. But explain that the GitHub infrastructure is the prerequisite -- AI agents need a repo to read, a pipeline to deploy through, and a review process to gate output. Without this foundation, AI can't plug in.
9. **Remove Terraform from Stage 2.** It solves a problem they don't have yet. Moves to Stage 5 when new AWS resources need to be codified.
10. **Remove Jira/Confluence.** No PM tool was confirmed. Ask on the call first.
11. **Remove Snyk from Stage 4.** GitHub's built-in secret scanning + Dependabot covers them for now.
12. **Label Stage 5 as future state** so the call focuses on Stages 1-3, which is the actual engagement.
13. **Sean is Admin, not Trisha.** Sean runs the GitHub workflow day-to-day. Trisha is the compliance approval gate via required reviewer, not a repo administrator.
14. **Keep the compliance section (FDCPA, TCPA, SOC 2, GLBA) and the JST tools section as-is.** Both are strong.