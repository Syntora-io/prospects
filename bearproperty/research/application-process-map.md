# Bear Property - LIHTC Application Process Map

## End-to-End Flow (Current State)

```
APPLICANT APPLIES (RealPage online application)
        |
        v
REALPAGE DUMPS INTO GENERIC WAITING LIST BUCKET
        |
        v
[MANUAL] STAFF OPENS EACH APPLICATION ONE BY ONE
        |
        v
[MANUAL] QUICK HAND CALCULATION OF INCOME
        |
        |--- Hourly? Multiply by 2080
        |--- Salary? Take annual figure
        |--- Tips/commissions/bonuses on pay stub?
        |        |
        |        v
        |    [MANUAL] Call employer: "What do you anticipate
        |    they'll earn in next 12 months?"
        |
        v
[MANUAL] CHECK ALL INCOME SOURCES
        |
        |--- Employment income (wages, overtime, tips, commissions, bonuses)
        |--- Child support / divorce decree
        |--- Social Security
        |--- Disability income
        |--- Any informal support (e.g., someone buying diapers)
        |--- ANY dollar entering the household
        |
        v
[MANUAL] ASSET CHECK
        |
        |--- Assets > $5,000 --> VERIFY
        |--- Assets < $5,000 + HOME layering --> VERIFY ANYWAY
        |--- Assets < $5,000, no HOME --> self-certification OK
        |
        v
[MANUAL] PROGRAM-SPECIFIC CHECKS
        |
        |--- HOME units --> student status verification required
        |--- Other layered programs --> varies by site
        |
        v
[MANUAL] DETERMINE AMI BUCKET
        |
        |--- 40% AMI (highest demand, lowest rent)
        |--- 50% AMI
        |--- 60% AMI (fill quickly)
        |--- 70% AMI
        |--- 80% AMI
        |
        v
DECISION POINT: Does a matching unit exist?
        |
    YES |                    NO
        v                     v
   ASSIGN UNIT         ADD TO WAITING LIST
        |                     |
        v                     v
   CONTINUE TO          [MANUAL] Annotate AMI
   FULL PROCESSING      bucket next to name
   (rental verify,      (e.g., "40", "50")
   credit/background,           |
   TIC completion)              v
                        SITTING IN WAITING LIST
                        (90-day expiration timer)
                                |
                                v
                        [MANUAL] Must address
                        within 90 days or
                        application expires
                                |
                                v
                        When unit opens:
                        [MANUAL] Sort waiting list
                        by AMI annotation,
                        start at top of matching
                        bucket, work down
```

## Where the Time Goes

| Step | Manual? | Who | Time Impact |
|------|---------|-----|-------------|
| Open each application | Yes | Admin | 40+ hrs/week |
| Calculate income | Yes | Admin | Biggest bottleneck |
| Determine AMI bucket | Yes | Admin | Core of the problem |
| Annotate waiting list | Yes | Admin | Workaround for RealPage limitation |
| Sort waiting list by AMI | Yes | Admin/Leasing | Every time a unit opens |
| Contact applicant with status | Yes | Leasing agents | Delayed, causing bad reviews |
| Call employers for tips/commissions | Yes | Admin/Leasing | Required by tax credit rules |
| Full file processing | Yes | Leasing/Compliance | Standard, less pain here |
| Credit/background screening | No | Screening provider | Already dialed in |

## Calculations That Can Be Automated

### 1. Gross Annual Income (Primary)
- **Hourly**: hourly rate x 2080 = annual
- **Salary**: straight annual figure
- **Overtime**: need employer projection OR historical average x anticipated hours
- **Tips/commissions/bonuses**: employer must verify anticipated 12-month figure (can't fully automate -- but CAN flag that follow-up is needed)

### 2. AMI Bucket Assignment
- Take calculated gross annual income
- Compare against AMI limits for the property's county/MSA
- Factor in household size
- Assign to highest qualifying bucket (40%, 50%, 60%, 70%, 80%)
- Flag if over income for all buckets (deny) or under income

### 3. Asset Imputation
- Total assets > $5,000: calculate imputed income (passbook rate x total assets)
- Add imputed income to gross annual income
- Re-check AMI bucket after adding

### 4. Program-Specific Flags
- HOME layered: flag for asset verification regardless of amount
- HOME layered: flag for student status verification
- Other programs: configurable rules per property

### 5. Waiting List Sorting
- Auto-assign AMI bucket tag based on calculated income
- Auto-sort waiting list by AMI bucket
- Auto-match to available unit types
- Surface "next in line" when a unit becomes available

### 6. Automated Communications
- Application received confirmation
- Preliminary AMI qualification estimate
- Waiting list placement notification
- Status updates when unit becomes available
- Denial notifications with reason

## What CANNOT Be Automated (Human Required)
- Calling employers for tips/commissions/bonuses projection
- Verifying informal income sources
- Judgment calls on income discrepancies
- Reviewing divorce decrees, child support orders
- Overriding when applicant underreported/overreported income
- Final TIC review and sign-off
- Resident interaction, tours, relationship building

## Denial Rate Context
- 4-5 denials for every 1 acceptance
- Reasons: credit/background failure, over income, under income
- If automation pre-screens income before full processing, massive time savings on the 80% that get denied anyway
