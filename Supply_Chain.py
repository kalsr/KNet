# Features:

 # Generate 50 sample SBOM/package-manifest rows (Refresh to regenerate)

 # Upload JSON, CSV, or plain text manifests

 #  Rule-based risky dependency detection (untrusted source, suspicious version, legacy version,  

 # license concerns, known-vulnerable simulated list)

 #  Display table, highlighted flagged rows, charts, and download (CSV/JSON)

 # Small simulated MCP enrichment hook (placeholder)

 # THIS APPLICATION IS DESIGNED BY RANDY SINGH FROM KNET CONSULTING GROUP.



import streamlit as st

import pandas as pd

import numpy as np

from datetime import datetime, timedelta

import json

from io import StringIO



st.set_page_config(page_title="MCP SBOM Monitor", layout="wide")



# ---------------------------

# Helper: CSS for colored buttons & badges

# ---------------------------

st.markdown(

    """

    <style>

    /* colored action buttons simulated via containers */

    .action-btn {

      display:inline-block;

      padding:10px 18px;

      margin:4px;

      border-radius:8px;

      color:white;

      font-weight:600;

      cursor:pointer;

      text-align:center;

    }

    .btn-green { background:#16a34a; } /* success */

    .btn-blue  { background:#0ea5e9; } /* primary */

    .btn-red   { background:#ef4444; } /* danger */

    .badge { display:inline-block; padding:4px 8px; border-radius:6px; color: #fff; font-weight:600; }

    .badge-high { background:#ef4444; } /* red */

    .badge-med { background:#f59e0b; }  /* amber */

    .badge-low { background:#10b981; }  /* green */

    .monospace { font-family: monospace; background:#f3f4f6; padding:8px; border-radius:6px; }

    </style>

    """,

    unsafe_allow_html=True,

)



# ---------------------------

# Sample SBOM generator

# ---------------------------

def generate_sample_sbom(n=50, start_time=None):

    if start_time is None:

        start_time = datetime.utcnow()

    rng = np.random.default_rng(seed=int(start_time.timestamp()))

    # sample package names (mix of common and random)

    base_pkgs = [

        "libcrypto", "utils-net", "http-parser", "data-serialize", "auth-core", "xmlproc",

        "protobuf-lite", "openssl-fips", "pkg-legacy", "json-utils", "thirdparty-ui", "zip-handler"

    ]

    suppliers = ["official-repo", "mirrorcorp", "internal-repo", "unknown-source", "thirdparty-supplier"]

    licenses = ["MIT", "Apache-2.0", "GPL-2.0", "Proprietary", "BSD-3-Clause", "UNKNOWN"]

    rows = []

    for i in range(n):

        pkg = rng.choice(base_pkgs + [f"pkg-extra-{rng.integers(1,500)}"])

        # generate version numbers, sometimes '0.x' or rc/beta

        if rng.random() < 0.12:

            # suspicious pre-release

            version = f"{rng.integers(0,2)}.{rng.integers(0,10)}.0-{rng.choice(['alpha','beta','rc'])}{rng.integers(1,9)}"

        else:

            version = f"{rng.integers(0,3)}.{rng.integers(0,10)}.{rng.integers(0,10)}"

        supplier = rng.choice(suppliers)

        lic = rng.choice(licenses)

        # simulate a 'latest_known' version for comparison

        latest_major = rng.integers(1,3)

        latest_minor = rng.integers(0,10)

        latest = f"{latest_major}.{latest_minor}.0"

        # simulate a download_url

        download_url = f"https://{supplier}.example/{pkg}/{version}.tar.gz"

        rows.append({

            "timestamp": (start_time - timedelta(minutes=rng.integers(0,120))).isoformat(),

            "package": pkg,

            "version": version,

            "supplier": supplier,

            "license": lic,

            "download_url": download_url,

            "latest_known_version": latest,

            "notes": ""

        })

    df = pd.DataFrame(rows)

    return df



# ---------------------------

# Detection heuristics

# ---------------------------

