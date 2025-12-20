

# File: app.py

import streamlit as st
import requests
import os
from dotenv import load_dotenv, set_key
from groq import Groq

# =========================================================
# ENV SETUP
# =========================================================
load_dotenv()

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Multi-LLM Hub",
    page_icon="🧠",
    layout="wide"
)

# =========================================================
# PROFESSIONAL UI STYLES
# =========================================================
st.markdown("""
<style>
.stApp {
    background-color: #f6f8fa;
    font-family: "Segoe UI", sans-serif;
}
h1, h2, h3 { color: #1f2937; }
div.stButton > button {
    border-radius: 4px;
    background-color: #2563eb;
    color: white;
    font-weight: 600;
    padding: 10px 22px;
    border: none;
}
div.stButton > button:hover {
    background-color: #1e40af;
}
section[data-testid="stSidebar"] {
    background-color: #111827;
    color: white;
}
section[data-testid="stSidebar"] label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================
st.session_state.setdefault("HF_API_KEY", os.getenv("HF_API_KEY", ""))
st.session_state.setdefault("GROQ_API_KEY", os.getenv("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", ""))

# =========================================================
# LLM FUNCTIONS
# =========================================================
def query_ollama(prompt, model):
    url = "http://localhost:11434/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": False}
    r = requests.post(url, json=payload, timeout=60)
    return r.json().get("response", "No response")

def query_huggingface(prompt, model):
    headers = {"Authorization": f"Bearer {st.session_state.HF_API_KEY}"}
    payload = {"inputs": prompt}
    r = requests.post(
        f"https://api-inference.huggingface.co/models/{model}",
        headers=headers,
        json=payload,
        timeout=60
    )
    data = r.json()
    if isinstance(data, list) and "generated_text" in data[0]:
        return data[0]["generated_text"]
    return str(data)

def query_groq(prompt, model):
    if not st.session_state.GROQ_API_KEY:
        raise ValueError("Groq API key not set")
    client = Groq(api_key=st.session_state.GROQ_API_KEY)
    chat = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return chat.choices[0].message.content

# =========================================================
# HEADER
# =========================================================
st.title("🧠 Multi-LLM Hub")
st.subheader("Enterprise-grade Open-Source LLM Interface")

# =========================================================
# SIDEBAR – API KEYS
# =========================================================
st.sidebar.title("🔐 API Key Manager")

with st.sidebar.expander("Manage API Keys"):
    hf_key = st.text_input("Hugging Face API Key", type="password",
                           value=st.session_state.HF_API_KEY)
    groq_key = st.text_input("Groq API Key", type="password",
                             value=st.session_state.GROQ_API_KEY)

    if st.button("💾 Save API Keys"):
        st.session_state.HF_API_KEY = hf_key
        st.session_state.GROQ_API_KEY = groq_key
        set_key(".env", "HF_API_KEY", hf_key)
        set_key(".env", "GROQ_API_KEY", groq_key)
        st.sidebar.success("✅ Keys saved")

st.sidebar.markdown("---")

# =========================================================
# MODEL SELECTION (FIXED)
# =========================================================
provider = st.sidebar.selectbox(
    "Select Provider",
    ["Ollama (Local)", "Hugging Face", "Groq"]
)

MODEL_MAP = {
    "Ollama (Local)": ["llama3", "mistral", "phi3"],
    "Hugging Face": [
        "mistralai/Mistral-7B-Instruct",
        "google/gemma-7b"
    ],
    "Groq": [
        "llama3-70b-8192",
        "mixtral-8x7b-32768"
    ]
}

model = st.sidebar.selectbox("Select Model", MODEL_MAP[provider])

# =========================================================
# PROMPT
# =========================================================
prompt = st.text_area("Enter your prompt", height=200)

# =========================================================
# VALIDATION
# =========================================================
def validate_keys():
    if provider == "Hugging Face" and not st.session_state.HF_API_KEY:
        st.error("❌ Hugging Face API key missing")
        return False
    if provider == "Groq" and not st.session_state.GROQ_API_KEY:
        st.error("❌ Groq API key missing")
        return False
    return True

# =========================================================
# GENERATE
# =========================================================
if st.button("🚀 Generate Response"):
    if not prompt.strip():
        st.warning("⚠️ Please enter a prompt")
    elif validate_keys():
        with st.spinner("🧠 Thinking..."):
            try:
                if provider == "Ollama (Local)":
                    result = query_ollama(prompt, model)
                elif provider == "Hugging Face":
                    result = query_huggingface(prompt, model)
                else:
                    result = query_groq(prompt, model)

                st.markdown("### 💡 Model Response")
                st.success(result)

            except Exception as e:
                st.error(f"❌ Error: {e}")

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.caption("© 2025 • Multi-LLM Hub • Open-Source AI Interface")
