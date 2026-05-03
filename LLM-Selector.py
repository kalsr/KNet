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

# APIs
from openai import OpenAI
from groq import Groq
import anthropic

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
# USER INPUT
# -------------------------------
st.subheader("💬 Enter Your Question")
user_input = st.text_area("Enter your query...", height=150)

# -------------------------------
# SELECT LLM
# -------------------------------
selected_llm = st.selectbox("🚀 Select LLM", list(LLMS.keys()))

# -------------------------------
# INIT API CLIENTS
# -------------------------------
def get_clients():
    clients = {}

    try:
        clients["openai"] = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))
    except:
        clients["openai"] = None

    try:
        clients["groq"] = Groq(api_key=st.secrets.get("GROQ_API_KEY"))
    except:
        clients["groq"] = None

    try:
        clients["claude"] = anthropic.Anthropic(api_key=st.secrets.get("CLAUDE_API_KEY"))
    except:
        clients["claude"] = None

    try:
        clients["mistral"] = OpenAI(
            api_key=st.secrets.get("MISTRAL_API_KEY"),
            base_url="https://api.mistral.ai/v1"
        )
    except:
        clients["mistral"] = None

    return clients

clients = get_clients()

# -------------------------------
# API CALL FUNCTIONS
# -------------------------------
def call_openai(prompt):
    if not clients["openai"]:
        return "❌ OpenAI API key missing"

    try:
        resp = clients["openai"].chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"OpenAI Error: {e}"


def call_groq(prompt):
    if not clients["groq"]:
        return "❌ Groq API key missing"

    try:
        resp = clients["groq"].chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"Groq Error: {e}"


def call_claude(prompt):
    if not clients["claude"]:
        return "❌ Claude API key missing"

    try:
        resp = clients["claude"].messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.content[0].text
    except Exception as e:
        return f"Claude Error: {e}"


def call_mistral(prompt):
    if not clients["mistral"]:
        return "❌ Mistral API key missing"

    try:
        resp = clients["mistral"].chat.completions.create(
            model="mistral-small",
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"Mistral Error: {e}"

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
        url = LLMS[selected_llm]["url"]

        st.warning(f"⚠️ {selected_llm} requires login")

        st.markdown(f"### 👉 Open {selected_llm}")
        st.markdown(f"[Click Here to Open {selected_llm}]({url})")

        st.markdown("### 📋 Copy Your Prompt Below:")
        st.code(user_input, language="text")

        st.markdown(f"### 🔙 After using {selected_llm}, paste response below:")

        response = st.text_area("Paste Response Here", height=200)

# -------------------------------
# EXPORT SECTION (UNCHANGED)
# -------------------------------
if response:

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    json_data = {
        "llm": selected_llm,
        "input": user_input,
        "response": response,
        "timestamp": timestamp
    }

    # JSON
    st.download_button("📥 Download JSON",
        json.dumps(json_data, indent=4),
        f"output_{timestamp}.json")

    # CSV
    df = pd.DataFrame([json_data])
    st.download_button("📥 Download CSV",
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
        Paragraph(f"Input: {user_input}", styles['Normal']),
        Spacer(1, 12),
        Paragraph(f"Response: {response}", styles['Normal'])
    ]

    doc.build(story)

    st.download_button("📥 Download PDF",
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