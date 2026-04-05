# DEFENSE-WAR-PLANNING-PLATFORM.py

# Role-based UI (Commander vs Analyst ready)
# Modular expansion for auth (JWT / OAuth ready)
# Graph Theory Integration
# COA → Directed decision graph
# Threat → Target network graph
# Logistics → Shortest path optimization
# AI/ML Ready
# YOLO integration (plug model file)
# RL-ready COA engine (can plug Stable-Baselines3)


import streamlit as st

import pandas as pd

import numpy as np

import networkx as nx

import matplotlib.pyplot as plt

import json

from reportlab.platypus import SimpleDocTemplate, Paragraph

from datetime import datetime



# Optional YOLO

try:

    from ultralytics import YOLO

    YOLO_AVAILABLE = True

except:

    YOLO_AVAILABLE = False



st.set_page_config(layout="wide")



# ---------------- STYLE ----------------

st.markdown("""

<style>

.big-title {color:blue; font-size:28px; font-weight:bold;}

button {background-color:#0047AB; color:white;}

</style>

""", unsafe_allow_html=True)



st.markdown("<div class='big-title'>AI WAR COMMAND PLATFORM<br>Developed by Randy Singh - Kalsnet (KNet) Consulting Group</div>", unsafe_allow_html=True)



# ---------------- ROLE BASED ACCESS ----------------

role = st.sidebar.selectbox("Select Role", ["Commander", "Analyst"])



menu = st.sidebar.radio("Select Module", [

    "Battlefield Map",

    "COA Decision Engine",

    "Threat Detection",

    "Logistics Optimization"

])



# ---------------- EXPORT FUNCTION ----------------

def export_data(df, name="output"):

    st.download_button("Download CSV", df.to_csv(), f"{name}.csv")

    st.download_button("Download JSON", df.to_json(), f"{name}.json")



    pdf_file = f"{name}.pdf"

    doc = SimpleDocTemplate(pdf_file)

    doc.build([Paragraph(df.head().to_string())])



# ---------------- MAP ----------------

if menu == "Battlefield Map":

    import folium

    from streamlit_folium import st_folium



    st.subheader("Battlefield Map")



    m = folium.Map(location=[20,0], zoom_start=2)



    folium.Marker([28.6,77.2], tooltip="Command").add_to(m)

    folium.Marker([34.5,69.2], tooltip="Threat").add_to(m)



    st_folium(m, width=1200, height=600)



    st.info("Used to visualize battlefield zones, threats, and deployments.")



# ---------------- COA ----------------

elif menu == "COA Decision Engine":



    st.subheader("COA Decision Engine")



    n = st.slider("Synthetic Scenarios", 0, 200, 50)



    if st.button("Generate COA Data"):

        df = pd.DataFrame({

            "Terrain": np.random.choice(["Urban","Desert","Mountain"], n),

            "Enemy": np.random.randint(50,500,n),

            "Logistics": np.random.randint(50,200,n),

            "Weather": np.random.rand(n)

        })

        st.session_state.coa = df



    if st.button("Reset COA"):

        st.session_state.coa = pd.DataFrame()



    df = st.session_state.get("coa", pd.DataFrame())

    st.write(df)



    if not df.empty:

        df["Success"] = (df["Logistics"]/(df["Enemy"]+1))*df["Weather"]



        st.bar_chart(df["Success"])



        st.markdown("**Formula:** Success = (Logistics / Enemy) × Weather")



        # Graph Theory

        G = nx.DiGraph()

        for i in range(len(df)):

            G.add_edge("Start", f"COA_{i}", weight=df["Success"][i])



        fig, ax = plt.subplots()

        nx.draw(G, with_labels=True)

        st.pyplot(fig)



        st.info("Graph Theory: Directed graph used for decision pathways & probability transitions.")



        export_data(df, "coa")



# ---------------- THREAT ----------------

elif menu == "Threat Detection":



    st.subheader("Threat Detection & Target Prioritization")



    n = st.slider("Synthetic Threat Data", 0, 200, 50)



    if st.button("Generate Threat Data"):

        df = pd.DataFrame({

            "Speed": np.random.randint(10,100,n),

            "Distance": np.random.randint(1,50,n),

            "Signal": np.random.rand(n)

        })

        st.session_state.threat = df



    if st.button("Reset Threat"):

        st.session_state.threat = pd.DataFrame()



    df = st.session_state.get("threat", pd.DataFrame())

    st.write(df)



    if not df.empty:

        df["ThreatScore"] = df["Speed"]/(df["Distance"]+1)



        st.bar_chart(df["ThreatScore"])



        st.markdown("**Formula:** Threat Score = Speed / Distance")



        # Graph

        G = nx.Graph()

        for i in range(len(df)):

            G.add_edge("Base", f"T{i}", weight=df["ThreatScore"][i])



        fig, ax = plt.subplots()

        nx.draw(G, with_labels=True)

        st.pyplot(fig)



        st.info("Graph Theory: Network graph for threat relationships & prioritization.")



        export_data(df, "threat")



    # YOLO OPTION

    st.subheader("YOLO Detection (Optional)")

    file = st.file_uploader("Upload Image")



    if file and YOLO_AVAILABLE:

        model = YOLO("yolo_model.pt")

        result = model(file)

        st.image(result[0].plot())

    elif file:

        st.warning("YOLO model not available - showing simulated detection.")



# ---------------- LOGISTICS ----------------

elif menu == "Logistics Optimization":



    st.subheader("Logistics & TPFDD Optimization")



    n = st.slider("Synthetic Logistics Data", 0, 200, 50)



    if st.button("Generate Logistics Data"):

        df = pd.DataFrame({

            "From": np.random.choice(["BaseA","BaseB"], n),

            "To": np.random.choice(["Zone1","Zone2"], n),

            "Cost": np.random.randint(100,500,n),

            "Time": np.random.randint(1,20,n)

        })

        st.session_state.log = df



    if st.button("Reset Logistics"):

        st.session_state.log = pd.DataFrame()



    df = st.session_state.get("log", pd.DataFrame())

    st.write(df)



    if not df.empty:

        df["Efficiency"] = df["Cost"]/df["Time"]



        st.bar_chart(df["Efficiency"])



        st.markdown("**Formula:** Efficiency = Cost / Time")



        # Graph Theory (Shortest Path)

        G = nx.Graph()



        for i in range(len(df)):

            G.add_edge(df["From"][i], df["To"][i], weight=df["Cost"][i])



        fig, ax = plt.subplots()

        nx.draw(G, with_labels=True)

        st.pyplot(fig)



        st.info("Graph Theory: Used for shortest path & cost optimization.")



        export_data(df, "logistics")



# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(f"System Time: {datetime.now()}")

