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

#  NEW: GROQ KEY INSTRUCTIONS
st.sidebar.markdown("###  How to Create Groq API Key")
st.sidebar.markdown(f"""
Using :contentReference[oaicite:0]{index=0}:

1. Go to: https://console.groq.com  
2. Sign up (free)  
3. Navigate to **API Keys**  
4. Click **Create API Key**  
5. Copy the full key (starts with `gsk_...`)  
6. Paste it into this sidebar  

""")

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

#  NEW: EXPLANATION SECTION
st.markdown("###  How Emotion Signals Are Interpreted")

st.info("""
**Voice Tone**
- Derived from speech patterns or selected manually
- Excited → high energy, positive intent
- Angry → frustration, urgency
- Sad → low energy, possible disengagement

**Facial Expression**
- Represents visual emotional cues
- Happy → satisfaction / positive engagement
- Stressed → pressure or overload
- Bored → low engagement

**Browsing Behavior**
- Keywords reflect user intent and mindset
- Example:
  - "shopping, deals" → interest / positive intent
  - "errors, fix, issue" → frustration
  - "news, random" → neutral browsing

These signals are combined with text input to infer overall emotional state.
""")

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

            if "choices" in result:
                return result

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

    #  NEW: INSIGHT EXPLANATION
    st.info("""
**How Insights Are Derived**
- AI combines all input signals (text + tone + facial + behavior)
- It detects patterns using language understanding
- Outputs:
  - Emotion → dominant feeling
  - Intention → what user likely wants
  - Preferences → behavioral tendencies
""")

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

    #  NEW: CHART EXPLANATION
    st.info("""
**Emotion Confidence Calculation (Simulated)**
- Scores represent probability distribution of detected emotions
- Example:
  - Happy = 60% confidence
  - Stressed = 30%
  - Bored = 10%
- These are illustrative values for visualization
- In advanced systems, this would be computed using ML models or probability scoring
""")

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