SIMULATED_KNOWN_VULNERABLE = {"openssl-fips", "pkg-legacy", "http-parser"}  # example flagged packages



UNTRUSTED_SUPPLIERS = {"unknown-source", "thirdparty-supplier"}

LICENSE_RISK = {"Proprietary", "UNKNOWN", "GPL-2.0"}  # in some DoD contexts GPL-2.0 may be undesirable



def parse_version_to_tuple(version_str):

    """

    Parse 'major.minor.patch' from version-like string.

    If has pre-release like '-beta' return a flag.

    """

    pre_release = False

    s = version_str

    if "-" in s:

        s, _ = s.split("-", 1)

        pre_release = True

    parts = s.split(".")

    nums = []

    for p in parts[:3]:

        try:

            nums.append(int(p))

        except:

            nums.append(0)

    while len(nums) < 3:

        nums.append(0)

    return tuple(nums), pre_release



def detect_risks(df, outdated_major_threshold=0):

    """

    Returns a DataFrame with added detection columns:

    - untrusted_supplier_flag

    - suspicious_version_flag (pre-release or major==0)

    - outdated_flag (major < latest_major)

    - license_risk_flag

    - known_vuln_flag

    - risk_score (0-100)

    - risk_level (LOW/MED/HIGH)

    """

    df = df.copy()

    df['untrusted_supplier'] = df['supplier'].isin(UNTRUSTED_SUPPLIERS)

    parsed = df['version'].apply(parse_version_to_tuple)

    df['version_tuple'] = parsed.apply(lambda x: x[0])

    df['pre_release'] = parsed.apply(lambda x: x[1])

    df['major_version'] = df['version_tuple'].apply(lambda t: t[0])

    # outdated if major < latest_major (simulated compare)

    def latest_major(lat_str):

        t, _ = parse_version_to_tuple(lat_str)

        return t[0]

    df['latest_major'] = df['latest_known_version'].apply(latest_major)

    df['outdated'] = df['major_version'] < df['latest_major']

    df['suspicious_version'] = df['pre_release'] | (df['major_version'] == 0)

    df['license_risk'] = df['license'].isin(LICENSE_RISK)

    df['known_vuln'] = df['package'].isin(SIMULATED_KNOWN_VULNERABLE)

    # compute risk score: simple weighted sum

    df['risk_score'] = (

        df['untrusted_supplier'].astype(int) * 30 +

        df['suspicious_version'].astype(int) * 20 +

        df['outdated'].astype(int) * 15 +

        df['license_risk'].astype(int) * 15 +

        df['known_vuln'].astype(int) * 40

    )

    # Clip to 100

    df['risk_score'] = df['risk_score'].clip(0, 100)

    def level(s):

        if s >= 60:

            return "HIGH"

        elif s >= 30:

            return "MEDIUM"

        else:

            return "LOW"

    df['risk_level'] = df['risk_score'].apply(level)

    return df



# ---------------------------

# MCP placeholder enrich function (simulated)

# ---------------------------

def mcp_enrich_simulate(df, simulate_delay_ms=0):

    """

    Placeholder to show where an MCP call (or model call) could enrich packages.

    This simulation adds an 'mcp_comment' field indicating recommended action.

    Replace this with real MCP integration in production.

    """

    def comment(row):

        lvl = row['risk_level']

        if lvl == "HIGH":

            return "Quarantine package; urgent review. (Simulated MCP recommendation)"

        elif lvl == "MEDIUM":

            return "Schedule security review; consider replacement or patch."

        else:

            return "Acceptable; monitor."

    df = df.copy()

    df['mcp_comment'] = df.apply(comment, axis=1)

    return df



# ---------------------------

# UI layout and controls

# ---------------------------

st.title("MCP — SBOM / Supply-Chain Monitor (Prototype)")

st.markdown("Monitor software package manifests (SBOM-like records) for risky dependencies. Prototype for DoD-focused supply-chain monitoring using MCP-style enrichment.")



# Top action buttons (colored look)

action_col1, action_col2, action_col3, action_col4 = st.columns([1,1,1,1])

