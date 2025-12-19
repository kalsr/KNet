

# app.py

# Multi-LLM Demo App



import os

import requests

import streamlit as st

from groq import Groq



# -----------------------------

# Page Config

# -----------------------------

st.set_page_config(

    page_title="Multi-LLM Demo",

    page_icon="🧠",

    layout="wide"

)



st.title("🧠 Multi-LLM Playground")

st.caption("Compare multiple free-tier LLMs with a clean UI")



# -----------------------------

# API Keys

# -----------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")



# -----------------------------

# LLM Functions

# -----------------------------

def call_groq(prompt):

    client = Groq(api_key=GROQ_API_KEY)

    res = client.chat.completions.create(

        model="llama3-70b-8192",

        messages=[{"role": "user", "content": prompt}]

    )

    return res.choices[0].message.content





def call_openrouter(prompt):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {

        "Authorization": f"Bearer {OPENROUTER_API_KEY}",

        "Content-Type": "application/json"

    }

    payload = {

        "model": "mistralai/mistral-7b-instruct",

        "messages": [{"role": "user", "content": prompt}]

    }

    res = requests.post(url, headers=headers, json=payload)

    return res.json()["choices"][0]["message"]["content"]





def call_together(prompt):

    url = "https://api.together.xyz/v1/chat/completions"

    headers = {

        "Authorization": f"Bearer {TOGETHER_API_KEY}",

        "Content-Type": "application/json"

    }

    payload = {

        "model": "meta-llama/Llama-3-70b-chat-hf",

        "messages": [{"role": "user", "content": prompt}]

    }

    res = requests.post(url, headers=headers, json=payload)

    return res.json()["choices"][0]["message"]["content"]



# -----------------------------

# UI

# -----------------------------

model = st.selectbox(

    "Choose LLM Provider",

    ["Groq (LLaMA-3)", "OpenRouter (Mistral)", "Together AI (LLaMA-3)"]

)



prompt = st.text_area("Ask a question", height=140)

ask = st.button("Ask")



if ask and prompt:

    with st.spinner("Thinking..."):

        try:

            if model.startswith("Groq"):

                output = call_groq(prompt)

            elif model.startswith("OpenRouter"):

                output = call_openrouter(prompt)

            else:

                output = call_together(prompt)



            st.subheader("Response")

            st.write(output)



        except Exception as e:

            st.error(f"Error: {e}")
