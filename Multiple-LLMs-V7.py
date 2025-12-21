
import streamlit as st
import requests

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Hugging Face Router Chat",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Hugging Face Router Chat")
st.caption("Using meta-llama/Llama-3.1-8B-Instruct with Router API")

# =========================================================
# VERIFY API KEY
# =========================================================
HF_API_KEY = st.secrets.get("HF_API_KEY", None)

if not HF_API_KEY:
    st.error("❌ Hugging Face API key missing in .streamlit/secrets.toml")
    st.stop()

# =========================================================
# SESSION STATE FOR CHAT
# =========================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================================
# FUNCTION TO CALL HF ROUTER CHAT API
# =========================================================
def query_huggingface_router(prompt, model="meta-llama/Llama-3.1-8B-Instruct"):
    url = "https://router.huggingface.co/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        data = response.json()
        # extract assistant message
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {e}"

# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================================================
# USER INPUT
# =========================================================
user_input = st.chat_input("Type your message here...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("HF Router is thinking..."):
            reply = query_huggingface_router(user_input)
            st.markdown(reply)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": reply})

# =========================================================
# RESET BUTTON
# =========================================================
if st.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.experimental_rerun()
