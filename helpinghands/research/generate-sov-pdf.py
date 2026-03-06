"""Generate Share of Voice baseline PDF report for Gosia."""

from fpdf import FPDF


class ReportPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, "Prepared by Parker Gawne, Syntora", align="R")
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"{self.page_no()}", align="C")


def separator(pdf, y_offset=0):
    y = pdf.get_y() + y_offset
    pdf.set_draw_color(200, 200, 200)
    pdf.line(10, y, 200, y)
    pdf.set_y(y + 3)


def stat_box(pdf, label, value, x, y, w=42, h=28):
    """Draw a bordered stat box."""
    pdf.set_draw_color(180, 180, 180)
    pdf.rect(x, y, w, h)
    # Value
    pdf.set_xy(x, y + 4)
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w, 10, value, align="C")
    # Label
    pdf.set_xy(x, y + 15)
    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w, 5, label, align="C")


def section_title(pdf, text):
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)


def body_text(pdf, text):
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(190, 5, text)
    pdf.ln(1)


def table_row(pdf, cols, widths, bold=False, bg=False):
    """Draw a table row."""
    style = "B" if bold else ""
    if bg:
        pdf.set_fill_color(240, 240, 240)
    pdf.set_font("Helvetica", style, 8.5)
    pdf.set_text_color(0, 0, 0)
    h = 6
    for i, (col, w) in enumerate(zip(cols, widths)):
        pdf.cell(w, h, col, border=0, fill=bg, align="L" if i == 0 else "C")
    pdf.ln(h)


