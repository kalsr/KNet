# Multiple-LLMs-API-Key

import streamlit as st
from openai import OpenAI
from groq import Groq
import anthropic

# ---------------------------------
# Page Config
# ---------------------------------
st.set_page_config(
    page_title="Multi-Provider LLM Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Multi-Provider LLM Chatbot")
st.caption("OpenAI • Groq • Anthropic • Azure OpenAI")

# ---------------------------------
# Sidebar
# ---------------------------------
with st.sidebar:
    provider = st.selectbox(
        "Select Provider",
        ["Groq (FREE)", "OpenAI", "Anthropic", "Azure OpenAI"]
    )

    if st.button("🔄 Reset Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------------
# Session State
# ---------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------
# Display Chat
# ---------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------------
# User Input
# ---------------------------------
user_input = st.chat_input("Ask something...")

def call_llm(provider, prompt):
    if provider == "Groq (FREE)":
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        resp = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content

    if provider == "OpenAI":
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content

    if provider == "Anthropic":
        client = anthropic.Anthropic(
            api_key=st.secrets["ANTHROPIC_API_KEY"]
        )
        msg = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return msg.content[0].text

    if provider == "Azure OpenAI":
        client = OpenAI(
            api_key=st.secrets["AZURE_OPENAI_KEY"],
            base_url=f"{st.secrets['AZURE_OPENAI_ENDPOINT']}/openai/deployments/{st.secrets['AZURE_OPENAI_DEPLOYMENT']}",
            default_headers={"api-key": st.secrets["AZURE_OPENAI_KEY"]}
        )
        resp = client.chat.completions.create(
            model=st.secrets["AZURE_OPENAI_DEPLOYMENT"],
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content

# ---------------------------------
# Run Chat
# ---------------------------------
if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                reply = call_llm(provider, user_input)
            except Exception as e:
                reply = f"❌ Error: {e}"

            st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )


