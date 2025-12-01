# menu_10_llms_placeholder.py
import streamlit as st
import requests
import json
from html import escape

st.set_page_config(page_title="Menu Driven 10 LLMs", layout="wide")

# -------------------------
# PROFESSIONAL HEADER
# -------------------------
st.markdown("""
<div style='background:#0b1b2b;padding:18px;border-radius:8px;margin-bottom:12px'>
  <h1 style='color:#fff;text-align:center;margin:0;font-weight:800'>Menu-Driven 10-LLM Demo</h1>
  <h4 style='color:#cfe8ff;text-align:center;margin:6px 0 0 0'>Designed by Randy Singh — KNet Consulting Group</h4>
</div>
""", unsafe_allow_html=True)

# -------------------------
# LLM list & unique colors
# -------------------------
LLMS = [
    "OpenAI GPT-4.1",
    "Anthropic Claude 3",
    "Google Gemini 1.5",
    "Groq Llama-3",
    "Mistral Large",
    "Cohere Command-R",
    "DeepSeek R1",
    "Perplexity Sonar",
    "LLaMA (HF API)",
    "Falcon (HF API)"
]

LLM_COLORS = {
    "OpenAI GPT-4.1": "#1f8ef1",
    "Anthropic Claude 3": "#7c4dff",
    "Google Gemini 1.5": "#0f9d58",
    "Groq Llama-3": "#ff5c8a",
    "Mistral Large": "#ff7f50",
    "Cohere Command-R": "#006d6d",
    "DeepSeek R1": "#3f51b5",
    "Perplexity Sonar": "#009688",
    "LLaMA (HF API)": "#607d8b",
    "Falcon (HF API)": "#8bc34a"
}

# -------------------------
# Initialize session state
# -------------------------
if "active_llm" not in st.session_state:
    st.session_state.active_llm = None
if "messages" not in st.session_state:
    st.session_state.messages = []  # list of {"role":"user"/"assistant", "content":...}

# -------------------------
# Render top colored buttons (HTML form GET approach)
# -------------------------
st.markdown("### Select an LLM to open")
cols = st.columns(10)
for i, llm in enumerate(LLMS):
    with cols[i]:
        button_html = f"""
        <form action="/" method="get">
            <button style="
                background-color:{LLM_COLORS[llm]};
                color:white;
                width:100%;
                height:56px;
                border-radius:8px;
                border:none;
                font-weight:700;
                cursor:pointer;
            " name="llm" value="{escape(llm)}">{escape(llm)}</button>
        </form>
        """
        st.markdown(button_html, unsafe_allow_html=True)

# -------------------------
# Detect clicked LLM via query params
# -------------------------
q = st.experimental_get_query_params()
if "llm" in q:
    chosen = q["llm"][0]
    if chosen in LLMS:
        # When user changes selection, reset messages
        if st.session_state.active_llm != chosen:
            st.session_state.active_llm = chosen
            st.session_state.messages = []

# If no LLM selected, show helpful info and stop
if not st.session_state.active_llm:
    st.markdown("---")
    st.info("Click any colored button above to open that LLM's chat screen. Use Exit to return to menu.")
    st.stop()

# -------------------------
# Helper: friendly missing-key message
# -------------------------
def missing_key_message(provider_name, secret_name):
    return (f"**API key missing for {provider_name}.** Add `{secret_name}` in `.streamlit/secrets.toml` "
            "or in Streamlit Cloud secrets. The UI will work; the model needs a key to return real results.")

# -------------------------
# Per-provider callers (use st.secrets; return string)
# Keep implementation generic and safe to run with placeholders.
# -------------------------
def call_openai(prompt, model="gpt-4o-mini"):
    key = st.secrets.get("OPENAI_API_KEY")
    if not key:
        return missing_key_message("OpenAI", "OPENAI_API_KEY")
    try:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {key}", "Content-Type":"application/json"}
        payload = {"model": model, "messages":[{"role":"user","content":prompt}], "max_tokens":512}
        res = requests.post(url, headers=headers, json=payload, timeout=60)
        if res.status_code != 200:
            return f"OpenAI API Error {res.status_code}: {res.text}"
        j = res.json()
        return j["choices"][0]["message"]["content"]
    except Exception as e:
        return f"OpenAI call failed: {e}"