with action_col1:

    # Generate sample

    if st.button("Generate sample (50)", key="gen", help="Generate 50 sample SBOM records"):

        st.session_state['sbom_df'] = generate_sample_sbom(50)

        st.session_state['last_action'] = "generated"

with action_col2:

    if st.button("Refresh sample", key="refresh"):

        st.session_state['sbom_df'] = generate_sample_sbom(50)

        st.session_state['last_action'] = "refreshed"

with action_col3:

    uploaded = st.file_uploader("Upload SBOM (JSON, CSV, TXT)", type=['json','csv','txt'])

with action_col4:

    if st.button("Run detection & Enrich (MCP)", key="run"):

        st.session_state['run_detection'] = True



# initialize session state

if 'sbom_df' not in st.session_state:

    st.session_state['sbom_df'] = generate_sample_sbom(50)

if 'run_detection' not in st.session_state:

    st.session_state['run_detection'] = False



# Option panel (sidebar)

st.sidebar.header("Detection Settings")

outdated_major_threshold = st.sidebar.number_input("Outdated major threshold (not used in default logic)", value=0, min_value=0)

show_only_flags = st.sidebar.checkbox("Show only flagged/high-risk packages", value=False)

download_prefix = st.sidebar.text_input("Download filename prefix", value="sbom_results")



# Upload parsing logic

def parse_upload(file_uploader):

    if file_uploader is None:

        return None, "no_file"

    name = file_uploader.name.lower()

    content = file_uploader.getvalue().decode('utf-8')

    try:

        if name.endswith('.json'):

            payload = json.loads(content)

            # try to coerce into rows: if it's a list of objects, ok

            if isinstance(payload, dict):

                # maybe single object with "packages" key

                if 'packages' in payload and isinstance(payload['packages'], list):

                    df = pd.DataFrame(payload['packages'])

                else:

                    # wrap single dict

                    df = pd.DataFrame([payload])

            elif isinstance(payload, list):

                df = pd.DataFrame(payload)

            else:

                return None, "unsupported_json_structure"

        elif name.endswith('.csv'):

            df = pd.read_csv(StringIO(content))

        else:

            # plain text: treat each line as a package row in the format:

            # package,version,supplier,license

            rows = []

            for ln in content.splitlines():

                ln = ln.strip()

                if not ln:

                    continue

                parts = [p.strip() for p in ln.split(',')]

                # be lenient

                pkg = parts[0] if len(parts) > 0 else ""

                ver = parts[1] if len(parts) > 1 else "0.0.0"

                supp = parts[2] if len(parts) > 2 else "unknown-source"

                lic = parts[3] if len(parts) > 3 else "UNKNOWN"

                rows.append({

                    "timestamp": datetime.utcnow().isoformat(),

                    "package": pkg,

                    "version": ver,

                    "supplier": supp,

                    "license": lic,

                    "download_url": "",

                    "latest_known_version": "1.0.0",

                    "notes": ""

                })

            df = pd.DataFrame(rows)

        # ensure required columns exist

        for col in ["timestamp","package","version","supplier","license","download_url","latest_known_version"]:

            if col not in df.columns:

                df[col] = "" if col != "timestamp" else datetime.utcnow().isoformat()

        return df, "ok"

    except Exception as e:

        return None, f"parse_error: {e}"



# If uploaded, parse and replace current dataset

if uploaded is not None:

    parsed_df, status = parse_upload(uploaded)

    if parsed_df is None:

        st.error(f"Upload parse error: {status}")

    else:

        st.session_state['sbom_df'] = parsed_df.head(10000)  # safety cap

        st.success(f"Uploaded dataset parsed: {len(st.session_state['sbom_df'])} rows")



# Main display area

sbom_df = st.session_state['sbom_df'].copy()

st.subheader("SBOM / Package Manifest (preview)")

st.write("Rows:", len(sbom_df))

st.dataframe(sbom_df.head(50))



# Run detection automatically if user requested

