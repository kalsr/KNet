

# DEFENSE-WAR-PLANNING-PLATFORM1.py

import streamlit as st
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
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
.title-bar {
    color:#0033cc;
    font-size:40px;
    font-weight:bold;
    text-align:center;
    padding:15px;
}
.subtitle {
    text-align:center;
    font-size:18px;
    color:#555;
}
.section-header {
    color:#0047AB;
    font-size:24px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<div class='title-bar'>Kalsnet (KNet) AI WAR COMMAND PLATFORM</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Developed by Randy Singh – KNet Consulting Group</div>", unsafe_allow_html=True)

# ---------------- ROLE ----------------
role = st.sidebar.selectbox("Select Role", ["Commander", "Analyst"])

# Role Explanation
st.markdown("### 🔹 Role Description")

if role == "Commander":
    st.info("""
**Commander Role:**
- Focuses on **strategic decision-making and mission outcomes**
- Uses **COA (Course of Action) Engine** to evaluate mission success
- Monitors battlefield and prioritizes high-value targets
- Makes final operational decisions based on AI insights

**Key Difference:** Commander focuses on **decision & action**
""")
else:
    st.info("""
**Analyst Role:**
- Focuses on **data analysis, threat detection, and intelligence gathering**
- Evaluates patterns, anomalies, and risk indicators
- Supports commanders with **data-driven insights**
- Works heavily with threat models and detection systems

**Key Difference:** Analyst focuses on **data & intelligence**
""")

# ---------------- MENU ----------------
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

# ==========================================================
# ---------------- BATTLEFIELD MAP ----------------
# ==========================================================
if menu == "Battlefield Map":

    import folium
    from streamlit_folium import st_folium

    st.markdown("<div class='section-header'>Battlefield Map</div>", unsafe_allow_html=True)

    st.info("""
**Module Purpose:**
The Battlefield Map provides a **real-time geospatial visualization** of operational zones.

**Role in Operations:**
- Commanders visualize deployment zones and threats
- Analysts monitor geographic threat distribution

**Tools Used:**
- Streamlit, Folium (mapping), Python

**Real-World Benefit:**
Enhances **situational awareness and mission planning** by visualizing threats and assets globally.
""")

    m = folium.Map(location=[20,0], zoom_start=2)
    folium.Marker([28.6,77.2], tooltip="Command Center").add_to(m)
    folium.Marker([34.5,69.2], tooltip="Threat Zone").add_to(m)

    st_folium(m, width=1200, height=600)

# ==========================================================
# ---------------- COA ENGINE ----------------
# ==========================================================
elif menu == "COA Decision Engine":

    st.markdown("<div class='section-header'>COA Decision Engine</div>", unsafe_allow_html=True)

    st.info("""
**Module Purpose:**
Generates and evaluates **Courses of Action (COA)** using AI-based scoring.

**Role in Operations:**
- Commanders simulate mission success scenarios
- Analysts validate assumptions using data

**Tools Used:**
- Pandas, NumPy, NetworkX, Matplotlib

**Real-World Benefit:**
Supports **mission planning, war-gaming, and predictive decision-making**.
""")

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

        G = nx.DiGraph()
        for i in range(len(df)):
            G.add_edge("Start", f"COA_{i}", weight=df["Success"][i])

        fig, ax = plt.subplots()
        nx.draw(G, with_labels=True)
        st.pyplot(fig)

        st.success("Graph Theory Applied: Directed decision graph for mission pathways.")

        export_data(df, "coa")

# ==========================================================
# ---------------- THREAT DETECTION ----------------
# ==========================================================
elif menu == "Threat Detection":

    st.markdown("<div class='section-header'>Threat Detection</div>", unsafe_allow_html=True)

    st.info("""
**Module Purpose:**
Detects and prioritizes threats using AI scoring models.

**Role in Operations:**
- Analysts detect anomalies and suspicious activity
- Commanders prioritize threats for response

**Tools Used:**
- Pandas, NumPy, NetworkX, Matplotlib, YOLO (optional)

**Real-World Benefit:**
Enables **real-time threat detection and proactive defense strategies**.
""")

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

        G = nx.Graph()
        for i in range(len(df)):
            G.add_edge("Base", f"T{i}", weight=df["ThreatScore"][i])

        fig, ax = plt.subplots()
        nx.draw(G, with_labels=True)
        st.pyplot(fig)

        st.success("Graph Theory Applied: Network graph for threat relationships.")

        export_data(df, "threat")

    # YOLO
    st.subheader("YOLO Object Detection (Optional)")
    file = st.file_uploader("Upload Image")

    if file and YOLO_AVAILABLE:
        model = YOLO("yolo_model.pt")
        result = model(file)
        st.image(result[0].plot())
    elif file:
        st.warning("YOLO model not available.")

# ==========================================================
# ---------------- LOGISTICS ----------------
# ==========================================================
elif menu == "Logistics Optimization":

    st.markdown("<div class='section-header'>Logistics Optimization</div>", unsafe_allow_html=True)

    st.info("""
**Module Purpose:**
Optimizes logistics movement and supply chain efficiency.

**Role in Operations:**
- Commanders allocate resources efficiently
- Analysts evaluate cost/time tradeoffs

**Tools Used:**
- Pandas, NumPy, NetworkX (Shortest Path)

**Real-World Benefit:**
Improves **supply chain efficiency, reduces cost, and speeds deployment**.
""")

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

        G = nx.Graph()
        for i in range(len(df)):
            G.add_edge(df["From"][i], df["To"][i], weight=df["Cost"][i])

        fig, ax = plt.subplots()
        nx.draw(G, with_labels=True)
        st.pyplot(fig)

        st.success("Graph Theory Applied: Shortest path optimization.")

        export_data(df, "logistics")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption(f"System Time: {datetime.now()}")