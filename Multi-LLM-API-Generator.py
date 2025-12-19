

 # Multi-LLM Hub – Single File Streamlit App





# File: app.py

import streamlit as st

import requests

import os

from dotenv import load_dotenv, set_key

from groq import Groq



# =========================================================

# ENV SETUP

# =========================================================

load_dotenv()



# =========================================================

# PAGE CONFIG

# =========================================================

st.set_page_config(

    page_title="Multi-LLM Hub",

    page_icon="🧠",

    layout="wide"

)



# =========================================================

# PROFESSIONAL UI STYLES

# =========================================================

st.markdown("""

<style>

.stApp {

    background-color: #f6f8fa;

    font-family: "Segoe UI", sans-serif;

}



h1, h2, h3 {

    color: #1f2937;

}



textarea {

    border-radius: 8px !important;

    border: 1px solid #cbd5e1 !important;

}



div.stButton > button {

    border-radius: 4px;

    background-color: #2563eb;

    color: white;

    font-weight: 600;

    padding: 10px 22px;

    border: none;

}



div.stButton > button:hover {

    background-color: #1e40af;

}



section[data-testid="stSidebar"] {

    background-color: #111827;

    color: white;

}



section[data-testid="stSidebar"] h1,

section[data-testid="stSidebar"] h2,

section[data-testid="stSidebar"] h3,

section[data-testid="stSidebar"] label {

    color: white !important;

}

</style>

""", unsafe_allow_html=True)



# =========================================================

# SESSION STATE INITIALIZATION

# =========================================================

if "HF_API_KEY" not in st.session_state:

    st.session_state.HF_API_KEY = os.getenv("HF_API_KEY", "")



if "GROQ_API_KEY" not in st.session_state:

    st.session_state.GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")



# =========================================================

# LLM FUNCTIONS

# =========================================================

def query_ollama(prompt, model):

    url = "http://localhost:11434/api/generate"

    payload = {"model": model, "prompt": prompt, "stream": False}

    response = requests.post(url, json=payload)

    return response.json().get("response", "No response")



def query_huggingface(prompt, model):

    headers = {

        "Authorization": f"Bearer {st.session_state.HF_API_KEY}"

    }

    payload = {"inputs": prompt}

    response = requests.post(

        f"https://api-inference.huggingface.co/models/{model}",

        headers=headers,

        json=payload

    )

    return response.json()[0]["generated_text"]



def query_groq(prompt, model):

    client = Groq(api_key=st.session_state.GROQ_API_KEY)

    chat = client.chat.completions.create(

        model=model,

        messages=[{"role": "user", "content": prompt}]

    )

    return chat.choices[0].message.content



# =========================================================

# MAIN HEADER

# =========================================================

st.title("🧠 Multi-LLM Hub")

st.subheader("Enterprise-grade Open-Source LLM Interface")



# =========================================================

# SIDEBAR – API KEY MANAGER

# =========================================================

st.sidebar.title("🔐 API Key Manager")



with st.sidebar.expander("Manage API Keys", expanded=False):

    hf_key = st.text_input(

        "Hugging Face API Key",

        type="password",

        value=st.session_state.HF_API_KEY

    )



    groq_key = st.text_input(

        "Groq API Key",

        type="password",

        value=st.session_state.GROQ_API_KEY

    )



    if st.button("💾 Save API Keys"):

        st.session_state.HF_API_KEY = hf_key

        st.session_state.GROQ_API_KEY = groq_key

        set_key(".env", "HF_API_KEY", hf_key)

        set_key(".env", "GROQ_API_KEY", groq_key)

        st.sidebar.success("✅ Keys saved successfully")



st.sidebar.markdown("---")



# =========================================================

# SIDEBAR – MODEL SELECTION

# =========================================================

st.sidebar.title("⚙️ LLM Selection")



provider = st.sidebar.selectbox(

    "Select Provider",

    ["Ollama (Local)", "Hugging Face", "Groq"]

)



MODEL_MAP = {

    "Ollama (Local)": ["llama3", "mistral", "phi3"],

    "Hugging Face": [

        "mistralai/Mistral-7B-Instruct",

        "google/gemma-7b"

    ],

    "Grok": [

        "llama3-70b-8192",

        "mixtral-8x7b-32768"

    ]

}



model = st.sidebar.selectbox("Select Model", MODEL_MAP[provider])



# =========================================================

# MAIN PROMPT AREA

# =========================================================

prompt = st.text_area(

    "Enter your prompt",

    height=200,

    placeholder="Ask anything…"

)



# =========================================================

# VALIDATION

# =========================================================

def validate_keys():

    if provider == "Hugging Face" and not st.session_state.HF_API_KEY:

        st.error("❌ Hugging Face API key not set")

        return False

    if provider == "Groq" and not st.session_state.GROQ_API_KEY:

        st.error("❌ Groq API key not set")

        return False

    return True



# =========================================================

# GENERATE BUTTON

# =========================================================

if st.button("🚀 Generate Response"):

    if not prompt.strip():

        st.warning("⚠️ Please enter a prompt")

    elif validate_keys():

        with st.spinner("🧠 Thinking..."):

            try:

                if provider == "Ollama (Local)":

                    result = query_ollama(prompt, model)

                elif provider == "Hugging Face":

                    result = query_huggingface(prompt, model)

                elif provider == "Groq":

                    result = query_groq(prompt, model)



                st.markdown("### 💡 Model Response")

                st.success(result)



            except Exception as e:

                st.error(f"❌ Error: {str(e)}")



# =========================================================

# FOOTER

# =========================================================

st.markdown("---")

st.caption("© 2025 • Multi-LLM Hub • Open-Source AI Interface")







