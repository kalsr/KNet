

import streamlit as st
import requests

# Optional SDKs
try:
    from groq import Groq
except:
    Groq = None

try:
    from openai import OpenAI
except:
    OpenAI = None

try:
    import anthropic
except:
    anthropic = None

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Multi-LLM Hub",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Multi-LLM Hub")
st.caption("Groq • Hugging Face • OpenAI • Anthropic • Azure • Ollama")

# =====================================================
# SESSION STATE
# =====================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================================
# SECRETS DIAGNOSTICS (IMPORTANT)
# =====================================================
st.sidebar.header("🔑 API Keys Status")

secrets = st.secrets.to_dict()

def has(key):
    return key in secrets and secrets[key] != ""

providers = {}

if has("GROQ_API_KEY"):
    st.sidebar.success("Groq key loaded")
    providers["Groq"] = ["llama-3.1-8b-instant"]
else:
    st.sidebar.warning("Groq key missing")

if has("HF_API_KEY"):
    st.sidebar.success("Hugging Face key loaded")
    providers["Hugging Face"] = ["meta-llama/Llama-3.1-8B-Instruct"]
else:
    st.sidebar.warning("Hugging Face key missing")

if has("OPENAI_API_KEY"):
    st.sidebar.success("OpenAI key loaded")
    providers["OpenAI"] = ["gpt-4o-mini"]
else:
    st.sidebar.warning("OpenAI key missing")

if has("ANTHROPIC_API_KEY"):
    st.sidebar.success("Anthropic key loaded")
    providers["Anthropic"] = ["claude-3-haiku-20240307"]
else:
    st.sidebar.warning("Anthropic key missing")

if has("AZURE_OPENAI_KEY"):
    st.sidebar.success("Azure OpenAI key loaded")
    providers["Azure OpenAI"] = [secrets.get("AZURE_OPENAI_DEPLOYMENT", "deployment")]
else:
    st.sidebar.warning("Azure OpenAI key missing")

# Ollama always available
providers["Ollama (Local)"] = ["llama3", "mistral", "phi3"]

# =====================================================
# PROVIDER SELECTION
# =====================================================
provider = st.sidebar.selectbox(
    "Select LLM Provider",
    list(providers.keys())
)

model = st.sidebar.selectbox(
    "Select Model",
    providers[provider]
)

# =====================================================
# PROMPT
# =====================================================
prompt = st.text_area(
    "Enter your prompt",
    height=150,
    placeholder="Ask anything..."
)

# =====================================================
# QUERY FUNCTIONS
# =====================================================
def query_groq(prompt):
    client = Groq(api_key=secrets["GROQ_API_KEY"])
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return r.choices[0].message.content

def query_hf(prompt):
    r = requests.post(
        "https://router.huggingface.co/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {secrets['HF_API_KEY']}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 150
        },
        timeout=60
    )
    return r.json()["choices"][0]["message"]["content"]

def query_openai(prompt):
    client = OpenAI(api_key=secrets["OPENAI_API_KEY"])
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return r.choices[0].message.content

def query_anthropic(prompt):
    client = anthropic.Anthropic(api_key=secrets["ANTHROPIC_API_KEY"])
    r = client.messages.create(
        model=model,
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )
    return r.content[0].text

def query_azure(prompt):
    client = OpenAI(
        api_key=secrets["AZURE_OPENAI_KEY"],
        base_url=f"{secrets['AZURE_OPENAI_ENDPOINT']}/openai/deployments/{secrets['AZURE_OPENAI_DEPLOYMENT']}",
        default_headers={"api-key": secrets["AZURE_OPENAI_KEY"]}
    )
    r = client.chat.completions.create(
        model=secrets["AZURE_OPENAI_DEPLOYMENT"],
        messages=[{"role": "user", "content": prompt}]
    )
    return r.choices[0].message.content

def query_ollama(prompt):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=60
    )
    return r.json().get("response", "No response")

# =====================================================
# EXECUTE
# =====================================================
if st.button("🚀 Generate"):
    if not prompt.strip():
        st.warning("Enter a prompt")
    else:
        with st.spinner("Thinking..."):
            try:
                if provider == "Groq":
                    result = query_groq(prompt)
                elif provider == "Hugging Face":
                    result = query_hf(prompt)
                elif provider == "OpenAI":
                    result = query_openai(prompt)
                elif provider == "Anthropic":
                    result = query_anthropic(prompt)
                elif provider == "Azure OpenAI":
                    result = query_azure(prompt)
                else:
                    result = query_ollama(prompt)

                st.success(result)

            except Exception as e:
                st.error(f"❌ {e}")
