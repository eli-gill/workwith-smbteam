"""
Sales Companion PDF Template — SMB Team
========================================
This template generates the 2-page internal Sales Companion PDF for the sales rep.
It uses reportlab. Do not modify the layout, colors, fonts, styles, or structure.
Only replace the # FILL: placeholders with audit-specific content.

IMPORTANT: The final PDF must be exactly 2 pages. If content overflows to a third
page, shorten bullet text — do not remove sections.

All bullet text must be scannable: one idea per bullet, 8th-grade reading level.
Each "What it does for her/him:" bullet states the transformation, not the deliverable.
Each scoping rationale bullet states one fact with one conclusion.

Output filename: [FirmName]_[Date]_Sales_Companion.pdf
  - FirmName: spaces replaced with underscores
  - Date: MMDDYYYY format
  - Save to the root of the project folder (same location as the Growth Audit HTML)
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Fonts — SMB Team brand font is Poppins. Embedded so it renders the
# same regardless of what's installed on the machine opening the PDF. ──
_FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")
pdfmetrics.registerFont(TTFont("Poppins", os.path.join(_FONT_DIR, "Poppins-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Poppins-Bold", os.path.join(_FONT_DIR, "Poppins-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Poppins-Italic", os.path.join(_FONT_DIR, "Poppins-Italic.ttf")))
pdfmetrics.registerFontFamily(
    "Poppins", normal="Poppins", bold="Poppins-Bold",
    italic="Poppins-Italic", boldItalic="Poppins-Bold",
)

# ── Colors — SMB Team brand colors (Deep Wood Blue, Ocean Blue) plus the
# existing semantic grays/reds/savings-green, which stay as they were. ──
DARK_NAVY = HexColor("#003A59")     # Deep Wood Blue — brand primary
SECTION_BLUE = HexColor("#0091C9")  # Ocean Blue — brand accent, section headers
ACCENT_GREEN = HexColor("#3B6D11")  # savings/positive-outcome green — matches the audit report
MEDIUM_GRAY = HexColor("#555555")
LIGHT_GRAY = HexColor("#888888")
RULE_GRAY = HexColor("#CCCCCC")
QUOTE_BG = HexColor("#F5F7F0")
WHITE = HexColor("#FFFFFF")
RED_WARNING = HexColor("#CC0000")
RED_ACCENT = HexColor("#C0392B")

OUTPUT_PATH = "legacy-wealth-legal/Legacy_Wealth_Legal_September_10_2026_Sales_Companion.pdf"


def add_page_elements(canvas, doc):
    """Draws red warning header and confidential footer on every page. DO NOT MODIFY."""
    canvas.saveState()
    width, height = letter
    canvas.setFont("Poppins-Bold", 10)
    canvas.setFillColor(RED_WARNING)
    canvas.drawCentredString(width / 2, height - 0.38 * inch,
                             "FOR INTERNAL USE ONLY; DO NOT SHARE.")
    canvas.setStrokeColor(RED_WARNING)
    canvas.setLineWidth(0.5)
    canvas.line(0.6 * inch, height - 0.44 * inch,
                width - 0.6 * inch, height - 0.44 * inch)
    canvas.setFont("Poppins", 7)
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
    "title", fontName="Poppins-Bold", fontSize=16, leading=20,
    textColor=DARK_NAVY, spaceAfter=1)
S["subtitle"] = ParagraphStyle(
    "subtitle", fontName="Poppins", fontSize=9.5, leading=13,
    textColor=LIGHT_GRAY, spaceAfter=3)
S["section"] = ParagraphStyle(
    "section", fontName="Poppins-Bold", fontSize=11, leading=15,
    textColor=SECTION_BLUE, spaceBefore=6, spaceAfter=2)
S["subsection"] = ParagraphStyle(
    "subsection", fontName="Poppins-Bold", fontSize=10, leading=13,
    textColor=DARK_NAVY, spaceBefore=2, spaceAfter=1)
S["bullet"] = ParagraphStyle(
    "bullet", fontName="Poppins", fontSize=9.5, leading=13,
    textColor=MEDIUM_GRAY, leftIndent=12, bulletIndent=0,
    spaceBefore=1, spaceAfter=1)
S["bullet_dark"] = ParagraphStyle(
    "bullet_dark", fontName="Poppins", fontSize=9.5, leading=13,
    textColor=DARK_NAVY, leftIndent=12, bulletIndent=0,
    spaceBefore=1, spaceAfter=1)
S["quote"] = ParagraphStyle(
    "quote", fontName="Poppins-Italic", fontSize=9.5, leading=13,
    textColor=DARK_NAVY, leftIndent=6, rightIndent=6,
    spaceBefore=1, spaceAfter=1)
S["snap_label"] = ParagraphStyle(
    "snap_label", fontName="Poppins-Bold", fontSize=8.5, leading=11,
    textColor=LIGHT_GRAY)
S["snap_value"] = ParagraphStyle(
    "snap_value", fontName="Poppins", fontSize=9.5, leading=12,
    textColor=DARK_NAVY)
S["objection_q"] = ParagraphStyle(
    "objection_q", fontName="Poppins-Bold", fontSize=9.5, leading=13,
    textColor=RED_ACCENT, spaceBefore=2, spaceAfter=0)
S["objection_a"] = ParagraphStyle(
    "objection_a", fontName="Poppins", fontSize=9.5, leading=13,
    textColor=MEDIUM_GRAY, leftIndent=8, spaceAfter=2)
S["price_main"] = ParagraphStyle(
    "price_main", fontName="Poppins-Bold", fontSize=9.5, leading=13,
    textColor=DARK_NAVY)
S["price_detail"] = ParagraphStyle(
    "price_detail", fontName="Poppins", fontSize=8.5, leading=12,
    textColor=MEDIUM_GRAY)
S["savings"] = ParagraphStyle(
    "savings", fontName="Poppins-Bold", fontSize=9.5, leading=13,
    textColor=ACCENT_GREEN, alignment=TA_CENTER, spaceBefore=3)
S["disclaimer"] = ParagraphStyle(
    "disclaimer", fontName="Poppins-Italic", fontSize=8.5, leading=11,
    textColor=LIGHT_GRAY, spaceBefore=1, spaceAfter=1)


# ── Helpers — DO NOT MODIFY ──
def b(text):
    """Gray bullet for scoping rationale, obstacles, and technical details."""
    return Paragraph(f"<bullet>&bull;</bullet> {text}", S["bullet"])

def bd(text):
    """Dark bullet for transformation statements and what she/he wants."""
    return Paragraph(f"<bullet>&bull;</bullet> {text}", S["bullet_dark"])

def thin_rule():
    return HRFlowable(width="100%", thickness=0.5, color=RULE_GRAY,
                       spaceBefore=3, spaceAfter=3)

def quote_block(text):
    """Quote block with subtle background for prospect's own words."""
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

