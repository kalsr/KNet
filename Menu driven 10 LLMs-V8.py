import streamlit as st
import requests

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(page_title="Menu Driven 10 LLMs", layout="wide")

# ============================================================
# TITLE BAR
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
# LLM CONFIGURATION
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
# TOP MENU BUTTONS WITH UNIQUE COLORS
# ============================================================
st.markdown("### Select an LLM:")
cols = st.columns(10)

for idx, llm_name in enumerate(llm_list):
    with cols[idx]:
        button_clicked = st.button(
            llm_name,
            key=f"llm_btn_{idx}",
        )
        # Inject button colors via CSS
        st.markdown(f"""
            <style>
            div.stButton > button#{st.session_state.get(f"llm_btn_{idx}", '')} {{
                background-color: {llm_colors[llm_name]};
                color: white;
                font-weight: bold;
                border-radius: 10px;
            }}
            </style>
        """, unsafe_allow_html=True)
        if button_clicked:
            st.session_state.active_llm = llm_name
            st.session_state.messages = []
            st.rerun()  # <-- NEW, safe rerun

# ============================================================
# EXIT IF NO LLM SELECTED
# ============================================================
if not st.session_state.active_llm:
    st.info("⬆ Select any LLM above to begin chatting.")
    st.stop()

# ============================================================
# REAL API CALL PLACEHOLDER
# ============================================================
def call_llm_api(provider, prompt):
    try:
        # Replace these placeholders with real API calls
        if provider == "OpenAI GPT-4.1":
            headers = {"Authorization": f"Bearer {st.secrets.OPENAI_API_KEY}"}
            data = {
                "model": "gpt-4.1-mini",
                "messages": [{"role": "user", "content": prompt}]
            }
            r = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data
            )
            return r.json()["choices"][0]["message"]["content"]

        # Placeholder for other LLMs
        return f"[{provider}] Response for: {prompt}"

    except Exception as e:
        return f"API Error: {str(e)}"

# ============================================================
# CHAT INTERFACE
# ============================================================
st.markdown(f"## 💬 Chat with **{st.session_state.active_llm}**")

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 {st.session_state.active_llm}:** {msg['content']}")

# User input
prompt = st.text_input("Enter your message:")

# SEND BUTTON
if st.button("Send"):
    if prompt.strip():
        st.session_state.messages.append({"role": "user", "content": prompt})
        reply = call_llm_api(st.session_state.active_llm, prompt)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()  # <-- safe rerun

# CLEAR CHAT
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# EXIT TO MENU
if st.button("Exit to Menu"):
    st.session_state.active_llm = None
    st.session_state.messages = []
    st.rerun()
