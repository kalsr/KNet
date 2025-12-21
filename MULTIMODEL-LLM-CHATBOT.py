# MULTIMODEL LLM CHATBOT (FIXED OLLAMA CONNECTION)

import streamlit as st
import ollama
import requests

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Multi-Model LLM Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Multi-Model LLM Chatbot (Ollama)")
st.caption("ChatGPT-style interface with selectable local LLMs")

# ---------------------------------
# Check Ollama Server Health
# ---------------------------------
OLLAMA_HOST = "http://localhost:11434"

def ollama_is_running():
    try:
        r = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=2)
        return r.status_code == 200
    except Exception:
        return False

if not ollama_is_running():
    st.error(
        "❌ Ollama server is not reachable.\n\n"
        "Please make sure Ollama is running:\n"
        "`ollama serve`"
    )
    st.stop()

# Explicit Ollama client
client = ollama.Client(host=OLLAMA_HOST)

# ---------------------------------
# Sidebar – Model Selector
# ---------------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    model_name = st.selectbox(
        "Select LLM Model",
        [
            "llama3",
            "mistral",
            "phi",
            "gemma",
            "llama2"
        ]
    )

    st.markdown("**Active Model**")
    st.code(model_name)

    if st.button("🔄 Reset Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------------
# Initialize Session State
# ---------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_model" not in st.session_state:
    st.session_state.current_model = model_name

# Reset chat when model changes
if st.session_state.current_model != model_name:
    st.session_state.messages = []
    st.session_state.current_model = model_name
    st.rerun()

# ---------------------------------
# Display Chat History
# ---------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------------
# Chat Input
# ---------------------------------
user_input = st.chat_input(f"Message {model_name}...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner(f"{model_name} is thinking..."):
            try:
                response = client.chat(
                    model=model_name,
                    messages=st.session_state.messages
                )
                bot_reply = response["message"]["content"]

            except Exception as e:
                bot_reply = (
                    "❌ Failed to generate response.\n\n"
                    f"**Details:** {e}"
                )

            st.markdown(bot_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
