# KNet Cyber Threat Hunting Studio (Streamlit Edition)
# Designed by Randy Singh – Kalsnet (KNet) Consulting Group

import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

# ---------------- DATA ENGINE ----------------

def generate_synthetic_data(count):
    data = []
    for _ in range(count):
        data.append({
            "user": random.choice(["alice", "bob", "charlie", "admin"]),
            "login_hour": random.randint(0, 23),
            "failed_attempts": random.randint(0, 10),
            "api_calls": random.randint(10, 500),
            "command_entropy": round(random.uniform(1.0, 7.5), 2),
            "data_out_mb": random.randint(1, 1000)
        })
    return pd.DataFrame(data)

# ---------------- THREAT HUNTS ----------------

def hunt_threats(df):
    results = {
        "Suspicious Login": df[
            (df["login_hour"] < 6) | (df["failed_attempts"] > 5)
        ],
        "API Abuse": df[df["api_calls"] > 300],
        "Command Abuse": df[df["command_entropy"] > 6.0],
        "Data Exfiltration": df[df["data_out_mb"] > 700]
    }
    return results

# ---------------- AGENTIC ANALYTICS ----------------

def agentic_explanation(results):
    output = ["### 🧠 Agentic Threat Hunter Findings\n"]

    if all(len(v) == 0 for v in results.values()):
        return "✅ No high-risk activity detected. Environment operating normally."

    for threat, records in results.items():
        if len(records) > 0:
            output.append(
                f"#### 🔴 {threat}\n"
                f"- Impacted Records: **{len(records)}**\n"
            )

            if threat == "Suspicious Login":
                output.append(
                    "- **Risk:** Credential abuse or brute-force attempts\n"
                    "- **Fix:** Enforce MFA, account lockout, conditional access\n"
                )

            elif threat == "API Abuse":
                output.append(
                    "- **Risk:** Data scraping or DoS\n"
                    "- **Fix:** Rate limiting, API gateway, token rotation\n"
                )

            elif threat == "Command Abuse":
                output.append(
                    "- **Risk:** Privilege escalation or malware\n"
                    "- **Fix:** EDR, least privilege, command auditing\n"
                )

            elif threat == "Data Exfiltration":
                output.append(
                    "- **Risk:** IP theft or compliance violation\n"
                    "- **Fix:** DLP, outbound inspection, encryption\n"
                )

    return "\n".join(output)

# ---------------- PIE CHART ----------------

def draw_pie(results):
    labels = []
    sizes = []

    for k, v in results.items():
        if len(v) > 0:
            labels.append(f"{k} ({len(v)})")
            sizes.append(len(v))

    if not sizes:
        return None

    fig, ax = plt.subplots()
    ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")
    return fig

# ---------------- STREAMLIT UI ----------------

st.set_page_config(
    page_title="KNet Cyber Threat Hunting Studio",
    layout="wide"
)

st.markdown(
    """
    <div style="background-color:#0b3c5d;padding:15px;border-radius:5px">
        <h1 style="color:white;text-align:center;">
            KNet Cyber Threat Hunting Studio
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- CONTROLS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    record_count = st.slider("Synthetic Records", 10, 500, 100)

with col2:
    generate_btn = st.button("🚀 Generate Data")

with col3:
    uploaded_file = st.file_uploader("📁 Upload CSV", type=["csv"])

# ---------------- DATA HANDLING ----------------

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame()

if generate_btn:
    st.session_state.data = generate_synthetic_data(record_count)

if uploaded_file:
    st.session_state.data = pd.read_csv(uploaded_file)

# ---------------- DISPLAY DATA ----------------

if not st.session_state.data.empty:
    st.subheader("📊 Synthetic / Uploaded Records")
    st.dataframe(st.session_state.data, use_container_width=True)

    # ---------------- ANALYSIS ----------------
    results = hunt_threats(st.session_state.data)

    col_left, col_right = st.columns([1, 2])

    with col_left:
        st.subheader("📈 Threat Distribution")
        fig = draw_pie(results)
        if fig:
            st.pyplot(fig)
        else:
            st.info("No threats detected.")

    with col_right:
        st.subheader("🧠 Findings & Remediation")
        st.markdown(agentic_explanation(results))

else:
    st.info("Generate or upload data to begin threat hunting.")

# ---------------- FOOTER ----------------

st.markdown(
    "<hr><center><b>Designed by Randy Singh – Kalsnet (KNet) Consulting Group</b></center>",
    unsafe_allow_html=True
)
