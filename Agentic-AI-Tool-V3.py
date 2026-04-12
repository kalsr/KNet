

# ==========================================================
# KALSNET (KNet) – COMPLETE AGENTIC AI PLATFORM (FINAL FIXED)
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

st.markdown("### 🚀 Autonomous Agentic AI + Analytics + Reporting Engine")

# ----------------------------------------------------------
# SIDEBAR - API KEY INPUT
# ----------------------------------------------------------
st.sidebar.title("🔑 GROQ Configuration")

api_key = st.sidebar.text_input("Enter GROQ API Key:", type="password")

def clean_key(key):
    return key.strip().replace("\n", "").replace("\r", "").replace('"', '').replace("'", "")

if not api_key:
    st.warning("⚠️ Please enter your GROQ API key to continue.")
    st.stop()

api_key = clean_key(api_key)

# ----------------------------------------------------------
# INIT CLIENT
# ----------------------------------------------------------
try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error("❌ Failed to initialize GROQ client")
    st.write(str(e))
    st.stop()

# ----------------------------------------------------------
# SAFE AI EXECUTION ENGINE (MULTI-MODEL FALLBACK)
# ----------------------------------------------------------
def run_agentic_ai(task):
    models = [
        "llama3-8b-8192",
        "mixtral-8x7b-32768"
    ]

    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a high-level Agentic AI system that performs structured reasoning and analysis."
                    },
                    {
                        "role": "user",
                        "content": task
                    }
                ],
                temperature=0.7,
                max_tokens=1024
            )

            return response.choices[0].message.content, model

        except Exception:
            continue

    return None, None

# ----------------------------------------------------------
# AGENTIC TASK INPUT
# ----------------------------------------------------------
st.subheader("🤖 Agentic AI Task Input")

task = st.text_area(
    "Enter your task (e.g., Cyber analysis, business report, threat detection):"
)

run = st.button("🚀 Run Agentic AI")

# ----------------------------------------------------------
# MAIN EXECUTION
# ----------------------------------------------------------
if run:

    # VALIDATION
    if not task or task.strip() == "":
        st.warning("⚠️ Task cannot be empty.")
        st.stop()

    result, model_used = run_agentic_ai(task.strip())

    if not result:
        st.error("❌ AI execution failed on all models.")
        st.stop()

    st.success(f"✅ AI Completed using model: {model_used}")
    st.write(result)

    # ------------------------------------------------------
    # ANALYTICS ENGINE (SIMULATED INTELLIGENCE DATA)
    # ------------------------------------------------------
    data = {
        "Category": ["Low Risk", "Medium Risk", "High Risk", "Critical"],
        "Count": [15, 30, 18, 7]
    }

    df = pd.DataFrame(data)

    st.subheader("📊 Agentic AI Analytics Dashboard")
    st.dataframe(df)

    # ------------------------------------------------------
    # BAR CHART
    # ------------------------------------------------------
    fig1, ax1 = plt.subplots()
    ax1.bar(df["Category"], df["Count"])
    ax1.set_title("Risk Distribution - Bar Chart")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

    # ------------------------------------------------------
    # PIE CHART
    # ------------------------------------------------------
    fig2, ax2 = plt.subplots()
    ax2.pie(df["Count"], labels=df["Category"], autopct="%1.1f%%")
    ax2.set_title("Risk Distribution - Pie Chart")
    st.pyplot(fig2)

    # ------------------------------------------------------
    # EXPORT CSV
    # ------------------------------------------------------
    st.download_button(
        "⬇️ Download CSV",
        df.to_csv(index=False),
        "knet_results.csv",
        "text/csv"
    )

    # ------------------------------------------------------
    # EXPORT JSON
    # ------------------------------------------------------
    st.download_button(
        "⬇️ Download JSON",
        json.dumps(data, indent=2),
        "knet_results.json",
        "application/json"
    )

    # ------------------------------------------------------
    # EXPORT PDF REPORT
    # ------------------------------------------------------
    def generate_pdf(text):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()

        content = [
            Paragraph("Kalsnet (KNet) Agentic AI Report", styles["Title"]),
            Spacer(1, 12),
            Paragraph(text.replace("\n", "<br/>"), styles["BodyText"])
        ]

        doc.build(content)
        buffer.seek(0)
        return buffer

    st.download_button(
        "⬇️ Download PDF Report",
        generate_pdf(result),
        "knet_report.pdf",
        "application/pdf"
    )

# ----------------------------------------------------------
# SYSTEM EXPLANATION
# ----------------------------------------------------------
st.markdown("---")
st.subheader("📖 How This Agentic AI System Works")

st.markdown("""
This **Kalsnet (KNet) Agentic AI Platform** integrates GROQ LLaMA/Mixtral models to perform intelligent task execution.

### 🔹 Workflow:
1. User submits a task (analysis, report, cyber scenario, etc.)
2. System validates input and cleans API key
3. GROQ AI executes reasoning using fallback models
4. Output is generated as structured intelligence
5. System creates synthetic risk analytics dataset
6. Data is visualized using:
   - 📊 Bar Chart (categorical comparison)
   - 🥧 Pie Chart (percentage distribution)
7. Results are exported in:
   - CSV (structured data)
   - JSON (machine-readable format)
   - PDF (executive report)

### 🔹 Use Cases:
- Cybersecurity threat analysis
- SOC dashboards
- Business intelligence reports
- AI-driven decision support systems
- Simulation-based analytics

This design simulates **enterprise-level Agentic AI workflows used in defense, cybersecurity, and analytics platforms.**
""")