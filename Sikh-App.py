

# Streamlit SIKH App Code
# Sikh-App.py

import streamlit as st
from openai import OpenAI

# ----------------------------------------
# Load OpenAI API Key securely
# ----------------------------------------
api_key = st.secrets.get("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY not found in Streamlit secrets.")
    st.stop()

# Initialize OpenAI client WITH key
client = OpenAI(api_key=api_key)

# ----------------------------------------
# Streamlit UI
# ----------------------------------------
st.set_page_config(
    page_title="Sikh Knowledge Explorer",
    layout="centered"
)

st.title("🕉️ Sikh Knowledge Explorer")
st.write(
    "Click a button below to learn about Sikh Gurus, "
    "the Guru Granth Sahib, or Sikh history."
)

# Sidebar options
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

# ----------------------------------------
# OpenAI call
# ----------------------------------------
def get_chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a knowledgeable and respectful expert on Sikhism."
            },
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

# ----------------------------------------
# Display output
# ----------------------------------------
if topic:
    with st.spinner("Fetching information..."):
        answer = get_chatgpt_response(topic)

    st.subheader("📘 Information")
    st.write(answer)
else:
    st.info("Please select a topic from the sidebar to begin.")
