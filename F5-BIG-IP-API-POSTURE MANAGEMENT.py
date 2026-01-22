

# ============================================================
# F5 BIG-IP API POSTURE MANAGEMENT – STREAMLIT VERSION
# Designed by Randy Singh
# Kalsnet (KNet) Consulting Group
# ============================================================

import streamlit as st
import pandas as pd
import random
import time
import matplotlib.pyplot as plt

# -------------------------------
# STREAMLIT PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="F5 BIG-IP API Posture Management", layout="wide")

# -------------------------------
# TOP BLUE BANNER
# -------------------------------
st.markdown(
    """
    <div style="background-color:#003366;padding:15px;border-radius:5px">
        <h2 style="color:white;text-align:center;">
            API Posture Management Program<br>
            Designed by Randy Singh – Kalsnet (KNet) Consulting Group
        </h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# -------------------------------
# RESET HANDLER
# -------------------------------
if "reset" not in st.session_state:
    st.session_state.reset = False

def reset_all():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()

# -------------------------------
# SYNTHETIC DATA GENERATOR
# -------------------------------
def generate_f5_bigip_records(num_records):
    apis = [
        '/api/v1/users', '/api/v1/products', '/api/v1/orders',
        '/api/v2/customers', '/api/v2/inventory',
        '/login', '/logout'
    ]
    status_codes = [200, 201, 204, 400, 401, 403, 404, 429, 500]

    records = []
    for _ in range(num_records):
        record = {
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()),
            "src_ip": f"203.0.{random.randint(1,255)}.{random.randint(1,255)}",
            "dst_ip": f"192.168.{random.randint(0,1)}.{random.randint(1,255)}",
            "src_port": random.randint(1024, 65535),
            "dst_port": random.choice([80, 443]),
            "virtual_server": "vs_http",
            "pool": "HTTP_Pool",
            "pool_member": f"192.168.{random.randint(0,1)}.{random.randint(1,255)}",
            "http_request": f"GET {random.choice(apis)} HTTP/1.1",
            "status_code": random.choice(status_codes),
            "bytes_in": random.randint(100, 5000),
            "bytes_out": random.randint(500, 10000),
            "request_time": round(random.uniform(0.1, 2.0), 3)
        }
        records.append(record)

    return pd.DataFrame(records)

# -------------------------------
# API POSTURE ANALYSIS
# -------------------------------
def analyze_posture(df):
    df["api"] = df["http_request"].str.split().str[1]

    posture = df.groupby("api").agg(
        hits=("api", "count"),
        success=("status_code", lambda x: (x < 400).sum()),
        failure=("status_code", lambda x: (x >= 400).sum()),
        avg_latency=("request_time", "mean")
    ).reset_index()

    return posture

# -------------------------------
# THREAT DETECTION
# -------------------------------
def detect_threats(df, posture):
    threats = []
    recommendations = []

    if (df["status_code"] == 401).sum() > 5:
        threats.append("Excessive authentication failures (401)")
        recommendations.append("Implement MFA and credential brute-force protection")

    if (df["status_code"] == 429).sum() > 3:
        threats.append("API rate abuse detected (429)")
        recommendations.append("Enable F5 BIG-IP rate limiting and bot defense")

    if (df["status_code"] == 500).sum() > 3:
        threats.append("Backend instability (500 errors)")
        recommendations.append("Investigate backend services and enable health checks")

    if posture["avg_latency"].max() > 1.5:
        threats.append("High API latency detected")
        recommendations.append("Enable caching, optimize backend services")

    if not threats:
        threats.append("No critical threats detected")
        recommendations.append("Continue continuous monitoring")

    return threats, recommendations

# -------------------------------
# SIDEBAR CONTROLS
# -------------------------------
st.sidebar.header("Controls")

record_count = st.sidebar.slider(
    "Generate Synthetic F5 Records",
    min_value=0,
    max_value=100,
    value=50
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Real F5 BIG-IP CSV Data",
    type=["csv"]
)

# -------------------------------
# DATA SELECTION
# -------------------------------
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Real F5 data loaded successfully")
else:
    df = generate_f5_bigip_records(record_count)

# -------------------------------
# ANALYSIS
# -------------------------------
posture = analyze_posture(df)
threats, recommendations = detect_threats(df, posture)

# -------------------------------
# DASHBOARD METRICS
# -------------------------------
st.subheader("API Usage & Security Posture")

col1, col2, col3 = st.columns(3)
col1.metric("Total API Calls", len(df))
col2.metric("Unique APIs", df["http_request"].nunique())
col3.metric("Detected Threats", len(threats))

# -------------------------------
# CHARTS
# -------------------------------
st.subheader("HTTP Status Code Distribution")
fig1, ax1 = plt.subplots()
df["status_code"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax1)
ax1.set_ylabel("")
st.pyplot(fig1)

st.subheader("API Hits per Endpoint")
fig2, ax2 = plt.subplots()
posture.set_index("api")["hits"].plot.bar(ax=ax2)
ax2.set_ylabel("Hits")
ax2.set_xlabel("API Endpoint")
st.pyplot(fig2)

# -------------------------------
# TABLES
# -------------------------------
st.subheader("API Posture Summary")
st.dataframe(posture)

# -------------------------------
# THREATS & MITIGATION
# -------------------------------
st.subheader("Detected Threats")
for t in threats:
    st.error(t)

st.subheader("Mitigation Recommendations")
for r in recommendations:
    st.success(r)

# -------------------------------
# RAW DATA
# -------------------------------
with st.expander("View Raw F5 BIG-IP Records"):
    st.dataframe(df)

# -------------------------------
# RESET BUTTON
# -------------------------------
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: red;
        color: white;
        font-size: 18px;
        height: 50px;
        width: 100%;
        border-radius: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("RESET ALL DATA"):
    reset_all()
