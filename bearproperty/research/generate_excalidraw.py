"""
Bear Property Management - Excalidraw Presentation
Single-column vertical flow. Color-coded with legend.
"""
import json
import random

random.seed(42)
elements = []
_id = [0]

def uid():
    _id[0] += 1
    return f"e{_id[0]}"

def seed():
    return random.randint(1, 2**31)

# --- Palette: 4 semantic colors + neutrals ---
# PAIN = current manual process, problems, bottlenecks
PAIN = "#c92a2a"
PAIN_BG = "#fff5f5"
# SOLUTION = what we build, automated steps, outcomes
SOLUTION = "#2b8a3e"
SOLUTION_BG = "#ebfbee"
# INFO = RealPage, tech details, API endpoints, data
INFO = "#1864ab"
INFO_BG = "#e7f5ff"
# ACTION = decisions needed, flags, things Bear must do
ACTION = "#e67700"
ACTION_BG = "#fff4e6"
# QUOTE = Sara's words
QUOTE_BORDER = "#868e96"
QUOTE_BG = "#f8f9fa"
# Neutrals
ACCENT = "#495057"
BLACK = "#1e1e1e"
DARK = "#343a40"
MED = "#868e96"
LIGHT = "#dee2e6"
LIGHTER = "#f1f3f5"
BG = "#f8f9fa"
WHITE = "#ffffff"

# --- Layout constants ---
W = 1000          # content width
LEFT = 100        # left margin
CY = [100]        # current Y position (mutable list for closure)

def advance(amount):
    CY[0] += amount

def rect(x, y, w, h, stroke=LIGHT, bg="transparent", fill="solid", sw=1, ss="solid", rough=0, group=[]):
    el = {
        "id": uid(), "type": "rectangle", "x": x, "y": y,
        "width": w, "height": h, "angle": 0,
        "strokeColor": stroke, "backgroundColor": bg,
        "fillStyle": fill, "strokeWidth": sw, "strokeStyle": ss,
        "roughness": rough, "opacity": 100, "groupIds": list(group),
        "roundness": {"type": 3}, "seed": seed(), "version": 1,
        "versionNonce": seed(), "isDeleted": False, "boundElements": None,
        "updated": 1709500000000, "link": None, "locked": False, "frameId": None
    }
    elements.append(el)
    return el["id"]

def text(x, y, txt, size=16, color=BLACK, family=1, align="left", group=[], width=None):
    lines = txt.split("\n")
    est_w = width or max(len(l) for l in lines) * size * 0.55
    est_h = len(lines) * size * 1.25
    el = {
        "id": uid(), "type": "text", "x": x, "y": y,
        "width": est_w, "height": est_h, "angle": 0,
        "strokeColor": color, "backgroundColor": "transparent",
        "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
        "roughness": 0, "opacity": 100, "groupIds": list(group),
        "roundness": None, "seed": seed(), "version": 1,
        "versionNonce": seed(), "isDeleted": False, "boundElements": None,
        "updated": 1709500000000, "link": None, "locked": False,
        "text": txt, "fontSize": size, "fontFamily": family,
        "textAlign": align, "verticalAlign": "top",
        "containerId": None, "originalText": txt,
        "autoResize": True, "lineHeight": 1.25, "frameId": None
    }
    elements.append(el)
    return el["id"]

def arrow_down(x, length=40):
    el = {
        "id": uid(), "type": "arrow", "x": x, "y": CY[0],
        "width": 0, "height": length, "angle": 0,
        "strokeColor": MED, "backgroundColor": "transparent",
        "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
        "roughness": 0, "opacity": 100, "groupIds": [],
        "roundness": {"type": 2}, "seed": seed(), "version": 1,
        "versionNonce": seed(), "isDeleted": False, "boundElements": None,
        "updated": 1709500000000, "link": None, "locked": False,
        "points": [[0, 0], [0, length]],
        "startBinding": None, "endBinding": None,
        "startArrowhead": None, "endArrowhead": "arrow",
        "frameId": None, "elbowed": False
    }
    elements.append(el)
    advance(length + 10)

def divider():
    """Horizontal line divider between sections"""
    el = {
        "id": uid(), "type": "line", "x": LEFT, "y": CY[0],
        "width": W, "height": 0, "angle": 0,
        "strokeColor": LIGHT, "backgroundColor": "transparent",
        "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
        "roughness": 0, "opacity": 100, "groupIds": [],
        "roundness": {"type": 2}, "seed": seed(), "version": 1,
        "versionNonce": seed(), "isDeleted": False, "boundElements": None,
        "updated": 1709500000000, "link": None, "locked": False,
        "points": [[0, 0], [W, 0]],
        "startBinding": None, "endBinding": None,
        "startArrowhead": None, "endArrowhead": None,
        "frameId": None
    }
    elements.append(el)
    advance(40)

def section_title(title):
    advance(30)
    divider()
    text(LEFT, CY[0], title, size=48, color=BLACK, family=1)
    advance(70)

