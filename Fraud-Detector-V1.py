# Fraud-Detector-V1.py


import streamlit as st
import random
import matplotlib.pyplot as plt

# -----------------------------
# SIMPLE FRAUD DETECTION LOGIC
# -----------------------------
def detect_fraud(lines):
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
# STREAMLIT APP
# -----------------------------
def main():

    st.set_page_config(page_title="Fraud Detector – KNet Consulting", layout="wide")

    # ---------- TITLE (BLUE) ----------
    st.markdown("""
        <div style="background-color:#007bff;padding:20px;border-radius:10px;">
            <h1 style="color:white;text-align:center;">
                Fraud / Scam Detector – KNet Consulting
            </h1>
            <h3 style="color:white;text-align:center;">
                Designed & Developed by Randy Singh
            </h3>
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ---------- SESSION STORAGE ----------
    if "sample_data" not in st.session_state:
        st.session_state.sample_data = []

    if "file_data" not in st.session_state:
        st.session_state.file_data = []

    # ---------- BUTTON STYLES ----------
    BUTTON_STYLE_GREEN = """
        <style>
        .green-btn button {
            background-color: #28a745 !important;
            color: white !important;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 16px;
        }
        </style>
    """

    BUTTON_STYLE_RED = """
        <style>
        .red-btn button {
            background-color: #e60000 !important;
            color: white !important;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 16px;
        }
        </style>
    """

    st.markdown(BUTTON_STYLE_GREEN, unsafe_allow_html=True)
    st.markdown(BUTTON_STYLE_RED, unsafe_allow_html=True)

    # ---------- LOG GENERATION ----------
    st.header("Generate Sample Log Data")

    n = st.slider("Select number of sample entries (0–100)", 0, 100, 20)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Generate Sample Data", key="gen", help="Generate sample logs"):
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
        if st.button("Reset Sample Data", key="reset", help="Clear all data"):
            st.session_state.sample_data = []
            st.success("Sample data reset.")

    # ---------- FILE UPLOAD ----------
    with col3:
        uploaded = st.file_uploader("Upload Log File", type=["txt", "log"])
        if uploaded:
            lines = uploaded.read().decode("utf-8").splitlines()
            st.session_state.file_data = lines
            st.success("File loaded successfully!")

    st.divider()

    # ---------- ANALYSIS ----------
    st.header("Fraud Analysis")

    if st.button("Run Fraud Analysis", key="analyze"):
        logs = st.session_state.sample_data or st.session_state.file_data

        if not logs:
            st.warning("No logs to analyze!")
            return

        score, flagged = detect_fraud(logs)

        # Risk level
        if score > 40:
            risk = "HIGH"
        elif score > 15:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        # RESULT PANEL
        st.subheader("📄 Fraud Analysis Report")
        st.markdown(f"**Fraud Risk Score:** `{score}`")
        st.markdown(f"**Risk Level:** `{risk}`")

        st.markdown("### Suspicious Entries Found:")
        if flagged:
            st.code("\n".join(flagged))
        else:
            st.info("No suspicious activity found.")

        # PIE CHART ----------
        suspicious_count = len(flagged)
        clean_count = max(1, len(logs) - suspicious_count)  # avoid zero division

        fig, ax = plt.subplots()
        ax.pie([suspicious_count, clean_count],
               labels=["Suspicious", "Normal"],
               autopct="%1.1f%%")
        ax.set_title("Fraud vs Clean Activity Distribution")

        st.pyplot(fig)

        # ---------- RECOMMENDATIONS ----------
        st.subheader("✔️ Recommendations to Avoid Scams & Frauds")
        st.markdown("""
        - Use **multi-factor authentication (MFA)** on all accounts  
        - Never click links in unexpected emails or SMS  
        - Avoid using the same password across accounts  
        - Use a **password manager**  
        - Verify the sender before responding to financial requests  
        - Monitor login alerts and access history regularly  
        - Block suspicious IPs or repeated failed login attempts  
        - Keep firewalls and antivirus tools active and updated  
        """)

    st.divider()

    # ---------- DISPLAY LOGS ----------
    st.header("Current Log Data")

    if st.session_state.sample_data:
        st.subheader("Sample Generated Data")
        st.code("\n".join(st.session_state.sample_data))

    if st.session_state.file_data:
        st.subheader("Uploaded File Data")
        st.code("\n".join(st.session_state.file_data))


# Run App
if __name__ == "__main__":
    main()


