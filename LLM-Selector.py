

# ==========================================================
# KALSNET (KNet) – AGENTIC AI LLM ORCHESTRATION PLATFORM
# Developed by Randy Singh – Kalsnet (KNet) Consulting Group
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

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
<h1 style='color:#0B3D91; text-align:center; font-weight:bold;'>
KALSNET (KNet) – Agentic AI LLM Orchestration Platform
</h1>
<h3 style='color:#0B3D91; text-align:center; font-weight:bold;'>
Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</h3>
<hr>
""", unsafe_allow_html=True)

# -------------------------------
# FREE LLM LIST + PROMPTS
# -------------------------------
llm_prompts = {
    "ChatGPT": "Go to https://chat.openai.com and paste your task.",
    "Claude": "Go to https://claude.ai and enter your prompt.",
    "Gemini": "Go to https://gemini.google.com and run your query.",
    "DeepSeek Chat": "Go to https://chat.deepseek.com and paste your task.",
    "Perplexity": "Go to https://www.perplexity.ai and ask your question.",
    "Grok": "Go to https://x.ai and use Grok chat interface.",
    "Microsoft Copilot": "Go to https://copilot.microsoft.com and enter your prompt.",
    "Mistral Le Chat": "Go to https://chat.mistral.ai and run your query.",
    "Qwen Chat": "Go to https://chat.qwen.ai and enter your task.",
    "Kimi": "Go to https://kimi.moonshot.cn and paste your query."
}

# -------------------------------
# USER INPUT
# -------------------------------
st.subheader("🧠 Enter Your Task")
user_input = st.text_area("", height=150)

# -------------------------------
# LLM SELECTION (PROFESSIONAL UI)
# -------------------------------
st.subheader("🚀 Select Free LLM Platform")

selected_llm = st.selectbox(
    "Choose LLM",
    list(llm_prompts.keys())
)

# -------------------------------
# DISPLAY PROMPT INSTRUCTIONS
# -------------------------------
st.markdown(f"""
<div style='background:#f4f6f9;padding:15px;border-radius:10px;border-left:6px solid #0B3D91;'>
<b>📘 How to Use {selected_llm}:</b><br><br>
{llm_prompts[selected_llm]}
</div>
""", unsafe_allow_html=True)

# -------------------------------
# MULTI-AGENT SYSTEM
# -------------------------------
def planner_agent(task):
    return f"Plan: Break task into steps for '{task}'"

def analyzer_agent(plan):
    return f"Analysis: Executing -> {plan}"

def reporter_agent(result):
    return f"Report: Final output generated from -> {result}"

# -------------------------------
# RUN AI (SIMULATION)
# -------------------------------
response = ""

if st.button("⚡ Run Agentic AI") and user_input:

    plan = planner_agent(user_input)
    analysis = analyzer_agent(plan)
    response = reporter_agent(analysis)

    st.success("✅ Agentic AI Execution Complete")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.text_area("Planner Output", plan, height=150)
    with col2:
        st.text_area("Analyzer Output", analysis, height=150)
    with col3:
        st.text_area("Final Report", response, height=150)

# -------------------------------
# ANALYTICS DASHBOARD
# -------------------------------
if response:
    st.subheader("📊 Analytics Dashboard")

    data = pd.DataFrame({
        "Stage": ["Planner", "Analyzer", "Reporter"],
        "Confidence": [
            random.randint(70, 95),
            random.randint(75, 98),
            random.randint(80, 99)
        ]
    })

    fig, ax = plt.subplots()
    ax.bar(data["Stage"], data["Confidence"])
    ax.set_title("Agent Confidence Levels")

    st.pyplot(fig)

# -------------------------------
# EXPORT OPTIONS
# -------------------------------
if response:

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    json_data = {
        "llm": selected_llm,
        "input": user_input,
        "response": response,
        "timestamp": timestamp
    }

    st.subheader("📥 Download Results")

    col1, col2, col3 = st.columns(3)

    # JSON
    with col1:
        st.download_button(
            "⬇️ JSON",
            json.dumps(json_data, indent=4),
            f"output_{timestamp}.json"
        )

    # CSV
    with col2:
        df = pd.DataFrame([json_data])
        st.download_button(
            "⬇️ CSV",
            df.to_csv(index=False),
            f"output_{timestamp}.csv"
        )

    # PDF
    with col3:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()

        story = [
            Paragraph("KALSNET AGENTIC AI REPORT", styles['Title']),
            Spacer(1, 12),
            Paragraph(f"LLM: {selected_llm}", styles['Normal']),
            Paragraph(f"Input: {user_input}", styles['Normal']),
            Spacer(1, 12),
            Paragraph(f"Response: {response}", styles['Normal'])
        ]

        doc.build(story)

        st.download_button(
            "⬇️ PDF",
            buffer.getvalue(),
            f"output_{timestamp}.pdf"
        )

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:gray;'>
Enterprise Agentic-AI | Multi-LLM Access Gateway | Free LLM Integration Layer
</p>
""", unsafe_allow_html=True)
