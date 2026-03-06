# Sales Cycle -- Helping Hands Cleaning (Residential)

Confirmed on discovery call 2026-03-02 with Gosia Baran.

---

## Current Flow (Business Hours)

```
Inbound Call (business hours)
    |
    v
Sales Rep Answers
    |
    v
Runs Sales Script:
  - Square footage (primary pricing input)
  - If unknown: bedrooms, bathrooms, number of floors
  - Pets (yes/no, type)
  - Service type (recurring, deep clean, move-in/out, etc.)
  - Service area confirmation
    |
    v
Live Quote Given Over Phone
    |
    +-- ACCEPT -----> GHL welcome email fires
    |                     |
    |                     v
    |                 MaidCentral (scheduling, dispatch, billing, portal)
    |
    +-- DECLINE ----> GHL prospect nurture funnel
                          |
                          v
                      Automated emails + SMS until convert or drop
```

### What Exists Today
- Sales script + SOP documented (Gosia will share)
- GHL handles all marketing automation (nurture, welcome emails, chat widget)
- MaidCentral handles all ops (scheduling, dispatch, invoicing, customer portal)
- Google Ads drives inbound (managed in-house by Gosia, not Edge Digital)
- GHL and MaidCentral are NOT connected -- manual handoff between systems

### What Does NOT Exist
- No after-hours or weekend lead capture
- No automated quoting (tried MaidCentral online quoting, stopped it)
- No GHL-to-MaidCentral automation (someone manually bridges the two)
- No call recording/transcription for sales quality
- No lead source attribution from AI search/AEO pages

---

## After-Hours Gap

### The Problem
Nobody answers after business hours or on weekends. Leads either hit voicemail or don't call back. Gosia cannot quantify missed volume but flagged this as the #1 priority.

### Hours Needing AI Coverage

Office hours per website: Mon-Fri 8:00 AM - 5:00 PM, Saturday 10:00 AM - 3:00 PM. Phone: (630) 530-1324.

| Window | Current Coverage | AI Coverage Needed |
|--------|-----------------|-------------------|
| Mon-Fri 8 AM - 5 PM | Human sales reps | No |
| Mon-Fri 5 PM - 8 AM | None | Yes |
| Saturday 10 AM - 3 PM | Human sales reps | No |
| Saturday 3 PM - Sunday end | None | Yes |
| Sunday all day | None | Yes |
| Holidays | None | Yes |

Confirm with Gosia that these hours are still accurate.

### Routing Requirements
- Phone system needs time-based routing rules
- During business hours: ring to human sales team (no change)
- After hours: forward to AI voice agent
- Need to determine: what phone system are they using today? Options:
  - GHL built-in phone (LeadConnector/Twilio)
  - Separate VoIP provider
  - Traditional landline with forwarding capability
- If GHL phone: time-based routing can be configured in GHL workflows
- If external: need call forwarding rules to route to Vapi number after hours

### Failover Logic
- AI agent cannot handle the call -> offer to schedule a callback during business hours
- Caller requests a human -> take message, log in GHL, flag for morning follow-up
- Technical failure -> fallback to voicemail with next-business-day callback promise

---

## AI Voice Agent Design

### Stack
| Component | Tool | Purpose |
|-----------|------|---------|
| Voice | 11 Labs | Natural-sounding voice (already in use) |
| Orchestration | Vapi | Call routing, conversation management, tool calling |
| CRM logging | GHL API | Log call data, create/update contacts, trigger nurture |
| Knowledge | Sales script + SOP | Gosia will provide for agent training |

### Conversation Flow

```
Incoming After-Hours Call
    |
    v
Greeting:
  "Thanks for calling Helping Hands Cleaning Services.
   Our office is currently closed, but I can help you
   get a quote right now. Can I ask you a few questions?"
    |
    +-- YES --------> Quote Flow
    |
    +-- NO/OTHER ---> "No problem. Can I take your name and
                       number so someone can call you back
                       first thing tomorrow morning?"
                           |
                           v
                       Log callback request in GHL
                       Tag: after-hours-callback
```

### Quote Flow

```
1. "What type of cleaning are you looking for?"
   -> Recurring, deep clean, move-in/out, one-time, other

2. "Do you know the square footage of your home?"
   |
   +-- YES -> Record sq ft, skip to step 3
   |
   +-- NO --> Fallback questions:
              "How many bedrooms?"
              "How many bathrooms?"
              "How many floors?"
              -> Estimate sq ft range from inputs

3. "Do you have any pets?"
   -> Yes/no, type if yes

4. "What city are you located in?"
   -> Validate against 33+ service area cities
   |
   +-- IN AREA -----> Continue
   +-- OUT OF AREA -> "I'm sorry, we don't currently
                       service that area. Can I suggest..."

5. "What's your preferred day and time for service?"
   -> General preference (not live booking)

6. Generate quote range based on inputs
   -> Use pricing logic from sales script/SOP
   -> Present as range, not exact ("Based on what you've
      told me, a recurring cleaning for your home would
      typically be between $X and $Y per visit.")

7. "Would you like to go ahead and get scheduled?"
   |
   +-- YES -> Collect: name, email, phone, address
   |          Log in GHL as new contact
   |          Tag: after-hours-booking, service type, city
   |          "Great! Someone from our team will confirm
   |           your first appointment tomorrow morning."
   |
   +-- NOT SURE -> "No problem. I'll send you an email
                    with the quote details so you can
                    think it over."
                    Log in GHL, enter nurture sequence
```

