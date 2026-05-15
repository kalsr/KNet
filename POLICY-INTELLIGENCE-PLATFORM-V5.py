# =========================================================
# AI Governance & Public Policy Intelligence Platform
# FIXED EXPORT MODULE (PDF + WORD + CSV + JSON WORKING)
# =========================================================

import streamlit as st
from groq import Groq
import json
import pandas as pd
from io import BytesIO
from datetime import datetime

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from docx import Document

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(page_title="AI Governance Platform", layout="wide")

# =========================================================
# SIMPLE SESSION STATE INIT (SAFETY)
# =========================================================

if "result" not in st.session_state:
    st.session_state["result"] = None

# =========================================================
# EXPORT FIX ENGINE (REWRITTEN - FULLY STABLE)
# =========================================================

def export_pdf(text: str):
    """Reliable PDF export using ReportLab"""

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("AI Governance & Policy Report", styles["Title"]))
    content.append(Spacer(1, 12))

    # clean formatting for PDF
    safe_text = text.replace("\n", "<br/>")
    content.append(Paragraph(safe_text, styles["BodyText"]))

    doc.build(content)

    buffer.seek(0)
    return buffer.getvalue()


def export_word(text: str):
    """Reliable Word export (.docx)"""

    doc = Document()
    doc.add_heading("AI Governance & Policy Report", 0)
    doc.add_paragraph(text)

    buffer = BytesIO()
    doc.save(buffer)

    buffer.seek(0)
    return buffer.getvalue()


def export_csv(text: str):
    """CSV export for analytics ingestion"""

    df = pd.DataFrame({
        "report": [text],
        "timestamp": [str(datetime.now())]
    })

    csv_buffer = BytesIO()
    csv_buffer.write(df.to_csv(index=False).encode("utf-8"))
    csv_buffer.seek(0)

    return csv_buffer.getvalue()


def export_json(text: str):
    """JSON export for API / automation"""

    payload = {
        "report": text,
        "timestamp": str(datetime.now()),
        "source": "AI Governance Platform"
    }

    json_buffer = BytesIO()
    json_buffer.write(json.dumps(payload, indent=2).encode("utf-8"))
    json_buffer.seek(0)

    return json_buffer.getvalue()

# =========================================================
# UI SECTION (REPORTS WITH FIXED DOWNLOADS)
# =========================================================

st.title("AI Governance Platform - Export Module Fix")

st.subheader("Reports")

if st.session_state["result"]:

    report = st.session_state["result"]

    st.text_area("Generated Report", report, height=300)

    st.markdown("### Export Options (FIXED)")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.download_button(
            "⬇ PDF Report",
            data=export_pdf(report),
            file_name="AI_Governance_Report.pdf",
            mime="application/pdf"
        )

    with col2:
        st.download_button(
            "⬇ Word Report",
            data=export_word(report),
            file_name="AI_Governance_Report.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    with col3:
        st.download_button(
            "⬇ CSV Data",
            data=export_csv(report),
            file_name="AI_Governance_Report.csv",
            mime="text/csv"
        )

    with col4:
        st.download_button(
            "⬇ JSON API",
            data=export_json(report),
            file_name="AI_Governance_Report.json",
            mime="application/json"
        )

else:
    st.info("No report generated yet. Run Policy Generator first.")