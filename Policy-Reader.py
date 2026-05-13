
import streamlit as st
import os

st.set_page_config(page_title="Policy Reader App", layout="wide")

st.title("Policy Reader - Fixed Version")

st.write("Upload or paste policy text and get a clean structured view.")

api_key = st.secrets.get("OPENAI_API_KEY", None)

if not api_key:
    st.warning("OpenAI API key not found in secrets. Add it in .streamlit/secrets.toml")

text = st.text_area("Enter Policy Text", height=300)

if st.button("Process"):
    if not text:
        st.error("Please enter policy text")
    else:
        st.subheader("Processed Output")
        st.write(text.upper())
        st.success("Processing complete (demo transformation)")