story.append(Paragraph("Legacy Wealth Legal", S["title"]))
story.append(Paragraph("Sales Companion  |  September 10, 2026  |  Rep: Jacob Meissner", S["subtitle"]))
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
    [Paragraph("Martin Birenbaum", S["snap_value"]),
     Paragraph("Not stated (goal: $500K–$1M)", S["snap_value"]),
     Paragraph("Solo (0 staff)", S["snap_value"]),
     Paragraph("3 — Solo Practitioner", S["snap_value"]),
     Paragraph("15% (default)", S["snap_value"]),
     Paragraph("Palmetto Bay, FL", S["snap_value"])],
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
story.append(Paragraph("Martin wants a firm that runs itself so he can stop being the \"Chief Everything Officer\" and get his time back.", S["subsection"]))

story.append(quote_block("Chief Everything Officer"))
story.append(Spacer(1, 1))
story.append(quote_block("$1k/mo AI vs. $50k/yr salary"))
story.append(Spacer(1, 2))

story.append(Paragraph("<b>What he wants:</b>", S["subsection"]))
story.append(bd("<b>A firm that runs itself.</b> AI handles busywork so he can step back."))
story.append(bd("<b>To avoid becoming a boss.</b> Resistant to hiring; compares AI cost to salary cost."))
story.append(bd("<b>A real estate planning brand.</b> Separate from his old business-law identity."))

story.append(Spacer(1, 2))

story.append(Paragraph("<b>What is stopping him:</b>", S["subsection"]))
story.append(b("<b>Zero public presence.</b> No GBP, no reviews, no website content."))
story.append(b("<b>No process behind the workload.</b> ~100 daily emails, handled ad hoc."))
story.append(b("<b>No revenue baseline.</b> Only a goal is stated, not a current figure."))
story.append(b("<b>Disqualified from AI today.</b> LAW requires 1-2 staff; he has zero."))

story.append(thin_rule())

# ── Why Not AI or Marketing Yet ──
story.append(Paragraph("Why Not AI or Marketing Yet", S["section"]))

story.append(Paragraph("<b>What it does for him:</b>", S["subsection"]))
story.append(bd("Confirms AI Workforce Pro is the right eventual fit — just not usable yet."))
story.append(bd("Keeps this proposal honest, instead of pitching marketing he didn't ask for."))
story.append(bd("Sets the milestones that unlock AI and marketing on the scheduled follow-up call."))

story.append(Paragraph("<b>AI Workforce Pro — not eligible today  |  Phase 2, once staffed</b>", S["subsection"]))
story.append(b("LAW rule: solo firms with zero support staff aren't eligible, regardless of call topic."))
story.append(b("Revenue not confirmed at the $500K floor LAW requires — only a goal was stated."))
story.append(b("Transcript says \"$350/mo\"; approved price is $1,597/mo bundled — reconcile with Martin."))
story.append(b("No marketing included either — not requested this call; deferred to Phase 3."))

story.append(thin_rule())

# ── Why This Coaching Package ──
story.append(Paragraph("Why This Coaching Package", S["section"]))

