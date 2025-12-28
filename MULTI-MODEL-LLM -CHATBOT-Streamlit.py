import streamlit as st
import subprocess

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Multi-Model LLM Chatbot (Ollama)",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Multi-Model LLM Chatbot")
st.caption("Local Ollama models • No API keys • Windows safe")

# --------------------------------------------------
# AVAILABLE MODELS
# --------------------------------------------------
MODELS = ["llama3", "mistral", "phi", "gemma", "llama2"]

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "model" not in st.session_state:
    st.session_state.model = MODELS[0]

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# SIDEBAR (MODEL SELECTION = EXIT + RESTART)
# --------------------------------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    selected_model = st.selectbox(
        "Select LLM Model",
        MODELS,
        index=MODELS.index(st.session_state.model)
    )

    # If user switches model → reset chat (same as exiting old model)
    if selected_model != st.session_state.model:
        st.session_state.model = selected_model
        st.session_state.messages = []
        st.rerun()

    st.markdown(f"**Active Model:** `{st.session_state.model}`")

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.info("To fully exit, close the browser tab.")

# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --------------------------------------------------
# OLLAMA CLI CALL (UNICODE SAFE)
# --------------------------------------------------
def call_ollama(model, prompt):
    process = subprocess.Popen(
        ["ollama", "run", model],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, stderr = process.communicate(
        input=prompt.encode("utf-8")
    )

    if process.returncode != 0:
        return stderr.decode("utf-8", errors="ignore")

    return stdout.decode("utf-8", errors="ignore").strip()

# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------
user_input = st.chat_input(f"Message {st.session_state.model}...")

if user_input:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = call_ollama(st.session_state.model, user_input)

            if not reply:
                reply = "❌ Ollama returned empty output."

            st.markdown(reply)

    # Assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
