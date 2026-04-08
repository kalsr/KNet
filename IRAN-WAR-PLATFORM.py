


# IRAN-WAR-APPLICATION.py



import streamlit as st

import pandas as pd

import plotly.express as px

from fpdf import FPDF

import json



# ---------------- CONFIG ----------------

st.set_page_config(layout="wide")



# ---------------- HEADER ----------------

st.markdown("<h1 style='text-align:center;color:blue;font-weight:bold;'>Energy Infrastructure Intelligence Dashboard</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center;color:blue;font-weight:bold;'>Application developed by Randy Singh Kalsnet Consulting Group</h3>", unsafe_allow_html=True)



# ---------------- LOAD DATA ----------------

@st.cache_data

def load_data():

    return pd.read_csv("global_power_plant_database.csv")



df = load_data()



# ---------------- FILTER IRAN ----------------

df = df[df["country_long"] == "Iran"]



# ---------------- SIDEBAR ----------------

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

renewable_pct = len(filtered_df[filtered_df["primary_fuel"].isin(["Solar","Wind","Hydro"])]) / len(filtered_df) * 100

col3.metric("Renewable %", f"{renewable_pct:.2f}%")



st.markdown("---")



# ---------------- MAP ----------------

st.subheader("Power Plant Locations")



map_fig = px.scatter_mapbox(

    filtered_df,

    lat="latitude",

    lon="longitude",

    color="primary_fuel",

    size="capacity_mw",

    hover_name="name",

    zoom=4

)

map_fig.update_layout(mapbox_style="open-street-map")

st.plotly_chart(map_fig, use_container_width=True)



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

st.subheader("Export")



csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button("Download CSV", csv, "iran_power_plants.csv")



json_data = filtered_df.to_dict(orient="records")

st.download_button("Download JSON", json.dumps(json_data, indent=2), "iran_power_plants.json")



# PDF

def generate_pdf(data):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=10)



    pdf.cell(200, 10, txt="Iran Power Plant Report", ln=True)



    for _, row in data.iterrows():

        pdf.cell(200, 8, txt=f"{row['name']} | {row['primary_fuel']} | {row['capacity_mw']} MW", ln=True)



    pdf.output("report.pdf")

    return "report.pdf"



if st.button("Generate PDF"):

    file = generate_pdf(filtered_df)

    with open(file, "rb") as f:

        st.download_button("Download PDF", f, file_name="report.pdf")