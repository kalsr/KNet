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

from openai import OpenAI
from groq import Groq
import anthropic

# -------------------------------
# PAGE CONFIG (UNCHANGED)
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
# SESSION STATE (NEW – FLOW CONTROL)
# -------------------------------
if "step" not in st.session_state:
    st.session_state.step = "select_llm"

if "response" not in st.session_state:
    st.session_state.response = ""

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "selected_llm" not in st.session_state:
    st.session_state.selected_llm = None

# -------------------------------
# LLM CONFIG
# -------------------------------
LLMS = {
    "ChatGPT (OpenAI)": {"type": "api"},
    "Claude (Anthropic)": {"type": "api"},
    "Groq (LLaMA3)": {"type": "api"},
    "Mistral": {"type": "api"},

    "Gemini": {"type": "redirect", "url": "https://gemini.google.com"},
    "Perplexity": {"type": "redirect", "url": "https://www.perplexity.ai"},
    "Grok": {"type": "redirect", "url": "https://x.ai"},
    "Microsoft Copilot": {"type": "redirect", "url": "https://copilot.microsoft.com"},
    "Qwen Chat": {"type": "redirect", "url": "https://chat.qwen.ai"},
    "Kimi": {"type": "redirect", "url": "https://kimi.moonshot.cn"}
}

# -------------------------------
# INPUT UI FLOW
# -------------------------------

if st.session_state.step == "select_llm":

    st.subheader("💬 Select LLM")

    st.session_state.selected_llm = st.selectbox(
        "Choose your model",
        list(LLMS.keys())
    )

    if st.button("➡️ Continue"):
        st.session_state.step = "ask_question"
        st.rerun()

# -------------------------------
# ASK QUESTION STEP
# -------------------------------
elif st.session_state.step == "ask_question":

    st.subheader(f"💬 Ask Question to {st.session_state.selected_llm}")

    st.session_state.input_text = st.text_area(
        "Enter your query...",
        height=150
    )

    if st.button("⚡ Get Response"):

        selected = st.session_state.selected_llm
        prompt = st.session_state.input_text

        if not prompt.strip():
            st.warning("Please enter a question")
        else:

            if LLMS[selected]["type"] == "api":

                if selected == "Groq (LLaMA3)":
                    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
                    res = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    st.session_state.response = res.choices[0].message.content

                elif selected == "ChatGPT (OpenAI)":
                    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                    res = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    st.session_state.response = res.choices[0].message.content

                elif selected == "Claude (Anthropic)":
                    client = anthropic.Anthropic(api_key=st.secrets["CLAUDE_API_KEY"])
                    res = client.messages.create(
                        model="claude-3-haiku-20240307",
                        max_tokens=1000,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    st.session_state.response = res.content[0].text

                elif selected == "Mistral":
                    client = OpenAI(
                        api_key=st.secrets["MISTRAL_API_KEY"],
                        base_url="https://api.mistral.ai/v1"
                    )
                    res = client.chat.completions.create(
                        model="mistral-small",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    st.session_state.response = res.choices[0].message.content

            else:
                st.session_state.response = f"Redirect LLM → {selected}"

            st.session_state.step = "show_result"
            st.rerun()

# -------------------------------
# RESULT + DOWNLOAD (UNCHANGED)
# -------------------------------
elif st.session_state.step == "show_result":

    st.success("✅ Response Generated")

    st.text_area("📄 Output", st.session_state.response, height=250)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    json_data = {
        "llm": st.session_state.selected_llm,
        "input": st.session_state.input_text,
        "response": st.session_state.response,
        "timestamp": timestamp
    }

    # JSON
    st.download_button(
        "📥 Download JSON",
        json.dumps(json_data, indent=4),
        f"output_{timestamp}.json"
    )

    # CSV
    df = pd.DataFrame([json_data])
    st.download_button(
        "📥 Download CSV",
        df.to_csv(index=False),
        f"output_{timestamp}.csv"
    )

    # PDF
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    story = [
        Paragraph("KALSNET AGENTIC AI REPORT", styles['Title']),
        Spacer(1, 12),
        Paragraph(f"LLM: {st.session_state.selected_llm}", styles['Normal']),
        Paragraph(f"Input: {st.session_state.input_text}", styles['Normal']),
        Spacer(1, 12),
        Paragraph(f"Response: {st.session_state.response}", styles['Normal'])
    ]

    doc.build(story)

    st.download_button(
        "📥 Download PDF",
        buffer.getvalue(),
        f"output_{timestamp}.pdf"
    )

    # RESET BUTTON (KEY FEATURE YOU WANTED)
    if st.button("🔄 Use Another LLM"):
        st.session_state.step = "select_llm"
        st.session_state.response = ""
        st.session_state.input_text = ""
        st.session_state.selected_llm = None
        st.rerun()

# -------------------------------
# FOOTER (UNCHANGED)
# -------------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:gray;'>
Enterprise Agentic-AI | Multi-LLM Orchestration | Cyber/DoD Ready Platform
</p>
""", unsafe_allow_html=True)