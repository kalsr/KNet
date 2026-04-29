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

# OPTIONAL APIs (UNCOMMENT WHEN KEYS AVAILABLE)
# from openai import OpenAI
# from groq import Groq
# from transformers import pipeline

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
# LLM METADATA (EXPLANATIONS)
# -------------------------------
llm_info = {
    "GPT-4": {"type": "Paid", "access": "OpenAI API Key from platform.openai.com"},
    "GPT-3.5": {"type": "Free/Paid", "access": "Limited free, API via OpenAI"},
    "Google-Bard": {"type": "Free", "access": "Google account via Gemini/Bard UI"},
    "LLaMA": {"type": "Free/Open", "access": "Meta / HuggingFace / Replicate"},
    "Groq LLM": {"type": "Free Tier", "access": "console.groq.com API key"},
    "HuggingFace": {"type": "Free/Paid", "access": "huggingface.co token"},
}

# -------------------------------
# USER INPUT
# -------------------------------
st.subheader(" Enter Your Task")
user_input = st.text_area("Enter mission / AI task...", height=150)

# -------------------------------
# MODE SELECTION (CYBER / DOD)
# -------------------------------
mode = st.selectbox(" Select Mission Mode", [
    "General AI",
    "Cyber Defense",
    "Threat Hunting",
    "Fraud Detection",
    "DoD Mission Planning"
])

# -------------------------------
# AUTO MODEL SELECTION
# -------------------------------
def auto_select_llm(task):
    if "cyber" in task.lower():
        return "Groq LLM"
    elif "analysis" in task.lower():
        return "GPT-4"
    elif "translate" in task.lower():
        return "HuggingFace"
    return "GPT-3.5"

auto_llm = auto_select_llm(user_input) if user_input else None

st.info(f"🤖 Auto-selected LLM: {auto_llm}")

# -------------------------------
# LLM SELECTION BUTTONS
# -------------------------------
st.subheader("🚀 Select LLM Platform")

selected_llm = st.radio(
    "Choose LLM:",
    list(llm_info.keys())
)

# -------------------------------
# LLM INFO DISPLAY
# -------------------------------
info = llm_info[selected_llm]

st.markdown(f"""
### 📘 {selected_llm} Details
- **Type:** {info['type']}
- **Access:** {info['access']}
""")

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
# RUN AI
# -------------------------------
response = ""
if st.button("⚡ Run Agentic AI") and user_input:

    plan = planner_agent(user_input)
    analysis = analyzer_agent(plan)
    response = reporter_agent(analysis)

    st.success(" Agentic AI Execution Complete")

    st.text_area(" Planner Output", plan)
    st.text_area(" Analyzer Output", analysis)
    st.text_area(" Final Report", response)

# -------------------------------
# ANALYTICS DASHBOARD
# -------------------------------
if response:
    st.subheader(" Analytics Dashboard")

    data = pd.DataFrame({
        "Stage": ["Planner", "Analyzer", "Reporter"],
        "Confidence": [random.randint(70, 95), random.randint(75, 98), random.randint(80, 99)]
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
        "mode": mode,
        "input": user_input,
        "response": response,
        "timestamp": timestamp
    }

    # JSON
    st.download_button(" Download JSON",
        json.dumps(json_data, indent=4),
        f"output_{timestamp}.json")

    # CSV
    df = pd.DataFrame([json_data])
    st.download_button(" Download CSV",
        df.to_csv(index=False),
        f"output_{timestamp}.csv")

    # PDF
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    story = [
        Paragraph("KALSNET AGENTIC AI REPORT", styles['Title']),
        Spacer(1, 12),
        Paragraph(f"LLM: {selected_llm}", styles['Normal']),
        Paragraph(f"Mode: {mode}", styles['Normal']),
        Paragraph(f"Input: {user_input}", styles['Normal']),
        Spacer(1, 12),
        Paragraph(f"Response: {response}", styles['Normal'])
    ]

    doc.build(story)

    st.download_button(" Download PDF",
        buffer.getvalue(),
        f"output_{timestamp}.pdf")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:gray;'>
Enterprise Agentic-AI | Multi-LLM Orchestration | Cyber/DoD Ready Platform
</p>
""", unsafe_allow_html=True)