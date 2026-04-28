# Emotions-Tracking.py (FINAL STABLE VERSION)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
from fpdf import FPDF

# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(page_title="AI Behavior Insight Analyzer", layout="wide")

# --------------------------
# HEADER
# --------------------------
st.markdown("""
<div style='background:#4A90E2;padding:20px;border-radius:10px;color:white;text-align:center;font-size:28px;font-weight:bold;'>
AI Behavior Insight Analyzer<br>
<small>Developed by Randy Singh | Kalsnet (KNet)</small>
</div>
""", unsafe_allow_html=True)

# --------------------------
# SIDEBAR
# --------------------------
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Groq API Key", type="password")

# --------------------------
# INPUTS
# --------------------------
st.markdown("### Input Signals")

col1, col2 = st.columns(2)

with col1:
    text_input = st.text_area("User Text / Chat Input")
    typing_speed = st.slider("Typing Speed", 10, 120, 40)

with col2:
    voice_tone = st.selectbox("Voice Tone", ["Neutral", "Excited", "Angry", "Sad"])
    facial_expression = st.selectbox("Facial Expression", ["Neutral", "Happy", "Stressed", "Bored"])

browsing_behavior = st.text_input("Browsing Behavior")

# --------------------------
# ROBUST LLM CALL (AUTO-FALLBACK)
# --------------------------
def analyze_with_groq(prompt, api_key):

    url = "https://api.groq.com/openai/v1/chat/completions"

    models = [
        "llama-3.3-70b-versatile",
        "llama-3.3-8b-instant"
    ]

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    for model in models:
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "Return ONLY valid JSON."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2,
            "response_format": {"type": "json_object"}
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            result = response.json()

            # If success → return
            if "choices" in result:
                return result

            # If model deprecated → try next
            if "error" in result and "decommissioned" in str(result["error"]):
                continue

            return result

        except Exception as e:
            return {"error": str(e)}

    return {"error": "All models failed or deprecated."}

# --------------------------
# BUTTON
# --------------------------
if st.button("Analyze Behavior"):

    if not api_key:
        st.error("Please enter API key")
        st.stop()

    prompt = f"""
Analyze behavior:

Text: {text_input}
Typing speed: {typing_speed}
Voice tone: {voice_tone}
Facial expression: {facial_expression}
Browsing behavior: {browsing_behavior}

Return JSON:
{{
 "emotion": "",
 "intention": "",
 "preferences": "",
 "explanation": ""
}}
"""

    result = analyze_with_groq(prompt, api_key)

    # --------------------------
    # ERROR HANDLING
    # --------------------------
    if "error" in result:
        st.error("API Error")
        st.json(result)
        st.stop()

    try:
        output = result["choices"][0]["message"]["content"]

        # SAFE PARSE
        data = json.loads(output)

    except:
        st.error("Parsing Error")
        st.write("Raw response:")
        st.json(result)
        st.stop()

    # --------------------------
    # DISPLAY
    # --------------------------
    st.success("Analysis Complete")

    st.markdown("### Insights")
    st.write("Emotion:", data.get("emotion"))
    st.write("Intention:", data.get("intention"))
    st.write("Preferences:", data.get("preferences"))

    st.markdown("### Explanation")
    st.info(data.get("explanation"))

    # --------------------------
    # CHART
    # --------------------------
    st.markdown("### Emotion Confidence")

    emotions = ["Happy", "Stressed", "Bored"]
    scores = [0.6, 0.3, 0.1]

    fig, ax = plt.subplots()
    ax.bar(emotions, scores)
    st.pyplot(fig)

    # --------------------------
    # EXPORTS
    # --------------------------
    df = pd.DataFrame([data])

    st.download_button("Download CSV",
                       df.to_csv(index=False),
                       "analysis.csv")

    st.download_button("Download JSON",
                       json.dumps(data, indent=2),
                       "analysis.json")

    # PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for k, v in data.items():
        pdf.multi_cell(0, 10, f"{k}: {v}")

    pdf_file = "analysis.pdf"
    pdf.output(pdf_file)

    with open(pdf_file, "rb") as f:
        st.download_button("Download PDF", f, file_name=pdf_file)