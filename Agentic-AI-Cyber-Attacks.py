# Below is a clean enterprise structure (single-file version for now, can later split into modules):

import streamlit as st

import pandas as pd

import numpy as np

import sqlite3

import matplotlib.pyplot as plt

from sklearn.ensemble import IsolationForest

from fpdf import FPDF

import hashlib

import random



# -----------------------------

# BRANDING

# -----------------------------

st.markdown("""

<h1 style='color:blue; text-align:center;'>

KNet Cyber Range Platform<br>

Developed by Randy Singh (Kalsnet Consulting Group)

</h1>

""", unsafe_allow_html=True)



# -----------------------------

# DATABASE SETUP

# -----------------------------

conn = sqlite3.connect("knet.db", check_same_thread=False)

c = conn.cursor()



c.execute('''CREATE TABLE IF NOT EXISTS users

             (username TEXT, password TEXT, role TEXT)''')



# Default admin

def create_user(u, p, r):

    c.execute("INSERT INTO users VALUES (?, ?, ?)", (u, hashlib.sha256(p.encode()).hexdigest(), r))

    conn.commit()



# -----------------------------

# AUTH SYSTEM

# -----------------------------

def login(username, password):

    c.execute("SELECT * FROM users WHERE username=? AND password=?",

              (username, hashlib.sha256(password.encode()).hexdigest()))

    return c.fetchone()



st.sidebar.header("🔐 Login")



username = st.sidebar.text_input("Username")

password = st.sidebar.text_input("Password", type="password")



if st.sidebar.button("Login"):

    user = login(username, password)

    if user:

        st.session_state["role"] = user[2]

        st.success(f"Logged in as {user[2]}")

    else:

        st.error("Invalid credentials")



# -----------------------------

# DATA GENERATION

# -----------------------------

def generate_data(n):

    return pd.DataFrame({

        "Account": range(n),

        "Balance": np.random.randint(1000, 50000, n),

        "Transactions": np.random.randint(1, 100, n),

        "Status": ["Normal"]*n

    })



# -----------------------------

# ATTACK ENGINE

# -----------------------------

def attack_engine(df):

    df = df.copy()

    idx = np.random.choice(df.index, int(len(df)*0.3), replace=False)



    for i in idx:

        df.loc[i, "Balance"] *= random.uniform(0.2, 0.5)

        df.loc[i, "Status"] = "Compromised"



    return df



# -----------------------------

# DEFENSE ENGINE

# -----------------------------

def defense_engine(df):

    df = df.copy()

    df.loc[df["Status"]=="Compromised", "Status"] = "Recovered"

    df["Balance"] *= 1.1

    return df



# -----------------------------

# AI DETECTION

# -----------------------------

def detect_anomaly(df):

    model = IsolationForest(contamination=0.2)

    df["Anomaly"] = model.fit_predict(df[["Balance","Transactions"]])

    return df



# -----------------------------

# PDF REPORT

# -----------------------------

def export_pdf(df):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=8)



    for i, row in df.iterrows():

        pdf.cell(200, 6, txt=str(row.to_dict()), ln=True)



    pdf.output("report.pdf")



# -----------------------------

# MAIN APP

# -----------------------------

if "data" not in st.session_state:

    st.session_state.data = None



if "role" in st.session_state:



    role = st.session_state["role"]



    st.sidebar.header("⚙️ Controls")

    n = st.sidebar.slider("Records", 10, 100, 50)



    if st.sidebar.button("Generate Data"):

        st.session_state.data = generate_data(n)



    if st.sidebar.button("Reset"):

        st.session_state.data = None



    if st.session_state.data is not None:

        df = st.session_state.data



        st.subheader("📊 Financial System State")

        st.dataframe(df)



        # Admin only attack

        if role == "Admin":

            if st.button("🚨 Launch Attack"):

                st.session_state.data = attack_engine(df)



        # SOC defense

        if role in ["SOC", "Admin"]:

            if st.button("🛡️ Respond to Attack"):

                st.session_state.data = defense_engine(df)



        # AI detection

        if st.button("🤖 Run AI Detection"):

            st.session_state.data = detect_anomaly(df)



        # KPIs

        total = df["Balance"].sum()

        compromised = (df["Status"]=="Compromised").sum()



        col1, col2 = st.columns(2)

        col1.metric("Total Assets", f"${total:,.0f}")

        col2.metric("Compromised Accounts", compromised)



        # Visualization

        st.subheader("📉 Attack Impact")

        fig, ax = plt.subplots()

        df["Status"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)

        st.pyplot(fig)



        # Explanation

        st.subheader("📘 Explanation")

        st.write("""

        - Compromised: Financial breach occurred

        - Recovered: Defense actions applied

        - Anomaly: AI flagged suspicious activity

        """)



        # Export

        st.subheader("📁 Export")

        st.download_button("CSV", df.to_csv(), "data.csv")

        st.download_button("JSON", df.to_json(), "data.json")



        if st.button("Generate PDF"):

            export_pdf(df)

            with open("report.pdf", "rb") as f:

                st.download_button("Download PDF", f, "report.pdf")