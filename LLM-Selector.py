# ==========================================================
# KALSNET (KNet) – AGENTIC AI LLM ORCHESTRATION PLATFORM
# Developed by Randy Singh – Kalsnet (KNet) Consulting Group
# ==========================================================

import streamlit as st
import pandas as pd
import json
import datetime
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# -------------------------------
# HEADER (UNCHANGED)
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
# 10 FREE LLMs
# -------------------------------
llms = [
    "ChatGPT",
    "Claude",
    "Gemini",
    "DeepSeek Chat",
    "Perplexity",
    "Grok",
    "Microsoft Copilot",
    "Mistral Le Chat",
    "Qwen Chat",
    "Kimi"
]

# -------------------------------
# LLM LINKS (FOR USER GUIDANCE)
# -------------------------------
llm_links = {
    "ChatGPT": "https://chat.openai.com",
    "Claude": "https://claude.ai",
    "Gemini": "https://gemini.google.com",
    "DeepSeek Chat": "https://chat.deepseek.com",
    "Perplexity": "https://www.perplexity.ai",
    "Grok": "https://x.ai",
    "Microsoft Copilot": "https://copilot.microsoft.com",
    "Mistral Le Chat": "https://chat.mistral.ai",
    "Qwen Chat": "https://chat.qwen.ai",
    "Kimi": "https://kimi.moonshot.cn"
}

# -------------------------------
# SELECT LLM
# -------------------------------
st.subheader("🚀 Select Free LLM")

selected_llm = st.selectbox("Choose LLM", llms)

# -------------------------------
# DISPLAY SELECTED LLM
# -------------------------------
st.markdown(f"""
<div style='background:#f4f6f9;padding:15px;border-radius:10px;border-left:6px solid #0B3D91;'>
<b>Selected LLM:</b> {selected_llm}<br><br>
👉 Access: <a href="{llm_links[selected_llm]}" target="_blank">{llm_links[selected_llm]}</a>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# ASK QUESTION
# -------------------------------
st.subheader(f"💬 Ask {selected_llm}")

user_input = st.text_area("Enter your question", height=150)

# -------------------------------
# RESPONSE (SIMULATED – API READY)
# -------------------------------
response = ""

if st.button("⚡ Get Response") and user_input:

    # SIMULATED RESPONSE (Replace with API later)
    response = f"{selected_llm} response to: {user_input}"

    st.success("✅ Response Generated")

    st.text_area("LLM Response", response, height=200)

# -------------------------------
# DOWNLOAD OPTIONS
# -------------------------------
if response:

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    data = {
        "llm": selected_llm,
        "question": user_input,
        "response": response,
        "timestamp": timestamp
    }

    st.subheader("📥 Download Results")

    col1, col2, col3 = st.columns(3)

    # JSON
    with col1:
        st.download_button(
            "⬇️ JSON",
            json.dumps(data, indent=4),
            f"llm_output_{timestamp}.json"
        )

    # CSV
    with col2:
        df = pd.DataFrame([data])
        st.download_button(
            "⬇️ CSV",
            df.to_csv(index=False),
            f"llm_output_{timestamp}.csv"
        )

    # PDF
    with col3:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()

        story = [
            Paragraph("KALSNET LLM REPORT", styles['Title']),
            Spacer(1, 12),
            Paragraph(f"LLM: {selected_llm}", styles['Normal']),
            Paragraph(f"Question: {user_input}", styles['Normal']),
            Spacer(1, 12),
            Paragraph(f"Response: {response}", styles['Normal'])
        ]

        doc.build(story)

        st.download_button(
            "⬇️ PDF",
            buffer.getvalue(),
            f"llm_output_{timestamp}.pdf"
        )

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:gray;'>
Free LLM Access Gateway | KALSNET (KNet)
</p>
""", unsafe_allow_html=True)