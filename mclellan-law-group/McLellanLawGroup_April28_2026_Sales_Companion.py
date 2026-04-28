"""
Sales Companion PDF — McLellan Law Group, LLP
Sales Rep: Jacob Meissner | Date: April 28, 2026
Internal document — do not share with prospect.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)

# ── Colors — DO NOT MODIFY ──
DARK_NAVY = HexColor("#1a2332")
ACCENT_GREEN = HexColor("#3B6D11")
MEDIUM_GRAY = HexColor("#555555")
LIGHT_GRAY = HexColor("#888888")
RULE_GRAY = HexColor("#CCCCCC")
QUOTE_BG = HexColor("#F5F7F0")
WHITE = HexColor("#FFFFFF")
RED_WARNING = HexColor("#CC0000")
RED_ACCENT = HexColor("#C0392B")

OUTPUT_PATH = "mclellan-law-group/McLellanLawGroup_April28_2026_Sales_Companion.pdf"


def add_page_elements(canvas, doc):
    """Draws red warning header and confidential footer on every page. DO NOT MODIFY."""
    canvas.saveState()
    width, height = letter
    canvas.setFont("Helvetica-Bold", 10)
    canvas.setFillColor(RED_WARNING)
    canvas.drawCentredString(width / 2, height - 0.38 * inch,
                             "FOR INTERNAL USE ONLY; DO NOT SHARE.")
    canvas.setStrokeColor(RED_WARNING)
    canvas.setLineWidth(0.5)
    canvas.line(0.6 * inch, height - 0.44 * inch,
                width - 0.6 * inch, height - 0.44 * inch)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(LIGHT_GRAY)
    canvas.drawCentredString(width / 2, 0.28 * inch,
                             "SMB Team  |  Confidential  |  Internal Document")
    canvas.restoreState()


doc = SimpleDocTemplate(
    OUTPUT_PATH, pagesize=letter,
    topMargin=0.72 * inch, bottomMargin=0.42 * inch,
    leftMargin=0.6 * inch, rightMargin=0.6 * inch,
)

# ── Styles — DO NOT MODIFY ──
S = {}
S["title"] = ParagraphStyle(
    "title", fontName="Helvetica-Bold", fontSize=16, leading=20,
    textColor=DARK_NAVY, spaceAfter=1)
S["subtitle"] = ParagraphStyle(
    "subtitle", fontName="Helvetica", fontSize=9.5, leading=13,
    textColor=LIGHT_GRAY, spaceAfter=3)
S["section"] = ParagraphStyle(
    "section", fontName="Helvetica-Bold", fontSize=11, leading=15,
    textColor=ACCENT_GREEN, spaceBefore=6, spaceAfter=2)
S["subsection"] = ParagraphStyle(
    "subsection", fontName="Helvetica-Bold", fontSize=10, leading=13,
    textColor=DARK_NAVY, spaceBefore=2, spaceAfter=1)
S["bullet"] = ParagraphStyle(
    "bullet", fontName="Helvetica", fontSize=9.5, leading=13,
    textColor=MEDIUM_GRAY, leftIndent=12, bulletIndent=0,
    spaceBefore=1, spaceAfter=1)
S["bullet_dark"] = ParagraphStyle(
    "bullet_dark", fontName="Helvetica", fontSize=9.5, leading=13,
    textColor=DARK_NAVY, leftIndent=12, bulletIndent=0,
    spaceBefore=1, spaceAfter=1)
S["quote"] = ParagraphStyle(
    "quote", fontName="Helvetica-Oblique", fontSize=9.5, leading=13,
    textColor=DARK_NAVY, leftIndent=6, rightIndent=6,
    spaceBefore=1, spaceAfter=1)
S["snap_label"] = ParagraphStyle(
    "snap_label", fontName="Helvetica-Bold", fontSize=8.5, leading=11,
    textColor=LIGHT_GRAY)
S["snap_value"] = ParagraphStyle(
    "snap_value", fontName="Helvetica", fontSize=9.5, leading=12,
    textColor=DARK_NAVY)
S["objection_q"] = ParagraphStyle(
    "objection_q", fontName="Helvetica-Bold", fontSize=9.5, leading=13,
    textColor=RED_ACCENT, spaceBefore=2, spaceAfter=0)
S["objection_a"] = ParagraphStyle(
    "objection_a", fontName="Helvetica", fontSize=9.5, leading=13,
    textColor=MEDIUM_GRAY, leftIndent=8, spaceAfter=2)
S["price_main"] = ParagraphStyle(
    "price_main", fontName="Helvetica-Bold", fontSize=9.5, leading=13,
    textColor=DARK_NAVY)
S["price_detail"] = ParagraphStyle(
    "price_detail", fontName="Helvetica", fontSize=8.5, leading=12,
    textColor=MEDIUM_GRAY)
S["savings"] = ParagraphStyle(
    "savings", fontName="Helvetica-Bold", fontSize=9.5, leading=13,
    textColor=ACCENT_GREEN, alignment=TA_CENTER, spaceBefore=3)
S["disclaimer"] = ParagraphStyle(
    "disclaimer", fontName="Helvetica-Oblique", fontSize=8.5, leading=11,
    textColor=LIGHT_GRAY, spaceBefore=1, spaceAfter=1)


# ── Helpers — DO NOT MODIFY ──
def b(text):
    return Paragraph(f"<bullet>&bull;</bullet> {text}", S["bullet"])

def bd(text):
    return Paragraph(f"<bullet>&bull;</bullet> {text}", S["bullet_dark"])

def thin_rule():
    return HRFlowable(width="100%", thickness=0.5, color=RULE_GRAY,
                       spaceBefore=3, spaceAfter=3)

def quote_block(text):
    p = Paragraph(f'"{text}"', S["quote"])
    t = Table([[p]], colWidths=[6.5 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), QUOTE_BG),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


# ══════════════════════════════════════════════════════════
# PAGE 1
# ══════════════════════════════════════════════════════════
story = []

story.append(Paragraph("McLellan Law Group, LLP", S["title"]))
story.append(Paragraph("Sales Companion  |  April 28, 2026  |  Rep: Jacob Meissner", S["subtitle"]))
story.append(thin_rule())

# ── Prospect Snapshot ──
story.append(Paragraph("Prospect Snapshot", S["section"]))
snap = [
    [Paragraph("<b>Owner</b>", S["snap_label"]),
     Paragraph("<b>Revenue</b>", S["snap_label"]),
     Paragraph("<b>Team</b>", S["snap_label"]),
     Paragraph("<b>Stage</b>", S["snap_label"]),
     Paragraph("<b>Close Rate</b>", S["snap_label"]),
     Paragraph("<b>Location</b>", S["snap_label"])],
    [Paragraph("Claire Melehani &amp; Steven McLellan", S["snap_value"]),
     Paragraph("$320K collected; $366K billed (2025)", S["snap_value"]),
     Paragraph("3 attorneys + 1 ops", S["snap_value"]),
     Paragraph("Stage 4", S["snap_value"]),
     Paragraph("8–10% (Law Broker)", S["snap_value"]),
     Paragraph("Saratoga, CA", S["snap_value"])],
]
t1 = Table(snap, colWidths=[1.15*inch, 1.2*inch, 0.8*inch, 0.7*inch, 0.7*inch, 1.15*inch])
t1.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("TOPPADDING", (0,0), (-1,-1), 1), ("BOTTOMPADDING", (0,0), (-1,-1), 1),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("LINEBELOW", (0,1), (-1,1), 0.5, RULE_GRAY),
]))
story.append(t1)
story.append(Spacer(1, 4))

# ── Dominant Buying Motive ──
story.append(Paragraph("Dominant Buying Motive: FREEDOM", S["section"]))
story.append(Paragraph("Claire wants a firm that generates revenue and serves clients without requiring her to be present for every decision.", S["subsection"]))

story.append(quote_block("We're stuck in the Abyss — more revenue just means more partner workload, not more freedom."))
story.append(Spacer(1, 1))
story.append(quote_block("We want to build a general counsel subscription model — predictable, recurring revenue from clients on retainer."))
story.append(Spacer(1, 2))

story.append(Paragraph("<b>What she wants:</b>", S["subsection"]))
story.append(bd("<b>Escape the Abyss.</b> Growth should mean more freedom — not more hours."))
story.append(bd("<b>A firm that runs without her.</b> Both partners should be able to step away and revenue continues."))
story.append(bd("<b>Recurring revenue.</b> The general counsel subscription model is her stated next-stage goal."))

story.append(Spacer(1, 2))

story.append(Paragraph("<b>What is stopping her:</b>", S["subsection"]))
story.append(b("<b>Steven cannot delegate.</b> Every decision flows through him, capping output at his personal hours."))
story.append(b("<b>Intake converts at 8–10%.</b> 90% of prospects who raise their hand never become clients."))
story.append(b("<b>Collections gap.</b> $46K+ per year earned but uncollected — cash flow pressure against a $30K break-even."))
story.append(b("<b>No owned lead pipeline.</b> All leads come from a shared marketplace the firm does not control."))

story.append(thin_rule())

# ── Why This Marketing Package ──
story.append(Paragraph("Why This Marketing Package", S["section"]))

story.append(Paragraph("<b>What it does for her:</b>", S["subsection"]))
story.append(bd("Gives the firm an exclusive, owned lead pipeline — not a shared marketplace she competes in."))
story.append(bd("Puts McLellan Law Group in front of high-net-worth clients in San Jose and adjacent cities before they even call a competitor."))
story.append(bd("Turns the AI avatar video content the firm already produces into a paid channel that books consultations."))

story.append(Paragraph("<b>Full Service Marketing — Starter  |  $4,847/mo bundled</b>", S["subsection"]))
story.append(b("$600K goal from a $320K base is aggressive — Starter tier over Essentials per boundary rule."))
story.append(b("No Google Ads, LSA, or Meta ads currently — full channel launch required, not a sub-package."))
story.append(b("Costanzo (69 reviews) and Structure Law Group (27/5.0★) are active in paid and organic; waiting widens the gap."))

story.append(thin_rule())

# ── Why This Coaching Package ──
story.append(Paragraph("Why This Coaching Package", S["section"]))

story.append(Paragraph("<b>What it does for her:</b>", S["subsection"]))
story.append(bd("Builds the delegation systems that let Steven hand off casework — removing the personal ceiling on the firm's revenue."))
story.append(bd("Creates the operational infrastructure the general counsel subscription model requires before it can be sold."))
story.append(bd("Establishes a formal AR process to recover the $46K+ in earned revenue the firm is not collecting each year."))

story.append(Paragraph("<b>Elite Coach  |  $1,600/mo bundled</b>", S["subsection"]))
story.append(b("$320K collected revenue puts the firm in the Elite Coach tier."))
story.append(b("The Abyss pattern is a systems problem — coaching builds delegation structures, not just more marketing."))
story.append(b("Phase 2: FCOO Advisor added at $500K revenue to accelerate the self-managing layer."))


# ══════════════════════════════════════════════════════════
# PAGE 2
# ══════════════════════════════════════════════════════════
story.append(PageBreak())

story.append(Paragraph("McLellan Law Group — Sales Companion (continued)", S["title"]))
story.append(thin_rule())

# ── Why This Ad Spend ──
story.append(Paragraph("Why This Ad Spend", S["section"]))

story.append(Paragraph("<b>What it does for her:</b>", S["subsection"]))
story.append(bd("Replaces Law Broker's shared 8–10% funnel with exclusive leads the firm owns and controls."))
story.append(bd("At $8,000 estimated case value, a single signed client from ads covers 2–3 months of ad spend."))

story.append(Paragraph("<b>Recommended Ad Spend Range:</b>", S["subsection"]))
story.append(b("<b>Conservative:</b> $3,000/mo — channel minimums for business law (PPC $1,500 + LSA $500 + Meta $1,000)."))
story.append(b("<b>Aggressive:</b> $6,000/mo — Starter tier cap; $600K goal x 20% / 12 x 1.3 (Tier 2 Silicon Valley) = $13,000; capped at tier maximum."))

story.append(Paragraph("<b>Estimated Return on Investment:</b>", S["subsection"]))
story.append(b("<b>Conservative:</b> ~12 leads / 15% close = 2 cases x $8,000 = $16,000/mo vs. $3,000 spend = 5.3x return (est.)."))
story.append(b("<b>Aggressive:</b> ~30 leads / 15% close = 4–5 cases x $8,000 = $32,000–$40,000/mo vs. $6,000 spend = 5–7x return (est.)."))
story.append(Paragraph("<i>All figures are estimates based on business law CPL benchmarks and a 15% default close rate. Not guaranteed.</i>", S["disclaimer"]))

story.append(b("<b>Conservative basis:</b> Business law minimums — Google PPC $1,500 + LSA $500 + Meta $1,000 = $3,000."))
story.append(b("<b>Aggressive basis:</b> $600K x 20% / 12 x 1.3 (Tier 2) = $13,000; capped at Starter tier maximum of $6,000."))
story.append(b("Total at aggressive: $12,447/mo = 24.9% of $600K goal. Under the 35% cap."))

story.append(thin_rule())

# ── If She Pushes Back ──
story.append(Paragraph("If She Pushes Back", S["section"]))

story.append(Paragraph('"Google Ads are too expensive — we\'re not sure paid search works for civil litigation."', S["objection_q"]))
story.append(Paragraph("Law Broker is a shared marketplace; Google Ads delivers leads exclusively to McLellan. Costanzo (69 reviews) dominates local pack results where McLellan does not appear. One signed case at $8,000 ACV covers months of ad spend.", S["objection_a"]))

story.append(Paragraph('"Our collection rate is already a problem — I\'m not sure we can add more expenses right now."', S["objection_q"]))
story.append(Paragraph("The coaching builds the AR system that recovers the $46K+ already earned. That recovered revenue effectively funds the investment — without acquiring a single new client.", S["objection_a"]))

story.append(Paragraph('"Steven won\'t change — he doesn\'t delegate and has always worked this way."', S["objection_q"]))
story.append(Paragraph("Coaching builds scaffolding around Steven — documented workflows and handoff points — not a personality change. Claire already delegates; that model can be systematized without Steven's buy-in on day one.", S["objection_a"]))

story.append(Paragraph('"We want to start the general counsel subscription model before doing anything else."', S["objection_q"]))
story.append(Paragraph("The subscription model requires a self-managing firm first — no client pays a retainer to a firm where every decision needs a founding partner. Phase 1 systems are the prerequisite, not a detour.", S["objection_a"]))

story.append(thin_rule())

# ── Investment At A Glance ──
story.append(Paragraph("Investment At A Glance", S["section"]))

price_data = [
    [Paragraph("<b>Full Service Marketing — Starter</b>", S["price_main"]),
     Paragraph("$4,847/mo", S["price_main"])],
    [Paragraph("Google Ads, LSA, Meta, SEO, website optimization — all channels.", S["price_detail"]),
     Paragraph("<strike>$5,697</strike> stand alone", S["price_detail"])],
    [Paragraph("<b>Elite Coach</b>", S["price_main"]),
     Paragraph("$1,600/mo", S["price_main"])],
    [Paragraph("Weekly coaching, delegation systems, AR process, accountability structure.", S["price_detail"]),
     Paragraph("<strike>$2,497</strike> stand alone", S["price_detail"])],
    [Paragraph("<b>Recommended Ad Spend</b>", S["price_main"]),
     Paragraph("$3,000–$6,000/mo", S["price_main"])],
    [Paragraph("Goes to Google, LSA, and Meta — not to SMB Team.", S["price_detail"]),
     Paragraph("", S["price_detail"])],
]
pt = Table(price_data, colWidths=[4.5 * inch, 1.7 * inch])
pt.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 4),
    ("RIGHTPADDING", (0,0), (-1,-1), 4),
    ("TOPPADDING", (0,0), (-1,-1), 2),
    ("BOTTOMPADDING", (0,0), (-1,-1), 1),
    ("LINEBELOW", (0,1), (-1,1), 0.5, RULE_GRAY),
    ("LINEBELOW", (0,3), (-1,3), 0.5, RULE_GRAY),
    ("LINEBELOW", (0,5), (-1,5), 0.5, RULE_GRAY),
]))
story.append(pt)
story.append(Paragraph(
    "Total: $6,447/mo + $3,000–$6,000 ad spend  |  Save $1,747/mo by bundling  |  18.9%–24.9% of $600K goal (under 35% cap)",
    S["savings"]))

# ── Build ──
doc.build(story, onFirstPage=add_page_elements, onLaterPages=add_page_elements)
print(f"PDF created: {OUTPUT_PATH}")

from pypdf import PdfReader
r = PdfReader(OUTPUT_PATH)
page_count = len(r.pages)
print(f"Page count: {page_count}")
if page_count != 2:
    print("WARNING: Sales Companion must be exactly 2 pages. Shorten bullet text to fit.")
