

# Critical-Infrastructure-Intelligence-Platform (Enhanced with City Mapping)

import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import json
import os
import numpy as np

st.set_page_config(layout="wide")

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;color:blue;font-weight:bold;'>Iran's-Critical-Energy-Infrastructure-Intelligence-Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:blue;font-weight:bold;'>Developed by Randy Singh - Kalsnet (KNet) Consulting Group</h3>", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
st.sidebar.subheader("Upload Dataset (Optional)")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# ---------------- SAMPLE DATA ----------------
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

# ---------------- CITY MAPPING LOGIC ----------------
# Known major Iranian cities with lat/long
cities = {
    "Tehran": (35.6892, 51.3890),
    "Mashhad": (36.2605, 59.6168),
    "Isfahan": (32.6546, 51.6680),
    "Shiraz": (29.5918, 52.5837),
    "Tabriz": (38.0962, 46.2738),
    "Ahvaz": (31.3183, 48.6706),
    "Qom": (34.6416, 50.8746),
    "Kermanshah": (34.3142, 47.0650),
    "Urmia": (37.5527, 45.0761),
    "Zahedan": (29.4963, 60.8629)
}

# Function to find nearest city
def get_nearest_city(lat, lon):
    closest_city = None
    min_dist = float("inf")
    for city, (clat, clon) in cities.items():
        dist = (lat - clat)**2 + (lon - clon)**2
        if dist < min_dist:
            min_dist = dist
            closest_city = city
    return closest_city

# Apply city mapping
df["City"] = df.apply(lambda row: get_nearest_city(row["latitude"], row["longitude"]), axis=1)

# ---------------- SIDEBAR FILTER ----------------
st.sidebar.header("Filters")

fuel = st.sidebar.multiselect("Fuel Type", df["primary_fuel"].unique(), default=df["primary_fuel"].unique())
capacity = st.sidebar.slider("Capacity (MW)", 0, int(df["capacity_mw"].max()), (0, int(df["capacity_mw"].max())))

filtered_df = df[
    (df["primary_fuel"].isin(fuel)) &
    (df["capacity_mw"].between(capacity[0], capacity[1]))
]

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
Each point represents a power plant location:

- Latitude/Longitude → Exact GPS coordinates  
- City → Closest major city derived from coordinates  
- Size → Capacity (MW)  
- Color → Fuel type  

This enables **geospatial intelligence and infrastructure awareness**
""")

if not filtered_df.empty:
    fig = px.scatter_mapbox(
        filtered_df,
        lat="latitude",
        lon="longitude",
        color="primary_fuel",
        size="capacity_mw",
        hover_name="name",
        hover_data=["City"],
        zoom=4
    )
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- CITY TABLE ----------------
st.markdown("## 🔹 Power Plant Locations (City + Coordinates)")

st.dataframe(
    filtered_df[["name", "City", "latitude", "longitude", "primary_fuel", "capacity_mw"]],
    use_container_width=True
)

st.info("""
**How City Mapping Works:**
- Each plant has latitude & longitude
- System compares coordinates with known city locations
- Assigns nearest city using distance calculation

👉 This is commonly used in **GIS systems, satellite intelligence, and defense mapping**
""")

# ---------------- CHARTS ----------------
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
        pdf.cell(
            200, 8,
            txt=f"{row['name']} | {row['City']} | {row['primary_fuel']} | {row['capacity_mw']} MW",
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
