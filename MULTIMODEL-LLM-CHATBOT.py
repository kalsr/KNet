# MULTIMODEL LLM CHATBOT (WINDOWS-SAFE FIX)

import streamlit as st
import ollama
import time

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
# Try Connecting to Ollama (Graceful)
# ---------------------------------
def check_ollama():
    try:
        ollama.list()
        return True
    except Exception:
        return False

with st.spinner("Checking Ollama service..."):
    time.sleep(1)
    if not check_ollama():
        st.error(
            "❌ Ollama is not running.\n\n"
            "### Fix:\n"
            "1. Open **Start Menu → Ollama**\n"
            "2. OR run: `ollama serve`\n"
            "3. Refresh this page"
        )
        st.stop()

# ---------------------------------
# Sidebar – Model Selector
# ---------------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    model_name = st.selectbox(
        "Select LLM Model",
        ["llama3", "mistral", "phi", "gemma", "llama2"]
    )

    st.code(f"Active model: {model_name}")

    if st.button("🔄 Reset Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------------
# Session State
# ---------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

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
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model=model_name,
                messages=st.session_state.messages
            )
            reply = response["message"]["content"]
            st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
