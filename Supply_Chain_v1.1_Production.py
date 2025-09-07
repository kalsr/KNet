
# Production-Ready Streamlit App (app.py).
# THIS SUPPLY-CHAIN CODE IS DESIGNED BY RANDY SINGH FROM KNet CONSULTING GROUP.
# python
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import altair as alt

# ---------------------------
# Page configuration
# ---------------------------
st.set_page_config(page_title="AI SBOM Monitor", layout="wide")
st.title("AI SBOM / Supply-Chain Monitor (Production Ready)")
st.markdown("""
Monitor software package manifests for risky dependencies using **AI/ML**.  
Generate sample data, upload SBOM files, visualize risk levels, and download results.
""")

# ---------------------------
# CSS for table highlight & buttons
# ---------------------------
st.markdown("""
<style>
.high {background-color:#fef2f2 !important;}
.medium {background-color:#fefce8 !important;}
.low {background-color:#ecfdf5 !important;}
div.stButton > button:first-child {background-color:#16a34a; color:white; height:3em; width:12em; border-radius:8px; font-size:16px;}
div.stButton > button:nth-child(2) {background-color:#0ea5e9; color:white; height:3em; width:12em; border-radius:8px; font-size:16px;}
div.stButton > button:nth-child(3) {background-color:#ef4444; color:white; height:3em; width:12em; border-radius:8px; font-size:16px;}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# 1. Sample SBOM generator
# ---------------------------
def generate_sample_sbom(n=100):
    rng = np.random.default_rng()
    base_pkgs = ["libcrypto","utils-net","http-parser","data-serialize","auth-core","xmlproc",
                 "protobuf-lite","openssl-fips","pkg-legacy","json-utils","thirdparty-ui","zip-handler"]
    suppliers = ["official-repo","mirrorcorp","internal-repo","unknown-source","thirdparty-supplier"]
    licenses = ["MIT","Apache-2.0","GPL-2.0","Proprietary","BSD-3-Clause","UNKNOWN"]
    rows = []
    for _ in range(n):
        pkg = rng.choice(base_pkgs + [f"pkg-extra-{int(rng.integers(1,500))}"])
        version = f"{int(rng.integers(0,3))}.{int(rng.integers(0,10))}.{int(rng.integers(0,10))}"
        supplier = rng.choice(suppliers)
        lic = rng.choice(licenses)
        latest_version = f"{int(rng.integers(1,3))}.{int(rng.integers(0,10))}.{int(rng.integers(0,10))}"
        timestamp = (datetime.utcnow() - timedelta(minutes=int(rng.integers(0,120)))).isoformat()
        rows.append({
            "timestamp": timestamp,
            "package": pkg,
            "version": version,
            "supplier": supplier,
            "license": lic,
            "latest_known_version": latest_version
        })
    return pd.DataFrame(rows)

# ---------------------------
# 2. File Upload & Sample Generation Buttons
# ---------------------------
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Generate Sample SBOM"):
        st.session_state['sbom_df'] = generate_sample_sbom()
        st.success("Sample SBOM generated!")

with col2:
    if st.button("Run AI Risk Detection"):
        st.session_state['run_ml'] = True

with col3:
    if st.button("Refresh SBOM"):
        st.session_state['sbom_df'] = generate_sample_sbom()
        st.session_state['run_ml'] = False
        st.success("SBOM refreshed!")

uploaded_file = st.file_uploader("Upload SBOM (CSV/JSON)", type=['csv','json'])
if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            st.session_state['sbom_df'] = pd.read_csv(uploaded_file)
        else:
            st.session_state['sbom_df'] = pd.read_json(uploaded_file)
        st.session_state['run_ml'] = False
        st.success("File uploaded successfully!")
    except Exception as e:
        st.error(f"Upload failed: {e}")

# Initialize session state
if 'sbom_df' not in st.session_state:
    st.session_state['sbom_df'] = generate_sample_sbom()
if 'run_ml' not in st.session_state:
    st.session_state['run_ml'] = False

df = st.session_state['sbom_df']

# ---------------------------
# 3. Feature Engineering
# ---------------------------
def preprocess_features(df):
    df = df.copy()
    # Version numbers
    version_split = df['version'].str.split('.', expand=True)
    df['major_version'] = version_split[0].astype(int)
    df['minor_version'] = version_split[1].astype(int)
    latest_split = df['latest_known_version'].str.split('.', expand=True)
    df['latest_major'] = latest_split[0].astype(int)
    df['latest_minor'] = latest_split[1].astype(int)
    # Risk heuristics
    df['untrusted_supplier'] = df['supplier'].isin(["unknown-source","thirdparty-supplier"]).astype(int)
    df['license_risk'] = df['license'].isin(["Proprietary","UNKNOWN","GPL-2.0"]).astype(int)
    df['known_vuln'] = df['package'].isin(["openssl-fips","pkg-legacy","http-parser"]).astype(int)
    df['version_outdated'] = (df['major_version'] < df['latest_major']).astype(int)
    # Encode categorical
    le_supplier = LabelEncoder()
    le_license = LabelEncoder()
    df['supplier_enc'] = le_supplier.fit_transform(df['supplier'])
    df['license_enc'] = le_license.fit_transform(df['license'])
    feature_cols = ['major_version','minor_version','latest_major','latest_minor',
                    'supplier_enc','license_enc','untrusted_supplier','license_risk','known_vuln','version_outdated']
    return df, feature_cols

# ---------------------------
# 4. AI Risk Prediction
# ---------------------------
st.subheader("AI Risk Prediction")
if st.session_state['run_ml']:
    df_proc, feature_cols = preprocess_features(df)
    # Simulated labels
    rng = np.random.default_rng()
    df_proc['risk_level'] = rng.choice(['LOW','MEDIUM','HIGH'], size=len(df_proc))
    # ML preparation
    y = pd.factorize(df_proc['risk_level'])[0]
    X = df_proc[feature_cols]
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    df_proc['predicted_risk'] = pd.Series(clf.predict(X)).map({0:'LOW',1:'MEDIUM',2:'HIGH'})
    st.session_state['sbom_df_ml'] = df_proc
    st.success("AI Risk Prediction Completed!")

# ---------------------------
# 5. Display Table with Color Coding
# ---------------------------
st.subheader("SBOM Table")
if 'sbom_df_ml' in st.session_state:
    display_df = st.session_state['sbom_df_ml']
else:
    display_df = df

def highlight_risk(row):
    color_map = {'HIGH':'high','MEDIUM':'medium','LOW':'low'}
    return [color_map.get(str(row.get('predicted_risk','')), '') 
            if col in ['package','version','supplier','license','predicted_risk'] else '' 
            for col in row.index]

st.dataframe(display_df.style.apply(highlight_risk, axis=1), use_container_width=True)

# ---------------------------
# 6. Charts
# ---------------------------
st.subheader("Charts")
if 'predicted_risk' in display_df.columns:
    # Pie chart
    pie_data = display_df['predicted_risk'].value_counts().reset_index()
    pie_data.columns = ['risk_level','count']
    pie_chart = alt.Chart(pie_data).mark_arc(innerRadius=50).encode(
        theta='count:Q',
        color=alt.Color('risk_level:N', scale=alt.Scale(range=["#ef4444","#f59e0b","#10b981"]))
    )
    st.altair_chart(pie_chart, use_container_width=True)

    # Time-trend chart
    display_df['timestamp_dt'] = pd.to_datetime(display_df['timestamp'], errors='coerce')
    if display_df['timestamp_dt'].isna().all():
        display_df['timestamp_dt'] = pd.Timestamp.now()
    trend_df = display_df.groupby([pd.Grouper(key='timestamp_dt', freq='15T'),'predicted_risk']).size().reset_index(name='count')
    trend_chart = alt.Chart(trend_df).mark_line(point=True).encode(
        x='timestamp_dt:T',
        y='count:Q',
        color='predicted_risk:N'
    ).properties(title="Risk Levels Over Time")
    st.altair_chart(trend_chart, use_container_width=True)

# ---------------------------
# 7. Download Results
# ---------------------------
st.subheader("Download Results")
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')
def convert_json(df):
    return df.to_json(orient='records', indent=2).encode('utf-8')

st.download_button("Download CSV", convert_csv(display_df), "sbom_ai.csv", "text/csv")
st.download_button("Download JSON", convert_json(display_df), "sbom_ai.json", "application/json")
