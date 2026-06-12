# Email Isolation System Framework


import streamlit as st
import pandas as pd
import json
import numpy as np
from datetime import datetime
import plotly.express as px

# Export libraries
from io import BytesIO
from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(page_title="KNet Email Isolation System", layout="wide")

# ==========================
# HEADER (Bold Blue Title)
# ==========================
st.markdown("""
<h1 style='text-align: center; color: #0B3D91; font-weight: bold;'>
KNet Email Isolation & Threat Control Platform
</h1>
<h4 style='text-align: center; color: #0B3D91;'>
Developed by Ramdy Singh – Kalsnet (KNet) Consulting Group
</h4>
<hr>
""", unsafe_allow_html=True)


# ==========================
# SAMPLE DATA GENERATOR
# ==========================
def generate_data(rows):
    categories = ["Phishing", "Spam", "Malware", "Business Email Compromise", "Safe"]
    data = {
        "Email_ID": [f"MSG-{i}" for i in range(rows)],
        "Category": np.random.choice(categories, rows),
        "Risk_Score": np.random.randint(0, 100, rows),
        "Confidence": np.random.randint(50, 100, rows),
        "Timestamp": pd.date_range("2025-01-01", periods=rows, freq="H")
    }
    return pd.DataFrame(data)


# ==========================
# EXPORT FUNCTIONS
# ==========================
def export_json(df):
    return df.to_json(orient="records", indent=2)

def export_word(df):
    doc = Document()
    doc.add_heading("KNet Email Isolation Report", 0)

    for i, row in df.head(20).iterrows():
        doc.add_paragraph(str(row.to_dict()))

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

def export_pdf(df):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("KNet Email Isolation Report", styles["Title"]))
    content.append(Spacer(1, 12))

    for i, row in df.head(15).iterrows():
        content.append(Paragraph(str(row.to_dict()), styles["BodyText"]))
        content.append(Spacer(1, 8))

    doc.build(content)
    buffer.seek(0)
    return buffer


# ==========================
# SIDEBAR CONTROLS
# ==========================
st.sidebar.header("Control Panel")

rows = st.sidebar.slider("Generate Sample Records", 10, 300, 50)

if st.sidebar.button("Generate Data"):
    st.session_state["df"] = generate_data(rows)

uploaded_file = st.sidebar.file_uploader("Upload CSV or JSON", type=["csv", "json"])


# ==========================
# LOAD DATA
# ==========================
df = None

if "df" in st.session_state:
    df = st.session_state["df"]

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_json(uploaded_file)


if df is None:
    st.info("Generate or upload data to begin analysis.")
    st.stop()


# ==========================
# MAIN DASHBOARD
# ==========================
tab1, tab2, tab3, tab4 = st.tabs(
    ["📊 Dashboard", "📁 Data View", "📈 Analytics", "📤 Export"]
)

# --------------------------
# TAB 1: DASHBOARD
# --------------------------
with tab1:
    st.subheader("Risk Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Emails", len(df))
    col2.metric("Avg Risk Score", round(df["Risk_Score"].mean(), 2))
    col3.metric("High Risk (>70)", len(df[df["Risk_Score"] > 70]))

    fig = px.pie(df, names="Category", title="Email Category Distribution")
    st.plotly_chart(fig, use_container_width=True)


# --------------------------
# TAB 2: DATA VIEW
# --------------------------
with tab2:
    st.subheader("Dataset Viewer")
    st.dataframe(df, use_container_width=True)


# --------------------------
# TAB 3: ANALYTICS
# --------------------------
with tab3:
    st.subheader("Risk Analytics")

    fig2 = px.histogram(df, x="Risk_Score", nbins=20, title="Risk Score Distribution")
    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.box(df, y="Risk_Score", color="Category", title="Risk by Category")
    st.plotly_chart(fig3, use_container_width=True)


# --------------------------
# TAB 4: EXPORT
# --------------------------
with tab4:
    st.subheader("Export Results")

    json_data = export_json(df)
    word_file = export_word(df)
    pdf_file = export_pdf(df)

    st.download_button(
        "Download JSON",
        data=json_data,
        file_name="knet_data.json",
        mime="application/json"
    )

    st.download_button(
        "Download Word Report",
        data=word_file,
        file_name="knet_report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

    st.download_button(
        "Download PDF Report",
        data=pdf_file,
        file_name="knet_report.pdf",
        mime="application/pdf"
    )


# ==========================
# FOOTER
# ==========================
st.markdown("""
<br><hr>
<div style='text-align:center; color:#0B3D91; font-weight:bold;'>
KNet Consulting Group © 2026 | AI & Cyber Defense Engineering Platform
</div>
""", unsafe_allow_html=True)