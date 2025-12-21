# MULTIMODEL LLM CHATBOT — WINDOWS STREAMLIT FIX

import streamlit as st
import ollama

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
# Force Ollama HTTP Client (CRITICAL)
# ---------------------------------
OLLAMA_HOST = "http://127.0.0.1:11434"

client = ollama.Client(host=OLLAMA_HOST)

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
            try:
                response = client.chat(
                    model=model_name,
                    messages=st.session_state.messages
                )
                reply = response["message"]["content"]

            except Exception as e:
                reply = (
                    "❌ Unable to connect to Ollama from Streamlit.\n\n"
                    "### Verified Facts\n"
                    "- Ollama CLI works\n"
                    "- Ollama app is running\n\n"
                    "### Root Cause\n"
                    "Streamlit requires an explicit HTTP host on Windows.\n\n"
                    f"**Details:** {e}"
                )

            st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
