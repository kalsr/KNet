

import streamlit as st
import requests

# Optional SDKs
from groq import Groq
from openai import OpenAI
import anthropic

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Enterprise Multi-LLM Hub",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Enterprise Multi-LLM Hub")
st.caption("Groq • Hugging Face • OpenRouter • OpenAI • Anthropic • Azure • Ollama")

# =====================================================
# SESSION STATE
# =====================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================================
# SECRETS
# =====================================================
secrets = st.secrets

def has(k):
    return k in secrets and secrets[k] != ""

# =====================================================
# MODEL REGISTRY (EXPLICIT & USER-VISIBLE)
# =====================================================
MODEL_REGISTRY = {}

if has("GROQ_API_KEY"):
    MODEL_REGISTRY["Groq"] = [
        "llama-3.1-8b-instant",
        "llama-3.1-70b-versatile"
    ]

if has("HF_API_KEY"):
    MODEL_REGISTRY["Hugging Face"] = [
        "NousResearch/Hermes-3-Llama-3.1-8B"
    ]

if has("OPENROUTER_API_KEY"):
    MODEL_REGISTRY["OpenRouter"] = [
        "nousresearch/hermes-3-llama-3.1-8b",
        "mistralai/mistral-7b-instruct",
        "meta-llama/llama-3.1-8b-instruct"
    ]

if has("OPENAI_API_KEY"):
    MODEL_REGISTRY["OpenAI"] = [
        "gpt-4o-mini",
        "gpt-4o"
    ]

if has("ANTHROPIC_API_KEY"):
    MODEL_REGISTRY["Anthropic"] = [
        "claude-3-haiku-20240307",
        "claude-3-sonnet-20240229"
    ]

if has("AZURE_OPENAI_KEY"):
    MODEL_REGISTRY["Azure OpenAI"] = [
        secrets["AZURE_OPENAI_DEPLOYMENT"]
    ]

# Ollama is always available
MODEL_REGISTRY["Ollama (Local)"] = [
    "llama3",
    "mistral",
    "phi3"
]

# =====================================================
# SIDEBAR UI
# =====================================================
st.sidebar.header("🔌 LLM Selection")

provider = st.sidebar.selectbox(
    "Select Provider",
    list(MODEL_REGISTRY.keys())
)

model = st.sidebar.selectbox(
    "Select Model",
    MODEL_REGISTRY[provider]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🔑 Key Status")

for key in [
    "GROQ_API_KEY", "HF_API_KEY", "OPENROUTER_API_KEY",
    "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "AZURE_OPENAI_KEY"
]:
    st.sidebar.success(key) if has(key) else st.sidebar.warning(key)

# =====================================================
# PROMPT
# =====================================================
prompt = st.text_area(
    "Enter your prompt",
    height=160,
    placeholder="Ask anything…"
)

# =====================================================
# PROVIDER IMPLEMENTATIONS
# =====================================================
def groq_llm(prompt):
    client = Groq(api_key=secrets["GROQ_API_KEY"])
    return client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message.content

def hf_router(prompt):
    r = requests.post(
        "https://router.huggingface.co/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {secrets['HF_API_KEY']}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 300
        },
        timeout=60
    )
    data = r.json()
    if "error" in data:
        raise RuntimeError(data["error"])
    return data["choices"][0]["message"]["content"]

def openrouter_llm(prompt):
    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {secrets['OPENROUTER_API_KEY']}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 300
        },
        timeout=60
    )
    return r.json()["choices"][0]["message"]["content"]

def openai_llm(prompt):
    client = OpenAI(api_key=secrets["OPENAI_API_KEY"])
    return client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message.content

def anthropic_llm(prompt):
    client = anthropic.Anthropic(api_key=secrets["ANTHROPIC_API_KEY"])
    return client.messages.create(
        model=model,
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    ).content[0].text

def azure_llm(prompt):
    client = OpenAI(
        api_key=secrets["AZURE_OPENAI_KEY"],
        base_url=f"{secrets['AZURE_OPENAI_ENDPOINT']}/openai/deployments/{secrets['AZURE_OPENAI_DEPLOYMENT']}",
        default_headers={"api-key": secrets["AZURE_OPENAI_KEY"]}
    )
    return client.chat.completions.create(
        model=secrets["AZURE_OPENAI_DEPLOYMENT"],
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message.content

def ollama_llm(prompt):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=60
    )
    return r.json().get("response", "No response")

# =====================================================
# EXECUTION
# =====================================================
if st.button("🚀 Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Thinking…"):
            try:
                if provider == "Groq":
                    reply = groq_llm(prompt)
                elif provider == "Hugging Face":
                    try:
                        reply = hf_router(prompt)
                    except Exception:
                        st.warning("HF Router failed → falling back to OpenRouter")
                        reply = openrouter_llm(prompt)
                elif provider == "OpenRouter":
                    reply = openrouter_llm(prompt)
                elif provider == "OpenAI":
                    reply = openai_llm(prompt)
                elif provider == "Anthropic":
                    reply = anthropic_llm(prompt)
                elif provider == "Azure OpenAI":
                    reply = azure_llm(prompt)
                else:
                    reply = ollama_llm(prompt)

                st.success(reply)

            except Exception as e:
                st.error(f"❌ {e}")
