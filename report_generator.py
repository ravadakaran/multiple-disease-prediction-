"""
Clinical PDF Report Generator for Multiple Disease Prediction System.
Uses fpdf2 to produce structured, styled patient diagnostic screening reports.
"""

from datetime import datetime
from fpdf import FPDF


class ClinicalReportPDF(FPDF):
    def header(self):
        # Header banner
        self.set_fill_color(30, 41, 59)  # Slate dark
        self.rect(0, 0, 210, 25, "F")
        self.set_xy(10, 6)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(255, 255, 255)
        self.cell(0, 7, "MULTIPLE DISEASE PREDICTION SYSTEM", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 9)
        self.set_text_color(203, 213, 225)
        self.cell(0, 5, "Automated Diagnostic Risk Screening Report", new_x="LMARGIN", new_y="NEXT")
        self.ln(8)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, f"Page {self.page_no()} | Confidential Medical Screening Report | Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}", align="C")


def generate_pdf_report(
    disease_name: str,
    prediction_text: str,
    is_positive: bool,
    risk_score: float,
    metrics_dict: dict,
    recommendations: list[str],
    patient_name: str = "Anonymous Patient",
    patient_id: str = "MS-2026-001",
) -> bytes:
    """
    Generates a PDF document in bytes.
    """
    pdf = ClinicalReportPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # 1. Patient & Metadata Block
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(95, 5, f"Patient Name: {patient_name}", new_x="RIGHT", new_y="TOP")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(71, 85, 105)
    pdf.cell(95, 5, f"Patient ID: {patient_id}", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(95, 5, f"Screening Module: {disease_name}", new_x="RIGHT", new_y="TOP")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(71, 85, 105)
    pdf.cell(95, 5, f"Generated: {datetime.now().strftime('%B %d, %Y - %H:%M')}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    # 2. Executive Diagnostic Summary Card
    if is_positive:
        bg_r, bg_g, bg_b = 254, 242, 242  # Red tint
        border_r, border_g, border_b = 239, 68, 68
        text_r, text_g, text_b = 153, 27, 27
        badge = "ELEVATED RISK / POSITIVE"
    else:
        bg_r, bg_g, bg_b = 240, 253, 244  # Green tint
        border_r, border_g, border_b = 34, 197, 94
        text_r, text_g, text_b = 22, 101, 52
        badge = "LOW RISK / NEGATIVE"

    pdf.set_fill_color(bg_r, bg_g, bg_b)
    pdf.set_draw_color(border_r, border_g, border_b)
    pdf.set_line_width(0.4)
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.rect(x, y, 190, 24, "FD")

    pdf.set_xy(x + 4, y + 3)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(text_r, text_g, text_b)
    pdf.cell(0, 6, f"Diagnostic Assessment: {badge}", new_x="LMARGIN", new_y="NEXT")

    pdf.set_x(x + 4)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(100, 5, f"Finding: {prediction_text}", new_x="RIGHT", new_y="TOP")
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(82, 5, f"Estimated Risk Index: {risk_score:.1f}%", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(y + 27)

    # 3. Clinical Biomarkers Table
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 7, "Recorded Clinical Parameters & Biomarkers", new_x="LMARGIN", new_y="NEXT")

    # Table Header
    pdf.set_fill_color(241, 245, 249)
    pdf.set_draw_color(203, 213, 225)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(71, 85, 105)
    pdf.cell(95, 7, " Biomarker / Variable Name", border=1, fill=True)
    pdf.cell(95, 7, " Value Recorded", border=1, fill=True, align="C", new_x="LMARGIN", new_y="NEXT")

    # Table Rows
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(15, 23, 42)
    fill_toggle = False
    for k, v in metrics_dict.items():
        row_bg = (248, 250, 252) if fill_toggle else (255, 255, 255)
        pdf.set_fill_color(*row_bg)
        pdf.cell(95, 6, f" {k}", border=1, fill=True)
        val_str = f"{v:.4f}" if isinstance(v, float) else str(v)
        pdf.cell(95, 6, f" {val_str}", border=1, fill=True, align="C", new_x="LMARGIN", new_y="NEXT")
        fill_toggle = not fill_toggle

    pdf.ln(4)

    # 4. Clinical Recommendations
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 6, "Suggested Medical Actions & Follow-up", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(51, 65, 85)
    for rec in recommendations:
        pdf.cell(5, 5, chr(149), new_x="RIGHT", new_y="TOP")
        pdf.multi_cell(185, 5, rec)

    pdf.ln(3)

    # 5. Formal Disclaimer Block
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(100, 116, 139)
    disclaimer_text = (
        "Notice: This predictive report is generated via machine learning statistical classification models for preliminary "
        "risk screening and educational analysis. It does NOT constitute a confirmed medical diagnosis. Patients should consult "
        "a licensed healthcare practitioner, physician, or specialist for comprehensive laboratory testing and medical guidance."
    )
    pdf.multi_cell(190, 4, disclaimer_text)

    return bytes(pdf.output())

