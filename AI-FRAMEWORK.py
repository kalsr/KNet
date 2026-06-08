


# ARTIFICIAL INTELLIGENCE TAXONOMY & FRAMEWORK (PYTHON VERSION)
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
# HEADER (BOLD BLUE TITLE BAR)
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
# AI TAXONOMY CLASSES
# -----------------------------
class LearningIntelligence:
    def __init__(self):
        self.modeling_simulation = ""
        self.deep_learning = ""
        self.machine_learning = ""
        self.nlp = ""
        self.data_mining = ""


class AdvancedComputing:
    def __init__(self):
        self.supercomputing = ""
        self.neuromorphic = ""
        self.quantum = ""


class AISystems:
    def __init__(self):
        self.virtual_reality = ""
        self.computer_vision = ""
        self.virtual_agents = ""


# -----------------------------
# SESSION STATE
# -----------------------------
if "li" not in st.session_state:
    st.session_state.li = LearningIntelligence()

if "ac" not in st.session_state:
    st.session_state.ac = AdvancedComputing()

if "ais" not in st.session_state:
    st.session_state.ais = AISystems()


# -----------------------------
# MAIN MENU
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

    li = st.session_state.li

    if choice == "Show Entire LI Taxonomy":

        li.modeling_simulation = "Modeling & Simulation helps understand system behavior without real-world testing."
        li.deep_learning = "Deep Learning mimics human learning and problem-solving."
        li.machine_learning = "Machine Learning enables systems to learn without explicit programming."
        li.nlp = "NLP processes and understands human language (DARPA programs like BOLT & LORELEI)."
        li.data_mining = "Data Mining discovers patterns in large datasets."

        st.subheader("FULL LEARNING & INTELLIGENCE TAXONOMY")

        st.write("🔹 Modeling & Simulation:", li.modeling_simulation)
        st.write("🔹 Deep Learning:", li.deep_learning)
        st.write("🔹 Machine Learning:", li.machine_learning)
        st.write("🔹 NLP:", li.nlp)
        st.write("🔹 Data Mining:", li.data_mining)

    elif choice == "Modeling & Simulation":
        li.modeling_simulation = "Modeling & Simulation helps understand system behavior without real-world testing."
        st.success(li.modeling_simulation)

    elif choice == "Deep Learning":
        li.deep_learning = "Deep Learning mimics human learning and problem-solving."
        st.success(li.deep_learning)

    elif choice == "Machine Learning":
        li.machine_learning = "Machine Learning enables systems to learn without explicit programming."
        st.success(li.machine_learning)

    elif choice == "Natural Language Processing":
        li.nlp = "NLP processes and understands human language (DARPA programs like BOLT & LORELEI)."
        st.success(li.nlp)

    elif choice == "Data Mining":
        li.data_mining = "Data Mining discovers patterns in large datasets."
        st.success(li.data_mining)


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

    ac = st.session_state.ac

    if choice == "Show Entire AC Taxonomy":

        ac.supercomputing = "Supercomputing measures performance in FLOPS."
        ac.neuromorphic = "Neuromorphic engineering mimics brain-like architectures using VLSI systems."
        ac.quantum = "Quantum computing uses qubits capable of superposition."

        st.subheader("FULL ADVANCED COMPUTING TAXONOMY")

        st.write("🔹 Supercomputing:", ac.supercomputing)
        st.write("🔹 Neuromorphic Engineering:", ac.neuromorphic)
        st.write("🔹 Quantum Computing:", ac.quantum)

    elif choice == "Supercomputing":
        ac.supercomputing = "Supercomputing measures performance in FLOPS."
        st.success(ac.supercomputing)

    elif choice == "Neuromorphic Engineering":
        ac.neuromorphic = "Neuromorphic engineering mimics brain-like architectures using VLSI systems."
        st.success(ac.neuromorphic)

    elif choice == "Quantum Computing":
        ac.quantum = "Quantum computing uses qubits capable of superposition."
        st.success(ac.quantum)


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

    ais = st.session_state.ais

    if choice == "Show Entire AIS Taxonomy":

        ais.virtual_reality = "Virtual Reality creates immersive digital environments."
        ais.computer_vision = "Computer Vision enables machines to interpret images and video."
        ais.virtual_agents = "Virtual Agents are AI systems that interact with users intelligently."

        st.subheader("FULL AI SYSTEMS TAXONOMY")

        st.write("🔹 Virtual Reality:", ais.virtual_reality)
        st.write("🔹 Computer Vision:", ais.computer_vision)
        st.write("🔹 Virtual Agents:", ais.virtual_agents)

    elif choice == "Virtual Reality":
        ais.virtual_reality = "Virtual Reality creates immersive digital environments."
        st.success(ais.virtual_reality)

    elif choice == "Computer Vision":
        ais.computer_vision = "Computer Vision enables machines to interpret images and video."
        st.success(ais.computer_vision)

    elif choice == "Virtual Agents":
        ais.virtual_agents = "Virtual Agents are AI systems that interact with users intelligently."
        st.success(ais.virtual_agents)


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