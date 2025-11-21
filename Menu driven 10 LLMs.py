# Menu driven 10 LLMs
# Professional GUI, 
# Menu-driven interface for the top 10 open-source LLMs, 
# Instructions for accessing each, 
# Sample data generator, 
# Upload functionality, 
# Reset button, and a title bar. 
# This will be fully functional for demo purposes.

# streamlit_llm_demo.py

import streamlit as st

import pandas as pd

import json



# -----------------------------

# Title Bar

# -----------------------------

st.set_page_config(page_title="LLM Demo App", layout="wide")

st.markdown(

    """

    <div style='background-color:#4CAF50;padding:15px;border-radius:5px'>

        <h2 style='color:white;text-align:center;'>LLM Demo Application</h2>

        <h4 style='color:white;text-align:center;'>Developed by Randy Singh, KNet Consulting Group</h4>

    </div>

    """,

    unsafe_allow_html=True

)



# -----------------------------

# Sidebar Menu

# -----------------------------

st.sidebar.title("LLM Menu")

llm_options = [

    "1. GPT4All",

    "2. LLaMA",

    "3. MPT",

    "4. Falcon",

    "5. BLOOM",

    "6. Dolly",

    "7. Vicuna",

    "8. OpenAssistant",

    "9. RWKV",

    "10. Alpaca"

]

selected_llm = st.sidebar.radio("Select an LLM to demo:", llm_options)



# Instructions dictionary for demo purposes

llm_instructions = {

    "1. GPT4All": "Visit https://gpt4all.io/ to download models and instructions for local usage.",

    "2. LLaMA": "Access via Meta's release or Hugging Face: https://huggingface.co/models?search=llama",

    "3. MPT": "MosaicML provides MPT models: https://www.mosaicml.com/mpt",

    "4. Falcon": "Visit https://huggingface.co/models?search=falcon for open-source Falcon LLMs.",

    "5. BLOOM": "BLOOM models are available via Hugging Face: https://huggingface.co/bigscience/bloom",

    "6. Dolly": "Dolly LLM from Databricks: https://github.com/databricks/dolly",

    "7. Vicuna": "Vicuna is available through LLaMA fine-tunes: https://vicuna.lmsys.org/",

    "8. OpenAssistant": "OpenAssistant project: https://open-assistant.io/",

    "9. RWKV": "RWKV LLM: https://github.com/BlinkDL/RWKV-LM",

    "10. Alpaca": "Alpaca is Stanford fine-tuned LLaMA: https://github.com/tatsu-lab/stanford_alpaca"

}



# Display LLM info

st.subheader(f"Selected LLM: {selected_llm}")

st.info(llm_instructions[selected_llm])



# -----------------------------

# Sample Data Generator

# -----------------------------

st.subheader("Sample Data Generator")

sample_size = st.slider("Select number of sample data points:", min_value=0, max_value=100, value=10)

if st.button("Generate Sample Data", key="gen"):

    sample_data = pd.DataFrame({

        "id": range(1, sample_size + 1),

        "value": [round(x*0.75 + 10, 2) for x in range(sample_size)]

    })

    st.success(f"{sample_size} sample data points generated!")

    st.dataframe(sample_data)



# -----------------------------

# Upload Your Own Data

# -----------------------------

st.subheader("Upload Your Own Data")

uploaded_file = st.file_uploader("Upload CSV, Excel or JSON", type=["csv", "xlsx", "json"])



if uploaded_file:

    try:

        if uploaded_file.name.endswith("csv"):

            user_data = pd.read_csv(uploaded_file)

        elif uploaded_file.name.endswith("xlsx"):

            user_data = pd.read_excel(uploaded_file)

        elif uploaded_file.name.endswith("json"):

            user_data = pd.read_json(uploaded_file)

        else:

            user_data = None

        if user_data is not None:

            st.success(f"Uploaded {uploaded_file.name} successfully!")

            st.dataframe(user_data)

    except Exception as e:

        st.error(f"Error reading file: {e}")



# -----------------------------

# Reset Data Button

# -----------------------------

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Reset Data", key="reset", help="Reset all generated/uploaded data"):

    st.experimental_rerun()



# -----------------------------

# Footer

# -----------------------------

st.markdown(

    """

    <hr>

    <p style='text-align:center;color:gray;font-size:12px;'>Demo application for showcasing open-source LLMs. Developed by Randy Singh, KNet Consulting Group.</p>

    """,

    unsafe_allow_html=True

)



