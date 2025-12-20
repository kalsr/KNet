import streamlit as st
import requests
import os
from dotenv import load_dotenv
from groq import Groq

# =========================================================
# LOAD ENV (MUST BE FIRST)
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
# SESSION STATE INIT (SAFE)
# =========================================================
if "HF_API_KEY" not in st.session_state:
    st.session_state.HF_API_KEY = os.getenv("HF_API_KEY", "")

if "GROQ_API_KEY" not in st.session_state:
    st.session_state.GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# =========================================================
# UI STYLES
# =========================================================
st.markdown("""
<style>
.stApp { background-color: #f6f8fa; font-family: Segoe UI; }
section[data-testid="stSidebar"] { background-color: #111827; }
section[data-testid="stSidebar"] label { color: white !important; }
</style>
""", unsafe_allow_html=True)

# =========================================================
# LLM FUNCTIONS
# =========================================================
def query_ollama(prompt, model):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=60
    )
    return r.json().get("response", "No response")

def query_huggingface(prompt, model):
    headers = {"Authorization": f"Bearer {st.session_state.HF_API_KEY}"}
    r = requests.post(
        f"https://api-inference.huggingface.co/models/{model}",
        headers=headers,
        json={"inputs": prompt},
        timeout=60
    )
    data = r.json()
    if isinstance(data, list):
        return data[0].get("generated_text", str(data))
    return str(data)

def query_groq(prompt, model):
    if not st.session_state.GROQ_API_KEY:
        raise RuntimeError("Groq API key not loaded")
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
# SIDEBAR — PROVIDER / MODEL
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
def validate():
    if provider == "Groq" and not st.session_state.GROQ_API_KEY:
        st.error("❌ Groq API key not found. Check .env file.")
        return False
    if provider == "Hugging Face" and not st.session_state.HF_API_KEY:
        st.error("❌ Hugging Face API key missing")
        return False
    return True

# =========================================================
# GENERATE
# =========================================================
if st.button("🚀 Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt")
    elif validate():
        with st.spinner("Thinking..."):
            try:
                if provider == "Ollama (Local)":
                    response = query_ollama(prompt, model)
                elif provider == "Hugging Face":
                    response = query_huggingface(prompt, model)
                else:
                    response = query_groq(prompt, model)

                st.success(response)

            except Exception as e:
                st.error(str(e))

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.caption("© 2025 • Multi-LLM Hub")
