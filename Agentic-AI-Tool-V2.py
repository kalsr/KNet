

# ==========================================================
# KALSNET (KNet) – AGENTIC AI PLATFORM (FIXED & STABLE)
# ==========================================================

import streamlit as st
from groq import Groq
import pandas as pd
import json
import matplotlib.pyplot as plt
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------
st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------
st.markdown(
    "<h1 style='color:blue;'>Kalsnet (KNet) – Agentic AI Platform</h1>",
    unsafe_allow_html=True
)

st.markdown("### 🚀 Autonomous AI Task Execution & Analytics Dashboard")

# ----------------------------------------------------------
# SIDEBAR - API KEY INPUT
# ----------------------------------------------------------
st.sidebar.title("🔑 GROQ API Configuration")

api_key = st.sidebar.text_input("Enter GROQ API Key:", type="password")

# ----------------------------------------------------------
# CLEAN KEY FUNCTION
# ----------------------------------------------------------
def clean_key(key):
    return key.strip().replace("\n", "").replace("\r", "").replace('"', "").replace("'", "")

if not api_key:
    st.warning("Please enter your GROQ API key.")
    st.stop()

api_key = clean_key(api_key)

# ----------------------------------------------------------
# INIT GROQ CLIENT
# ----------------------------------------------------------
try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error(f"❌ Failed to initialize GROQ client: {str(e)}")
    st.stop()

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
st.subheader("🤖 Agentic AI Task")

task = st.text_area("Enter your AI task (e.g., Cyber analysis, report generation):")

run = st.button("Run Agentic AI")

# ----------------------------------------------------------
# MAIN EXECUTION
# ----------------------------------------------------------
if run and task:

    try:
        with st.spinner("⚡ Running Agentic AI..."):

            response = client.chat.completions.create(
                model="llama3-8b-8192",   # ✅ FIXED MODEL
                messages=[
                    {"role": "system", "content": "You are an advanced Agentic AI system for analysis and reporting."},
                    {"role": "user", "content": task}
                ],
                temperature=0.7
            )

            result = response.choices[0].message.content

        st.success("✅ AI Execution Complete")
        st.write(result)

    except Exception as e:
        st.error("❌ GROQ REQUEST FAILED")
        st.write(str(e))
        st.stop()

    # ------------------------------------------------------
    # SYNTHETIC ANALYTICS DATA
    # ------------------------------------------------------
    data = {
        "Category": ["Low Risk", "Medium Risk", "High Risk", "Critical"],
        "Count": [12, 28, 14, 6]
    }

    df = pd.DataFrame(data)

    st.subheader("📊 Analytics Dashboard")
    st.dataframe(df)

    # ------------------------------------------------------
    # BAR CHART
    # ------------------------------------------------------
    fig1, ax1 = plt.subplots()
    ax1.bar(df["Category"], df["Count"])
    ax1.set_title("Risk Distribution (Bar Chart)")
    st.pyplot(fig1)

    # ------------------------------------------------------
    # PIE CHART
    # ------------------------------------------------------
    fig2, ax2 = plt.subplots()
    ax2.pie(df["Count"], labels=df["Category"], autopct="%1.1f%%")
    ax2.set_title("Risk Distribution (Pie Chart)")
    st.pyplot(fig2)

    # ------------------------------------------------------
    # EXPORT CSV
    # ------------------------------------------------------
    st.download_button(
        "⬇️ Download CSV",
        df.to_csv(index=False),
        "results.csv",
        "text/csv"
    )

    # ------------------------------------------------------
    # EXPORT JSON
    # ------------------------------------------------------
    st.download_button(
        "⬇️ Download JSON",
        json.dumps(data, indent=2),
        "results.json",
        "application/json"
    )

    # ------------------------------------------------------
    # EXPORT PDF
    # ------------------------------------------------------
    def create_pdf(text):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()

        content = [
            Paragraph("Kalsnet Agentic AI Report", styles["Title"]),
            Spacer(1, 12),
            Paragraph(text.replace("\n", "<br/>"), styles["BodyText"])
        ]

        doc.build(content)
        buffer.seek(0)
        return buffer

    st.download_button(
        "⬇️ Download PDF Report",
        create_pdf(result),
        "report.pdf",
        "application/pdf"
    )

# ----------------------------------------------------------
# EXPLANATION SECTION
# ----------------------------------------------------------
st.markdown("---")
st.subheader("📖 How This System Works")

st.markdown("""
This platform uses **GROQ LLaMA 3 (8B model)** to execute user-defined agentic tasks.

The workflow is:
1. User submits a task (e.g., cyber analysis, reporting)
2. GROQ AI processes the request using LLM inference
3. Output is structured into:
   - Text response (AI reasoning)
   - Structured dataset (risk simulation)
4. Data is visualized using:
   - Matplotlib Bar Chart (category comparison)
   - Pie Chart (percentage distribution)
5. Outputs are exported in:
   - CSV (data analysis)
   - JSON (API integration)
   - PDF (executive report)

This simulates an **Agentic AI pipeline used in cybersecurity, SOC analytics, and decision intelligence systems**.
""")