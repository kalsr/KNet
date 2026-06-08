

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


# =========================================================
#  NEW EDUCATIONAL INTRO SECTION (IMPORTANT ADDITION)
# =========================================================
st.markdown("""
##  What is AI Taxonomy & Framework?

###  Artificial Intelligence Taxonomy
AI Taxonomy is the **structured classification of Artificial Intelligence domains**, where AI capabilities are organized into logical groups such as:
- Learning & Intelligence
- Advanced Computing
- AI Systems

It helps us understand **WHAT AI IS MADE OF** and how different technologies relate.

---

###  Artificial Intelligence Framework
An AI Framework is the **architecture or blueprint that connects all AI components together**.

It defines:
- How AI systems are built
- How data flows through AI modules
- How intelligence is applied in real-world systems

---

###  Together:
- Taxonomy = *Classification (WHAT exists)*
- Framework = *Structure (HOW it works together)*

---

###  High-Level AI Structure
""")

# -----------------------------
# GLOBAL AI MAP DIAGRAM
# -----------------------------
st.graphviz_chart("""
digraph {
    AI -> "Learning & Intelligence"
    AI -> "Advanced Computing"
    AI -> "AI Systems"

    "Learning & Intelligence" -> ML
    "Learning & Intelligence" -> DL
    "Advanced Computing" -> Quantum
    "AI Systems" -> Vision
    "AI Systems" -> Agents
}
""")


# -----------------------------
# SIMPLE DIAGRAM FUNCTION
# -----------------------------
def diagram(title, content):
    st.markdown(f"###  {title}")
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
# (UNCHANGED STRUCTURE - ENHANCED CONTENT ONLY)
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
        ###  Real-World Examples
        - Flight simulator training (pilot systems)
        - Military battlefield simulations
        - Weather prediction models
        - Automotive crash testing

        ###  Purpose
        Reduce cost, risk, and improve decision accuracy before real deployment.
        """)

        diagram("Modeling & Simulation Flow", """
        digraph {
            Data -> Model -> Simulation -> Analysis -> Decision
        }
        """)

    elif choice == "Deep Learning":

        st.success("Deep Learning mimics human brain neural processing.")

        st.markdown("""
        ###  Real-World Examples
        - Face recognition (iPhone FaceID)
        - Self-driving cars (Tesla Autopilot)
        - ChatGPT / LLMs
        - Medical imaging diagnosis

        ###  Key Idea
        Uses multi-layer neural networks to learn patterns from massive datasets.
        """)

        diagram("Deep Learning Neural Network", """
        digraph {
            Input -> "Hidden Layer 1" -> "Hidden Layer 2" -> Output
        }
        """)

    elif choice == "Machine Learning":

        st.success("Machine Learning enables systems to learn from data without explicit programming.")

        st.markdown("""
        ###  Real-World Examples
        - Fraud detection (banks)
        - Netflix recommendations
        - Spam email filtering
        - Predictive maintenance

        ###  Key Idea
        Systems improve automatically using data patterns.
        """)

        diagram("Machine Learning Pipeline", """
        digraph {
            Data -> Training -> Model -> Prediction
        }
        """)

    elif choice == "Natural Language Processing":

        st.success("NLP allows machines to understand human language.")

        st.markdown("""
        ###  Real-World Examples
        - Chatbots (customer service)
        - Google Translate
        - Siri / Alexa
        - Sentiment analysis (social media)

        ###  Key Idea
        Converts human language into machine-understandable format.
        """)

        diagram("NLP Processing Flow", """
        digraph {
            Text -> Tokenization -> Understanding -> Response
        }
        """)

    elif choice == "Data Mining":

        st.success("Data Mining extracts hidden patterns from large datasets.")

        st.markdown("""
        ###  Real-World Examples
        - Amazon shopping patterns
        - Crime prediction
        - Healthcare analytics
        - Credit scoring

        ###  Key Idea
        Finds hidden insights from massive datasets.
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
        ###  Real-World Examples
        - Weather forecasting (NOAA)
        - NASA space simulations
        - Nuclear research models
        - Large-scale cryptography

        ###  Purpose
        Solve extremely complex problems using parallel computing power.
        """)

        diagram("Supercomputing Architecture", """
        digraph {
            Input -> CPU_Clusters -> Parallel_Processing -> Output
        }
        """)

    elif choice == "Neuromorphic Engineering":

        st.success("Neuromorphic computing mimics the human brain structure.")

        st.markdown("""
        ###  Real-World Examples
        - Intel Loihi brain chip
        - Robotics perception systems
        - Smart sensors
        - Edge AI devices

        ###  Key Idea
        Hardware designed like biological neurons.
        """)

        diagram("Neuromorphic System", """
        digraph {
            Sensors -> Neurons -> Synapses -> Decision
        }
        """)

    elif choice == "Quantum Computing":

        st.success("Quantum computing uses qubits and quantum physics principles.")

        st.markdown("""
        ###  Real-World Examples
        - Drug discovery
        - Financial modeling
        - Encryption systems
        - Climate modeling

        ###  Key Idea
        Uses quantum superposition for massive parallel computation.
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
        ###  Real-World Examples
        - VR gaming (Meta Quest)
        - Military simulation training
        - Virtual surgery training
        - Architecture visualization

        ###  Purpose
        Create fully immersive digital environments.
        """)

        diagram("Virtual Reality System", """
        digraph {
            User -> Headset -> Virtual_Environment -> Interaction
        }
        """)

    elif choice == "Computer Vision":

        st.success("Computer Vision enables machines to interpret images and video.")

        st.markdown("""
        ###  Real-World Examples
        - Tesla autonomous driving
        - Facial recognition systems
        - Medical image diagnostics
        - Drone surveillance

        ###  Key Idea
        Machines "see" and interpret visual data.
        """)

        diagram("Computer Vision Pipeline", """
        digraph {
            Image -> Processing -> Feature_Extraction -> Classification
        }
        """)

    elif choice == "Virtual Agents":

        st.success("Virtual Agents are intelligent AI-based assistants.")

        st.markdown("""
        ###  Real-World Examples
        - ChatGPT
        - Alexa / Google Assistant
        - Customer support bots
        - AI trading assistants

        ###  Key Idea
        AI systems that interact naturally with humans.
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