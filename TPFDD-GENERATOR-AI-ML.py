

# TPFDD-GENERATOR-V4 (AI/ML Enhanced)
import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
import json

# PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# ML
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

st.set_page_config(layout="wide")

# -----------------------------
# TITLE
# -----------------------------
st.markdown(
    "<h1 style='text-align:center; color:blue;'>"
    "Enterprise TPFDD Generator Using AI/ML Platform<br>"
    "Developed by Randy Singh – Kalsnet (KNet) Group"
    "</h1>",
    unsafe_allow_html=True
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("Controls")
num_records = st.sidebar.slider("Synthetic TPFDD Records", 0, 300, 100)
scenario = st.sidebar.selectbox(
    "Scenario",
    ["Steady State", "Rapid Deployment", "Major Theater War"]
)
generate_btn = st.sidebar.button("Generate TPFDD")
simulate_btn = st.sidebar.button("Run Simulation")
reset_btn = st.sidebar.button("Reset")

# -----------------------------
# SCENARIO EXPLANATION
# -----------------------------
st.subheader("Scenario Explanation")
if scenario == "Steady State":
    st.info("""
    **Steady State Operations** represent routine, ongoing military logistics activities. 
    Forces are deployed in a predictable and sustained manner with balanced transportation 
    planning. There is minimal urgency, allowing optimized scheduling, cost efficiency, 
    and reduced operational risk.
    """)
elif scenario == "Rapid Deployment":
    st.warning("""
    **Rapid Deployment** focuses on quickly mobilizing forces in response to emerging threats. 
    Airlift is heavily prioritized, timelines are compressed, and logistics operate under 
    time-sensitive conditions. This scenario tests responsiveness, agility, and surge capability.
    """)
elif scenario == "Major Theater War":
    st.error("""
    **Major Theater War (MTW)** represents large-scale, high-intensity conflict. 
    Massive personnel and equipment movement occurs across multiple domains using 
    both air and sea. This scenario stresses full logistics capacity, coordination, 
    and sustainment over extended operations.
    """)

# -----------------------------
# SESSION STATE
# -----------------------------
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()

# -----------------------------
# DATA GENERATION
# -----------------------------
def generate_tpfdd(n):
    data = []
    base_date = datetime.now()
    for i in range(n):
        ald = base_date + timedelta(days=random.randint(1, 5))
        ead = ald + timedelta(days=random.randint(2, 5))
        rdd = ead + timedelta(days=random.randint(3, 10))
        data.append({
            "ULN": f"ULN{i}",
            "Parent ULN": f"PARENT{random.randint(1,10)}",
            "Force Type": random.choice(["Combat", "Support", "Logistics"]),
            "Mode": random.choice(["Air", "Sea"]),
            "POE": random.choice(["Dover AFB", "Norfolk", "San Diego"]),
            "POD": random.choice(["Qatar", "Kuwait", "Germany"]),
            "Personnel": random.randint(50, 800),
            "Weight (STON)": random.randint(10, 500),
            "ALD": ald,
            "EAD": ead,
            "RDD": rdd,
            "Priority": random.randint(1, 5),
            "Status": "Planned"
        })
    return pd.DataFrame(data)

# -----------------------------
# SIMULATION
# -----------------------------
def simulate(df):
    df = df.copy()
    for i in range(len(df)):
        transit = random.randint(1, 3) if df.loc[i, "Mode"] == "Air" else random.randint(7, 20)
        arrival = df.loc[i, "EAD"] + timedelta(days=transit)
        df.loc[i, "Status"] = "On-Time" if arrival <= df.loc[i, "RDD"] else "Delayed"
    return df

# -----------------------------
# BUTTON ACTIONS
# -----------------------------
if generate_btn:
    st.session_state.df = generate_tpfdd(num_records)

if simulate_btn and not st.session_state.df.empty:
    st.session_state.df = simulate(st.session_state.df)

if reset_btn:
    st.session_state.df = pd.DataFrame()

df = st.session_state.df

# -----------------------------
# AI/ML PREDICTION
# -----------------------------
def apply_ml_prediction(df):
    if df.empty:
        return df
    df_ml = df.copy()
    # Encode categorical features
    le_mode = LabelEncoder()
    le_force = LabelEncoder()
    le_poe = LabelEncoder()
    le_pod = LabelEncoder()
    df_ml['Mode_enc'] = le_mode.fit_transform(df_ml['Mode'])
    df_ml['Force_enc'] = le_force.fit_transform(df_ml['Force Type'])
    df_ml['POE_enc'] = le_poe.fit_transform(df_ml['POE'])
    df_ml['POD_enc'] = le_pod.fit_transform(df_ml['POD'])
    # Encode target
    le_status = LabelEncoder()
    df_ml['Status_enc'] = le_status.fit_transform(df_ml['Status'])
    # Features
    features = ['Mode_enc','Force_enc','POE_enc','POD_enc','Personnel','Weight (STON)','Priority']
    X = df_ml[features]
    y = df_ml['Status_enc']
    # Train simple Random Forest
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X, y)
    df_ml['Predicted_Status_enc'] = clf.predict(X)
    df_ml['Predicted Status'] = le_status.inverse_transform(df_ml['Predicted_Status_enc'])
    return df_ml.drop(columns=['Mode_enc','Force_enc','POE_enc','POD_enc','Status_enc','Predicted_Status_enc'])

