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

# API CLIENTS (INSTALL REQUIRED LIBS)
from openai import OpenAI
from groq import Groq
import anthropic

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# -------------------------------
# HEADER (KEEP SAME)
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
# INPUT
# -------------------------------
st.subheader("💬 Enter Your Question")
user_input = st.text_area("Enter your query...", height=150)

# -------------------------------
# SELECT LLM
# -------------------------------
selected_llm = st.selectbox("🚀 Select LLM", list(LLMS.keys()))

# -------------------------------
# API CLIENT INIT (SAFE)
# -------------------------------
def get_clients():
    clients = {}
    try:
        clients["openai"] = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    except:
        clients["openai"] = None

    try:
        clients["groq"] = Groq(api_key=st.secrets["GROQ_API_KEY"])
    except:
        clients["groq"] = None

    try:
        clients["claude"] = anthropic.Anthropic(api_key=st.secrets["CLAUDE_API_KEY"])
    except:
        clients["claude"] = None

    try:
        clients["mistral"] = OpenAI(
            api_key=st.secrets["MISTRAL_API_KEY"],
            base_url="https://api.mistral.ai/v1"
        )
    except:
        clients["mistral"] = None

    return clients

clients = get_clients()

# -------------------------------
# API CALLS
# -------------------------------
def call_openai(prompt):
    client = clients["openai"]
    if not client:
        return "❌ OpenAI API Key missing"

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content


def call_groq(prompt):
    client = clients["groq"]
    if not client:
        return "❌ Groq API Key missing"

    resp = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content


def call_claude(prompt):
    client = clients["claude"]
    if not client:
        return "❌ Claude API Key missing"

    resp = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.content[0].text


def call_mistral(prompt):
    client = clients["mistral"]
    if not client:
        return "❌ Mistral API Key missing"

    resp = client.chat.completions.create(
        model="mistral-small",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content


# -------------------------------
# EXECUTION
# -------------------------------
response = ""

if st.button("⚡ Get Response") and user_input:

    if LLMS[selected_llm]["type"] == "api":

        if selected_llm == "ChatGPT (OpenAI)":
            response = call_openai(user_input)

        elif selected_llm == "Claude (Anthropic)":
            response = call_claude(user_input)

        elif selected_llm == "Groq (LLaMA3)":
            response = call_groq(user_input)

        elif selected_llm == "Mistral":
            response = call_mistral(user_input)

        st.success("✅ Response Generated")
        st.text_area("📄 Output", response, height=250)

    else:
        # REDIRECT FLOW
        url = LLMS[selected_llm]["url"]

        st.warning(f"⚠️ {selected_llm} requires account/login")

        st.markdown(f"""
### 👉 Open {selected_llm}
[Click Here to Open {selected_llm}]({url})

### 📋 Your Prompt (Copy & Paste)