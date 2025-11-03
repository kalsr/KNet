import streamlit as st

files = {
    "Machine Learning": "/mnt/data/ml_sample.csv",
    "NLP": "/mnt/data/nlp_sample.csv",
    "Computer Vision": "/mnt/data/cv_sample.csv",
    "Speech/Audio": "/mnt/data/speech_sample.csv",
    "Reinforcement Learning": "/mnt/data/rl_sample.csv",
    "Data & Preprocessing": "/mnt/data/data_prep_sample.csv",
    "Model Optimization": "/mnt/data/model_opt_sample.csv",
    "Agentic AI": "/mnt/data/agentic_ai_sample.csv",
    "MLOps": "/mnt/data/mlops_sample.csv"
}

st.title("Download All Sample Data")

for name, path in files.items():
    with open(path, "rb") as f:
        st.download_button(
            label=f"⬇️ Download {name} Sample CSV",
            data=f,
            file_name=path.split("/")[-1],
            mime="text/csv"
        )
