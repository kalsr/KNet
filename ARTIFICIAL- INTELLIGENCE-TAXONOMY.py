# ARTIFICIAL INTELLIGENCE TAXONOMY & FRAMEWORK (ENHANCED VERSION)
# Developed by Randy Singh – Kalsnet (KNet) Consulting Group

import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Taxonomy Framework",
    layout="wide"
)

# -----------------------------
# HEADER (UNCHANGED TOP TITLE)
# -----------------------------
st.markdown("""
<div style='text-align:center; padding:10px;'>

<h1 style='color:#0056D2; font-weight:bold; font-size:44px;'>
ARTIFICIAL INTELLIGENCE TAXONOMY & FRAMEWORK
</h1>

<h3 style='color:#0056D2; font-weight:bold;'>
Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</h3>

</div>
""", unsafe_allow_html=True)


# -----------------------------
# SIMPLE DIAGRAM FUNCTION
# -----------------------------
def diagram(title, content):
    st.markdown(f"### 📊 {title}")
    st.graphviz_chart(content)


# -----------------------------
# SIDEBAR MENU
# -----------------------------
menu = st.sidebar.radio(
    "AI TAXONOMY MENU",
    [
        "Learning & Intelligence (LI)",
        "Advanced Computing (AC)",
        "AI Systems (AIS)"
    ]
)

# =========================================================
# LEARNING & INTELLIGENCE
# =========================================================
if menu == "Learning & Intelligence (LI)":

    st.header("LEARNING & INTELLIGENCE CATEGORY")

    choice = st.selectbox(
        "Select Subcategory",
        [
            "Show Entire LI Taxonomy",
            "Modeling & Simulation",
            "Deep Learning",
            "Machine Learning",
            "Natural Language Processing",
            "Data Mining"
        ]
    )

    if choice == "Modeling & Simulation":

        st.success("Modeling & Simulation helps understand system behavior without real-world testing.")

        st.markdown("""
        ### 📌 Examples
        - Flight simulator training (pilot training systems)
        - Military battlefield simulations
        - Weather prediction models
        - Automotive crash testing simulations
        """)

        diagram("Modeling & Simulation Flow", """
        digraph {
            Data -> Model -> Simulation -> Analysis -> Decision
        }
        """)

    elif choice == "Deep Learning":

        st.success("Deep Learning mimics human brain neural processing.")

        st.markdown("""
        ### 📌 Examples
        - Face recognition (iPhone FaceID)
        - Self-driving cars
        - ChatGPT / Large Language Models
        - Medical image diagnosis
        """)

        diagram("Deep Learning Neural Network", """
        digraph {
            Input -> "Hidden Layer 1" -> "Hidden Layer 2" -> Output
        }
        """)

    elif choice == "Machine Learning":

        st.success("Machine Learning enables systems to learn from data without explicit programming.")

        st.markdown("""
        ### 📌 Examples
        - Fraud detection in banking
        - Netflix recommendation engine
        - Spam email filtering
        - Predictive maintenance in industry
        """)

        diagram("Machine Learning Pipeline", """
        digraph {
            Data -> Training -> Model -> Prediction
        }
        """)

    elif choice == "Natural Language Processing":

        st.success("NLP allows machines to understand human language.")

        st.markdown("""
        ### 📌 Examples
        - Chatbots (customer service bots)
        - Google Translate
        - Voice assistants (Alexa, Siri)
        - Sentiment analysis on social media
        """)

        diagram("NLP Processing Flow", """
        digraph {
            Text -> Tokenization -> Understanding -> Response
        }
        """)

    elif choice == "Data Mining":

        st.success("Data Mining extracts hidden patterns from large datasets.")

        st.markdown("""
        ### 📌 Examples
        - Market basket analysis (Amazon shopping)
        - Crime pattern detection
        - Healthcare trend analysis
        - Credit scoring models
        """)

        diagram("Data Mining Process", """
        digraph {
            Data -> Cleaning -> Pattern_Discovery -> Insights
        }
        """)


# =========================================================
# ADVANCED COMPUTING
# =========================================================
elif menu == "Advanced Computing (AC)":

    st.header("ADVANCED COMPUTING CATEGORY")

    choice = st.selectbox(
        "Select Subcategory",
        [
            "Show Entire AC Taxonomy",
            "Supercomputing",
            "Neuromorphic Engineering",
            "Quantum Computing"
        ]
    )

    if choice == "Supercomputing":

        st.success("Supercomputing performs extremely high-speed calculations (FLOPS).")

        st.markdown("""
        ### 📌 Examples
        - Weather forecasting systems (NOAA models)
        - Nuclear simulations
        - Space exploration modeling (NASA)
        - Cryptography research
        """)

        diagram("Supercomputing Architecture", """
        digraph {
            Input -> CPU_Clusters -> Parallel_Processing -> Output
        }
        """)

    elif choice == "Neuromorphic Engineering":

        st.success("Neuromorphic computing mimics the human brain structure.")

        st.markdown("""
        ### 📌 Examples
        - Brain-inspired AI chips (Intel Loihi)
        - Robotics perception systems
        - Smart sensors
        - Edge AI devices
        """)

        diagram("Neuromorphic System", """
        digraph {
            Sensors -> Neurons -> Synapses -> Decision
        }
        """)

    elif choice == "Quantum Computing":

        st.success("Quantum computing uses qubits and superposition principles.")

        st.markdown("""
        ### 📌 Examples
        - Drug discovery simulation
        - Financial risk modeling
        - Cryptography breaking/encryption
        - Climate modeling
        """)

        diagram("Quantum Computing Model", """
        digraph {
            Qubits -> Superposition -> Entanglement -> Result
        }
        """)


# =========================================================
# AI SYSTEMS
# =========================================================
elif menu == "AI Systems (AIS)":

    st.header("AI SYSTEMS CATEGORY")

    choice = st.selectbox(
        "Select Subcategory",
        [
            "Show Entire AIS Taxonomy",
            "Virtual Reality",
            "Computer Vision",
            "Virtual Agents"
        ]
    )

    if choice == "Virtual Reality":

        st.success("Virtual Reality creates immersive simulated environments.")

        st.markdown("""
        ### 📌 Examples
        - VR gaming (Meta Quest)
        - Military training simulations
        - Virtual surgery training
        - Architecture visualization
        """)

        diagram("Virtual Reality System", """
        digraph {
            User -> Headset -> Virtual_Environment -> Interaction
        }
        """)

    elif choice == "Computer Vision":

        st.success("Computer Vision enables machines to interpret images and video.")

        st.markdown("""
        ### 📌 Examples
        - Autonomous vehicles (Tesla vision system)
        - Facial recognition systems
        - Medical imaging diagnosis
        - Drone surveillance systems
        """)

        diagram("Computer Vision Pipeline", """
        digraph {
            Image -> Processing -> Feature_Extraction -> Classification
        }
        """)

    elif choice == "Virtual Agents":

        st.success("Virtual Agents are intelligent AI-based assistants.")

        st.markdown("""
        ### 📌 Examples
        - ChatGPT
        - Customer support bots
        - Alexa / Google Assistant
        - AI trading assistants
        """)

        diagram("Virtual Agent Flow", """
        digraph {
            User_Query -> AI_Model -> Response -> User
        }
        """)


# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center;color:#0056D2;font-weight:bold;'>"
    "AI Taxonomy Framework | Developed by Randy Singh – KNet Consulting Group"
    "</div>",
    unsafe_allow_html=True
)