if not df.empty:
    df = apply_ml_prediction(df)
    st.session_state.df = df

# -----------------------------
# DATA DISPLAY
# -----------------------------
st.subheader("TPFDD Data")
if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.info("No data generated yet.")

# -----------------------------
# TPFDD FIELD EXPLANATION
# -----------------------------
st.subheader("TPFDD Field Explanation")
st.markdown("""
- **ULN (Unit Line Number):** Unique identifier for each deployment element.
- **Parent ULN:** Links related units for hierarchical planning.
- **Force Type:** Mission role (Combat, Support, Logistics).
- **Mode:** Transport method (Air/Sea).
- **POE/POD:** Embarkation and Debarkation ports.
- **Personnel & Weight:** Manpower and equipment.
- **ALD/EAD/RDD:** Load/arrival/deadline dates.
- **Priority:** Movement precedence.
- **Status:** Actual deployment status.
- **Predicted Status:** AI/ML predicted status based on features.
""")

# -----------------------------
# DASHBOARD
# -----------------------------
if not df.empty:
    st.subheader("Operational Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Mode Distribution")
        st.bar_chart(df["Mode"].value_counts())
        st.write("### Status Distribution")
        st.bar_chart(df["Status"].value_counts())
        st.write("### Predicted Status Distribution")
        st.bar_chart(df["Predicted Status"].value_counts())
    with col2:
        st.write("### Personnel by Force Type")
        st.bar_chart(df.groupby("Force Type")["Personnel"].sum())
        st.write("### RDD Timeline")
        timeline = df.copy()
        timeline["RDD"] = pd.to_datetime(timeline["RDD"])
        st.line_chart(timeline["RDD"].value_counts().sort_index())

# -----------------------------
# DASHBOARD INSIGHTS
# -----------------------------
st.subheader("Dashboard Insights")
st.markdown("""
- **Mode Distribution:** Air vs Sea transport reliance.
- **Status Distribution:** Actual mission success vs delays.
- **Predicted Status:** AI/ML forecast of deployment timelines.
- **Personnel by Force Type:** Allocation of manpower.
- **RDD Timeline:** Peaks and operational pressure periods.
""")

# -----------------------------
# EXPORTS
# -----------------------------
if not df.empty:
    st.subheader("Export Options")
    col1, col2, col3 = st.columns(3)
    # CSV
    csv = df.to_csv(index=False)
    col1.download_button("Download CSV", csv, "tpfdd.csv")
    # JSON
    json_data = df.to_json(orient="records", date_format="iso")
    col2.download_button("Download JSON", json_data, "tpfdd.json")
    # PDF
    def create_pdf(dataframe):
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()
        content = []
        content.append(Paragraph("Enterprise TPFDD Report", styles["Title"]))
        content.append(Spacer(1, 10))
        table_data = [list(dataframe.columns)]
        for _, row in dataframe.head(50).iterrows():
            table_data.append([str(x) for x in row])
        table = Table(table_data)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("FONTSIZE", (0, 0), (-1, -1), 6),
        ]))
        content.append(table)
        doc.build(content)
        buffer.seek(0)
        return buffer
    if col3.button("Generate PDF"):
        pdf_buffer = create_pdf(df)
        col3.download_button("Download PDF", data=pdf_buffer, file_name="tpfdd_report.pdf", mime="application/pdf")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.success("✔ Enterprise TPFDD Simulation Ready with AI/ML Prediction")
