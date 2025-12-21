import streamlit as st
import requests

# Optional LLM SDKs
try:
    from groq import Groq
except ImportError:
    Groq = None

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

try:
    import anthropic
except ImportError:
    anthropic = None

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Multi-LLM Hub",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Multi-LLM Hub")
st.subheader("Enterprise-Grade Unified LLM Interface")

# =========================================================
# VERIFY SECRETS
# =========================================================
available_secrets = list(st.secrets.keys())
st.sidebar.subheader("🔑 API Keys Status")
if "GROQ_API_KEY" in st.secrets:
    st.sidebar.success("Groq key loaded")
else:
    st.sidebar.warning("Groq key missing")

if "HF_API_KEY" in st.secrets:
    st.sidebar.success("Hugging Face key loaded")
else:
    st.sidebar.warning("Hugging Face key missing")

if "OPENAI_API_KEY" in st.secrets:
    st.sidebar.success("OpenAI key loaded")
else:
    st.sidebar.warning("OpenAI key missing")

if "ANTHROPIC_API_KEY" in st.secrets:
    st.sidebar.success("Anthropic key loaded")
else:
    st.sidebar.warning("Anthropic key missing")

if "AZURE_OPENAI_KEY" in st.secrets:
    st.sidebar.success("Azure OpenAI key loaded")
else:
    st.sidebar.warning("Azure OpenAI key missing")

# =========================================================
# PROVIDERS AND MODELS
# =========================================================
provider_map = {}
if "GROQ_API_KEY" in st.secrets and Groq is not None:
    provider_map["Groq"] = ["llama-3.1-8b-instant", "llama-3.1-16b-instant"]
if "HF_API_KEY" in st.secrets:
    provider_map["Hugging Face"] = ["mistralai/Mistral-7B-Instruct", "google/gemma-7b"]
provider_map["Ollama (Local)"] = ["llama3", "mistral", "phi3"]  # local only
if "OPENAI_API_KEY" in st.secrets:
    provider_map["OpenAI"] = ["gpt-4o-mini", "gpt-4o"]
if "ANTHROPIC_API_KEY" in st.secrets:
    provider_map["Anthropic"] = ["claude-3-haiku-20240307"]
if "AZURE_OPENAI_KEY" in st.secrets:
    provider_map["Azure OpenAI"] = ["gpt-4o"]

# Sidebar provider selection
provider = st.sidebar.selectbox(
    "Select LLM Provider",
    list(provider_map.keys())
)
model = st.sidebar.selectbox("Select Model", provider_map[provider])

# =========================================================
# PROMPT INPUT
# =========================================================
prompt = st.text_area(
    "Enter your prompt",
    height=200,
    placeholder="Ask anything…"
)

# =========================================================
# QUERY FUNCTIONS
# =========================================================
def query_groq(prompt, model):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        chat = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return chat.choices[0].message.content
    except Exception as e:
        return f"❌ Groq error: {e}"

def query_huggingface(prompt, model):
    hf_key = st.secrets.get("HF_API_KEY", "")
    if not hf_key:
        return "❌ Hugging Face API key missing"
    headers = {"Authorization": f"Bearer {hf_key}"}
    try:
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
    except Exception as e:
        return f"❌ Hugging Face error: {e}"

def query_openai(prompt, model):
    try:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"❌ OpenAI error: {e}"

def query_anthropic(prompt, model):
    try:
        client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
        msg = client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return msg.content[0].text
    except Exception as e:
        return f"❌ Anthropic error: {e}"

def query_azure_openai(prompt, model):
    try:
        client = OpenAI(
            api_key=st.secrets["AZURE_OPENAI_KEY"],
            base_url=f"{st.secrets['AZURE_OPENAI_ENDPOINT']}/openai/deployments/{st.secrets['AZURE_OPENAI_DEPLOYMENT']}",
            default_headers={"api-key": st.secrets["AZURE_OPENAI_KEY"]}
        )
        resp = client.chat.completions.create(
            model=st.secrets["AZURE_OPENAI_DEPLOYMENT"],
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"❌ Azure OpenAI error: {e}"

def query_ollama(prompt, model):
    try:
        r = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=60
        )
        return r.json().get("response", "No response from Ollama")
    except Exception as e:
        return f"❌ Ollama error: {e}"

# =========================================================
# GENERATE RESPONSE
# =========================================================
if st.button("🚀 Generate Response"):
    if not prompt.strip():
        st.warning("⚠️ Please enter a prompt")
    else:
        with st.spinner("🧠 Thinking..."):
            if provider == "Groq":
                result = query_groq(prompt, model)
            elif provider == "Hugging Face":
                result = query_huggingface(prompt, model)
            elif provider == "OpenAI":
                result = query_openai(prompt, model)
            elif provider == "Anthropic":
                result = query_anthropic(prompt, model)
            elif provider == "Azure OpenAI":
                result = query_azure_openai(prompt, model)
            else:
                result = query_ollama(prompt, model)

            st.markdown("### 💡 Model Response")
            st.success(result)
