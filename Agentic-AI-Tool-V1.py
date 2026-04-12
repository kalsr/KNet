

# ==========================================================
# KALSNET (KNet) – AGENTIC AI PLATFORM WITH GROQ
# ==========================================================

import streamlit as st
from groq import Groq
import pandas as pd
import json
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt
import io

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------
st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# ----------------------------------------------------------
# HEADER (KALSNET BRANDING)
# ----------------------------------------------------------
st.markdown(
    "<h1 style='color:blue;'>Kalsnet (KNet) – Agentic AI Platform</h1>",
    unsafe_allow_html=True
)

st.markdown("### 🚀 Autonomous AI Task Execution & Analytics Dashboard")

# ----------------------------------------------------------
# SIDEBAR – GROQ KEY INPUT
# ----------------------------------------------------------
st.sidebar.title("🔑 GROQ API Configuration")

api_key = st.sidebar.text_input("Enter GROQ API Key:", type="password")

if not api_key:
    st.warning("Please enter your GROQ API key in the sidebar.")
    st.stop()

client = Groq(api_key=api_key)

# ----------------------------------------------------------
# AGENTIC TASK INPUT
# ----------------------------------------------------------
st.subheader("🤖 Agentic AI Task")

task = st.text_area("Enter your AI task (e.g., Cyber Threat Analysis, Data Insights):")

run = st.button("Run Agentic AI")

# ----------------------------------------------------------
# RUN AI
# ----------------------------------------------------------
if run and task:

    with st.spinner("⚡ Running Agentic AI..."):

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are an advanced Agentic AI system."},
                {"role": "user", "content": task}
            ]
        )

        result = response.choices[0].message.content

    st.success("✅ AI Execution Complete")
    st.write(result)

    # ------------------------------------------------------
    # CREATE SYNTHETIC ANALYTICS DATA
    # ------------------------------------------------------
    data = {
        "Category": ["Low Risk", "Medium Risk", "High Risk", "Critical"],
        "Count": [10, 25, 15, 5]
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
    # EXPORT: CSV
    # ------------------------------------------------------
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download CSV", csv, "results.csv", "text/csv")

    # ------------------------------------------------------
    # EXPORT: JSON
    # ------------------------------------------------------
    json_data = json.dumps(data, indent=2)
    st.download_button("⬇️ Download JSON", json_data, "results.json", "application/json")

    # ------------------------------------------------------
    # EXPORT: PDF
    # ------------------------------------------------------
    def create_pdf():
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()

        content = []
        content.append(Paragraph("Kalsnet Agentic AI Report", styles["Title"]))
        content.append(Spacer(1, 12))
        content.append(Paragraph(result, styles["BodyText"]))

        doc.build(content)
        buffer.seek(0)
        return buffer

    pdf = create_pdf()
    st.download_button("⬇️ Download PDF", pdf, "report.pdf", "application/pdf")

# ----------------------------------------------------------
# EXPLANATION SECTION
# ----------------------------------------------------------
st.markdown("---")
st.subheader("📖 How Charts & Graphs Are Generated")

st.markdown("""
The analytics dashboard uses **synthetic structured data** generated within the application to simulate real-world AI output categorization. 
A **Pandas DataFrame** is created with predefined risk categories and associated counts, representing the distribution of analyzed events.

The **bar chart** is generated using Matplotlib by mapping each category to its numerical count, allowing clear comparison of risk levels across categories. 
The **pie chart** visualizes the same dataset as proportional segments, showing percentage contribution of each category to the total dataset.

Both charts are rendered dynamically using `matplotlib.pyplot`, where:
- The bar chart uses categorical axes and frequency values
- The pie chart calculates percentage distribution automatically

These visualizations simulate how real Agentic AI systems present insights such as:
- Threat distribution
- Risk scoring breakdown
- Operational intelligence summaries

This approach can be extended to real datasets such as:
- Cybersecurity logs
- Financial transactions
- TPFDD deployment data
- SOC alert metrics

The export functions convert this structured data into **CSV (tabular format)**, **JSON (API-ready format)**, and **PDF (executive report format)** for operational and decision-making use.
""")