if st.session_state.get('run_detection', False) or st.button("Run detection now", key="manual_run"):

    detected = detect_risks(sbom_df)

    enriched = mcp_enrich_simulate(detected)

    st.session_state['detected_df'] = enriched

    st.session_state['run_detection'] = False

else:

    # if previously detected, show it

    detected = st.session_state.get('detected_df', None)

    if detected is None:

        detected = detect_risks(sbom_df)

        enriched = mcp_enrich_simulate(detected)

        st.session_state['detected_df'] = enriched

    else:

        enriched = detected



# Show summary metrics

st.markdown("---")

st.subheader("Summary Metrics")

col_a, col_b, col_c, col_d = st.columns(4)

with col_a:

    st.metric("Total packages", len(enriched))

with col_b:

    high_count = (enriched['risk_level'] == 'HIGH').sum()

    st.metric("High-risk", int(high_count))

with col_c:

    med_count = (enriched['risk_level'] == 'MEDIUM').sum()

    st.metric("Medium-risk", int(med_count))

with col_d:

    low_count = (enriched['risk_level'] == 'LOW').sum()

    st.metric("Low-risk", int(low_count))



# Show flagged table and visual badges

st.markdown("### Flagged packages (examples)")

if show_only_flags:

    view_df = enriched[enriched['risk_level'] != 'LOW'].sort_values('risk_score', ascending=False)

else:

    view_df = enriched.sort_values('risk_score', ascending=False)



# Color-coded risk column for display

def risk_badge_html(level):

    if level == 'HIGH':

        return '<span class="badge badge-high">HIGH</span>'

    elif level == 'MEDIUM':

        return '<span class="badge badge-med">MED</span>'

    else:

        return '<span class="badge badge-low">LOW</span>'



# Prepare display table (limit to 500 rows)

display_df = view_df.copy()

display_df_disp = display_df.head(500)[[

    'timestamp','package','version','supplier','license','latest_known_version','risk_score','risk_level','mcp_comment'

]].reset_index(drop=True)



# Show a styled dataframe with small HTML badges

def render_table_with_badges(df):

    # create html table

    html = "<div style='max-height:420px; overflow:auto;'><table style='width:100%; border-collapse:collapse;'>"

    # header

    html += "<tr>"

    for c in df.columns:

        html += f"<th style='text-align:left; padding:6px; border-bottom:1px solid #ddd'>{c}</th>"

    html += "</tr>"

    # rows

    for _, row in df.iterrows():

        html += "<tr>"

        for c in df.columns:

            val = row[c]

            if c == 'risk_level':

                val = risk_badge_html(val)

            html += f"<td style='padding:6px; border-bottom:1px solid #f3f4f6'>{val}</td>"

        html += "</tr>"

    html += "</table></div>"

    st.markdown(html, unsafe_allow_html=True)



render_table_with_badges(display_df_disp)



# Charts: risk distribution and top packages

st.markdown("---")

st.subheader("Charts")

chart_col1, chart_col2 = st.columns([1,1])

with chart_col1:

    st.markdown("**Risk level distribution**")

    risk_counts = enriched['risk_level'].value_counts().reindex(['HIGH','MEDIUM','LOW']).fillna(0)

    st.bar_chart(risk_counts)



with chart_col2:

    st.markdown("**Top risky packages (by risk_score)**")

    top = enriched.sort_values('risk_score', ascending=False).head(10)

    if not top.empty:

        top_chart = top.set_index('package')['risk_score']

        st.bar_chart(top_chart)

    else:

        st.info("No packages to plot")



# Downloads

st.markdown("---")

st.subheader("Download results")

csv_bytes = enriched.to_csv(index=False).encode('utf-8')

json_bytes = enriched.to_json(orient='records', date_format='iso').encode('utf-8')



st.download_button(f"Download full results CSV ({download_prefix}_results.csv)", csv_bytes, file_name=f"{download_prefix}_results.csv", mime="text/csv")

st.download_button(f"Download full results JSON ({download_prefix}_results.json)", json_bytes, file_name=f"{download_prefix}_results.json", mime="application/json")

