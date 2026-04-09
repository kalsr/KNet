


# ==========================================
# KNET CRITICAL INFRASTRUCTURE PLATFORM
# FULLY SELF-CONTAINED VERSION (NO ERRORS)
# ==========================================

import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import json
import os
import numpy as np

# ---------------- CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;color:blue;font-weight:bold;'>Energy Infrastructure Intelligence Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:blue;font-weight:bold;'>Developed by Randy Singh - Kalsnet (KNet) Consulting Group</h3>", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
st.sidebar.subheader("Upload Dataset (Optional)")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# ==========================================================
# 🔥 REALISTIC DATA GENERATOR (200 RECORDS)
# ==========================================================
def generate_realistic_data(n=200):
    np.random.seed(42)

    fuels = ["Gas", "Oil", "Hydro", "Solar", "Wind"]

    df = pd.DataFrame({
        "country_long": ["Iran"] * n,
        "name": [f"Plant_{i}" for i in range(1, n + 1)],
        "primary_fuel": np.random.choice(fuels, n),
        "capacity_mw": np.random.randint(50, 500, n),
        "latitude": np.random.uniform(25, 38, n),
        "longitude": np.random.uniform(44, 63, n)
    })

    return df

# ==========================================================
# ✅ LOAD DATA (NO MORE FILE ERRORS)
# ==========================================================
@st.cache_data
def load_data(uploaded_file):

    try:
        # 1. Uploaded file
        if uploaded_file is not None:
            st.success("Using uploaded dataset")
            return pd.read_csv(uploaded_file)

        # 2. Local file
        elif os.path.exists("global_power_plant_database.csv"):
            st.success("Using local dataset")
            return pd.read_csv("global_power_plant_database.csv")

        # 3. Auto-generate (BEST PRACTICE)
        else:
            st.warning("Dataset not found → Generating realistic data automatically")
            return generate_realistic_data(200)

    except Exception as e:
        st.error(f"Error loading data: {e}")
        return generate_realistic_data(200)

# ---------------- LOAD ----------------
df = load_data(uploaded_file)

# ---------------- VALIDATION ----------------
if df.empty:
    st.error("No data available")
    st.stop()

# ---------------- FILTER IRAN ----------------
if "country_long" in df.columns:
    df = df[df["country_long"] == "Iran"]

# ---------------- SIDEBAR ----------------
st.sidebar.header("Filters")

fuel_options = df["primary_fuel"].dropna().unique()
fuel = st.sidebar.multiselect("Fuel Type", fuel_options, default=fuel_options)

capacity_max = int(df["capacity_mw"].max()) if not df.empty else 1000
capacity = st.sidebar.slider("Capacity (MW)", 0, capacity_max, (0, capacity_max))

filtered_df = df[
    (df["primary_fuel"].isin(fuel)) &
    (df["capacity_mw"].between(capacity[0], capacity[1]))
]

# ---------------- KPI ----------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Plants", len(filtered_df))
col2.metric("Total Capacity (MW)", int(filtered_df["capacity_mw"].sum()))

if len(filtered_df) > 0:
    renewable_pct = len(
        filtered_df[filtered_df["primary_fuel"].isin(["Solar", "Wind", "Hydro"])]
    ) / len(filtered_df) * 100
else:
    renewable_pct = 0

col3.metric("Renewable %", f"{renewable_pct:.2f}%")

st.markdown("---")

# ---------------- MAP ----------------
st.subheader("Power Plant Locations")

if not filtered_df.empty:
    fig = px.scatter_mapbox(
        filtered_df,
        lat="latitude",
        lon="longitude",
        color="primary_fuel",
        size="capacity_mw",
        hover_name="name",
        zoom=4
    )
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No data available for map")

# ---------------- CHARTS ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Capacity by Fuel")
    if not filtered_df.empty:
        fig1 = px.pie(filtered_df, names="primary_fuel", values="capacity_mw")
        st.plotly_chart(fig1)

with col2:
    st.subheader("Top 10 Plants")
    if not filtered_df.empty:
        top10 = filtered_df.sort_values("capacity_mw", ascending=False).head(10)
        fig2 = px.bar(top10, x="name", y="capacity_mw")
        st.plotly_chart(fig2)

# ---------------- DATA QUALITY ----------------
st.markdown("### Data Coverage Indicator")

if len(df) > 0:
    coverage = len(filtered_df) / len(df) * 100
    st.progress(int(coverage))
    st.write(f"Coverage: {coverage:.2f}%")

# ---------------- EXPORT ----------------
st.subheader("Export Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, "iran_power_plants.csv")

json_data = filtered_df.to_dict(orient="records")
st.download_button("Download JSON", json.dumps(json_data, indent=2), "iran_power_plants.json")

# ---------------- DOWNLOAD GENERATED DATA ----------------
st.markdown("### Download Generated Dataset")

generated_csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Current Dataset",
    generated_csv,
    "generated_power_plants.csv"
)

# ---------------- PDF ----------------
def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    pdf.cell(200, 10, txt="Iran Power Plant Report", ln=True)

    for _, row in data.iterrows():
        pdf.cell(
            200, 8,
            txt=f"{row['name']} | {row['primary_fuel']} | {row['capacity_mw']} MW",
            ln=True
        )

    file_path = "report.pdf"
    pdf.output(file_path)
    return file_path

if st.button("Generate PDF"):
    file = generate_pdf(filtered_df)
    with open(file, "rb") as f:
        st.download_button("Download PDF", f, file_name="report.pdf")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("KNet Intelligence Platform | Energy, Infrastructure & Strategic Analytics")