def build_pdf():
    pdf = ReportPDF()
    pdf.set_auto_page_break(auto=True, margin=22)
    pdf.add_page()

    # ---- Title ----
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 11, "AI Search Visibility Report", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 6, "Helping Hands Cleaning Services  |  March 2, 2026", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # ---- Intro ----
    pdf.set_text_color(40, 40, 40)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(190, 5.5, (
        "We ran an initial sample of 35 queries that homeowners commonly ask AI "
        "assistants like ChatGPT, Perplexity, and Google Gemini when looking for "
        "a cleaning service. This report shows how often Helping Hands was "
        "recommended. A full audit of thousands of individual prompts across "
        "your service area will follow."
    ))
    pdf.ln(4)

    # ---- Stat Boxes ----
    box_y = pdf.get_y()
    stat_box(pdf, "Sample Queries", "35", 10, box_y)
    stat_box(pdf, "Times Recommended", "7", 56, box_y)
    stat_box(pdf, "Overall Rate", "20%", 102, box_y)
    stat_box(pdf, "Without Brand Name", "12.5%", 148, box_y)
    pdf.set_y(box_y + 34)

    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 5, (
        "\"Without brand name\" means people searching for a cleaning service "
        "without typing \"Helping Hands\" specifically."
    ), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    separator(pdf)

    # ---- The Problem ----
    section_title(pdf, "The Problem")
    body_text(pdf, (
        "When someone searches Google, your 1,000+ reviews and 4.9-star rating "
        "help you show up. But when someone asks ChatGPT or Google's AI for a "
        "cleaning service recommendation, those reviews are not enough. AI tools "
        "need to find answers on your website -- and right now, your website does "
        "not have the kind of content AI tools are looking for. "
        "The result: AI assistants recommend national franchises like Maid Brigade "
        "and MaidPro instead of Helping Hands, even in your own service area."
    ))
    separator(pdf)

    # ---- Where You Show Up ----
    section_title(pdf, "Where You Show Up vs. Where You Do Not")
    pdf.ln(1)

    widths = [65, 25, 25, 75]
    table_row(pdf, ["Category", "Tested", "Found", "Notes"], widths, bold=True, bg=True)

    rows = [
        ["Brand name searches", "3", "3", "Expected -- searching by name"],
        ["City-specific searches", "10", "2", "Only Wheaton and Oak Park"],
        ["Service-specific searches", "6", "1", "Only post-construction"],
        ["Conversational questions", "4", "1", "Only 1 of 4 Elmhurst queries"],
        ["Pricing questions", "4", "0", "Zero visibility"],
        ["Decision questions", "4", "0", "Zero visibility"],
        ["Eco/trust questions", "4", "0", "Zero visibility"],
    ]
    for i, row in enumerate(rows):
        table_row(pdf, row, widths, bg=(i % 2 == 1))

    pdf.ln(2)
    body_text(pdf, (
        "You are absent from 8 of 10 cities tested -- including Elmhurst, your "
        "headquarters. When someone asks ChatGPT \"best house cleaning service in "
        "Elmhurst IL,\" Helping Hands does not appear."
    ))
    separator(pdf)

    # ---- Why This Happens ----
    # Only page break if not enough room for title + intro + full table (~70mm)
    if pdf.get_y() > 220:
        pdf.add_page()
    section_title(pdf, "Why This Happens")
    body_text(pdf, (
        "Different AI tools get their information from different places:"
    ))

    widths2 = [40, 70, 80]
    table_row(pdf, ["AI Tool", "Where It Gets Info", "Your Visibility"], widths2, bold=True, bg=True)
    ai_rows = [
        ["Perplexity", "Google Maps, Yelp, directories", "Strong (listed first)"],
        ["Google Gemini", "Google Maps, Business Profile", "Likely strong"],
        ["ChatGPT", "Website content (58%)", "Weak (20%)"],
        ["Google AI Overviews", "Business Profile, YouTube", "Mixed"],
    ]
    for i, row in enumerate(ai_rows):
        table_row(pdf, row, widths2, bg=(i % 2 == 1))

    pdf.ln(1)
    body_text(pdf, (
        "AI tools that look at directories and Google Maps already find you "
        "because your reviews are excellent. AI tools that look at website "
        "content do not find you because your website does not have the right "
        "kind of pages for them to read."
    ))
    separator(pdf)

    # ---- Competitor Comparison ----
    section_title(pdf, "Who AI Recommends Instead")
    body_text(pdf, (
        "When Helping Hands does not appear, these companies get recommended. "
        "These are all national franchises -- you are the only independent "
        "company appearing at all."
    ))

    widths3 = [80, 50, 60]
    table_row(pdf, ["Company", "Mentions (of 35)", "Type"], widths3, bold=True, bg=True)
    comp_rows = [
        ["Helping Hands", "4 non-brand", "Independent (you)"],
        ["Maid Brigade", "4", "National franchise"],
        ["MaidPro", "3", "National franchise"],
        ["Molly Maid", "2", "National franchise"],
        ["Merry Maids", "2", "National franchise"],
    ]
    for i, row in enumerate(comp_rows):
        table_row(pdf, row, widths3, bg=(i % 2 == 1))

    pdf.ln(1)
    body_text(pdf, (
        "You are already tied with Maid Brigade for most non-brand mentions, "
        "and you are doing this with zero AI-specific content. There is "
        "significant room to grow."
    ))
    separator(pdf)

    # ---- What We Do About It ----
    section_title(pdf, "What We Do About It")

    fixes = [
        [
            "Location-specific answer pages",
            "33 cities x 8 service types = 264+ pages. Each one directly answers "
            "the question someone would ask an AI assistant, like \"Who is the "
            "best house cleaning service in Naperville IL?\""
        ],
        [
            "Pricing content",
            "Pages that answer real pricing questions like \"How much does deep "
            "cleaning cost in DuPage County?\" AI tools love specific, transparent "
            "pricing information."
        ],
        [
            "Decision content",
            "Pages that help people choose: \"House cleaning vs maid service,\" "
            "\"What to look for in a cleaning company.\" These queries currently "
            "go entirely to your competitors."
        ],
        [
            "Eco and trust content",
            "Green cleaning is your differentiator, but AI tools do not know that. "
            "Dedicated pages about your products, process, and certifications fix this."
        ],
        [
            "AI-readable formatting",
            "Every page is formatted so AI tools can quickly extract and cite your "
            "answers. This includes behind-the-scenes tags that AI tools use to "
            "understand your business."
        ],
    ]

    for i, (title, desc) in enumerate(fixes):
        pdf.set_font("Helvetica", "B", 9.5)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(190, 5, f"{i + 1}.  {title}", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(60, 60, 60)
        pdf.set_x(20)
        pdf.multi_cell(170, 4.5, desc)
        pdf.ln(1)

    separator(pdf)

    # ---- What We Track ----
    section_title(pdf, "What We Track Going Forward")

    tracks = [
        "Overall AI visibility rate across thousands of real prompts",
        "Non-brand visibility (searches that do not include your company name)",
        "Pricing and decision query coverage (currently 0%)",
        "City-level coverage across your full 33-city service area",
    ]
    for t in tracks:
        pdf.set_font("Helvetica", "", 9.5)
        pdf.set_text_color(40, 40, 40)
        pdf.cell(5, 5, "-")
        pdf.cell(185, 5, t, new_x="LMARGIN", new_y="NEXT")

    pdf.ln(3)

    # ---- Bottom note ----
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(120, 120, 120)
    pdf.multi_cell(190, 5, (
        "This report is a preliminary baseline from a 35-query sample. "
        "Our full audit will test thousands of individual prompts across "
        "every city, service type, and question format to give you a "
        "complete picture of your AI visibility."
    ))

    out_path = (
        r"C:\Users\Parker Gawne\Desktop\Syntora\Clients\prospects"
        r"\helpinghands\research\AI-Search-Visibility-Report.pdf"
    )
    pdf.output(out_path)
    print(f"PDF saved to: {out_path}")


if __name__ == "__main__":
    build_pdf()
