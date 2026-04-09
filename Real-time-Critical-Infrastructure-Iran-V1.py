


# ==========================================
# KNET CRITICAL INFRASTRUCTURE PLATFORM
# ENHANCED VERSION WITH USER CONTROLS
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

# ==========================================================
# 🔹 DATA SOURCE SELECTION (NEW)
# ==========================================================
st.sidebar.header("Data Source Selection")

data_source = st.sidebar.radio(
    "Choose Data Source:",
    ["Use Generated Data", "Upload Your Own Data"]
)

uploaded_file = None
if data_source == "Upload Your Own Data":
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# ==========================================================
# 🔥 REALISTIC DATA GENERATOR
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

    # Add pseudo city label (NEW)
    df["location_name"] = df["latitude"].round(2).astype(str) + ", " + df["longitude"].round(2).astype(str)

    return df

# ==========================================================
# ✅ LOAD DATA
# ==========================================================
@st.cache_data
def load_data(uploaded_file, data_source, n_records):

    try:
        if data_source == "Upload Your Own Data" and uploaded_file is not None:
            st.success("Using uploaded dataset")
            df = pd.read_csv(uploaded_file)

        elif os.path.exists("global_power_plant_database.csv"):
            st.success("Using local dataset")
            df = pd.read_csv("global_power_plant_database.csv")

        else:
            st.warning("Using system-generated dataset")
            df = generate_realistic_data(200)

        return df.head(n_records)

    except Exception as e:
        st.error(f"Error loading data: {e}")
        return generate_realistic_data(n_records)

# ==========================================================
# 🔹 RECORD SELECTION (NEW)
# ==========================================================
st.sidebar.header("Record Selection")

n_records = st.sidebar.slider("Select Number of Records", 10, 200, 100)

# ---------------- LOAD ----------------
df = load_data(uploaded_file, data_source, n_records)

# ---------------- VALIDATION ----------------
if df.empty:
    st.error("No data available")
    st.stop()

# ---------------- FILTER IRAN ----------------
if "country_long" in df.columns:
    df = df[df["country_long"] == "Iran"]

# ==========================================================
# 🔹 FILTERS
# ==========================================================
st.sidebar.header("Filters")

fuel_options = df["primary_fuel"].dropna().unique()
fuel = st.sidebar.multiselect("Fuel Type", fuel_options, default=fuel_options)

capacity_max = int(df["capacity_mw"].max())
capacity = st.sidebar.slider("Capacity (MW)", 0, capacity_max, (0, capacity_max))

filtered_df = df[
    (df["primary_fuel"].isin(fuel)) &
    (df["capacity_mw"].between(capacity[0], capacity[1]))
]

# ==========================================================
# 🔹 SHOW SELECTED DATA (NEW)
# ==========================================================
st.markdown("## Selected Data View")

st.info("Displaying filtered dataset with all available fields including geographic coordinates and fuel type.")

st.dataframe(filtered_df, use_container_width=True)

# ==========================================================
# KPI
# ==========================================================
col1, col2, col3 = st.columns(3)

col1.metric("Total Plants", len(filtered_df))
col2.metric("Total Capacity (MW)", int(filtered_df["capacity_mw"].sum()))

renewable_pct = (
    len(filtered_df[filtered_df["primary_fuel"].isin(["Solar", "Wind", "Hydro"])]) 
    / len(filtered_df) * 100
    if len(filtered_df) > 0 else 0
)

col3.metric("Renewable %", f"{renewable_pct:.2f}%")

st.markdown("---")

# ==========================================================
# MAP
# ==========================================================
st.subheader("Power Plant Locations by Fuel Type")

st.info("""
Each marker represents a power plant location.

- Color = Fuel Type  
- Size = Capacity  
- Hover = Name + Location  
""")

if not filtered_df.empty:
    fig = px.scatter_mapbox(
        filtered_df,
        lat="latitude",
        lon="longitude",
        color="primary_fuel",
        size="capacity_mw",
        hover_name="name",
        hover_data=["location_name", "capacity_mw"],
        zoom=4
    )
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# FUEL-SPECIFIC LOCATION VIEW (NEW)
# ==========================================================
st.markdown("## Fuel Type Location Breakdown")

selected_fuel = st.selectbox("Select Fuel Type to View Locations", fuel_options)

fuel_df = filtered_df[filtered_df["primary_fuel"] == selected_fuel]

st.write(f"Showing locations for: {selected_fuel}")

st.dataframe(fuel_df[["name", "primary_fuel", "capacity_mw", "latitude", "longitude", "location_name"]])

# ==========================================================
# CHARTS
# ==========================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Capacity by Fuel")
    fig1 = px.pie(filtered_df, names="primary_fuel", values="capacity_mw")
    st.plotly_chart(fig1)

with col2:
    st.subheader("Top 10 Plants")
    top10 = filtered_df.sort_values("capacity_mw", ascending=False).head(10)
    fig2 = px.bar(top10, x="name", y="capacity_mw")
    st.plotly_chart(fig2)

# ==========================================================
# DATA QUALITY
# ==========================================================
st.markdown("### Data Coverage Indicator")

coverage = len(filtered_df) / len(df) * 100 if len(df) > 0 else 0
st.progress(int(coverage))
st.write(f"Coverage: {coverage:.2f}%")

# ==========================================================
# EXPORT
# ==========================================================
st.subheader("Export Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, "iran_power_plants.csv")

json_data = filtered_df.to_dict(orient="records")
st.download_button("Download JSON", json.dumps(json_data, indent=2), "iran_power_plants.json")

# ==========================================================
# PDF
# ==========================================================
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