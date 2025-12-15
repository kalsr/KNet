


# Fraud/Scam-Detector



import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

from PIL import Image, ImageDraw

import pytesseract

from fpdf import FPDF

import random

import io



# -------------------------------------------------

# PAGE CONFIG

# -------------------------------------------------

st.set_page_config(

    page_title="Fraud & Scam Detection System",

    layout="wide"

)



# -------------------------------------------------

# GLOBAL STYLES (PROFESSIONAL GUI)

# -------------------------------------------------

st.markdown("""

<style>

body {

    font-family: 'Segoe UI', sans-serif;

}

.header-box {

    background: linear-gradient(90deg, #0b4f9c, #1fa2ff);

    padding: 22px;

    border-radius: 12px;

    color: white;

    text-align: center;

    font-size: 26px;

    font-weight: bold;

}

.subheader {

    font-size: 20px;

    font-weight: 600;

    margin-top: 10px;

}

.stButton button {

    border-radius: 6px;

    padding: 8px 22px;

    font-size: 15px;

    font-weight: 600;

    background-color: #1fa2ff;

    color: white;

}

.reset-btn button {

    background-color: red !important;

    color: white !important;

    font-weight: 700;

}

</style>

""", unsafe_allow_html=True)



# -------------------------------------------------

# HEADER

# -------------------------------------------------

st.markdown("""

<div class="header-box">

This application is designed & developed by <br>

<b>Randy Singh</b> – <b>KNet Consulting Group</b>

</div>

""", unsafe_allow_html=True)



st.markdown("### 🚨 Enterprise Fraud & Scam Detection Platform")



# -------------------------------------------------

# FRAUD LOGIC (RULE-BASED – PLUG ML LATER)

# -------------------------------------------------

KEYWORDS = [

    "urgent", "verify", "suspended", "click", "password",

    "bank", "wire", "lottery", "won", "gift card"

]



def detect_fraud(text):

    score = sum(1 for k in KEYWORDS if k in text.lower())

    result = "Fraud / Scam" if score >= 2 else "Legitimate"

    return result, score



# -------------------------------------------------

# DEMO GENERATORS

# -------------------------------------------------

def sample_text():

    return random.choice([

        "URGENT! Your bank account is suspended. Click here immediately.",

        "Congratulations! You won a lottery. Send gift cards now.",

        "Team meeting rescheduled to 3 PM tomorrow."

    ])



def sample_image():

    img = Image.new("RGB", (650, 220), "white")

    draw = ImageDraw.Draw(img)

    draw.text((20, 60),

              "URGENT NOTICE\nVerify your bank account now!",

              fill="black")

    return img



# -------------------------------------------------

# SESSION STATE

# -------------------------------------------------

if "results" not in st.session_state:

    st.session_state.results = pd.DataFrame(

        columns=["Source", "Content", "Score", "Result"]

    )



def add_result(src, content):

    res, score = detect_fraud(content)

    st.session_state.results.loc[len(st.session_state.results)] = \[src, content, score, res]

        

    return res, score



# -------------------------------------------------

# TABS

# -------------------------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([

    "✍ Text / Email",

    "📷 Screenshot",

    "🎲 Sample Generator",

    "📊 Analytics",

    "📤 Upload & Export"

])



# -------------------------------------------------

# TAB 1 – TEXT / EMAIL

# -------------------------------------------------

with tab1:

    st.markdown("<div class='subheader'>Text / Email Fraud Detection</div>",

                unsafe_allow_html=True)



    text = st.text_area("Enter Email or Text")



    col1, col2, col3 = st.columns(3)



    with col1:

        if st.button("Detect Fraud"):

            if text:

                r, s = add_result("Manual Text", text)

                st.success(f"Result: {r} | Score: {s}")



    with col2:

        if st.button("Generate Sample Text"):

            demo = sample_text()

            st.info(demo)



    with col3:

        if st.button("Reset", key="rt1"):

            st.session_state.results = st.session_state.results.iloc[0:0]



# -------------------------------------------------

# TAB 2 – SCREENSHOT

# -------------------------------------------------

with tab2:

    st.markdown("<div class='subheader'>Screenshot Fraud Detection</div>",

                unsafe_allow_html=True)



    img_file = st.file_uploader(

        "Upload Screenshot", type=["png", "jpg", "jpeg"]

    )



    if img_file:

        img = Image.open(img_file)

        st.image(img, width=400)

        text = pytesseract.image_to_string(img)

        r, s = add_result("Screenshot Upload", text)

        st.warning(text)

        st.success(f"Result: {r} | Score: {s}")



    if st.button("Generate Demo Screenshot"):

        demo_img = sample_image()

        st.image(demo_img, caption="Generated Scam Screenshot")



# -------------------------------------------------

# TAB 3 – SAMPLE DATA

# -------------------------------------------------

with tab3:

    st.markdown("<div class='subheader'>Sample Data Generator</div>",

                unsafe_allow_html=True)



    n = st.slider("Number of Sample Records", 5, 50, 10)



    data = []

    for _ in range(n):

        t = sample_text()

        r, s = detect_fraud(t)

        data.append([t, s, r])



    df_demo = pd.DataFrame(data, columns=["Text", "Score", "Result"])

    st.dataframe(df_demo)



    fig, ax = plt.subplots()

    df_demo["Result"].value_counts().plot.pie(

        autopct="%1.1f%%", ax=ax

    )

    st.pyplot(fig)



# -------------------------------------------------

# TAB 4 – ANALYTICS

# -------------------------------------------------

with tab4:

    st.markdown("<div class='subheader'>Overall Detection Analytics</div>",

                unsafe_allow_html=True)



    if not st.session_state.results.empty:

        st.dataframe(st.session_state.results)



        fig, ax = plt.subplots()

        st.session_state.results["Result"].value_counts().plot(

            kind="bar", ax=ax

        )

        st.pyplot(fig)



# -------------------------------------------------

# TAB 5 – UPLOAD & EXPORT

# -------------------------------------------------

with tab5:

    st.markdown("<div class='subheader'>Upload & Export Results</div>",

                unsafe_allow_html=True)



    file = st.file_uploader("Upload CSV/Text File", type=["csv", "txt"])



    if file:

        df = pd.read_csv(file, header=None, names=["Text"])

        for t in df["Text"]:

            add_result("Uploaded File", t)



    col1, col2 = st.columns(2)



    with col1:

        if st.button("Export CSV"):

            csv = st.session_state.results.to_csv(index=False).encode()

            st.download_button(

                "Download CSV", csv, "fraud_results.csv"

            )



    with col2:

        if st.button("Export PDF"):

            pdf = FPDF()

            pdf.add_page()

            pdf.set_font("Arial", size=10)

            for _, r in st.session_state.results.iterrows():

                pdf.multi_cell(

                    0, 8,

                    f"{r['Source']} | {r['Result']} | Score: {r['Score']}\n{r['Content']}\n"

                )

            buffer = io.BytesIO()

            pdf.output(buffer)

            st.download_button(

                "Download PDF", buffer.getvalue(), "fraud_results.pdf"

            )



# -------------------------------------------------

# FOOTER

# -------------------------------------------------

st.markdown("---")

st.markdown(

    "© KNet Consulting Group | Enterprise Fraud & Scam Detection Platform"

)


