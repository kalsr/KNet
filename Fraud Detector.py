# Streamlit Fraud Detector.py

# fraud_detector_streamlit.py

import streamlit as st
import random

# -----------------------------
# SIMPLE FRAUD DETECTION LOGIC
# -----------------------------
def detect_fraud(lines):
    """Simple rule-based fraud detection."""
    suspicious_keywords = [
        "failed login", "invalid", "denied", "unauthorized",
        "error 403", "multiple attempts", "blocked", "blacklisted"
    ]

    score = 0
    flagged_lines = []

    for line in lines:
        for word in suspicious_keywords:
            if word.lower() in line.lower():
                score += 10
                flagged_lines.append(line.strip())

    return score, flagged_lines


# -----------------------------
# STREAMLIT UI APPLICATION
# -----------------------------
def main():

    st.set_page_config(page_title="Fraud Detector – KNet Consulting", layout="wide")

    st.title("🔍 Fraud / Scam Detector – KNet Consulting")
    st.markdown("Designed & Developed by **Randy Singh**")

    st.divider()

    # Session state storage (replacement for Tkinter instance variables)
    if "sample_data" not in st.session_state:
        st.session_state.sample_data = []

    if "file_data" not in st.session_state:
        st.session_state.file_data = []

    # ---------- SLIDER ----------
    st.header("Generate Random Sample Log Data")

    n = st.slider(
        "Select number of sample log entries (0–100)",
        min_value=0, max_value=100, value=20
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Generate Sample Data"):
            sample = []
            for i in range(n):
                entry_type = random.choice([
                    "OK", "FAILED LOGIN", "ACCESS DENIED",
                    "USER VALID", "UNAUTHORIZED ATTEMPT"
                ])
                sample.append(f"Event {i+1}: {entry_type}")

            st.session_state.sample_data = sample
            st.success("Sample data generated!")

    with col2:
        if st.button("Reset Sample Data"):
            st.session_state.sample_data = []
            st.success("Sample data reset.")

    # ---------- FILE UPLOAD ----------
    with col3:
        uploaded = st.file_uploader("Upload Your Log File", type=["txt", "log"])

        if uploaded:
            lines = uploaded.read().decode("utf-8").splitlines()
            st.session_state.file_data = lines
            st.success("File successfully loaded!")

    st.divider()

    # ---------- ANALYSIS ----------
    st.header("Run Fraud Detection")

    if st.button("Run Fraud Analysis"):

        logs = st.session_state.sample_data or st.session_state.file_data

        if not logs:
            st.warning("No log data available to analyze!")
            return

        score, flagged = detect_fraud(logs)

        # Risk calculation
        if score > 40:
            risk = "HIGH"
        elif score > 15:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        st.subheader("📄 Fraud Analysis Report")

        st.write(f"**Fraud Risk Score:** `{score}`")
        st.write(f"**Risk Level:** `{risk}`")

        st.markdown("---")
        st.write("### Suspicious Entries")

        if flagged:
            st.code("\n".join(flagged))
        else:
            st.info("No suspicious log entries detected.")

    # ---------- SHOW CURRENT LOGS ----------
    st.divider()
    st.header("Current Log Data")

    if st.session_state.sample_data:
        st.write("### Sample Data:")
        st.code("\n".join(st.session_state.sample_data))

    if st.session_state.file_data:
        st.write("### Uploaded File Data:")
        st.code("\n".join(st.session_state.file_data))


# -----------------------------
# RUN STREAMLIT APP
# -----------------------------
if __name__ == "__main__":
    main()
