# Global-Threat-Detector-6g

import streamlit as st

import pandas as pd

import numpy as np

import random

import matplotlib.pyplot as plt

from fpdf import FPDF

import geopandas as gpd

from shapely.geometry import Point



# Sample threat data generator

def generate_sample_data(n=10):

    data = []

    for _ in range(n):

        # Randomly generate threat data: coordinates, threat type, timestamp, and severity

        lat = random.uniform(-90, 90)

        lon = random.uniform(-180, 180)

        threat_type = random.choice(['Missile Launch', 'Cyber-Attack', 'Drone Infiltration'])

        timestamp = pd.to_datetime(f"2025-12-01 {random.randint(0,23)}:{random.randint(0,59)}:{random.randint(0,59)}")

        severity = random.choice(['Low', 'Medium', 'High'])

        data.append([lat, lon, threat_type, timestamp, severity])

    df = pd.DataFrame(data, columns=['Latitude', 'Longitude', 'Threat Type', 'Timestamp', 'Severity'])

    return df



# Function to handle file upload (CSV)

def upload_data():

    uploaded_file = st.file_uploader("Upload your threat data (CSV)", type=["csv"])

    if uploaded_file is not None:

        data = pd.read_csv(uploaded_file)

        st.write("Data Uploaded Successfully!")

        return data

    return None



# Function to create a PDF report of the analysis

def save_to_pdf(data, filename="threat_analysis_report.pdf"):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Global Real-Time Threat Detection Report", ln=True, align='C')

    pdf.ln(10)



    for _, row in data.iterrows():

        pdf.multi_cell(0, 8, txt=f"Threat: {row['Threat Type']}\nLocation: ({row['Latitude']}, {row['Longitude']})\n"

                                  f"Timestamp: {row['Timestamp']}\nSeverity: {row['Severity']}\n")

        pdf.ln(5)



    pdf.output(filename)

    st.success(f"PDF saved as {filename}")



# Function to save results to CSV

def save_to_csv(data, filename="threat_analysis_results.csv"):

    data.to_csv(filename, index=False)

    st.success(f"Results saved to CSV: {filename}")



# Function to visualize the threat data

def visualize_threat_data(data):

    st.subheader("Threat Data Visualization")



    # Display map with threat locations (simplified version using latitude and longitude)

    gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['Longitude'], data['Latitude']))



    # Create a simple map with threats visualized

    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    ax = world.plot(figsize=(10, 6))

    gdf.plot(ax=ax, color='red', marker='o', markersize=50)



    plt.title("Global Threat Locations")

    st.pyplot(plt)



    # Show some summary statistics

    st.write(f"Total number of threats detected: {len(data)}")

    st.write(f"Threats by type:")

    st.write(data['Threat Type'].value_counts())



    # Display a severity breakdown chart

    severity_count = data['Severity'].value_counts()

    st.bar_chart(severity_count)



# Streamlit app interface

def main():

    st.title("Global Real-Time Threat Detection and Analysis")



    # Sidebar with options

    st.sidebar.header("Options")

    option = st.sidebar.selectbox("Select Action", ["Generate Sample Data", "Upload Your Data", "Reset"])



    if option == "Generate Sample Data":

        st.subheader("Generated Threat Data")

        data = generate_sample_data(n=10)

        st.write(data)

        visualize_threat_data(data)



    elif option == "Upload Your Data":

        data = upload_data()

        if data is not None:

            st.write(data)

            visualize_threat_data(data)



    elif option == "Reset":

        st.experimental_rerun()



    # Export results to CSV and PDF

    if st.button("Export to CSV"):

        if 'data' in locals():

            save_to_csv(data)

        else:

            st.warning("No data to export!")



    if st.button("Export to PDF"):

        if 'data' in locals():

            save_to_pdf(data)

        else:

            st.warning("No data to export!")



if __name__ == "__main__":

    main()



