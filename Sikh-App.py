import os
import streamlit as st
from openai import OpenAI

# --- DEBUG (safe, remove later) ---
st.write("Secrets detected:", list(st.secrets.keys()))

api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY not found. Add it via Streamlit Cloud → Settings → Secrets")
    st.stop()

client = OpenAI(api_key=api_key)


# -------------------------------
# UI CONFIG
# -------------------------------
st.set_page_config(
    page_title="Sikh Knowledge Explorer",
    layout="centered"
)

st.title("🕉️ Sikh Knowledge Explorer")
st.write(
    "Click a button below to learn about Sikh Gurus, "
    "the Guru Granth Sahib, or Sikh history."
)

# Sidebar
st.sidebar.header("Choose a Topic")

topic = None

if st.sidebar.button("Sikh Gurus"):
    topic = "Provide a clear and respectful overview of the Ten Sikh Gurus."

if st.sidebar.button("Guru Granth Sahib"):
    topic = (
        "Explain what the Guru Granth Sahib is, its significance in Sikhism, "
        "and its core teachings."
    )

if st.sidebar.button("Sikh History"):
    topic = (
        "Give an overview of Sikh history, including its origins, "
        "key events, and values."
    )

# -------------------------------
# OpenAI Call
# -------------------------------
def get_chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a knowledgeable expert on Sikhism."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

# -------------------------------
# Output
# -------------------------------
if topic:
    with st.spinner("Fetching information..."):
        answer = get_chatgpt_response(topic)
    st.subheader("📘 Information")
    st.write(answer)
else:
    st.info("Please select a topic from the sidebar.")