story.append(Paragraph("<b>What it does for him:</b>", S["subsection"]))
story.append(bd("Builds the revenue and case-value baseline he needs to track $500k-$1M."))
story.append(bd("Creates a real staffing plan so his first hire is a choice, not a scramble."))
story.append(bd("Gets him to the milestones that unlock the AI and marketing plan already on the calendar."))

story.append(Paragraph("<b>Elite Coach  |  $2,600/mo bundled</b>", S["subsection"]))
story.append(b("Revenue not confirmed — selected over Elite Coach Plus as the conservative fit."))
story.append(b("Clears the $2,497/mo minimum MRR floor."))
story.append(b("No marketing bundled — none was requested and none is being forced."))
story.append(b("Stand-alone $3,497/mo vs. $2,600/mo bundled — saves $897/mo."))


# ══════════════════════════════════════════════════════════
# PAGE 2
# ══════════════════════════════════════════════════════════
story.append(PageBreak())

story.append(Paragraph("Legacy Wealth Legal — Sales Companion (continued)", S["title"]))
story.append(thin_rule())

# ── Why No Ad Spend Yet ──
story.append(Paragraph("Why No Ad Spend Yet", S["section"]))

story.append(Paragraph("<b>What it does for him:</b>", S["subsection"]))
story.append(bd("Keeps this proposal free of a marketing spend he never asked for."))
story.append(bd("Previews what Phase 3 looks like once a revenue baseline is confirmed."))

story.append(Paragraph("<b>Phase 3 Preview (not part of this proposal):</b>", S["subsection"]))
story.append(b("<b>Conservative:</b> $10,200/mo — sum of estate planning channel minimums."))
story.append(b("<b>Aggressive:</b> $16,500/mo — 20% rule vs. the $500k-$1M goal, Miami Tier 2."))

story.append(Paragraph("<b>Estimated ROI (Phase 3 preview):</b>", S["subsection"]))
story.append(b("<b>Conservative:</b> 17 cases x $2,250 = $38,250/mo vs. $10.2K spend = 3.7x."))
story.append(b("<b>Aggressive:</b> 27 cases x $2,250 = $60,750/mo vs. $16.5K spend = 3.7x."))
story.append(Paragraph("<i>Estimates only. Not billed as part of this proposal.</i>", S["disclaimer"]))

story.append(Paragraph("<b>How the range was calculated:</b>", S["subsection"]))
story.append(b("Conservative: PPC $3,500 + LSA $2,000 + Meta retargeting $1,200 + lead gen $3,500."))
story.append(b("Aggressive: $750K midpoint x 20% ÷ 12 x Miami Tier 2 (1.3x) ≈ $16,500."))

story.append(thin_rule())

# ── If He Pushes Back ──
story.append(Paragraph("If He Pushes Back", S["section"]))

story.append(Paragraph('"I thought this call was about the $350/mo AI tool."', S["objection_q"]))
story.append(Paragraph("That price doesn't match our table ($1,597/mo bundled) — and as a solo practice, he doesn't yet qualify. Elite Coach is the fastest path to becoming eligible.", S["objection_a"]))

story.append(Paragraph('"Why coaching and not the AI tool I asked about?"', S["objection_q"]))
story.append(Paragraph("AI Workforce Pro needs 1-2 staff to implement. Elite Coach builds the baseline and hiring plan that gets him there, then AI comes in Phase 2.", S["objection_a"]))

story.append(Paragraph('"I don\'t want to hire anyone."', S["objection_q"]))
story.append(Paragraph("Elite Coach doesn't force a hire — it helps him decide when one makes sense, using his own cost-vs-value lens.", S["objection_a"]))

story.append(Paragraph('"Why isn\'t marketing part of this?"', S["objection_q"]))
story.append(Paragraph("Marketing wasn't this call's subject — Martin scheduled a follow-up to cover AI, coaching, and marketing together.", S["objection_a"]))

story.append(thin_rule())

# ── Investment At A Glance ──
# FILL: All pricing from the scoping calculation
story.append(Paragraph("Investment At A Glance", S["section"]))

price_data = [
    [Paragraph("<b>Elite Coach</b>", S["price_main"]),
     Paragraph("$2,600/mo", S["price_main"])],
    [Paragraph("Only package recommended this pass — builds the foundation for AI and marketing.", S["price_detail"]),
     Paragraph("<strike>$3,497</strike> stand alone", S["price_detail"])],
    [Paragraph("<b>AI Workforce Pro (Phase 2 preview)</b>", S["price_main"]),
     Paragraph("Not billed today", S["price_main"])],
    [Paragraph("Available once Martin adds his first support hire.", S["price_detail"]),
     Paragraph("", S["price_detail"])],
    [Paragraph("<b>Marketing (Phase 3 preview)</b>", S["price_main"]),
     Paragraph("$10,200–$16,500/mo", S["price_main"])],
    [Paragraph("Goes to Google, LSA, and Meta — not part of this proposal.", S["price_detail"]),
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
    "Total today: $2,600/mo  |  Save $897/mo vs. stand-alone  |  No ad spend or AI fee billed this pass",
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
