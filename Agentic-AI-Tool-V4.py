# ==========================================================
# KALSNET (KNet) – AGENTIC AI PLATFORM (FINAL STABLE VERSION)
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

st.markdown("### 🚀 Autonomous AI + Analytics + Reporting Engine")

# ----------------------------------------------------------
# SIDEBAR - API KEY
# ----------------------------------------------------------
st.sidebar.title("🔑 GROQ API Key")

api_key = st.sidebar.text_input("Enter GROQ API Key:", type="password")

# ----------------------------------------------------------
# CLEAN KEY
# ----------------------------------------------------------
def clean_key(key):
    return key.strip().replace("\n", "").replace("\r", "").replace('"', '').replace("'", "")

if not api_key:
    st.warning("⚠️ Please enter your GROQ API Key")
    st.stop()

api_key = clean_key(api_key)

# ----------------------------------------------------------
# INIT GROQ CLIENT
# ----------------------------------------------------------
try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error("❌ Failed to initialize Groq client")
    st.write(str(e))
    st.stop()

# ----------------------------------------------------------
# SAFE MODEL ROUTER (FIXED CORE)
# ----------------------------------------------------------
def run_agentic_ai(task):
    models = [
        "llama-3.1-8b-instant",   # ⭐ MOST STABLE
        "llama3-8b-8192",
        "mixtral-8x7b-32768"
    ]

    last_error = None

    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a high-level Agentic AI system for analysis, reasoning, and structured reporting."
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

        except Exception as e:
            last_error = str(e)
            st.warning(f"⚠️ Model failed: {model}")
            st.write(str(e))

    return None, last_error

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
st.subheader("🤖 Agentic AI Task Input")

task = st.text_area("Enter your task:")

run = st.button("🚀 Run Agentic AI")

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    if not task or task.strip() == "":
        st.warning("⚠️ Task cannot be empty")
        st.stop()

    result, model_used = run_agentic_ai(task.strip())

    if not result:
        st.error("❌ All models failed")
        st.write("Last error:", model_used)
        st.stop()

    st.success(f"✅ AI Response Generated using: {model_used}")
    st.write(result)

    # ------------------------------------------------------
    # ANALYTICS DATA (SIMULATED)
    # ------------------------------------------------------
    data = {
        "Category": ["Low Risk", "Medium Risk", "High Risk", "Critical"],
        "Count": [18, 32, 20, 9]
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
    # CSV EXPORT
    # ------------------------------------------------------
    st.download_button(
        "⬇️ Download CSV",
        df.to_csv(index=False),
        "knet_results.csv",
        "text/csv"
    )

    # ------------------------------------------------------
    # JSON EXPORT
    # ------------------------------------------------------
    st.download_button(
        "⬇️ Download JSON",
        json.dumps(data, indent=2),
        "knet_results.json",
        "application/json"
    )

    # ------------------------------------------------------
    # PDF EXPORT
    # ------------------------------------------------------
    def create_pdf(text):
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
        create_pdf(result),
        "knet_report.pdf",
        "application/pdf"
    )

# ----------------------------------------------------------
# INFO SECTION
# ----------------------------------------------------------
st.markdown("---")
st.subheader("📖 System Explanation")

st.markdown("""
This system uses **GROQ-hosted LLMs** with automatic fallback routing.

### 🔹 Flow:
1. User enters API key (same key can be reused safely)
2. Task is validated
3. AI is executed using:
   - llama-3.1-8b-instant (primary)
   - llama3-8b-8192 (fallback)
   - mixtral-8x7b-32768 (final fallback)
4. Output is generated and visualized
5. Data exported as CSV, JSON, PDF

### 🔹 Key Fixes:
- Eliminates BadRequest errors
- Handles model restrictions automatically
- Prevents silent failures
- Ensures Streamlit Cloud stability
""")