def call_anthropic(prompt):
    key = st.secrets.get("sk-ant-api03-G0w...wAAA")
    if not key:
        return missing_key_message("Anthropic", "sk-ant-api03-G0w...wAAA")
    try:
        url = "https://api.anthropic.com/v1/complete"  # some Anthropic APIs use different endpoints
        headers = {"x-api-key": key, "Content-Type":"application/json"}
        payload = {"model":"claude-3-opus-2024-10-07", "prompt": prompt, "max_tokens":512}
        res = requests.post(url, headers=headers, json=payload, timeout=60)
        if res.status_code != 200:
            return f"Anthropic API Error {res.status_code}: {res.text}"
        j = res.json()
        # extraction depends on API shape; try common fields
        return j.get("completion") or j.get("text") or str(j)
    except Exception as e:
        return f"Anthropic call failed: {e}"

def call_gemini(prompt):
    key = st.secrets.get("GEMINI_API_KEY")
    if not key:
        return missing_key_message("Google Gemini", "GEMINI_API_KEY")
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={key}"
        payload = {"prompt":{"messages":[{"author":"user","content":[{"type":"text","text":prompt}]}]}, "temperature":0.2}
        res = requests.post(url, json=payload, timeout=60)
        if res.status_code != 200:
            return f"Gemini API Error {res.status_code}: {res.text}"
        j = res.json()
        # Attempt to extract candidate text
        try:
            return j["candidates"][0]["content"][0]["text"]
        except Exception:
            return str(j)
    except Exception as e:
        return f"Gemini call failed: {e}"

def call_groq(prompt):
    key = st.secrets.get("GROQ_API_KEY")
    if not key:
        return missing_key_message("Groq", "GROQ_API_KEY")
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"  # common mapping
        headers = {"Authorization": f"Bearer {key}", "Content-Type":"application/json"}
        payload = {"model":"llama3-70b-8192","messages":[{"role":"user","content":prompt}]}
        res = requests.post(url, headers=headers, json=payload, timeout=60)
        if res.status_code != 200:
            return f"Groq API Error {res.status_code}: {res.text}"
        j = res.json()
        return j["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Groq call failed: {e}"

def call_mistral(prompt):
    key = st.secrets.get("MISTRAL_API_KEY")
    if not key:
        return missing_key_message("Mistral", "MISTRAL_API_KEY")
    try:
        url = "https://api.mistral.ai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {key}", "Content-Type":"application/json"}
        payload = {"model":"mistral-large", "messages":[{"role":"user","content":prompt}]}
        res = requests.post(url, headers=headers, json=payload, timeout=60)
        if res.status_code != 200:
            return f"Mistral API Error {res.status_code}: {res.text}"
        j = res.json()
        return j["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Mistral call failed: {e}"

def call_cohere(prompt):
    key = st.secrets.get("COHERE_API_KEY")
    if not key:
        return missing_key_message("Cohere", "COHERE_API_KEY")
    try:
        url = "https://api.cohere.ai/v1/generate"
        headers = {"Authorization": f"Bearer {key}", "Content-Type":"application/json"}
        payload = {"model":"command","prompt":prompt,"max_tokens":256}
        res = requests.post(url, headers=headers, json=payload, timeout=60)
        if res.status_code != 200:
            return f"Cohere API Error {res.status_code}: {res.text}"
        j = res.json()
        if "generations" in j and j["generations"]:
            return j["generations"][0].get("text","")
        return str(j)
    except Exception as e:
        return f"Cohere call failed: {e}"

def call_deepseek(prompt):
    key = st.secrets.get("DEEPSEEK_API_KEY")
    if not key:
        return missing_key_message("DeepSeek", "DEEPSEEK_API_KEY")
    try:
        url = "https://api.deepseek.com/v1/chat"
        headers = {"Authorization": f"Bearer {key}", "Content-Type":"application/json"}
        payload = {"model":"deepseek-chat","messages":[{"role":"user","content":prompt}]}
        res = requests.post(url, headers=headers, json=payload, timeout=60)
        if res.status_code != 200:
            return f"DeepSeek API Error {res.status_code}: {res.text}"
        j = res.json()
        if "choices" in j and j["choices"]:
            return j["choices"][0].get("message",{}).get("content","")
        return str(j)
    except Exception as e:
        return f"DeepSeek call failed: {e}"

def call_perplexity(prompt):
    key = st.secrets.get("PERPLEXITY_API_KEY")
    if not key:
        return missing_key_message("Perplexity", "PERPLEXITY_API_KEY")
    try:
        url = "https://api.perplexity.ai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {key}", "Content-Type":"application/json"}
        payload = {"model":"sonar-medium-online","messages":[{"role":"user","content":prompt}]}
        res = requests.post(url, headers=headers, json=payload, timeout=60)
        if res.status_code != 200:
            return f"Perplexity API Error {res.status_code}: {res.text}"
        j = res.json()
        if "choices" in j and j["choices"]:
            return j["choices"][0].get("message",{}).get("content","")
        return str(j)
    except Exception as e:
        return f"Perplexity call failed: {e}"

