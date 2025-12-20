import streamlit as st
import requests
from groq import Groq

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Multi-LLM Hub",
    page_icon="🧠",
    layout="wide"
)

# =========================================================
# HARD FAIL IF KEY MISSING (NO SILENT ERRORS)
# =========================================================
if "GROQ_API_KEY" not in st.secrets:
    st.error("❌ GROQ_API_KEY not found in Streamlit secrets")
    st.stop()

GROQ_API_KEY = st.secrets["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"]

# =========================================================
# VERIFY LOADING (ONE-TIME PROOF)
# =========================================================
st.sidebar.success("✅ Groq API key loaded")

# =========================================================
# GROQ FUNCTION
# =========================================================
def query_groq(prompt, model):
    client = Groq(api_key=GROQ_API_KEY)
    chat = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return chat.choices[0].message.content

# =========================================================
# UI
# =========================================================
st.title("🧠 Multi-LLM Hub – Groq Only (Verified)")

model = st.selectbox(
    "Select Groq Model",
    ["llama3-70b-8192", "mixtral-8x7b-32768"]
)

prompt = st.text_area("Enter your prompt", height=200)

if st.button("🚀 Generate"):
    if not prompt.strip():
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Thinking..."):
            try:
                response = query_groq(prompt, model)
                st.success(response)
            except Exception as e:
                st.error(str(e))
