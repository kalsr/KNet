

# Battlefield-Intelligence-And-Target-System-V1.py

import streamlit as st
import pandas as pd
import numpy as np
import json
from datetime import datetime
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(page_title="Battlefield AI System", layout="wide")

# ------------------------------
# HEADER
# ------------------------------
st.markdown(
    """
    <h2 style='color:blue; font-weight:bold;'>
    Application developed by Randy Singh from Kalsnet (KNet) Consulting Group
    </h2>
    <h1> Real-Time Battlefield Intelligence & Target Prioritization System</h1>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# SIDEBAR CONTROLS + EXPLANATION
# ------------------------------
st.sidebar.header(" Controls")

num_records = st.sidebar.slider("Synthetic Data Records", 0, 200, 50)

st.sidebar.markdown(" Data Field Explanation")
st.sidebar.info("""
-Target_ID-: Unique identifier for each detected target.

-Threat_Level-: Randomly generated (1–100) representing enemy threat severity.

-Distance_km-: Distance from base (1–500 km).

-Strategic_Value-: Importance of target (1–100).

-Civilian_Risk-: Risk to civilians (1–100).

These values are synthetically generated using **NumPy random functions** to simulate real battlefield intelligence feeds.
""")

if st.sidebar.button(" Generate New Data"):
    st.session_state["data"] = None

# ------------------------------
# DATA GENERATION
# ------------------------------
def generate_data(n):
    np.random.seed()
    data = pd.DataFrame({
        "Target_ID": range(1, n+1),
        "Threat_Level": np.random.randint(1, 100, n),
        "Distance_km": np.random.randint(1, 500, n),
        "Strategic_Value": np.random.randint(1, 100, n),
        "Civilian_Risk": np.random.randint(1, 100, n)
    })

    # AI Priority Score
    data["Priority_Score"] = (
        data["Threat_Level"] * 0.4 +
        data["Strategic_Value"] * 0.4 -
        data["Civilian_Risk"] * 0.2
    )

    return data.sort_values(by="Priority_Score", ascending=False)

if "data" not in st.session_state or st.session_state["data"] is None:
    st.session_state["data"] = generate_data(num_records)

df = st.session_state["data"]

# ------------------------------
# PRIORITY SCORE EXPLANATION
# ------------------------------
st.markdown(" How Priority Score is Calculated")
st.success("""
Priority Score is calculated using an AI-weighted formula:

- 40% Threat Level → Higher threat increases priority  
- 40% Strategic Value → Higher importance increases priority  
- 20% Civilian Risk → Higher risk reduces priority  

Formula:
Priority = (0.4 × Threat_Level) + (0.4 × Strategic_Value) − (0.2 × Civilian_Risk)

This ensures **high-impact, low-risk targets are prioritized**.
""")

# ------------------------------
# DISPLAY DATA
# ------------------------------
st.subheader(" Battlefield Intelligence Data")
st.dataframe(df, use_container_width=True)

# ------------------------------
# ACTION BUTTONS
# ------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    attack = st.button(" Launch Attack Simulation")

with col2:
    defense = st.button(" Defense Mode")

with col3:
    optimize = st.button(" Optimize Resources")

# ------------------------------
# SIMULATION RESULTS + EXPLANATION
# ------------------------------
if attack:
    st.success(" Attack Simulation Executed")

    st.info("""
    **How Attack Works:**
    - System selects top targets based on highest Priority Score
    - Combines threat severity + strategic importance
    - Avoids high civilian risk areas
    - Represents AI-assisted strike decision system
    """)

    st.write("Top 5 Targets Selected:")
    st.dataframe(df.head(5))


if defense:
    st.info(" Defense Mode Activated")

    st.info("""
    **How Defense Mode Works:**
    - Detects targets with Threat_Level > 80
    - Flags high-risk enemy activities
    - Simulates real-time threat monitoring system
    - Helps in early warning and interception
    """)

    st.write("High Threat Alerts:")
    st.dataframe(df[df["Threat_Level"] > 80])


if optimize:
    st.warning(" Resource Optimization Running...")

    st.info("""
    **How Resource Optimization Works:**
    - Selects targets with:
        • High Strategic Value (>70)
        • Low Civilian Risk (<30)
    - Ensures efficient use of limited resources
    - Maximizes mission success while minimizing collateral damage
    """)

    st.write("Optimal Targets (High Value, Low Civilian Risk):")
    st.dataframe(df[(df["Strategic_Value"] > 70) & (df["Civilian_Risk"] < 30)])

# ------------------------------
# VISUALIZATIONS
# ------------------------------
st.subheader(" Analytics Dashboard")

col1, col2 = st.columns(2)

# PIE CHART
with col1:
    st.write("Threat Distribution")
    fig1, ax1 = plt.subplots()
    bins = pd.cut(df["Threat_Level"], bins=3, labels=["Low", "Medium", "High"])
    bins.value_counts().plot.pie(autopct="%1.1f%%", ax=ax1)
    st.pyplot(fig1)

# BAR CHART
with col2:
    st.write("Top 10 Targets by Priority")
    fig2, ax2 = plt.subplots()
    df.head(10).plot.bar(x="Target_ID", y="Priority_Score", ax=ax2)
    st.pyplot(fig2)

# LINE CHART
st.write("Threat Trend")

st.info("""
**How Threat Trend is Generated:**
- Plots Threat_Level across all targets
- Simulates how threats evolve over time or sequence
- Helps identify escalation patterns or spikes
- Useful for predictive intelligence and planning
""")

fig3, ax3 = plt.subplots()
ax3.plot(df["Threat_Level"].values)
st.pyplot(fig3)

# ------------------------------
# EXPORT FUNCTIONS
# ------------------------------
st.subheader(" Export Results")

csv = df.to_csv(index=False)
st.download_button("Download CSV", csv, "battlefield_data.csv")

json_data = df.to_json(orient="records")
st.download_button("Download JSON", json_data, "battlefield_data.json")

def create_pdf(data):
    doc = SimpleDocTemplate("battlefield_report.pdf")
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("Battlefield Intelligence Report", styles["Title"]))
    content.append(Spacer(1, 12))

    for i, row in data.head(10).iterrows():
        text = f"Target {row['Target_ID']} - Priority Score: {row['Priority_Score']:.2f}"
        content.append(Paragraph(text, styles["Normal"]))
        content.append(Spacer(1, 8))

    doc.build(content)

create_pdf(df)

with open("battlefield_report.pdf", "rb") as f:
    st.download_button("Download PDF", f, "battlefield_report.pdf")

# ------------------------------
# FOOTER
# ------------------------------
st.markdown("---")
st.markdown("© 2026 Kalsnet (KNet) Consulting Group")