def call_hf(prompt, repo="gpt2"):
    key = st.secrets.get("HF_API_KEY")
    if not key:
        return missing_key_message("Hugging Face", "HF_API_KEY")
    try:
        url = f"https://api-inference.huggingface.co/models/{repo}"
        headers = {"Authorization": f"Bearer {key}"}
        payload = {"inputs": prompt, "options":{"wait_for_model":True}}
        res = requests.post(url, headers=headers, json=payload, timeout=120)
        if res.status_code != 200:
            return f"Hugging Face Error {res.status_code}: {res.text}"
        out = res.json()
        if isinstance(out, list) and "generated_text" in out[0]:
            return out[0]["generated_text"]
        return json.dumps(out)
    except Exception as e:
        return f"Hugging Face call failed: {e}"

def call_llama(prompt):
    key = st.secrets.get("LLAMA_API_KEY")
    if not key:
        return missing_key_message("Meta Llama", "LLAMA_API_KEY")
    try:
        url = "https://api.meta-llama.com/v1/chat/completions"  # hypothetical
        headers = {"Authorization": f"Bearer {key}", "Content-Type":"application/json"}
        payload = {"model":"llama-3","messages":[{"role":"user","content":prompt}]}
        res = requests.post(url, headers=headers, json=payload, timeout=60)
        if res.status_code != 200:
            return f"Llama API Error {res.status_code}: {res.text}"
        j = res.json()
        return j["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Llama call failed: {e}"

# -------------------------
# Router: choose correct caller
# -------------------------
def execute_llm(llm_name, prompt):
    if llm_name == "OpenAI GPT-4.1":
        return call_openai(prompt)
    if llm_name == "Anthropic Claude 3":
        return call_anthropic(prompt)
    if llm_name == "Google Gemini 1.5":
        return call_gemini(prompt)
    if llm_name == "Groq Llama-3":
        return call_groq(prompt)
    if llm_name == "Mistral Large":
        return call_mistral(prompt)
    if llm_name == "Cohere Command-R":
        return call_cohere(prompt)
    if llm_name == "DeepSeek R1":
        return call_deepseek(prompt)
    if llm_name == "Perplexity Sonar":
        return call_perplexity(prompt)
    if llm_name == "LLaMA (HF API)":
        # default repo; change later if you wish
        return call_hf(prompt, repo="meta-llama/Llama-2-7b-chat")
    if llm_name == "Falcon (HF API)":
        return call_hf(prompt, repo="tiiuae/falcon-7b-instruct")
    return "No mapping for this LLM."

# -------------------------
# Chat UI for active LLM
# -------------------------
st.markdown("---")
st.markdown(f"## 💬 Chat — **{st.session_state.active_llm}**")
st.markdown("<small>Type your prompt below and press Send. If a provider key is not set you will see a friendly instruction message.</small>", unsafe_allow_html=True)

# show previous messages
if st.session_state.messages:
    for m in st.session_state.messages:
        role = m.get("role")
        c = m.get("content")
        if role == "user":
            st.markdown(f"**🧑 You:** {escape(c)}")
        else:
            st.markdown(f"**🤖 {st.session_state.active_llm}:** {c}")

prompt = st.text_area("Enter your prompt here:", height=200)

c1, c2, c3 = st.columns([1,1,1])
with c1:
    if st.button("Send"):
        if not prompt or prompt.strip()=="":
            st.warning("Please enter a prompt first.")
        else:
            st.session_state.messages.append({"role":"user","content":prompt})
            with st.spinner("Calling model..."):
                reply = execute_llm(st.session_state.active_llm, prompt)
            st.session_state.messages.append({"role":"assistant","content":reply})
            # Show reply immediately (no rerun required)

with c2:
    if st.button("Clear Chat"):
        st.session_state.messages = []

with c3:
    if st.button("Exit to Menu"):
        # clear query param and session selection
        st.experimental_set_query_params()
        st.session_state.active_llm = None
        st.session_state.messages = []
        st.experimental_rerun()

st.markdown("---")
st.markdown("<small>To enable a provider: add its API key into `.streamlit/secrets.toml` or Streamlit Cloud secrets and restart the app.</small>", unsafe_allow_html=True)

