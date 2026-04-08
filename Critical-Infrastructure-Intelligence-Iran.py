



 # Critical-Infrastructure-Intelligence-Platform
 # Auto-load Global Power Plant Database
 # Country = Iran pre-filter
 # KPI Dashboard (Total Plants, Capacity, Renewable %)
 # Advanced filters (fuel type, capacity range)
 # Interactive map + clustering
 # Charts (fuel mix, top plants, distribution)
 # Data quality indicator (coverage %)
 # Export:CSV, JSON, PDF report (form, atted)

 # Professional UI styling (blue header, centered)
 # Sidebar controls (modern dashboard style)


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
st.markdown("<h1 style='text-align:center;color:blue;font-weight:bold;'>Iran's-Critical-Energy-Infrastructure-Intelligence-Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:blue;font-weight:bold;'>Developed by Randy Singh - Kalsnet (KNet) Consulting Group</h3>", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
st.sidebar.subheader("Upload Dataset (Optional)")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# ---------------- SAMPLE DATA GENERATOR ----------------
def generate_sample_data(n=120):
    fuels = ["Gas","Oil","Hydro","Solar","Wind"]
    return pd.DataFrame({
        "country_long": ["Iran"] * n,
        "name": [f"Plant_{i}" for i in range(n)],
        "primary_fuel": np.random.choice(fuels, n),
        "capacity_mw": np.random.randint(50, 500, n),
        "latitude": np.random.uniform(25, 38, n),
        "longitude": np.random.uniform(44, 63, n)
    })

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data(uploaded_file):
    if uploaded_file:
        return pd.read_csv(uploaded_file)
    elif os.path.exists("global_power_plant_database.csv"):
        return pd.read_csv("global_power_plant_database.csv")
    else:
        st.warning("Dataset not found. Using generated sample data.")
        return generate_sample_data(120)

df = load_data(uploaded_file)

if df.empty:
    st.error("No data available.")
    st.stop()

df = df[df["country_long"] == "Iran"]

# ---------------- SIDEBAR ----------------
st.sidebar.header("Filters")

fuel = st.sidebar.multiselect("Fuel Type", df["primary_fuel"].unique(), default=df["primary_fuel"].unique())
capacity = st.sidebar.slider("Capacity (MW)", 0, int(df["capacity_mw"].max()), (0, int(df["capacity_mw"].max())))

filtered_df = df[
    (df["primary_fuel"].isin(fuel)) &
    (df["capacity_mw"].between(capacity[0], capacity[1]))
]

# ---------------- EXPLANATIONS ----------------
st.markdown("## 🔹 Fuel Types & Relevance")
st.info("""
- **Gas:** Primary source for rapid power generation; critical for baseline energy supply.
- **Oil:** Backup and emergency generation; important during supply disruptions.
- **Hydro:** Renewable and stable; depends on water availability.
- **Solar:** Clean energy; dependent on sunlight conditions.
- **Wind:** Renewable; varies with wind patterns.

 These fuel types help assess **energy resilience, dependency, and vulnerability**.
""")

st.markdown("## 🔹 Data Fields Explained")
st.info("""
- **Plant Name:** Identifies the facility (collected from national energy registries)
- **Primary Fuel:** Type of energy source used
- **Capacity (MW):** Maximum power output (from engineering specifications)
- **Latitude/Longitude:** Geographic location (from GIS/satellite data)
- **Country:** Used for geopolitical filtering

 Data typically comes from **government databases, satellite mapping, and energy reports**.
""")

# ---------------- KPI ----------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Plants", len(filtered_df))
col2.metric("Total Capacity (MW)", int(filtered_df["capacity_mw"].sum()))

renewable_pct = len(filtered_df[filtered_df["primary_fuel"].isin(["Solar","Wind","Hydro"])]) / len(filtered_df) * 100 if len(filtered_df) else 0
col3.metric("Renewable %", f"{renewable_pct:.2f}%")

st.markdown("---")

# ---------------- MAP ----------------
st.subheader("Power Plant Locations")

st.info("""
This map shows where each power plant is physically located.

- Each dot = a power plant  
- Bigger dot = higher capacity  
- Color = fuel type  

 Example:
A large red dot means a **high-capacity oil plant**, while a green dot may represent **renewable energy like hydro or wind**.
""")

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

# ---------------- CHARTS ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Capacity by Fuel")
    st.info("""
This chart shows how total power capacity is distributed across fuel types.

 Helps answer:
- Which energy source dominates?
- How dependent is the country on fossil fuels vs renewables?
""")
    fig1 = px.pie(filtered_df, names="primary_fuel", values="capacity_mw")
    st.plotly_chart(fig1)

with col2:
    st.subheader("Top 10 Plants")
    st.info("""
This chart highlights the largest power plants by capacity.

 Helps identify:
- Critical infrastructure nodes
- High-value strategic targets
- Key contributors to national power supply
""")
    top10 = filtered_df.sort_values("capacity_mw", ascending=False).head(10)
    fig2 = px.bar(top10, x="name", y="capacity_mw")
    st.plotly_chart(fig2)

# ---------------- SAMPLE DATA DOWNLOAD ----------------
st.markdown("## 🔹 Generate Sample Dataset")

sample_df = generate_sample_data(120)
csv_sample = sample_df.to_csv(index=False).encode("utf-8")

st.download_button("Download 100+ Sample Dataset", csv_sample, "sample_power_data.csv")

# ---------------- EXPORT ----------------
st.subheader("Export Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, "iran_power_plants.csv")

json_data = filtered_df.to_dict(orient="records")
st.download_button("Download JSON", json.dumps(json_data, indent=2), "iran_power_plants.json")

# ---------------- PDF ----------------
def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    pdf.cell(200, 10, txt="Iran Power Plant Report", ln=True)

    for _, row in data.iterrows():
        pdf.cell(200, 8, txt=f"{row['name']} | {row['primary_fuel']} | {row['capacity_mw']} MW", ln=True)

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
