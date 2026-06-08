

# AI-Drone-Inspection-&-Risk-Assessment-Platform.py



import streamlit as st

import pandas as pd

import numpy as np

import random

import json

from datetime import datetime

import plotly.express as px



# -------------------------

# PAGE CONFIG

# -------------------------

st.set_page_config(

    page_title="KNet SkyGuard AI",

    layout="wide"

)



# -------------------------

# HEADER

# -------------------------

st.title("KNet SkyGuard AI™")

st.subheader(

    "AI Drone Inspection & Risk Assessment Platform"

)



st.caption(

    "Developed by Randy Singh – "

    "Kalsnet (KNet) Consulting Group"

)



st.markdown("---")



# -------------------------

# SESSION STATE

# -------------------------

if "df" not in st.session_state:

    st.session_state.df = pd.DataFrame()



# -------------------------

# SIDEBAR

# -------------------------

page = st.sidebar.selectbox(

    "Navigation",

    [

        "Dashboard",

        "Upload Data",

        "Synthetic Data",

        "Analytics",

        "Export Results",

        "Field Explanations",

        "Formula Explanations"

    ]

)



# -------------------------

# RISK FORMULA

# -------------------------

def calculate_risk(

    severity,

    weather,

    battery,

    confidence

):

    score = (

        severity * 0.40 +

        weather * 0.15 +

        battery * 0.15 +

        confidence * 0.30

    )



    return round(score, 2)





# -------------------------

# DASHBOARD

# -------------------------

if page == "Dashboard":



    st.header(

        "Executive Dashboard"

    )



    df = st.session_state.df



    c1, c2, c3, c4 = st.columns(4)



    c1.metric(

        "Total Inspections",

        len(df)

    )



    if not df.empty:



        avg_risk = round(

            df["Risk Score"].mean(),

            2

        )



        high_risk = len(

            df[df["Risk Score"] > 60]

        )



    else:

        avg_risk = 0

        high_risk = 0



    c2.metric(

        "Average Risk Score",

        avg_risk

    )



    c3.metric(

        "High Risk Assets",

        high_risk

    )



    c4.metric(

        "Compliance Score",

        "93%"

    )



    st.markdown("---")



    st.write("""

    This dashboard provides

    enterprise-level drone

    inspection intelligence.

    """)



# -------------------------

# REAL DATA UPLOAD

# -------------------------

elif page == "Upload Data":



    st.header(

        "Upload Real Data"

    )



    uploaded = st.file_uploader(

        "Upload CSV, Excel or JSON",

        type=[

            "csv",

            "xlsx",

            "json"

        ]

    )



    if uploaded:



        if uploaded.name.endswith(".csv"):

            df = pd.read_csv(uploaded)



        elif uploaded.name.endswith(".xlsx"):

            df = pd.read_excel(uploaded)



        elif uploaded.name.endswith(".json"):

            df = pd.read_json(uploaded)



        st.session_state.df = df



        st.success(

            "Data uploaded successfully!"

        )



        st.dataframe(

            df,

            use_container_width=True

        )



# -------------------------

# SYNTHETIC DATA

# -------------------------

elif page == "Synthetic Data":



    st.header(

        "Synthetic Data Generator"

    )



    n = st.slider(

        "Number of Records",

        0,

        250,

        50

    )



    col1, col2 = st.columns(2)



    with col1:



        if st.button(

            "Generate Records"

        ):



            rows = []



            for i in range(n):



                severity = random.randint(

                    1, 100

                )



                weather = random.randint(

                    1, 100

                )



                battery = random.randint(

                    1, 100

                )



                confidence = random.randint(

                    1, 100

                )



                risk = calculate_risk(

                    severity,

                    weather,

                    battery,

                    confidence

                )



                rows.append({



                    "Inspection ID":

                        f"INS-{1000+i}",



                    "Drone ID":

                        f"DR-{random.randint(1,50)}",



                    "Asset ID":

                        f"AST-{random.randint(100,999)}",



                    "Latitude":

                        round(

                            random.uniform(

                                36, 39

                            ), 6

                        ),



                    "Longitude":

                        round(

                            random.uniform(

                                -79, -75

                            ), 6

                        ),



                    "Altitude":

                        random.randint(

                            50, 400

                        ),



                    "Weather":

                        weather,



                    "Battery":

                        battery,



                    "Severity":

                        severity,



                    "Confidence":

                        confidence,



                    "Risk Score":

                        risk,



                    "Timestamp":

                        str(datetime.now())

                })



            st.session_state.df = (

                pd.DataFrame(rows)

            )



    with col2:



        if st.button(

            "Reset Records"

        ):

            st.session_state.df = (

                pd.DataFrame()

            )



            st.success(

                "All records reset."

            )



    st.dataframe(

        st.session_state.df,

        use_container_width=True

    )



# -------------------------

# ANALYTICS

# -------------------------

elif page == "Analytics":



    st.header(

        "Inspection Analytics"

    )



    df = st.session_state.df



    if not df.empty:



        fig = px.histogram(

            df,

            x="Risk Score",

            title="Risk Distribution"

        )



        st.plotly_chart(

            fig,

            use_container_width=True

        )



        fig2 = px.scatter(

            df,

            x="Severity",

            y="Risk Score",

            title="Severity vs Risk"

        )



        st.plotly_chart(

            fig2,

            use_container_width=True

        )



# -------------------------

# EXPORTS

# -------------------------

elif page == "Export Results":



    st.header(

        "Export Results"

    )



    df = st.session_state.df



    if not df.empty:



        st.download_button(

            "Download JSON",

            data=df.to_json(

                orient="records",

                indent=2

            ),

            file_name=

            "skyguard_results.json"

        )



# -------------------------

# FIELD EXPLANATIONS

# -------------------------

elif page == "Field Explanations":



    st.header(

        "Field Explanations"

    )



    st.table(pd.DataFrame({

        "Field": [

            "Inspection ID",

            "Drone ID",

            "Asset ID",

            "Latitude",

            "Longitude",

            "Altitude",

            "Weather",

            "Battery",

            "Severity",

            "Confidence",

            "Risk Score"

        ],



        "Purpose": [

            "Unique inspection",

            "Drone identity",

            "Asset tracked",

            "GPS location",

            "GPS location",

            "Flight height",

            "Weather impact",

            "Battery status",

            "Damage severity",

            "AI confidence",

            "Overall risk"

        ]

    }))



# -------------------------

# FORMULA EXPLANATION

# -------------------------

elif page == "Formula Explanations":



    st.header(

        "Formula Explanation"

    )



    st.latex(

        r'''

        RiskScore =

        (Severity \times 0.40)

        +

        (Weather \times 0.15)

        +

        (Battery \times 0.15)

        +

        (Confidence \times 0.30)

        '''

    )



    st.write("""

    **Severity (40%)**

    contributes most to risk.



    **Weather (15%)**

    affects inspection reliability.



    **Battery (15%)**

    affects drone stability.



    **Confidence (30%)**

    represents AI certainty.

    """)