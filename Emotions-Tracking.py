# Emotions-Tracking.py

import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import requests

import json

from fpdf import FPDF

from datetime import datetime



# --------------------------

# PAGE CONFIG

# --------------------------

st.set_page_config(page_title="AI Behavior Insight Analyzer", layout="wide")



# --------------------------

# CUSTOM CSS

# --------------------------

st.markdown("""

    <style>

    .main-title {

        background-color: #4A90E2;

        padding: 20px;

        border-radius: 10px;

        color: white;

        text-align: center;

        font-size: 28px;

        font-weight: bold;

    }

    .sub-text {

        text-align: center;

        color: #555;

    }

    .section {

        background-color: #F5F7FA;

        padding: 15px;

        border-radius: 10px;

        margin-top: 10px;

    }

    </style>

""", unsafe_allow_html=True)



# --------------------------

# HEADER

# --------------------------

st.markdown("""

<div class="main-title">

AI Behavior Insight Analyzer<br>

<small>Developed by Randy Singh | Kalsnet (KNet) Consulting Group</small>

</div>

""", unsafe_allow_html=True)



# --------------------------

# SIDEBAR - API KEY

# --------------------------

st.sidebar.header(" Configuration")

api_key = st.sidebar.text_input("Enter Groq API Key", type="password")



# --------------------------

# INPUT SECTION

# --------------------------

st.markdown("###  Input Signals")



col1, col2 = st.columns(2)



with col1:

    text_input = st.text_area("User Text / Chat Input")

    typing_speed = st.slider("Typing Speed (words/min)", 10, 120, 40)



with col2:

    voice_tone = st.selectbox("Voice Tone", ["Neutral", "Excited", "Angry", "Sad"])

    facial_expression = st.selectbox("Facial Expression", ["Neutral", "Happy", "Stressed", "Bored"])



browsing_behavior = st.text_input("Recent Browsing Behavior (keywords)")



# --------------------------

# LLM CALL FUNCTION

# --------------------------

def analyze_with_groq(prompt, api_key):

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {

        "Authorization": f"Bearer {api_key}",

        "Content-Type": "application/json"

    }



    payload = {

        "model": "llama3-70b-8192",

        "messages": [{"role": "user", "content": prompt}]

    }



    response = requests.post(url, headers=headers, json=payload)

    return response.json()



# --------------------------

# ANALYSIS BUTTON

# --------------------------

if st.button(" Analyze Behavior"):



    if not api_key:

        st.error("Please enter your Groq API key.")

    else:

        prompt = f"""

        Analyze the following human behavior signals:



        Text: {text_input}

        Typing speed: {typing_speed}

        Voice tone: {voice_tone}

        Facial expression: {facial_expression}

        Browsing behavior: {browsing_behavior}



        Provide:

        1. Emotion (happy, stressed, bored, etc.)

        2. Likely intention

        3. Preferences

        4. Explanation for each



        Respond in JSON format:

        {{

            "emotion": "",

            "intention": "",

            "preferences": "",

            "explanation": ""

        }}

        """



        result = analyze_with_groq(prompt, api_key)



        try:

            output = result["choices"][0]["message"]["content"]

            data = json.loads(output)



            st.success("Analysis Complete")



            # --------------------------

            # DISPLAY RESULTS

            # --------------------------

            st.markdown("###  Insights")



            st.write(f"**Emotion:** {data['emotion']}")

            st.write(f"**Intention:** {data['intention']}")

            st.write(f"**Preferences:** {data['preferences']}")



            st.markdown("###  Explanation")

            st.info(data["explanation"])



            # --------------------------

            # CHART

            # --------------------------

            st.markdown("###  Emotion Confidence (Simulated)")



            emotions = ["Happy", "Stressed", "Bored"]

            scores = [0.6, 0.3, 0.1]



            fig, ax = plt.subplots()

            ax.bar(emotions, scores)

            st.pyplot(fig)



            # --------------------------

            # EXPORT DATA

            # --------------------------

            df = pd.DataFrame([data])



            st.download_button(" Download CSV",

                               df.to_csv(index=False),

                               file_name="analysis.csv")



            st.download_button(" Download JSON",

                               json.dumps(data),

                               file_name="analysis.json")



            # PDF Export

            pdf = FPDF()

            pdf.add_page()

            pdf.set_font("Arial", size=12)



            for key, value in data.items():

                pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)



            pdf_file = "analysis.pdf"

            pdf.output(pdf_file)



            with open(pdf_file, "rb") as f:

                st.download_button(" Download PDF", f, file_name=pdf_file)



        except Exception as e:

            st.error("Error parsing response from LLM.")

            st.write(result)
