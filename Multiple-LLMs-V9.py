

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
    page_title="Enterprise Multi-LLM Hub",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Enterprise Multi-LLM Hub")
st.caption("Groq • Hugging Face Router • OpenRouter • OpenAI • Anthropic • Azure • Ollama")

# =====================================================
# SESSION STATE
# =====================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================================
# SECRETS
# =====================================================
secrets = st.secrets.to_dict()

def has(k): return k in secrets and secrets[k]

# =====================================================
# SIDEBAR – PROVIDERS
# =====================================================
st.sidebar.header("🔑 Provider Status")

providers = {}

if has("GROQ_API_KEY"):
    st.sidebar.success("Groq ✔")
    providers["Groq"] = ["llama-3.1-8b-instant"]

if has("HF_API_KEY"):
    st.sidebar.success("Hugging Face Router ✔")
    providers["Hugging Face"] = [
        "NousResearch/Hermes-3-Llama-3.1-8B"
    ]

if has("OPENROUTER_API_KEY"):
    st.sidebar.success("OpenRouter ✔")
    providers["OpenRouter"] = [
        "nousresearch/hermes-3-llama-3.1-8b",
        "mistralai/mistral-7b-instruct",
        "meta-llama/llama-3.1-8b-instruct"
    ]

if has("OPENAI_API_KEY"):
    st.sidebar.success("OpenAI ✔")
    providers["OpenAI"] = ["gpt-4o-mini"]

if has("ANTHROPIC_API_KEY"):
    st.sidebar.success("Anthropic ✔")
    providers["Anthropic"] = ["claude-3-haiku-20240307"]

if has("AZURE_OPENAI_KEY"):
    st.sidebar.success("Azure OpenAI ✔")
    providers["Azure OpenAI"] = [secrets["AZURE_OPENAI_DEPLOYMENT"]]

providers["Ollama (Local)"] = ["llama3", "mistral", "phi3"]

# =====================================================
# SELECTION
# =====================================================
provider = st.sidebar.selectbox("Select Provider", list(providers.keys()))
model = st.sidebar.selectbox("Select Model", providers[provider])

prompt = st.text_area("Enter prompt", height=160)

# =====================================================
# QUERY FUNCTIONS
# =====================================================
def hf_router(prompt, model):
    r = requests.post(
        "https://router.huggingface.co/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {secrets['HF_API_KEY']}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 256
        },
        timeout=60
    )
    data = r.json()
    if "error" in data:
        raise RuntimeError(data["error"])
    return data["choices"][0]["message"]["content"]

def openrouter(prompt, model):
    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {secrets['OPENROUTER_API_KEY']}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 256
        },
        timeout=60
    )
    return r.json()["choices"][0]["message"]["content"]

def groq(prompt):
    return Groq(api_key=secrets["GROQ_API_KEY"])\
        .chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        ).choices[0].message.content

def openai_llm(prompt):
    return OpenAI(api_key=secrets["OPENAI_API_KEY"])\
        .chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        ).choices[0].message.content

def anthropic_llm(prompt):
    return anthropic.Anthropic(api_key=secrets["ANTHROPIC_API_KEY"])\
        .messages.create(
            model=model,
            max_tokens=256,
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

def ollama(prompt):
    return requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False}
    ).json().get("response")

# =====================================================
# EXECUTION (WITH HF → OPENROUTER FALLBACK)
# =====================================================
if st.button("🚀 Generate"):
    if not prompt.strip():
        st.warning("Enter a prompt")
    else:
        with st.spinner("Thinking..."):
            try:
                if provider == "Hugging Face":
                    try:
                        result = hf_router(prompt, model)
                    except Exception:
                        st.warning("HF Router failed → falling back to OpenRouter")
                        result = openrouter(prompt, "nousresearch/hermes-3-llama-3.1-8b")

                elif provider == "OpenRouter":
                    result = openrouter(prompt, model)

                elif provider == "Groq":
                    result = groq(prompt)

                elif provider == "OpenAI":
                    result = openai_llm(prompt)

                elif provider == "Anthropic":
                    result = anthropic_llm(prompt)

                elif provider == "Azure OpenAI":
                    result = azure_llm(prompt)

                else:
                    result = ollama(prompt)

                st.success(result)

            except Exception as e:
                st.error(f"❌ {e}")
