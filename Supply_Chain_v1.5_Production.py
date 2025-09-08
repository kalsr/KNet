# LAST 1.5 PYTHON

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
# Page config
# ---------------------------
st.set_page_config(page_title="KNet Designed - AI SBOM Monitor", layout="wide")
st.title("KNet Designed AI SBOM / Supply-Chain Monitor (Production Ready)")
st.markdown("""
Monitor software package manifests for risky dependencies using **AI/ML**.  
Generate sample data, upload SBOM files, visualize risk levels, and download results.
""")

# ---------------------------
# CSS for buttons & badges
# ---------------------------
st.markdown("""
<style>
div.stButton > button {height:3em; width:12em; border-radius:8px; font-size:16px; color:white;}
div.stButton > button:nth-child(1){background-color:#16a34a;}
div.stButton > button:nth-child(2){background-color:#0ea5e9;}
div.stButton > button:nth-child(3){background-color:#ef4444;}
div.stButton > button:nth-child(4){background-color:#f97316;}
.badge-high {background-color:#ef4444; color:white; padding:3px 8px; border-radius:6px;}
.badge-medium {background-color:#f59e0b; color:white; padding:3px 8px; border-radius:6px;}
.badge-low {background-color:#10b981; color:white; padding:3px 8px; border-radius:6px;}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Sample SBOM generator
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
# Buttons & File Upload
# ---------------------------
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Generate Sample SBOM"):
        st.session_state['sbom_df'] = generate_sample_sbom(100)
        st.session_state['run_ml'] = False
        st.success("Sample SBOM generated!")

with col2:
    if st.button("Run AI Risk Detection"):
        st.session_state['run_ml'] = True

with col3:
    if st.button("Refresh SBOM"):
        st.session_state['sbom_df'] = generate_sample_sbom(100)
        st.session_state['run_ml'] = False
        st.success("SBOM refreshed!")

with col4:
    if st.button("Clear Records"):
        st.session_state['sbom_df'] = pd.DataFrame(columns=["timestamp","package","version","supplier","license","latest_known_version"])
        st.session_state['sbom_df_ml'] = pd.DataFrame()
        st.session_state['run_ml'] = False
        st.success("SBOM records cleared!")

uploaded_file = st.file_uploader("Upload SBOM (CSV/JSON/XLSX)", type=['csv','json','xlsx'])
if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            st.session_state['sbom_df'] = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            st.session_state['sbom_df'] = pd.read_json(uploaded_file)
        else:
            st.session_state['sbom_df'] = pd.read_excel(uploaded_file)
        st.session_state['run_ml'] = False
        st.success("File uploaded successfully!")
    except Exception as e:
        st.error(f"Upload failed: {e}")

# Initialize session state
if 'sbom_df' not in st.session_state:
    st.session_state['sbom_df'] = generate_sample_sbom(100)
if 'run_ml' not in st.session_state:
    st.session_state['run_ml'] = False

df = st.session_state['sbom_df']

# ---------------------------
# Feature Engineering
# ---------------------------
def preprocess_features(df):
    df = df.copy()
    version_split = df['version'].str.split('.', expand=True)
    df['major_version'] = version_split[0].astype(int)
    df['minor_version'] = version_split[1].astype(int)
    latest_split = df['latest_known_version'].str.split('.', expand=True)
    df['latest_major'] = latest_split[0].astype(int)
    df['latest_minor'] = latest_split[1].astype(int)
    df['untrusted_supplier'] = df['supplier'].isin(["unknown-source","thirdparty-supplier"]).astype(int)
    df['license_risk'] = df['license'].isin(["Proprietary","UNKNOWN","GPL-2.0"]).astype(int)
    df['known_vuln'] = df['package'].isin(["openssl-fips","pkg-legacy","http-parser"]).astype(int)
    df['version_outdated'] = (df['major_version'] < df['latest_major']).astype(int)
    le_supplier = LabelEncoder()
    le_license = LabelEncoder()
    df['supplier_enc'] = le_supplier.fit_transform(df['supplier'])
    df['license_enc'] = le_license.fit_transform(df['license'])
    feature_cols = ['major_version','minor_version','latest_major','latest_minor',
                    'supplier_enc','license_enc','untrusted_supplier','license_risk','known_vuln','version_outdated']
    return df, feature_cols

# ---------------------------
# AI Risk Prediction
# ---------------------------
st.subheader("AI Risk Prediction")
if st.session_state['run_ml'] and not df.empty:
    df_proc, feature_cols = preprocess_features(df)
    rng = np.random.default_rng()
    df_proc['risk_level'] = rng.choice(['LOW','MEDIUM','HIGH'], size=len(df_proc))
    y = pd.factorize(df_proc['risk_level'])[0]
    X = df_proc[feature_cols]
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    preds = clf.predict(X)
    df_proc['predicted_risk'] = pd.Series(preds).map({0:'LOW',1:'MEDIUM',2:'HIGH'}).fillna('LOW')
    st.session_state['sbom_df_ml'] = df_proc
    st.success("AI Risk Prediction Completed!")

# ---------------------------
# Display Table
# ---------------------------
st.subheader("SBOM Table")
if 'sbom_df_ml' in st.session_state and not st.session_state['sbom_df_ml'].empty:
    display_df = st.session_state['sbom_df_ml']
else:
    display_df = df

# Ensure predicted_risk exists
if 'predicted_risk' not in display_df.columns:
    display_df['predicted_risk'] = 'LOW'

def render_badge(risk):
    if risk=='HIGH':
        return f"<span class='badge-high'>{risk}</span>"
    elif risk=='MEDIUM':
        return f"<span class='badge-medium'>{risk}</span>"
    else:
        return f"<span class='badge-low'>{risk}</span>"

display_df['risk_badge'] = display_df['predicted_risk'].fillna('LOW').apply(render_badge)

if not display_df.empty:
    st.markdown(display_df.to_html(escape=False, index=False), unsafe_allow_html=True)
else:
    st.info("No SBOM records to display. Generate or upload data.")

# ---------------------------
# Charts
# ---------------------------
st.subheader("Charts")
if not display_df.empty and 'predicted_risk' in display_df.columns:
    pie_data = display_df['predicted_risk'].value_counts().reset_index()
    pie_data.columns = ['risk_level','count']
    pie_chart = alt.Chart(pie_data).mark_arc(innerRadius=50).encode(
        theta='count:Q',
        color=alt.Color('risk_level:N', scale=alt.Scale(range=["#ef4444","#f59e0b","#10b981"]))
    )
    st.altair_chart(pie_chart, use_container_width=True)

    display_df['timestamp_dt'] = pd.to_datetime(display_df['timestamp'], errors='coerce').fillna(pd.Timestamp.now())
    trend_df = display_df.groupby([pd.Grouper(key='timestamp_dt', freq='15T'),'predicted_risk']).size().reset_index(name='count')
    trend_chart = alt.Chart(trend_df).mark_line(point=True).encode(
        x='timestamp_dt:T',
        y='count:Q',
        color='predicted_risk:N'
    ).properties(title="Risk Levels Over Time")
    st.altair_chart(trend_chart, use_container_width=True)

# ---------------------------
# Download
# ---------------------------
st.subheader("Download Results")
def convert_csv(df):
    return df.drop(columns=['risk_badge'], errors='ignore').to_csv(index=False).encode('utf-8')
def convert_json(df):
    return df.drop(columns=['risk_badge'], errors='ignore').to_json(orient='records', indent=2).encode('utf-8')

if not display_df.empty:
    st.download_button("Download CSV", convert_csv(display_df), "sbom_ai.csv", "text/csv")
    st.download_button("Download JSON", convert_json(display_df), "sbom_ai.json", "application/json")