### Square Footage Estimation Logic

Gosia flagged this specifically: a 4-bedroom home can be 2,400 or 5,000 sq ft.

| Bedrooms | Bathrooms | Floors | Estimated Range |
|----------|-----------|--------|----------------|
| 2 | 1 | 1 | 900-1,200 sq ft |
| 3 | 2 | 1 | 1,200-1,800 sq ft |
| 3 | 2 | 2 | 1,500-2,200 sq ft |
| 4 | 2-3 | 2 | 2,000-3,200 sq ft |
| 4 | 3+ | 2+ | 2,800-4,500 sq ft |
| 5+ | 3+ | 2+ | 3,500-6,000+ sq ft |

These ranges need to be validated with Gosia's pricing matrix. The agent should quote the midpoint of the range and caveat: "This is an estimate based on what you've described. Your final price may vary slightly once we confirm the details."

### Edge Cases the Agent Must Handle
- Caller wants commercial cleaning -> "Let me connect you with our commercial team. Can I take your number and have Jim Wilson call you back?"
- Caller is an existing customer -> "I can help with scheduling changes. Can I get your name so I can pull up your account?" (check MaidCentral via API if available)
- Caller asks about eco-friendly products -> scripted response from Helping Hands' green cleaning messaging
- Caller speaks Spanish or Polish -> detect language, respond if possible or log for bilingual callback (Gosia is Polish, team may have bilingual staff)
- Caller is a vendor/solicitor -> politely end call, do not log as lead
- Multiple services requested -> quote each separately, offer bundle discount if applicable
- Price objection -> scripted response: 200% satisfaction guarantee, eco-friendly products, trained/vetted staff, 24 years in business

---

## Data Flow (After AI Call Completes)

```
Vapi Call Ends
    |
    v
Call transcript + recording saved (Vapi)
    |
    v
Webhook fires to GHL:
  - Create/update contact
  - Set tags: after-hours, service type, city, lead status
  - Add call notes: sq ft, bedrooms, bathrooms, pets, quote given
  - If booking: tag "after-hours-booking", trigger confirmation workflow
  - If callback: tag "after-hours-callback", trigger morning alert
  - If decline: enter standard nurture sequence
    |
    v
Morning Handoff:
  - Sales team reviews after-hours leads in GHL
  - Bookings get confirmed and entered into MaidCentral
  - Callbacks get priority follow-up
  - Nurture leads continue automated sequence
```

### GHL-to-MaidCentral Gap (Future Automation)
Currently manual. A human reads GHL and re-enters data into MaidCentral. This is a second automation opportunity:
- GHL webhook on "booking confirmed" tag -> Python script -> MaidCentral REST API -> create customer + schedule first appointment
- Requires: MaidCentral API credentials, field mapping between GHL and MC, error handling for scheduling conflicts
- Scope: Phase 2, after voice agent is stable

---

## Metrics to Track

| Metric | Source | Purpose |
|--------|--------|---------|
| After-hours calls received | Vapi | Volume of missed opportunity |
| Quotes given by AI | Vapi/GHL | Conversion funnel top |
| Bookings from AI calls | GHL tags | Direct revenue attribution |
| Callback requests | GHL tags | Leads that need human follow-up |
| Quote-to-booking rate | GHL | AI sales effectiveness |
| Average call duration | Vapi | Agent efficiency |
| Fallback-to-human rate | Vapi | Edge cases the agent can't handle |
| Morning confirmation rate | MaidCentral | Do after-hours bookings actually stick? |

### Target
Gosia wants 100 leads/week (currently 50-60). If the voice agent captures even 10-15 after-hours leads/week, that closes a significant portion of the gap. Combined with AEO driving new inbound volume, the 100/week target becomes realistic.

---

## Open Questions for Gosia
- [ ] What phone system are you using today? (GHL phone, separate VoIP, landline?)
- [ ] Confirm business hours: Mon-Fri 8-5, Sat 10-3 (per website)
- [ ] Share sales script + SOP
- [ ] Share current pricing matrix by sq ft / service type
- [ ] Do you want the AI to give exact quotes or ranges?
- [ ] Any bilingual requirements? (Spanish, Polish)
- [ ] Does MaidCentral API access require a separate license/fee?
- [ ] Who handles the morning follow-up on after-hours leads today? (Is there a process or is it ad hoc?)
