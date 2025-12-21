import streamlit as st
import requests
from groq import Groq

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Multi-LLM Hub",
    page_icon="🧠",
    layout="wide"
)

# =========================================================
# STARTUP VALIDATION (FAIL FAST, NO GUESSING)
# =========================================================
AVAILABLE_SECRETS = list(st.secrets.keys())

if "GROQ_API_KEY" not in st.secrets:
    st.error("❌ GROQ_API_KEY not found in Streamlit secrets")
    st.stop()

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
HF_API_KEY = st.secrets.get("HF_API_KEY", "")

# =========================================================
# SIDEBAR – SYSTEM STATUS
# =========================================================
st.sidebar.title("🔎 System Status")
st.sidebar.success("Groq API key loaded")

if HF_API_KEY:
    st.sidebar.success("Hugging Face key loaded")
else:
    st.sidebar.warning("Hugging Face key not set")

# =========================================================
# LLM QUERY FUNCTIONS
# =========================================================
def query_ollama(prompt, model):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=60
    )
    return r.json().get("response", "No response from Ollama")

def query_huggingface(prompt, model):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
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
    client = Groq(api_key=GROQ_API_KEY)
    chat = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return chat.choices[0].message.content

# =========================================================
# MAIN HEADER
# =========================================================
st.title("🧠 Multi-LLM Hub")
st.subheader("Enterprise-Grade Unified LLM Interface")

# =========================================================
# SIDEBAR – PROVIDER & MODEL SELECTION
# =========================================================
provider = st.sidebar.selectbox(
    "Select LLM Provider",
    ["Groq", "Hugging Face", "Ollama (Local)"]
)

MODEL_MAP = {
    "Groq": [
        "llama-3.1-8b-instant",  # active model
        "another_supported_model_here"
    ],
    "Hugging Face": [
        "openai/gpt‑oss‑120b",
        "meta-llama/Llama-2-7b-chat-hf"
    ],
    "Ollama (Local)": [
        "llama3",
        "mistral",
        "phi3"
    ]
}


model = st.sidebar.selectbox("Select Model", MODEL_MAP[provider])

# =========================================================
# PROMPT INPUT
# =========================================================
prompt = st.text_area(
    "Enter your prompt",
    height=200,
    placeholder="Ask anything…"
)

# =========================================================
# VALIDATION
# =========================================================
def validate():
    if provider == "Hugging Face" and not HF_API_KEY:
        st.error("❌ Hugging Face API key missing")
        return False
    return True

# =========================================================
# GENERATE RESPONSE
# =========================================================
if st.button("🚀 Generate Response"):
    if not prompt.strip():
        st.warning("⚠️ Please enter a prompt")
    elif validate():
        with st.spinner("🧠 Thinking..."):
            try:
                if provider == "Groq":
                    result = query_groq(prompt, model)
                elif provider == "Hugging Face":
                    result = query_huggingface(prompt, model)
                else:
                    result = query_ollama(prompt, model)

                st.markdown("### 💡 Model Response")
                st.success(result)

            except Exception as e:
                st.error(f"❌ Error: {e}")

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.caption("© 2025 • KNet Consulting • Multi-LLM Hub")