def subsection(title):
    advance(20)
    text(LEFT, CY[0], title, size=28, color=DARK, family=1)
    advance(45)

def body(txt, indent=0):
    text(LEFT + indent, CY[0], txt, size=16, color=DARK, family=1)
    lines = txt.split("\n")
    advance(len(lines) * 20 + 8)

def body_mono(txt, indent=0):
    text(LEFT + indent, CY[0], txt, size=14, color=ACCENT, family=3)
    lines = txt.split("\n")
    advance(len(lines) * 18 + 8)

def quote(txt, attribution="-- Sara Luster"):
    g = [uid()]
    lines = txt.split("\n")
    wrapped = []
    for line in lines:
        words = line.split()
        cur = ""
        for w in words:
            if len(cur) + len(w) + 1 <= 75:
                cur = (cur + " " + w) if cur else w
            else:
                wrapped.append(cur)
                cur = w
        if cur:
            wrapped.append(cur)
    h = (len(wrapped) + 1) * 20 + 30
    rect(LEFT, CY[0], W, h, stroke=QUOTE_BORDER, bg=QUOTE_BG, fill="solid", sw=1, ss="dashed", group=g)
    text(LEFT + 20, CY[0] + 15, '"' + "\n".join(wrapped) + '"', size=16, color=MED, family=3, group=g)
    text(LEFT + 20, CY[0] + h - 25, attribution, size=13, color=MED, family=3, group=g)
    advance(h + 15)

def stat_row(items, kind="neutral"):
    """Row of stat boxes. items = [(number, label), ...]. kind colors the border."""
    colors = {
        "pain": (PAIN, PAIN_BG, PAIN),
        "solution": (SOLUTION, SOLUTION_BG, SOLUTION),
        "info": (INFO, INFO_BG, INFO),
        "action": (ACTION, ACTION_BG, ACTION),
        "neutral": (DARK, LIGHTER, BLACK),
    }
    stroke, bg, txt_color = colors.get(kind, (DARK, LIGHTER, BLACK))
    n = len(items)
    box_w = (W - (n - 1) * 15) // n
    g = [uid()]
    for i, (num, label) in enumerate(items):
        x = LEFT + i * (box_w + 15)
        rect(x, CY[0], box_w, 70, stroke=stroke, bg=bg, fill="solid", sw=2, group=g)
        text(x + 15, CY[0] + 10, str(num), size=28, color=txt_color, family=1, group=g)
        text(x + 15, CY[0] + 45, label, size=13, color=MED, family=1, group=g)
    advance(85)

def flow_box(label, kind="neutral"):
    """kind: 'pain', 'solution', 'info', 'action', 'neutral'"""
    colors = {
        "pain": (PAIN, PAIN_BG),
        "solution": (SOLUTION, SOLUTION_BG),
        "info": (INFO, INFO_BG),
        "action": (ACTION, ACTION_BG),
        "neutral": (MED, WHITE),
    }
    stroke, bg = colors.get(kind, (MED, WHITE))
    lines = label.split("\n")
    h = max(45, len(lines) * 18 + 20)
    sw = 2
    rect(LEFT + 50, CY[0], W - 100, h, stroke=stroke, bg=bg, fill="solid", sw=sw)
    text(LEFT + 70, CY[0] + 10, label, size=14, color=BLACK, family=1)
    advance(h + 5)

