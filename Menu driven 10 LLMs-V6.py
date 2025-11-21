


### `menu_driven_10_llms.py`

# python
import streamlit as st
import requests


# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Menu Driven 10 LLMs",
    layout="wide"
)


# ============================================================
# PROFESSIONAL TITLE BAR
# ============================================================
st.markdown("""
    <div style='background-color:#222;padding:20px;border-radius:10px'>
        <h1 style='color:white;text-align:center;font-weight:bold;'>
            Menu Driven 10-LLM Demo Application
        </h1>
        <h3 style='color:#FFD700;text-align:center;'>
            Designed by Randy Singh — KNet Consulting Group
        </h3>
    </div>
""", unsafe_allow_html=True)


# ============================================================
# LLM COLOR PALETTE (10 UNIQUE COLORS)
# ============================================================
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


# ============================================================
# SESSION STATE INITIALIZATION
# ============================================================
if "active_llm" not in st.session_state:
    st.session_state.active_llm = None

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# TOP MENU BUTTONS (WITH UNIQUE COLORS)
# ============================================================
cols = st.columns(10)

for idx, llm_name in enumerate(llm_list):
    with cols[idx]:

        # Custom CSS for each button
        st.markdown(f"""
            <style>
            div.stButton > button#llm_{idx} {{
                background-color: {llm_colors[llm_name]} !important;
                color: white !important;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
            }}
            div.stButton > button#llm_{idx}:hover {{
                opacity: 0.85;
            }}
            </style>
        """, unsafe_allow_html=True)

        if st.button(llm_name, key=f"llm_{idx}", use_container_width=True):
            st.session_state.active_llm = llm_name
            st.session_state.messages = []
            st.rerun()


# If user has not selected an LLM yet
if not st.session_state.active_llm:
    st.info("⬆ Select any LLM above to begin chatting.")
    st.stop()


# ============================================================
# REAL API CALL HANDLER FOR EACH LLM
# ============================================================
def call_llm_api(provider, prompt):
    try:

        # 1 — OpenAI GPT-4.1
        if provider == "OpenAI GPT-4.1":
            headers = {"Authorization": f"Bearer {st.secrets.OPENAI_API_KEY}"}
            data = {
                "model": "gpt-4.1-mini",
                "messages": [{"role": "user", "content": prompt}]
            }
            r = requests.post("https://api.openai.com/v1/chat/completions",
                              headers=headers, json=data)
            return r.json()["choices"][0]["message"]["content"]

        # 2 — Claude 3 (Anthropic)
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
            r = requests.post("https://api.anthropic.com/v1/messages",
                              headers=headers, json=data)
            return r.json()["content"][0]["text"]

        # 3 — Google Gemini
        if provider == "Google Gemini 1.5":
            api_key = st.secrets.GEMINI_API_KEY
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            data = {"contents": [{"parts": [{"text": prompt}]}]}
            r = requests.post(url, json=data)
            return r.json()["candidates"][0]["content"]["parts"][0]["text"]

        # 4 — Groq Llama-3
        if provider == "Groq Llama-3":
            headers = {"Authorization": f"Bearer {st.secrets.GROQ_API_KEY}"}
            data = {
                "model": "llama3-70b-8192",
                "messages": [{"role": "user", "content": prompt}]
            }
            r = requests.post("https://api.groq.com/openai/v1/chat/completions",
                              headers=headers, json=data)
            return r.json()["choices"][0]["message"]["content"]

        # 5 — Mistral
        if provider == "Mistral Large":
            headers = {"Authorization": f"Bearer {st.secrets.MISTRAL_API_KEY}"}
            data = {
                "model": "mistral-large-latest",
                "messages": [{"role": "user", "content": prompt}]
            }
            r = requests.post("https://api.mistral.ai/v1/chat/completions",
                              headers=headers, json=data)
            return r.json()["choices"][0]["message"]["content"]

        # 6 — Cohere
        if provider == "Cohere Command-R":
            headers = {"Authorization": f"Bearer {st.secrets.COHERE_API_KEY}"}
            data = {
                "model": "command-r",
                "messages": [{"role": "user", "content": prompt}]
            }
            r = requests.post("https://api.cohere.ai/v1/chat",
                              headers=headers, json=data)
            return r.json()["text"]

        # 7 — DeepSeek
        if provider == "DeepSeek R1":
            headers = {"Authorization": f"Bearer {st.secrets.DEEPSEEK_API_KEY}"}
            data = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}]
            }
            r = requests.post("https://api.deepseek.com/chat/completions",
                              headers=headers, json=data)
            return r.json()["choices"][0]["message"]["content"]

        # 8 — Perplexity Sonar
        if provider == "Perplexity Sonar":
            headers = {"Authorization": f"Bearer {st.secrets.PERPLEXITY_API_KEY}"}
            data = {
                "model": "sonar-medium-online",
                "messages": [{"role": "user", "content": prompt}]
            }
            r = requests.post("https://api.perplexity.ai/chat/completions",
                              headers=headers, json=data)
            return r.json()["choices"][0]["message"]["content"]

        # 9 & 10 — HF Placeholder
        return "This model uses HuggingFace Inference API. Add HF key to enable."

    except Exception as e:
        return f"API Error: {str(e)}"


# ============================================================
# CHAT INTERFACE AREA
# ============================================================
st.markdown(f"## 💬 Chat with **{st.session_state.active_llm}**")

# Display previous chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 {st.session_state.active_llm}:** {msg['content']}")


# User message input
prompt = st.text_input("Enter your message:")

# SEND BUTTON
if st.button("Send"):
    if prompt.strip():
        st.session_state.messages.append({"role": "user", "content": prompt})
        reply = call_llm_api(st.session_state.active_llm, prompt)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

# CLEAR CHAT
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# EXIT TO MENU
if st.button("Exit to Menu"):
    st.session_state.active_llm = None
    st.session_state.messages = []
    st.rerun()
