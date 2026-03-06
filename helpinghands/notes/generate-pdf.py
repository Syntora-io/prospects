"""Generate AEO vetting questions PDF for Gosia."""

from fpdf import FPDF


class QuestionsPDF(FPDF):
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


def draw_separator(pdf):
    """Thin horizontal line."""
    y = pdf.get_y()
    pdf.set_draw_color(200, 200, 200)
    pdf.line(10, y, 200, y)
    pdf.ln(6)


def build_pdf():
    pdf = QuestionsPDF()
    pdf.set_auto_page_break(auto=True, margin=22)
    pdf.set_text_color(0, 0, 0)
    pdf.add_page()

    # --- Title ---
    pdf.ln(4)
    pdf.set_font("Helvetica", "B", 22)
    pdf.cell(0, 11, "Questions for Your SEO Agency Meeting", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 6, "Helping Hands Cleaning Services  |  March 2026", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(6)
    draw_separator(pdf)

    questions = [
        {
            "q": "Are you doing anything right now specifically for AI search -- like when people use ChatGPT, Perplexity, or Google's AI answers to find a cleaning service?",
            "why": (
                "AI search works differently than traditional Google search. "
                "If they say \"yes, our regular SEO covers that too,\" that is a sign "
                "they may not understand the difference. AI search engines use "
                "completely different methods to decide which businesses to recommend."
            ),
        },
        {
            "q": "I searched for a cleaning service in Naperville on ChatGPT and we didn't show up. What would you do to fix that?",
            "why": (
                "This forces a specific answer. Watch out for vague responses like "
                "\"we'll optimize your content.\" A good answer would include concrete "
                "steps -- like creating dedicated pages, updating business listings, "
                "or changing how the website shares information with AI tools."
            ),
        },
        {
            "q": "Do you know if our website currently allows AI tools like ChatGPT and Perplexity to read our pages? Or are they blocked?",
            "why": (
                "Most websites are set up to allow Google to read them, but AI tools "
                "use their own separate readers. If the website does not specifically "
                "allow these AI readers in, they cannot find your business. A good "
                "agency would know exactly which AI readers exist and whether "
                "your site allows them."
            ),
        },
        {
            "q": "Have you set up anything on our website that gives AI tools a summary of our business -- like an overview file they can read quickly?",
            "why": (
                "There is a newer feature that acts like a cheat sheet for AI tools. "
                "It tells them what your business does, what services you offer, and "
                "where to find key pages. Our SEO plugin may have auto-generated one, "
                "but if nobody has customized it, it is probably not helping."
            ),
        },
        {
            "q": "How do you measure whether AI assistants are actually recommending us? Do you have any reports that show that?",
            "why": (
                "Traditional SEO reports show Google rankings, clicks, and website "
                "traffic. But none of that tells you whether ChatGPT, Perplexity, or "
                "Gemini are recommending Helping Hands when people ask for a cleaning "
                "service. If they cannot show AI-specific reporting, they are not "
                "tracking it."
            ),
        },
        {
            "q": "Are you creating any content that is specifically designed for AI tools to read and reference -- separate from blog posts and the regular website pages?",
            "why": (
                "AI tools prefer a very specific format: direct answers to specific "
                "questions, organized in a way that is easy for them to pull from. "
                "This is different from a blog post written for a person to read. "
                "If all content is designed the same way, they may be missing "
                "the AI audience entirely."
            ),
        },
        {
            "q": "What kind of behind-the-scenes data tags do we have on our website? For example, do our service pages have FAQ tags that AI tools can read?",
            "why": (
                "AI tools rely on special invisible tags on your website to understand "
                "your business. Right now we have some basic ones, but we are missing "
                "important ones for individual services, frequently asked questions, "
                "and customer ratings. A good agency would know exactly what is there "
                "and what is missing."
            ),
        },
        {
            "q": "How many new pages are you creating for us each month? And how do you decide what topics to cover?",
            "why": (
                "For AI search, volume matters. Covering every combination of your "
                "services across all 33+ cities you serve means hundreds of pages, "
                "not a handful of blog posts per month. If they are producing 2-4 "
                "articles a month, that is traditional content marketing -- not "
                "enough for AI visibility."
            ),
        },
        {
            "q": "Are we listed on the newer directories and databases that AI tools pull information from? Not just Yelp and Google -- but places like Wikipedia-style databases and business data aggregators?",
            "why": (
                "AI tools pull business information from different places than Google "
                "does. We are well-listed on the traditional directories, but AI tools "
                "also reference knowledge databases, data aggregators, and review "
                "platforms that most cleaning companies are not listed on."
            ),
        },
        {
            "q": "What is your plan for making sure we show up when someone asks Google's Gemini or AI Overviews for a cleaning service recommendation?",
            "why": (
                "Google's own AI now answers questions at the top of search results "
                "before showing the regular links. This is the biggest near-term "
                "change. Google's AI pulls heavily from your Google Business Profile "
                "accuracy and YouTube videos -- even more than traditional website "
                "links. A strong answer would mention both of those."
            ),
        },
    ]

    for i, item in enumerate(questions):
        # Check if we need a new page
        if pdf.get_y() > 222:
            pdf.add_page()

        # Question number
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(0, 0, 0)
        q_text = f"{i + 1}.  {item['q']}"
        pdf.multi_cell(190, 6, q_text)
        pdf.ln(2)

        # Explanation
        pdf.set_font("Helvetica", "", 9.5)
        pdf.set_text_color(60, 60, 60)
        pdf.set_x(20)
        pdf.multi_cell(170, 5, item["why"])
        pdf.set_text_color(0, 0, 0)
        pdf.ln(4)
        draw_separator(pdf)

    out_path = r"C:\Users\Parker Gawne\Desktop\Syntora\Clients\prospects\helpinghands\notes\AEO-Vetting-Questions-Edge-Digital.pdf"
    pdf.output(out_path)
    print(f"PDF saved to: {out_path}")


if __name__ == "__main__":
    build_pdf()