def flow_arrow():
    arrow_down(LEFT + W // 2, 30)

def list_item(txt, indent=0):
    text(LEFT + 20 + indent, CY[0], txt, size=15, color=DARK, family=1)
    advance(22)

def table_row(cols, widths, header=False):
    g = [uid()]
    bg = LIGHTER if header else WHITE
    stroke = DARK if header else LIGHT
    sw = 1
    x = LEFT
    h = 32
    for i, (col, w) in enumerate(zip(cols, widths)):
        rect(x, CY[0], w, h, stroke=stroke, bg=bg, fill="solid", sw=sw, group=g)
        text(x + 10, CY[0] + 7, col, size=13, color=BLACK if header else DARK, family=1, group=g)
        x += w
    advance(h)


# ============================================================
# BUILD PRESENTATION -- SINGLE VERTICAL FLOW
# ============================================================

# --- TITLE ---
text(LEFT, CY[0], "Bear Property Management", size=56, color=BLACK, family=1)
advance(75)
text(LEFT, CY[0], "LIHTC Application Automation", size=28, color=MED, family=1)
advance(40)
text(LEFT, CY[0], "Syntora  |  Prepared for Sara Luster & Jenny Armor", size=16, color=MED, family=1)
advance(50)

# --- LEGEND ---
rect(LEFT, CY[0], W, 160, stroke=DARK, bg=WHITE, fill="solid", sw=2)
text(LEFT + 20, CY[0] + 12, "LEGEND", size=20, color=BLACK, family=1)

legend_y = CY[0] + 45
legend_items = [
    (PAIN, PAIN_BG, "Current state / manual process / pain point"),
    (SOLUTION, SOLUTION_BG, "Our solution / automated / what we build"),
    (INFO, INFO_BG, "Technical details / RealPage / data"),
    (ACTION, ACTION_BG, "Decision needed / flag / Bear must act"),
]
for i, (stroke_c, bg_c, label) in enumerate(legend_items):
    lx = LEFT + 20 + (i % 2) * 490
    ly = legend_y + (i // 2) * 40
    rect(lx, ly, 24, 24, stroke=stroke_c, bg=bg_c, fill="solid", sw=2)
    text(lx + 35, ly + 2, label, size=14, color=DARK, family=1)

# Quote legend
rect(LEFT + 20, legend_y + 80, 24, 24, stroke=QUOTE_BORDER, bg=QUOTE_BG, fill="solid", sw=1)
text(LEFT + 55, legend_y + 82, "Sara's direct quotes from discovery call", size=14, color=DARK, family=1)

advance(175)


# ============================================================
# SECTION 1: BEAR'S WORLD TODAY
# ============================================================
section_title("1. Bear's World Today")

stat_row([
    ("26", "LIHTC Communities"),
    ("576", "Units (Core List)"),
    ("4", "In Lease-Up"),
    ("7", "In Pipeline"),
], kind="info")

stat_row([
    ("7", "Staff on App Review"),
    ("40+", "Hrs/Week (1 Admin)"),
    ("4-5x", "Denial Ratio"),
    ("80%", "Wasted Manual Effort"),
], kind="pain")

subsection("Staffing Breakdown -- Core List")

list_item("1 Admin -- full-time 40+ hrs/week + overtime, just sorting and bucketing")
list_item("2 Leasing Agents -- following up sorted leads, group tours")
list_item("2 Assistant Managers -- normal management duties")
list_item("2 Unplanned Hires -- not budgeted, hired from volume")
advance(10)

quote("We did not anticipate that we would need them all on the front end. We are not even halfway through the project.")
quote("In Madison I almost have the opposite issue -- not enough leads. If we could fill this hole, they could go out and capture those leads and get more marketing done.")


# ============================================================
# SECTION 2: THE PROCESS TODAY
# ============================================================
section_title("2. The Process Today")

text(LEFT, CY[0], "Every step marked MANUAL is where your team spends time.", size=16, color=MED, family=1)
advance(30)

flow_box("Applicant fills out online application (RealPage)", kind="info")
flow_arrow()
flow_box("RealPage dumps into GENERIC waiting list bucket\nNo AMI sorting, no income calculation, nothing", kind="info")
flow_arrow()
flow_box("MANUAL  Admin opens each application one by one\n40+ hrs/week just on this step", kind="pain")
flow_arrow()
flow_box("MANUAL  Hand-calculate projected 12-month income\nHourly x 2080 | Salary | SS | Disability | Child support\nDivorce decree | Tips/commissions | Any dollar entering household", kind="pain")
flow_arrow()
flow_box("MANUAL  Check assets\n> $5K: verify + imputed income  |  < $5K + HOME: verify anyway\nHOME units: student status verification", kind="pain")
flow_arrow()
flow_box("MANUAL  Determine AMI bucket (40 / 50 / 60 / 70 / 80%)\nCompare income to HUD limits by county + household size", kind="pain")
flow_arrow()
flow_box("Unit available?  YES: assign unit  |  NO: add to waiting list", kind="action")
flow_arrow()
flow_box("MANUAL  Annotate AMI bucket next to name on waiting list\n90-day expiration timer -- must act or application dies", kind="pain")

advance(15)
quote("our software can't have someone fill out an application and then determine this person qualifies for a 40% unit... it needs someone to actually open that application, do a quick hand calculation on what they've entered as their income, and do like a best guess")
quote("we're putting like a little 40 or 50 or 60 next to their name so that when we go back to try to place someone off our waiting list, we can go, okay, let's sort it all by the 40s, start at the top of the 40 list")
quote("if we see tips, commissions or bonuses on their pay stub, we actually have to go a step further and call the employer back and say, hey, what do you anticipate that they'll earn in the next 12 months to the best of your ability")


# ============================================================
# SECTION 3: THE COMMUNICATION GAP
# ============================================================
section_title("3. The Communication Gap")

subsection("What Happens Today")
flow_box("Applicant applies", kind="info")
flow_arrow()
flow_box("SILENCE -- no confirmation, no status update", kind="pain")
flow_arrow()
flow_box("Staff buried in sorting -- no time to respond", kind="pain")
flow_arrow()
flow_box("Staff intends to follow up -- but it doesn't happen", kind="pain")
flow_arrow()
flow_box("Bad Google reviews about response time", kind="pain")

advance(15)
quote("all of the people who are applying are like, I haven't heard from anybody what's going on, but our team is like really just trying to hustle through")
quote("the thought is like, I'll get back to them, I'll let them know. But then when they really get back to them, it's been a group of time.")
quote("If you go and you look at our Google reviews, you'll see that a lot of the reviews are about response time. We admit that we know we have a problem. We're just buried.")

subsection("What Sara Asked For")
quote("We really want to make sure that we're sending something out to them right away to say, hey, we've received your application. We've determined based on the information that you provided, that you may qualify for this or that. And we've either added you to our waiting list or a person will reach out to you soon.")

advance(10)
list_item('1. "we\'ve received your application"  -->  Instant confirmation on submission')
list_item('2. "you may qualify for this or that"  -->  AMI bucket result after engine calculates')
list_item('3. "added you to our waiting list"  -->  Waitlist placement with position')
list_item('4. "a person will reach out to you soon"  -->  Staff notification: qualified applicant ready')

subsection("The Back-and-Forth Loops")

body("Loop 1: Tips / Commissions / Bonuses")
body("   Today: Staff sees it on pay stub --> calls employer --> no answer --> calls again", 20)
body("   Automated: Engine flags it --> generates VOE request --> tracks response --> auto-escalates", 20)
advance(10)

body("Loop 2: Income Underreporting")
body("   Today: Hand calc --> tentative bucket --> full processing reveals more income --> bucket changes", 20)
body("   Automated: Engine catches discrepancy --> confidence score LOW --> no false promises", 20)
advance(10)

body("Loop 3: Missing Documents")
body("   Today: Staff discovers missing docs --> calls applicant --> voicemail --> tries again", 20)
body("   Automated: Completeness check on submit --> SMS with specific items --> reminder Day 5, 10", 20)
advance(10)

body("Loop 4: 90-Day Waiting List Expiration")
body("   Today: Manual tracking. If nobody catches it, application just expires.", 20)
body("   Automated: Auto-warning to applicant at day 75. Confirm --> resets. No response --> flagged.", 20)


# ============================================================
# SECTION 4: THE REALPAGE GAP
# ============================================================
section_title("4. The RealPage Gap")

subsection("What RealPage Does")
list_item("Stores applications from online portal")
list_item("Maintains a generic waiting list")
list_item("Compliance document management")
list_item("Budgeting for affordable properties")

advance(5)
quote("on the affordable side, we really like the workflow that RealPage offers. We really like their budgeting software. They're kind of like a big monster software company where everything that you use costs a little extra.")

subsection("What RealPage Cannot Do")
list_item("Calculate projected 12-month income from application data")
list_item("Assign AMI bucket from income")
list_item("Sort waiting list by AMI")
list_item("Auto-communicate status to applicants")
list_item("Pre-screen the 80% that get denied")
list_item("Flag tips/commissions for employer callback")
list_item("Calculate imputed asset income (> $5K)")
list_item("Cross-property applicant matching")

advance(5)
quote("RealPage is kind of a pain in the butt, honestly")

subsection("Competitive Landscape")
cw = [W // 4, W // 4, W // 4, W // 4]
table_row(["Capability", "Pay Score", "Snappt", "Syntora"], cw, header=True)
table_row(["Income verification", "Yes ($12/rpt)", "No", "Yes"], cw)
table_row(["LIHTC 12-mo projection", "No", "No", "Yes"], cw)
table_row(["AMI bucket assignment", "No", "No", "Yes"], cw)
table_row(["Waiting list sorting", "No", "No", "Yes"], cw)
table_row(["Applicant communication", "No", "No", "Yes"], cw)
table_row(["Cross-property matching", "No", "No", "Yes"], cw)
table_row(["Document fraud detection", "No", "Yes (99.8%)", "No"], cw)

advance(15)
body("Pay Score tells you what someone earned. We tell you which AMI bucket")
body("they belong in and sort the waiting list. Different problem.")


# ============================================================
# SECTION 5: THE ENGINE
# ============================================================
section_title("5. The LIHTC Income Engine")

subsection("Income Sources -- Sara's Exact List")

body("EMPLOYMENT", 0)
list_item("Hourly:  rate x 2080 = annual", 20)
list_item("Salary:  straight annual figure", 20)
list_item("Overtime:  FLAG -- employer projection or historical avg", 20)
list_item("Tips:  FLAG -- employer must verify anticipated 12-month", 20)
list_item("Commissions:  FLAG -- employer must verify", 20)
list_item("Bonuses:  FLAG -- employer must verify", 20)
advance(5)

body("OTHER INCOME", 0)
list_item("Child support:  court-ordered annual", 20)
list_item("Divorce decree:  annual amount", 20)
list_item("Social Security:  annual benefit", 20)
list_item("Disability:  annual benefit", 20)
list_item('Informal support:  "if baby daddy\'s buying diapers, we would count that"', 20)
list_item("Self-employment:  Schedule C net (2-year average)", 20)
advance(5)

body("ASSETS", 0)
list_item("> $5,000:  verify + imputed income calculation", 20)
list_item("< $5,000 + HOME layering:  verify regardless", 20)
list_item("< $5,000, no HOME:  self-certification OK", 20)
list_item("HOME units:  student status verification required", 20)

subsection("Processing Logic")
body_mono("1. Sum all annual income (all members, all sources)")
body_mono("2. Add imputed asset income if total assets > $5,000")
body_mono("3. Total = gross annual household income")
body_mono("4. Load HUD income limits for property county + year")
body_mono("5. Look up limit by household size")
body_mono("6. Compare to AMI thresholds:")
body_mono("      <= 40% AMI limit  -->  Bucket: 40%", 20)
body_mono("      <= 50% AMI limit  -->  Bucket: 50%", 20)
body_mono("      <= 60% AMI limit  -->  Bucket: 60%", 20)
body_mono("      <= 70% AMI limit  -->  Bucket: 70%", 20)
body_mono("      <= 80% AMI limit  -->  Bucket: 80%", 20)
body_mono("      > 80% AMI limit   -->  OVER INCOME (deny)", 20)
body_mono("7. Assign LOWEST qualifying bucket")

advance(10)
body("Tax credit anticipates NEXT 12 months (not past 12 like HUD).")

subsection("Outputs Per Application")
list_item("AMI bucket assignment (40 / 50 / 60 / 70 / 80%)")
list_item("Calculated gross annual income with breakdown by source")
list_item("Confidence score:  HIGH | MEDIUM | LOW | DENIED")
list_item("Flags:  employer callback, missing docs, student status, over/under income")


# ============================================================
# SECTION 6: WHAT WE BUILD
# ============================================================
section_title("6. What We Build")

body("Two engines that work standalone today and integrate with RealPage when registration clears.")
body("Bear gets value in weeks. Integration runs in the background.")
advance(20)

# --- PRODUCT OVERVIEW ---
g_menu = [uid()]
rect(LEFT, CY[0], W, 280, stroke=DARK, bg=LIGHTER, fill="solid", sw=2, group=g_menu)
text(LEFT + 20, CY[0] + 15, "THE PLATFORM", size=24, color=BLACK, family=1, group=g_menu)

menu_items = [
    (SOLUTION, "A", "Communication Engine", "Response time, doc collection, applicant notifications"),
    (SOLUTION, "B", "LIHTC Income Engine", "AMI sorting, income calculation, waiting list dashboard"),
]
for i, (color, letter, name, desc) in enumerate(menu_items):
    my = CY[0] + 55 + i * 45
    rect(LEFT + 30, my, 36, 36, stroke=color, bg=WHITE, fill="solid", sw=2, group=g_menu)
    text(LEFT + 39, my + 6, letter, size=20, color=color, family=1, group=g_menu)
    text(LEFT + 80, my + 2, name, size=20, color=BLACK, family=1, group=g_menu)
    text(LEFT + 80, my + 24, desc, size=13, color=MED, family=1, group=g_menu)

# Integration as destination
int_y = CY[0] + 155
rect(LEFT + 20, int_y, W - 40, 2, stroke=MED, bg=MED, fill="solid", sw=1, group=g_menu)
text(LEFT + 20, int_y + 12, "REALPAGE INTEGRATION", size=20, color=INFO, family=1, group=g_menu)
text(LEFT + 20, int_y + 36, "Connects both engines directly to RealPage. No more CSV.", size=14, color=DARK, family=1, group=g_menu)
text(LEFT + 20, int_y + 56, "Registration starts Day 1. Bear uses standalone while it processes.", size=14, color=DARK, family=1, group=g_menu)
text(LEFT + 20, int_y + 76, "26 LIHTC communities today, 37 coming -- CSV doesn't scale. This is the end state.", size=14, color=DARK, family=1, group=g_menu)

advance(295)

subsection("How It Works")
flow_box("TODAY: Bear starts using A + B standalone (CSV in/out)", kind="solution")
flow_arrow()
flow_box("DAY 1: Bear sponsors RealPage vendor registration\nSyntora submits (every field already drafted)", kind="action")
flow_arrow()
flow_box("WEEKS 1-20: Registration processes in background\nBear is already getting value from both engines", kind="info")
flow_arrow()
flow_box("GO-LIVE: CSV handoff replaced by live API connection\nSame engines, same dashboard -- just automated pipes", kind="solution")

advance(10)
body("No waiting. No gap. Value from day one, full integration when it clears.")
advance(20)


# ============================================================
# SECTION 7: PRODUCT A -- COMMUNICATION ENGINE
# ============================================================
section_title("7. Product A: Communication Engine")

body("No RealPage dependency. No API access needed.")
body("Needs only applicant contact info (CSV export from RealPage).")
advance(15)

quote("If you go and you look at our Google reviews, you'll see that a lot of the reviews are about response time. We admit that we know we have a problem. We're just buried.")

subsection("Architecture")
flow_box("DATA IN\nApplicant contact info from RealPage CSV export\nApplication status events (submitted, missing docs, complete)", kind="info")
flow_arrow()
flow_box("DOCUMENT COMPLETENESS CHECK\nAll signatures?  Consecutive paystubs?  Bank statements all pages?\nSSI letter current year?  Child support order?  Asset affidavit?", kind="solution")
flow_arrow()
flow_box("INCOMPLETE  -->  Auto-generate missing document list\nSMS + email with specific items + mobile upload link", kind="action")
flow_arrow()
flow_box("AUTOMATED FOLLOW-UP\nDay 0: specific missing items sent  |  Day 5: reminder\nDay 10: final warning -- application on hold", kind="solution")
flow_arrow()
flow_box("COMPLETE  -->  Staff notified: ready for review\nApplicant notified: all docs received, processing", kind="solution")

subsection("What Sara Asked For -- Delivered Here")
advance(5)
quote("We really want to make sure that we're sending something out to them right away to say, hey, we've received your application. We've determined based on the information that you provided, that you may qualify for this or that. And we've either added you to our waiting list or a person will reach out to you soon.")
advance(5)
list_item('1. "we\'ve received your application"  -->  Instant confirmation on submit')
list_item('2. "added you to our waiting list"  -->  Waitlist position notification')
list_item('3. "a person will reach out to you soon"  -->  Staff gets action item')
list_item('4. Missing doc chase  -->  system handles it, not staff')
list_item('5. 90-day expiration  -->  auto-warning at day 75')

subsection("What This Solves")
stat_row([
    ("Response time", "Same-day vs weeks"),
    ("Doc chase", "Automated"),
    ("Google reviews", "Fix starts here"),
], kind="solution")

advance(5)
list_item("Staff stops calling applicants about missing documents")
list_item("Applicants stop calling Bear asking for status updates")
list_item("No more applications expiring because nobody caught the 90-day window")
list_item("Denial notices auto-generated with HUD/FCRA compliance")

advance(5)
quote("We want to keep our humans dealing with humans and see what we can do to eliminate some of the administrative duty for them")


# ============================================================
# SECTION 8: PRODUCT B -- LIHTC INCOME ENGINE
# ============================================================
section_title("8. Product B: LIHTC Income Engine")

body("No RealPage dependency. CSV export or manual entry.")
body("This is the waiting list sorting -- Sara's magic wand answer.")
advance(15)

subsection("Architecture")
flow_box("DATA IN\nCSV export from RealPage  |  Manual form entry  |  Bulk paste", kind="info")
flow_arrow()
flow_box("LIHTC INCOME ENGINE\nAll income sources  |  Asset imputation  |  AMI bucket assignment\nFlagging (tips, commissions, employer callback)  |  Confidence scoring", kind="solution")
flow_arrow()
flow_box("DASHBOARD\nApplication Inbox  |  AMI Sorted View  |  Action Queue\nWaiting List (next-in-line per bucket)  |  Unit Matching  |  Reports", kind="solution")
flow_arrow()
flow_box("DATA OUT\nSorted waiting list CSV (update RealPage manually)\nStaff action items  |  Reports  |  Audit trail", kind="solution")

advance(5)
body("If paired with Product A:")
flow_box("CONNECTS TO COMMUNICATION ENGINE\nAMI result triggers applicant notification\nFlags trigger staff action items\nDenials trigger cross-property matching", kind="solution")

subsection("What This Solves")
list_item("40+ hrs/week hand calculations  -->  batch upload, results in seconds")
list_item("80% wasted effort on denials  -->  pre-screen before full processing")
list_item("AMI bucket sorting  -->  automatic, no more writing 40/50/60 next to names")
list_item("Tips/commissions/bonuses  -->  flagged for employer callback automatically")
list_item("Asset imputation  -->  calculated, not guessed")


# ============================================================
# SECTION 9: REALPAGE INTEGRATION
# ============================================================
section_title("9. RealPage Integration")

body("The end state. 26 communities today, 37 coming -- CSV doesn't scale.")
body("Bear Real Estate Group needs this wired into the system they already run.")
body("Registration starts Day 1. Bear uses standalone engines while it processes.")
advance(15)

subsection("What Changes at Go-Live")
cw2 = [W // 2, W // 2]
table_row(["Standalone (Now)", "Integrated (Go-Live)"], cw2, header=True)
table_row(["CSV upload / form entry", "API auto-pulls new applications"], cw2)
table_row(["Same calculation engine", "Same calculation engine (no change)"], cw2)
table_row(["Same dashboard", "Same dashboard (no change)"], cw2)
table_row(["Same comms layer", "Same comms layer (no change)"], cw2)
table_row(["CSV export for RealPage", "UpdateProspect writes AMI back"], cw2)
table_row(["Manual waitlist update", "FinalSaveWaitlistTaxCredits auto-sorts"], cw2)

advance(10)
body("Same engines. Integration just removes the manual handoff.")
body("Everything Bear builds with standalone carries forward. Zero rework.")
body("Jenny gets portfolio-wide visibility the day this goes live.")

subsection("Registration Timeline")
flow_box("DAY 1: Bear sponsors vendor application\nSyntora submits (every field already drafted)", kind="action")
flow_arrow()
flow_box("WEEKS 1-4: RealPage reviews registration", kind="info")
flow_arrow()
flow_box("WEEKS 4-8: Infosec review + API sandbox access", kind="info")
flow_arrow()
flow_box("WEEKS 8-14: Syntora builds integration + testing", kind="solution")
flow_arrow()
flow_box("WEEKS 14-20: Certification + go-live\nManual CSV handoff replaced by live API connection", kind="solution")

subsection("RealPage API Endpoints")
body("READ:")
body_mono("  GetApplyNowWizardInitial    -- application field structure")
body_mono("  GetWizardPageData           -- submitted application data")
body_mono("  GetApplyNowSummaryDetails   -- full application summary")
body_mono("  GetEmployment               -- employment/income data")
body_mono("  GetUnitList                 -- available units by property")
body_mono("  GetAllProperties            -- property list across portfolio")
advance(5)
body("WRITE:")
body_mono("  UpdateProspect              -- write AMI bucket tag to prospect")
body_mono("  SaveWizardPageData          -- save calculated data back")
body_mono("  FinalSaveWaitlistTaxCredits -- place into correct waitlist bucket")

subsection("Vendor Application Status")
body("Application name: Syntora LIHTC Income Calculator")
body("Category: Income Verification  |  Type: API Integration")
body("APIs requested: Prospect Mgmt, Resident Mgmt, Pricing & Availability, Units")
body("Every field drafted. Ready to submit the day Bear sponsors.")


# ============================================================
# SECTION 10: COMMUNICATION ENGINE DEEP DIVE
# ============================================================
section_title("10. Communication Engine -- Deep Dive")

body("Detailed breakdown of the communication layer from Product A.")
advance(15)

subsection("Employer Verification Tracking")
body_mono("Day 0:    VOE sent to employer")
body_mono("Day 14:   No response  -->  auto-generate 2nd attempt")
body_mono("Day 30:   Still nothing  -->  flag for paystub fallback")
body_mono("          Staff notified: 'Employer has not responded. Document failed attempts.'")
advance(8)
body_mono("VOE received:")
body_mono("  Blank fields?      -->  flag for follow-up")
body_mono("  Matches paystubs?  -->  proceed to calculation")
body_mono("  Discrepancy?       -->  flag for oral verification")

subsection("120-Day Verification Countdown")
body_mono("All verifications must be dated within 120 days of cert effective date.")
body_mono("If process drags too long, verifications EXPIRE and must be re-obtained.")
advance(5)
body_mono("Dashboard color coding:")
body_mono("  < 60 days:    healthy")
body_mono("  60-90 days:   watch")
body_mono("  90-110 days:  act now")
body_mono("  110-120 days: EXPIRING")
body_mono("  > 120 days:   expired -- must re-obtain")

subsection("Applicant Lifecycle -- 12 Touchpoints")
cw3 = [40, 220, 380, 180, 180]
table_row(["#", "Trigger", "Message", "Channel", "Timing"], cw3, header=True)
table_row(["1", "Application submitted", "We received your application", "SMS + email", "Instant"], cw3)
table_row(["2", "Missing docs detected", "We need [items]. Upload: [link]", "SMS + email", "Hours"], cw3)
table_row(["3", "Reminder", "Application waiting on [items]", "SMS", "Day 5"], cw3)
table_row(["4", "Final warning", "Application on hold [date]", "SMS", "Day 10"], cw3)
table_row(["5", "All docs received", "All documents received", "SMS", "Instant"], cw3)
table_row(["6", "Engine complete", "May qualify for [X]% AMI", "Email", "Same day"], cw3)
table_row(["7", "Flags need resolution", "Verifying with employer", "SMS + email", "Same day"], cw3)
table_row(["8", "Bucket confirmed", "Eligibility confirmed", "Email", "Same day"], cw3)
table_row(["9", "Waitlisted", "Position: [X]", "SMS + email", "Same day"], cw3)
table_row(["10", "90-day warning", "Expires in 15 days", "SMS + email", "Day 75"], cw3)
table_row(["11", "Unit available", "Contact us in [X] days", "SMS + email", "Instant"], cw3)
table_row(["12", "Denied + redirect", "May qualify at [other property]", "Email", "Same day"], cw3)

subsection("Why SMS-First")
list_item("82% of adults earning <$30K own a smartphone")
list_item("16% of Americans are smartphone-only internet users (no home broadband)")
list_item("LIHTC applicants often check email infrequently")
list_item("Voicemails go unreturned on prepaid/limited-minute plans")
list_item("SMS works on every phone plan, every device")

subsection("Denial Notices -- Compliance")
list_item("HUD requires: all reasons, supporting records, dispute rights (14 days)")
list_item("FCRA requires: screening company info, right to free report (60 days)")
list_item("System auto-generates compliant notices. Dawn's team reviews templates once.")


# ============================================================
# SECTION 11: PORTFOLIO PLAY
# ============================================================
section_title("11. The Portfolio Play")

body("For Jenny -- asset management perspective.")
advance(15)

subsection("Cross-Property Matching")
flow_box("DENIED at Property A (Milwaukee County)\nIncome: $42,000  |  Household: 3\nMilwaukee 60% AMI: $40,080  --  OVER INCOME", kind="pain")
flow_arrow()
flow_box("System auto-checks all other Bear properties", kind="solution")
flow_arrow()
flow_box("Property B (Kenosha):    60% AMI = $43,200   QUALIFIES\nProperty C (Dane):       60% AMI = $44,520   QUALIFIES\nProperty D (Racine):     60% AMI = $41,400   QUALIFIES", kind="solution")
flow_arrow()
flow_box("Auto-message: You may qualify at [Property B]. Transfer your application?", kind="solution")

advance(10)
body("No competitor does this. Every denied applicant is a potential")
body("qualified tenant at another Bear property. Zero manual work.")

subsection("Scale")
list_item("26 communities today. 37 soon.")
list_item("Without automation: hire linearly. 1 per 100 units.")
list_item("With automation: engine handles 37 properties same as 1.")
list_item("Core List pilot proves the model, then roll portfolio-wide.")
list_item("Madison: solve sorting  -->  free staff for marketing and lead gen.")


# ============================================================
# SECTION 12: THE MATH
# ============================================================
section_title("12. The Math")

body("Cost of the problem -- Core List alone (576 units).")
advance(15)

subsection("Direct Labor Cost (Annual, Fully Loaded)")
cw4 = [W * 6 // 10, W * 4 // 10]
table_row(["Role", "Annual Cost"], cw4, header=True)
table_row(["Admin (sorting/bucketing)", "~$67,000"], cw4)
table_row(["2 Leasing Agents (50% on app follow-up)", "~$51,000"], cw4)
table_row(["2 Unplanned Hires", "~$103,000"], cw4)
table_row(["TOTAL", "~$221,000 / year"], cw4)

advance(15)
stat_row([
    ("80%", "Wasted on denials"),
    ("32 hrs", "Saved per week from pre-screening"),
    ("~$75K", "Vacancy loss recoverable"),
], kind="pain")

subsection("Portfolio Scale")
body("Core List alone = $221K labor + $75K vacancy per year.")
body("26 communities with similar ratios = the problem only grows.")
body("Growing to 37 -- without automation, staffing scales linearly.")
body("Tax credit clawback from manual calculation errors = catastrophic.")


# ============================================================
# SECTION 13: DECISIONS
# ============================================================
section_title("13. Decisions for Bear")

advance(5)
items = [
    ("Starting Point", "Communication Engine first? Income Engine first? Both at once?\nWe recommend both -- Communication Engine delivers value while Income Engine builds."),
    ("Pilot Property", "Core List (576 units, Milwaukee)? Or a different property?"),
    ("RealPage Registration", "Start Day 1 -- runs in background while Bear uses standalone.\nWe need: PMC ID, Site ID(s), confirmation contract allows third-party API access."),
    ("Compliance Validation", "Should Dawn Parmelee's team validate calculation logic before go-live?"),
    ("Communication Channel", "Notifications from Bear's domain (leasing@bearproperty.com)?\nEmail + SMS, or email only?\nCompliance review of notification templates?"),
    ("Data Access", "Can you export waiting list data from RealPage today?\nWhat income fields does the online application collect?\nAMI buckets same across all 26 or vary by property/county?"),
    ("Who's Involved Going Forward", "Sara (operations) + Jenny (asset management)\nDawn (compliance) -- when?\nRealPage account rep -- who?"),
]

for title, detail in items:
    lines = detail.split("\n")
    h = max(60, len(lines) * 20 + 40)
    rect(LEFT, CY[0], W, h, stroke=ACTION, bg=ACTION_BG, fill="solid", sw=2)
    text(LEFT + 20, CY[0] + 10, title, size=20, color=ACTION, family=1)
    text(LEFT + 20, CY[0] + 38, detail, size=14, color=DARK, family=1)
    advance(h + 12)


# ============================================================
# MAGIC WAND -- CLOSE
# ============================================================
advance(40)
divider()
advance(20)

rect(LEFT, CY[0], W, 180, stroke=DARK, bg=LIGHTER, fill="solid", sw=3)
text(LEFT + 30, CY[0] + 20, "Sara's Magic Wand Answer", size=28, color=DARK, family=1)
text(LEFT + 30, CY[0] + 65, '"The wait list sorting."', size=40, color=BLACK, family=1)
text(LEFT + 30, CY[0] + 120, '"We\'re spending a lot of time there."', size=20, color=MED, family=1)
text(LEFT + 30, CY[0] + 150, "-- Sara Luster, VP of Property & Portfolio Management", size=14, color=MED, family=3)


# ============================================================
# OUTPUT
# ============================================================
excalidraw = {
    "type": "excalidraw",
    "version": 2,
    "source": "https://excalidraw.com",
    "elements": elements,
    "appState": {
        "gridSize": 20,
        "gridStep": 5,
        "gridModeEnabled": False,
        "viewBackgroundColor": "#ffffff"
    },
    "files": {}
}

output = "bear-property-presentation.excalidraw"
with open(output, "w", encoding="utf-8") as f:
    json.dump(excalidraw, f, indent=2)

print(f"Generated: {output}")
print(f"Elements: {len(elements)}")
print(f"Canvas height: ~{CY[0]}px")
