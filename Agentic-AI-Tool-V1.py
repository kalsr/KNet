# ==========================================================
# GROQ STREAMLIT APP – FULL WORKING VERSION
# ==========================================================

import streamlit as st
from groq import Groq

st.set_page_config(page_title="GROQ AI Demo", layout="wide")

st.title("🚀 GROQ AI Chat Demo")

# ----------------------------------------------------------
# LOAD API KEY (from secrets)
# ----------------------------------------------------------
def load_groq_key():
    try:
        return st.secrets["GROQ_API_KEY"]
    except Exception as e:
        return None

api_key = load_groq_key()

# ----------------------------------------------------------
# DEBUG INFO (optional)
# ----------------------------------------------------------
with st.expander("🔍 Debug Info"):
    st.write("Secrets Loaded:", dict(st.secrets) if st.secrets else "No secrets found")
    st.write("API Key Found:", "YES" if api_key else "NO")

# ----------------------------------------------------------
# CHECK KEY
# ----------------------------------------------------------
if not api_key:
    st.error("❌ No GROQ API Key found. Check your .streamlit/secrets.toml file.")
    st.stop()

# ----------------------------------------------------------
# INIT CLIENT
# ----------------------------------------------------------
client = Groq(api_key=api_key)

# ----------------------------------------------------------
# CHAT UI
# ----------------------------------------------------------
user_input = st.text_input("Enter your prompt:")

if st.button("Submit") and user_input:
    try:
        with st.spinner("🤖 GROQ is thinking..."):
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": user_input}],
                temperature=0.7
            )

        output = response.choices[0].message.content
        st.success("✅ Response:")
        st.write(output)

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

# ----------------------------------------------------------
# FOOTER
# ----------------------------------------------------------
st.markdown("---")
st.markdown("Built with GROQ + Streamlit")