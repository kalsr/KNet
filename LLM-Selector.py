# ==========================================================
# KALSNET (KNet) – MULTI-LLM ORCHESTRATION PLATFORM
# FULL 10 LLM ENTERPRISE VERSION
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
# PAGE CONFIG
# ==========================================================
st.set_page_config(page_title="KNet Multi-LLM Hub", layout="wide")

# ==========================================================
# HEADER (UNCHANGED)
# ==========================================================
st.markdown("""
<h1 style='text-align:center; color:#0B3D91; font-weight:bold;'>
KALSNET (KNet) – Agentic AI LLM Orchestration Platform
</h1>
<h3 style='text-align:center; color:#0B3D91;'>
Multi-LLM Enterprise Control Center
</h3>
<hr>
""", unsafe_allow_html=True)

# ==========================================================
# SESSION STATE
# ==========================================================
for k in ["step", "llm", "prompt", "response"]:
    if k not in st.session_state:
        st.session_state[k] = "" if k != "step" else "select"

# ==========================================================
# 10 LLM DEFINITIONS
# ==========================================================
LLMS = {
    # API MODELS (REAL RESPONSE)
    "ChatGPT (OpenAI)": "api",
    "Claude (Anthropic)": "api",
    "Groq (LLaMA3)": "api",
    "Mistral": "api",

    # WEB MODELS (REDIRECT)
    "Gemini": "web",
    "Perplexity": "web",
    "Grok": "web",
    "Copilot": "web",
    "Qwen Chat": "web",
    "Kimi": "web"
}

WEB_LINKS = {
    "Gemini": "https://gemini.google.com",
    "Perplexity": "https://www.perplexity.ai",
    "Grok": "https://x.ai",
    "Copilot": "https://copilot.microsoft.com",
    "Qwen Chat": "https://chat.qwen.ai",
    "Kimi": "https://kimi.moonshot.cn"
}

# ==========================================================
# SIDEBAR – API KEY MANAGER (WITH INSTRUCTIONS)
# ==========================================================
st.sidebar.title("🔐 API Key Manager")

def key_input(label, key, url):
    st.sidebar.text_input(label, type="password", key=key)
    st.sidebar.caption(f"🔗 Get key: {url}")

key_input("OpenAI API Key", "OPENAI_KEY", "https://platform.openai.com/api-keys")
key_input("Groq API Key", "GROQ_KEY", "https://console.groq.com/keys")
key_input("Claude API Key", "CLAUDE_KEY", "https://console.anthropic.com")
key_input("Mistral API Key", "MISTRAL_KEY", "https://console.mistral.ai")

st.sidebar.markdown("---")
st.sidebar.info("Keys stored in session only. No persistence.")

# ==========================================================
# SAFE CLIENT GETTERS
# ==========================================================
def get_key(k):
    return st.session_state.get(k)

# ==========================================================
# API CALLS (SAFE)
# ==========================================================
def call_openai(prompt):
    key = get_key("OPENAI_KEY")
    if not key:
        return "❌ Missing OpenAI API Key"

    client = OpenAI(api_key=key)
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content


def call_groq(prompt):
    key = get_key("GROQ_KEY")
    if not key:
        return "❌ Missing Groq API Key"

    client = Groq(api_key=key)
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content


def call_claude(prompt):
    key = get_key("CLAUDE_KEY")
    if not key:
        return "❌ Missing Claude API Key"

    client = anthropic.Anthropic(api_key=key)
    res = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    return res.content[0].text


def call_mistral(prompt):
    key = get_key("MISTRAL_KEY")
    if not key:
        return "❌ Missing Mistral API Key"

    client = OpenAI(api_key=key, base_url="https://api.mistral.ai/v1")
    res = client.chat.completions.create(
        model="mistral-small",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content

# ==========================================================
# STEP 1 – SELECT LLM
# ==========================================================
if st.session_state.step == "select":

    st.subheader("🚀 Select One of 10 LLMs")

    st.session_state.llm = st.selectbox(
        "Choose LLM",
        list(LLMS.keys())
    )

    if st.button("Continue"):
        st.session_state.step = "use"
        st.rerun()

# ==========================================================
# STEP 2 – USE LLM
# ==========================================================
elif st.session_state.step == "use":

    llm = st.session_state.llm
    mode = LLMS[llm]

    st.subheader(f"💬 Using: {llm}")

    st.session_state.prompt = st.text_area("Enter your question", height=150)

    if st.button("⚡ Run"):

        if mode == "api":

            if llm == "ChatGPT (OpenAI)":
                st.session_state.response = call_openai(st.session_state.prompt)

            elif llm == "Groq (LLaMA3)":
                st.session_state.response = call_groq(st.session_state.prompt)

            elif llm == "Claude (Anthropic)":
                st.session_state.response = call_claude(st.session_state.prompt)

            elif llm == "Mistral":
                st.session_state.response = call_mistral(st.session_state.prompt)

        else:
            st.session_state.response = "🌐 Web LLM - Open in browser"

        st.session_state.step = "result"
        st.rerun()

# ==========================================================
# STEP 3 – RESULT VIEW
# ==========================================================
elif st.session_state.step == "result":

    st.success("✅ Response Ready")

    llm = st.session_state.llm

    if LLMS[llm] == "web":
        st.warning("This LLM runs in browser")
        st.markdown(f"[Open {llm}]({WEB_LINKS[llm]})")
        st.code(st.session_state.prompt)

    st.text_area("📄 Output", st.session_state.response, height=250)

    # ================= DOWNLOADS =================
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    data = {
        "llm": llm,
        "input": st.session_state.prompt,
        "response": st.session_state.response,
        "time": ts
    }

    st.download_button("📥 JSON", json.dumps(data, indent=4), f"{ts}.json")
    st.download_button("📥 CSV", pd.DataFrame([data]).to_csv(index=False), f"{ts}.csv")

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    doc.build([
        Paragraph("KNET AI REPORT", styles["Title"]),
        Spacer(1, 12),
        Paragraph(str(data), styles["Normal"])
    ])

    st.download_button("📥 PDF", buffer.getvalue(), f"{ts}.pdf")

    if st.button("🔄 Back to LLMs"):
        st.session_state.step = "select"
        st.session_state.response = ""
        st.session_state.prompt = ""
        st.session_state.llm = ""
        st.rerun()

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("""
<hr>
<p style='text-align:center; color:gray;'>
Enterprise Multi-LLM Orchestration Platform | KNet
</p>
""", unsafe_allow_html=True)