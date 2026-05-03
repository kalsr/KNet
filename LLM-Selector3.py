


# ==========================================================
# KALSNET (KNet) – MULTI-LLM ORCHESTRATION PLATFORM (UPDATED)
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

# ==========================================================
# CONFIG
# ==========================================================
st.set_page_config(page_title="KNet Multi-LLM Hub", layout="wide")

# ==========================================================
# HEADER
# ==========================================================
st.markdown("""
<h1 style='text-align:center; color:#0B3D91; font-weight:bold;'>
KALSNET (KNet) – Multi-LLM Orchestration Platform
</h1>
<hr>
""", unsafe_allow_html=True)

# ==========================================================
# SESSION STATE
# ==========================================================
if "response" not in st.session_state:
    st.session_state.response = ""

if "prompt" not in st.session_state:
    st.session_state.prompt = ""

# ==========================================================
# UPDATED LLM MAP (ChatGPT = WEB)
# ==========================================================
LLMS = {
    "ChatGPT (Free Web)": "web",   # ✅ CHANGED
    "Claude (Anthropic)": "api",
    "Groq (LLaMA3)": "api",
    "Mistral": "api",

    "Gemini": "web",
    "Perplexity": "web",
    "Grok": "web",
    "Microsoft Copilot": "web",
    "Qwen Chat": "web",
    "Kimi": "web"
}

WEB_LINKS = {
    "ChatGPT (Free Web)": "https://chat.openai.com",
    "Gemini": "https://gemini.google.com",
    "Perplexity": "https://www.perplexity.ai",
    "Grok": "https://x.ai",
    "Microsoft Copilot": "https://copilot.microsoft.com",
    "Qwen Chat": "https://chat.qwen.ai",
    "Kimi": "https://kimi.moonshot.cn"
}

# ==========================================================
# SIDEBAR – API KEYS (UNCHANGED)
# ==========================================================
st.sidebar.title(" API Keys")

st.session_state.OPENAI_KEY = st.sidebar.text_input("OpenAI Key", type="password")
st.sidebar.caption("Get: https://platform.openai.com/api-keys")

st.session_state.GROQ_KEY = st.sidebar.text_input("Groq Key", type="password")
st.sidebar.caption("Get: https://console.groq.com/keys")

st.session_state.CLAUDE_KEY = st.sidebar.text_input("Claude Key", type="password")
st.sidebar.caption("Get: https://console.anthropic.com")

st.session_state.MISTRAL_KEY = st.sidebar.text_input("Mistral Key", type="password")
st.sidebar.caption("Get: https://console.mistral.ai")

st.sidebar.markdown("---")
st.sidebar.info("Keys are used only during session (not stored)")

# ==========================================================
# LLM CALL FUNCTIONS (UNCHANGED)
# ==========================================================
def call_groq(prompt):
    if not st.session_state.GROQ_KEY:
        return "❌ Missing Groq Key"
    try:
        client = Groq(api_key=st.session_state.GROQ_KEY)
        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Groq Error: {e}"


def call_claude(prompt):
    if not st.session_state.CLAUDE_KEY:
        return "❌ Missing Claude Key"
    try:
        client = anthropic.Anthropic(api_key=st.session_state.CLAUDE_KEY)
        res = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        return res.content[0].text
    except Exception as e:
        return f"Claude Error: {e}"


def call_mistral(prompt):
    if not st.session_state.MISTRAL_KEY:
        return "❌ Missing Mistral Key"
    try:
        client = OpenAI(
            api_key=st.session_state.MISTRAL_KEY,
            base_url="https://api.mistral.ai/v1"
        )
        res = client.chat.completions.create(
            model="mistral-small",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Mistral Error: {e}"

# ==========================================================
# UI – LLM SELECTION
# ==========================================================
st.subheader(" Select LLM")

selected_llm = st.selectbox("Choose one of 10 LLMs", list(LLMS.keys()))

st.session_state.prompt = st.text_area("💬 Enter your question", height=150)

# ==========================================================
# RUN BUTTON
# ==========================================================
if st.button(" Run LLM"):

    if not st.session_state.prompt.strip():
        st.warning("Enter a question first")

    else:
        mode = LLMS[selected_llm]

        # ---------------- API MODE ----------------
        if mode == "api":

            if selected_llm == "Groq (LLaMA3)":
                st.session_state.response = call_groq(st.session_state.prompt)

            elif selected_llm == "Claude (Anthropic)":
                st.session_state.response = call_claude(st.session_state.prompt)

            elif selected_llm == "Mistral":
                st.session_state.response = call_mistral(st.session_state.prompt)

        # ---------------- WEB MODE ----------------
        else:
            st.session_state.response = "🌐 Use external LLM and paste response below"

            st.markdown(f"### 👉 Open {selected_llm}")
            st.markdown(f"[Click here to open {selected_llm}]({WEB_LINKS[selected_llm]})")

            st.markdown("### 📋 Copy your prompt:")
            st.code(st.session_state.prompt)

            st.markdown("### 🔙 Paste response here after using the LLM:")
            st.session_state.response = st.text_area("Paste Response", height=200)

# ==========================================================
# OUTPUT DISPLAY
# ==========================================================
if st.session_state.response:

    st.success(" Response Generated")

    st.markdown("## 📄 Output:")

    st.text_area("", st.session_state.response, height=300)

    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    data = {
        "llm": selected_llm,
        "input": st.session_state.prompt,
        "response": st.session_state.response,
        "time": ts
    }

    st.download_button(" JSON", json.dumps(data, indent=4), f"{ts}.json")
    st.download_button(" CSV", pd.DataFrame([data]).to_csv(index=False), f"{ts}.csv")

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    doc.build([
        Paragraph("KNET AI REPORT", styles["Title"]),
        Spacer(1, 12),
        Paragraph(str(data), styles["Normal"])
    ])

    st.download_button(" PDF", buffer.getvalue(), f"{ts}.pdf")

# ==========================================================
# RESET
# ==========================================================
if st.button(" Reset / Choose Another LLM"):
    st.session_state.response = ""
    st.session_state.prompt = ""
    st.rerun()

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("""
<hr>
<p style='text-align:center; color:gray;'>
Multi-LLM Orchestration Platform | KNet
</p>
""", unsafe_allow_html=True)