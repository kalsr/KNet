

# python
import streamlit as st
import requests

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(page_title="Menu Driven 10 LLMs",
                   layout="wide")

# ------------------------------------------------------------
# TITLE BAR – PROFESSIONAL HEADER
# ------------------------------------------------------------
st.markdown("""
    <div style='background-color:#222;padding:18px;border-radius:8px'>
        <h1 style='color:white;text-align:center;font-weight:bold;'>
            Menu-Driven 10-LLM Demo Application
        </h1>
        <h3 style='color:#FFD700;text-align:center;'>
            Designed by Randy Singh — KNet Consulting Group
        </h3>
    </div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# BUTTON COLORS FOR 10 LLMs
# ------------------------------------------------------------
llm_colors = {
    "OpenAI GPT-4.1": "#4CAF50",
    "Anthropic Claude 3": "#2196F3",
    "Google Gemini 1.5": "#9C27B0",
    "Groq Llama-3": "#E91E63",
    "Mistral Large": "#FF5722",
    "Cohere Command-R": "#795548",
    "DeepSeek R1": "#3F51B5",
    "Perplexity Sonar": "#009688",
    "LLaMA (HF API)": "#607D8B",
    "Falcon (HF API)": "#8BC34A",
}

llm_list = list(llm_colors.keys())

# ------------------------------------------------------------
# SESSION STATE INIT
# ------------------------------------------------------------
if "active_llm" not in st.session_state:
    st.session_state.active_llm = None

if "messages" not in st.session_state:
    st.session_state.messages = []


# ------------------------------------------------------------
# TOP BUTTON BAR FOR 10 LLMs
# ------------------------------------------------------------
cols = st.columns(10)
for i, llm_name in enumerate(llm_list):
    with cols[i]:
        if st.button(llm_name, use_container_width=True,
                     key=f"btn_{i}",
                     help=f"Open {llm_name} chat interface",
                     type="secondary"):
            st.session_state.active_llm = llm_name
            st.session_state.messages = []
            st.experimental_rerun()

# If no LLM selected, show message
if not st.session_state.active_llm:
    st.info("⬆ Select any LLM from above menu to begin.")
    st.stop()


# ------------------------------------------------------------
# FUNCTION: REAL API CALLS
# ------------------------------------------------------------
def call_llm_api(provider, prompt):
    try:

        # ---------------------- OPENAI ----------------------
        if provider == "OpenAI GPT-4.1":
            headers = {"Authorization": f"Bearer {st.secrets.OPENAI_API_KEY}"}
            data = {
                "model": "gpt-4.1-mini",
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers, json=data)
            return response.json()["choices"][0]["message"]["content"]

        # ---------------------- ANTHROPIC ----------------------
        if provider == "Anthropic Claude 3":
            headers = {
                "x-api-key": st.secrets.ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01"
            }
            data = {
                "model": "claude-3-sonnet-20240229",
                "max_tokens": 300,
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers=headers, json=data)
            return response.json()["content"][0]["text"]

        # ---------------------- GEMINI ----------------------
        if provider == "Google Gemini 1.5":
            api_key = st.secrets.GEMINI_API_KEY
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            data = {"contents": [{"parts": [{"text": prompt}]}]}
            response = requests.post(url, json=data)
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]

        # ---------------------- GROQ ----------------------
        if provider == "Groq Llama-3":
            headers = {"Authorization": f"Bearer {st.secrets.GROQ_API_KEY}"}
            data = {
                "model": "llama3-70b-8192",
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers, json=data)
            return response.json()["choices"][0]["message"]["content"]

        # ---------------------- MISTRAL ----------------------
        if provider == "Mistral Large":
            headers = {"Authorization": f"Bearer {st.secrets.MISTRAL_API_KEY}"}
            data = {
                "model": "mistral-large-latest",
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post(
                "https://api.mistral.ai/v1/chat/completions",
                headers=headers, json=data)
            return response.json()["choices"][0]["message"]["content"]

        # ---------------------- COHERE ----------------------
        if provider == "Cohere Command-R":
            headers = {"Authorization": f"Bearer {st.secrets.COHERE_API_KEY}"}
            data = {"model": "command-r", "messages": [{"role": "user", "content": prompt}]}
            response = requests.post(
                "https://api.cohere.ai/v1/chat",
                headers=headers, json=data)
            return response.json()["text"]

        # ---------------------- DEEPSEEK ----------------------
        if provider == "DeepSeek R1":
            headers = {"Authorization": f"Bearer {st.secrets.DEEPSEEK_API_KEY}"}
            data = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post(
                "https://api.deepseek.com/chat/completions",
                headers=headers, json=data)
            return response.json()["choices"][0]["message"]["content"]

        # ---------------------- PERPLEXITY ----------------------
        if provider == "Perplexity Sonar":
            headers = {"Authorization": f"Bearer {st.secrets.PERPLEXITY_API_KEY}"}
            data = {
                "model": "sonar-medium-online",
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post(
                "https://api.perplexity.ai/chat/completions",
                headers=headers, json=data)
            return response.json()["choices"][0]["message"]["content"]

        # ---------------------- DUMMY HF MODELS ----------------------
        if provider == "LLaMA (HF API)" or provider == "Falcon (HF API)":
            return "This is a placeholder. Add HF Inference API if required."

    except Exception as e:
        return f"API Error: {str(e)}"


# ------------------------------------------------------------
# LLM CHAT WINDOW
# ------------------------------------------------------------
st.markdown(f"### 💬 Chat with **{st.session_state.active_llm}**")

# Display chat history
for msg in st.session_state.messages:
    role, text = msg["role"], msg["content"]
    if role == "user":
        st.markdown(f"**🧑 You:** {text}")
    else:
        st.markdown(f"**🤖 {st.session_state.active_llm}:** {text}")

# User input
prompt = st.text_input("Enter your message:", key="chat_input")

# Send
if st.button("Send"):
    if prompt.strip():
        st.session_state.messages.append({"role": "user", "content": prompt})
        reply = call_llm_api(st.session_state.active_llm, prompt)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.experimental_rerun()

# Exit
if st.button("Exit to Menu"):
    st.session_state.active_llm = None
    st.session_state.messages = []
    st.experimental_rerun()

# Clear Chat
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()
