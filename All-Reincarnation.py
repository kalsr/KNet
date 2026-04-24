

# Reincarnation-Life.py



import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import json

from fpdf import FPDF



# ---------------------------

# App Title

# ---------------------------

st.set_page_config(page_title="Cycle of Life Explorer", layout="wide")



st.markdown(

    """

    <h1 style='text-align: center; color: #4CAF50;'>

    🌏 Cycle of Life Explorer (8.4 Million Yonis)

    </h1>

    <h4 style='text-align: center;'>

    Developed by Randy Singh from Kalsnet (KNet) Consulting Group

    </h4>

    <hr>

    """,

    unsafe_allow_html=True

)



# ---------------------------

# Data

# ---------------------------

categories = {

    "Aquatic": {

        "count": 900000,

        "color": "#1f77b4",

        "examples": ["Fish", "Shark", "Crab", "Octopus", "Frog"],

        "desc": "Aquatic beings live in water and represent early stages of life evolution."

    },

    "Plants": {

        "count": 2000000,

        "color": "#2ca02c",

        "examples": ["Tree", "Grass", "Cactus", "Flowering plants"],

        "desc": "Plants are immobile life forms and represent foundational life energy."

    },

    "Insects": {

        "count": 1100000,

        "color": "#ff7f0e",

        "examples": ["Ant", "Bee", "Worm", "Spider", "Snake"],

        "desc": "Includes insects, reptiles, and creeping organisms."

    },

    "Birds": {

        "count": 1000000,

        "color": "#9467bd",

        "examples": ["Eagle", "Parrot", "Sparrow", "Owl"],

        "desc": "Birds symbolize freedom and mobility in higher dimensions."

    },

    "Animals": {

        "count": 3000000,

        "color": "#8c564b",

        "examples": ["Lion", "Cow", "Dog", "Elephant"],

        "desc": "Animals represent advanced physical and emotional development."

    },

    "Humans": {

        "count": 400000,

        "color": "#d62728",

        "examples": ["Human beings", "Sages", "Thinkers"],

        "desc": "Human birth allows self-awareness and spiritual liberation."

    }

}



# ---------------------------

# Helper Functions

# ---------------------------

def create_dataframe():

    return pd.DataFrame({

        "Category": list(categories.keys()),

        "Count": [categories[c]["count"] for c in categories]

    })



def generate_pdf(category, data):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)



    pdf.cell(200, 10, txt=f"Category: {category}", ln=True)

    pdf.multi_cell(0, 10, txt=data["desc"])



    pdf.cell(200, 10, txt="Examples:", ln=True)

    for item in data["examples"]:

        pdf.cell(200, 10, txt=f"- {item}", ln=True)



    file_name = f"{category}.pdf"

    pdf.output(file_name)

    return file_name



# ---------------------------

# Buttons UI

# ---------------------------

st.subheader("Select a Life Category")



cols = st.columns(len(categories))



selected_category = None



for i, cat in enumerate(categories):

    if cols[i].button(cat):

        selected_category = cat



# ---------------------------

# Display Section

# ---------------------------

if selected_category:

    data = categories[selected_category]



    st.markdown(f"## 🌟 {selected_category} Category")



    # Description

    st.write(data["desc"])



    # Examples

    st.markdown("### 📋 Example Life Forms")

    for item in data["examples"]:

        st.write(f"- {item}")



    # ---------------------------

    # Charts

    # ---------------------------

    df = create_dataframe()



    st.markdown("### 📊 Distribution Chart")

    fig, ax = plt.subplots()

    ax.bar(df["Category"], df["Count"], color=[categories[c]["color"] for c in categories])

    plt.xticks(rotation=45)

    st.pyplot(fig)



    st.markdown("### 🥧 Pie Chart")

    fig2, ax2 = plt.subplots()

    ax2.pie(df["Count"], labels=df["Category"], autopct="%1.1f%%")

    st.pyplot(fig2)



    # ---------------------------

    # Export Options

    # ---------------------------

    st.markdown("### 💾 Export Data")



    # JSON

    json_data = json.dumps(data, indent=4)

    st.download_button("Download JSON", json_data, file_name=f"{selected_category}.json")



    # CSV

    csv_df = pd.DataFrame(data["examples"], columns=["Examples"])

    csv = csv_df.to_csv(index=False)

    st.download_button("Download CSV", csv, file_name=f"{selected_category}.csv")



    # PDF

    if st.button("Generate PDF"):

        pdf_file = generate_pdf(selected_category, data)

        with open(pdf_file, "rb") as f:

            st.download_button("Download PDF", f, file_name=pdf_file)



# ---------------------------

# Footer Summary Chart

# ---------------------------

st.markdown("---")

st.markdown("### 📊 Overall Life Distribution")



df_all = create_dataframe()

st.bar_chart(df_all.set_index("Category"))