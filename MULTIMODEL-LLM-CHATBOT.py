# MULTI-MODEL LLM CHATBOT — FINAL WINDOWS FIX
# Uses Ollama CLI correctly via subprocess

import streamlit as st
import subprocess

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
# Ollama CLI Call (CORRECT)
# ---------------------------------
def call_ollama_cli(model, prompt):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False   # allow error capture
    )

    if result.returncode != 0:
        return f"❌ Ollama error:\n{result.stderr}"

    return result.stdout.strip()

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
            reply = call_ollama_cli(model_name, user_input)

            if not reply:
                reply = "❌ Ollama returned empty output (unexpected)."

            st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
