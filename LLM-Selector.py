# ==========================================================
# KALSNET (KNet) – ENTERPRISE AGENTIC AI PLATFORM (V2)
# Multi-LLM Orchestration | AI Decision Intelligence
# Developed by Randy Singh
# ==========================================================

import streamlit as st
import pandas as pd
import json
import datetime
import io
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt

st.set_page_config(page_title="KNet Enterprise AI Platform", layout="wide")

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
<h1 style='color:#0B3D91; text-align:center;'>KALSNET (KNet) – Enterprise Agentic AI Platform</h1>
<h4 style='text-align:center;'>Multi-LLM Orchestration | Decision Intelligence | Cyber/DoD Ready</h4>
<hr>
""", unsafe_allow_html=True)

# -------------------------------
# FREE LLMs
# -------------------------------
LLMS = [
    "ChatGPT", "Claude", "Gemini", "DeepSeek",
    "Perplexity", "Grok", "Copilot", "Mistral",
    "Qwen", "Kimi"
]

# -------------------------------
# MODE PROMPT ENGINEERING
# -------------------------------
def build_prompt(task, mode):
    base = f"Task: {task}\n"

    if mode == "Cyber Defense":
        return base + "Analyze as a cybersecurity expert. Provide threats, risks, mitigation."
    elif mode == "Threat Hunting":
        return base + "Identify anomalies, suspicious patterns, and indicators of compromise."
    elif mode == "Fraud Detection":
        return base + "Detect fraud patterns, anomalies, and risk score."
    elif mode == "DoD Mission":
        return base + "Provide mission planning, risk analysis, and operational strategy."
    else:
        return base + "Provide a clear and structured response."

# -------------------------------
# UI LAYOUT (TABS)
# -------------------------------
tab1, tab2, tab3 = st.tabs(["🧠 Task & LLM Selection", "⚡ Execution", "📊 Analytics"])

# ===============================
# TAB 1 – INPUT
# ===============================
with tab1:

    st.subheader("Enter Mission Task")

    user_input = st.text_area("Task", height=150)

    mode = st.selectbox("Select Mode", [
        "General AI", "Cyber Defense", "Threat Hunting",
        "Fraud Detection", "DoD Mission"
    ])

    selected_llms = st.multiselect(
        "Select LLMs (Multi-Execution)",
        LLMS,
        default=["ChatGPT"]
    )

# ===============================
# TAB 2 – EXECUTION
# ===============================
with tab2:

    response_data = []

    if st.button("⚡ Run Enterprise AI") and user_input:

        engineered_prompt = build_prompt(user_input, mode)

        st.info("Prompt sent to selected LLMs")

        for llm in selected_llms:

            # SIMULATED RESPONSE (replace with API later)
            result = f"{llm} Response to: {engineered_prompt}"

            score = random.randint(75, 98)

            response_data.append({
                "LLM": llm,
                "Response": result,
                "Score": score
            })

        df = pd.DataFrame(response_data)

        st.success("Execution Complete")

        st.dataframe(df)

        # Executive Summary
        best = df.loc[df["Score"].idxmax()]

        st.markdown(f"""
        ### 🏆 Best LLM Recommendation
        **{best['LLM']}** performed best with score **{best['Score']}**
        """)

# ===============================
# TAB 3 – ANALYTICS
# ===============================
with tab3:

    if 'df' in locals():

        st.subheader("LLM Performance Comparison")

        fig, ax = plt.subplots()
        ax.bar(df["LLM"], df["Score"])
        ax.set_title("LLM Performance Scores")

        st.pyplot(fig)

        # -------------------------------
        # EXPORTS
        # -------------------------------
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        json_data = df.to_dict(orient="records")

        col1, col2, col3 = st.columns(3)

        # JSON
        with col1:
            st.download_button(
                "⬇️ JSON",
                json.dumps(json_data, indent=4),
                f"enterprise_{timestamp}.json"
            )

        # CSV
        with col2:
            st.download_button(
                "⬇️ CSV",
                df.to_csv(index=False),
                f"enterprise_{timestamp}.csv"
            )

        # PDF
        with col3:
            buffer = io.BytesIO()
            doc = SimpleDocTemplate(buffer)
            styles = getSampleStyleSheet()

            story = [Paragraph("KNET ENTERPRISE AI REPORT", styles['Title']), Spacer(1,12)]

            for r in json_data:
                story.append(Paragraph(f"{r['LLM']} (Score: {r['Score']})", styles['Normal']))
                story.append(Paragraph(r["Response"], styles['Normal']))
                story.append(Spacer(1,12))

            doc.build(story)

            st.download_button(
                "⬇️ PDF",
                buffer.getvalue(),
                f"enterprise_{timestamp}.pdf"
            )

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("""
<hr>
<p style='text-align:center;color:gray;'>
Enterprise AI | Multi-LLM Decision Intelligence | KALSNET (KNet)
</p>
""", unsafe_allow_html=True)