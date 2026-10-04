"""
AGI Mission Intelligence Suite
Developed by Randy Singh from Kalsnet (KNet) Consulting Group

Run with:  streamlit run AGI-MISSION-INTELLIGENCE.py
Requires agi_engine.py and exports.py in the same folder.
"""
from __future__ import annotations

import io
import math
from datetime import date

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import agi_engine as E
import exports as X

st.set_page_config(page_title="AGI Mission Intelligence Suite", layout="wide")

BLUE = "#0D47A1"
PALETTE = ["#0D47A1", "#00897B", "#F57C00", "#C62828", "#6A1B9A", "#2E7D32", "#5D4037", "#455A64"]
TODAY = date(2026, 10, 4) if date.today() < date(2026, 10, 4) else date.today()

# Plain (non f-string) CSS so the curly braces are never parsed as Python code.
CSS = """
<style>
.app-title { color:__BLUE__; font-weight:800; font-size:2.6rem; line-height:1.15; margin-bottom:0.1rem; }
.app-sub { color:__BLUE__; font-weight:700; font-size:1.15rem; margin-bottom:0.8rem; }
.why-box { background:#E3F2FD; border-left:6px solid __BLUE__; padding:0.8rem 1rem; border-radius:6px; margin:0.4rem 0 0.8rem 0; }
.step-box { background:#F1F8E9; border-left:6px solid #2E7D32; padding:0.6rem 1rem; border-radius:6px; margin:0.3rem 0; }
.warn-box { background:#FFF3E0; border-left:6px solid #F57C00; padding:0.6rem 1rem; border-radius:6px; margin:0.3rem 0; }
section[data-testid="stSidebar"] { background: linear-gradient(180deg,#0D47A1 0%,#1565C0 55%,#1E88E5 100%); }
section[data-testid="stSidebar"] * { color:#FFFFFF !important; }
section[data-testid="stSidebar"] [data-baseweb="select"] * { color:#0D47A1 !important; }
div[data-testid="stMetric"] { background:#F5F9FF; border:1px solid #BBDEFB; border-radius:8px; padding:0.5rem 0.8rem; }
</style>
<div class="app-title">AGI Mission Intelligence Suite</div>
<div class="app-sub">Developed by Randy Singh from Kalsnet (KNet) Consulting Group</div>
""".replace("__BLUE__", BLUE)

st.markdown(CSS, unsafe_allow_html=True)

PAGES = ["Overview", "Healthcare", "Cybersecurity", "Software Development", "Government and DoD",
         "AGI and Knowledge Graph", "Everyday Life Travel Planner"]

with st.sidebar:
    st.markdown("### Use Case Navigation")
    page = st.radio("Select a use case", PAGES, key="nav", label_visibility="collapsed")
    st.markdown("---")
    st.markdown("**How every use case works**")
    st.markdown("Observe, Understand, Reason, Plan, Act with human approval, Verify, Learn.")
    st.markdown("---")
    st.markdown("**Data**")
    st.markdown("Each use case starts on synthetic data. Choose Upload my own data inside the use case to "
                "analyze your file. Download the template first so your columns match.")
    st.markdown("---")
    st.caption("General intelligence behavior is implemented as a transparent orchestration agent: every "
               "conclusion is produced by a documented formula and recorded in a reasoning trace.")


# =============================================================================
# Shared helpers
# =============================================================================
def full_table(df: pd.DataFrame, key: str | None = None):
    """Show every row without inner scrolling where practical."""
    h = min(36 * (len(df) + 1) + 4, 2400)
    st.dataframe(df, height=h, hide_index=True, key=key)


def why_agi(intro: str, rows: list):
    st.markdown(f'<div class="why-box">{intro}</div>', unsafe_allow_html=True)
    st.markdown("**Traditional approach compared with an AGI approach**")
    st.dataframe(pd.DataFrame(rows, columns=["Capability", "Traditional tools", "AGI approach", "Benefit"]),
                 hide_index=True, height=36 * (len(rows) + 1) + 4)


def field_dictionary(fields: dict, df: pd.DataFrame | None = None):
    rows = []
    for f, d in fields.items():
        dtype, example = "", ""
        if df is not None and f in df.columns:
            dtype = "Number" if pd.api.types.is_numeric_dtype(df[f]) else "Text"
            example = str(df[f].iloc[0])
        rows.append({"Field": f, "Type": dtype, "Example": example, "Explanation and why it is used": d})
    st.dataframe(pd.DataFrame(rows), hide_index=True, height=36 * (len(rows) + 1) + 4)


def data_source(key: str, synthetic: pd.DataFrame, required: list, label: str, numeric: list | None = None):
    """Synthetic or uploaded data with validation. Returns (df, source_name)."""
    st.markdown(f"**{label}**")
    c1, c2 = st.columns([2, 1])
    with c1:
        choice = st.radio("Data source", ["Use synthetic data", "Upload my own data"], key=f"{key}_src",
                          horizontal=True)
    with c2:
        st.download_button("Download template (synthetic CSV)", synthetic.to_csv(index=False).encode(),
                           file_name=f"{key}_template.csv", mime="text/csv", key=f"{key}_tpl")
    if choice == "Upload my own data":
        up = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"], key=f"{key}_up")
        if up is None:
            st.info("No file uploaded yet. Synthetic data is shown until a valid file is provided.")
            return synthetic.copy(), "Synthetic"
        try:
            df = pd.read_csv(up) if up.name.lower().endswith(".csv") else pd.read_excel(up)
        except Exception as ex:  # noqa: BLE001
            st.error(f"Could not read the file: {ex}")
            return synthetic.copy(), "Synthetic"
        df.columns = [str(c).strip() for c in df.columns]
        missing = E.validate_columns(df, required)
        if missing:
            st.error("Uploaded file is missing required columns: " + ", ".join(missing) +
                     ". Synthetic data is used instead.")
            return synthetic.copy(), "Synthetic"
        for c in numeric or []:
            df[c] = pd.to_numeric(df[c], errors="coerce")
        bad = df[numeric].isna().any(axis=1) if numeric else pd.Series(False, index=df.index)
        if bad.any():
            st.warning(f"{int(bad.sum())} rows had non numeric values in numeric fields and were removed.")
            df = df[~bad].reset_index(drop=True)
        if len(df) == 0:
            st.error("No valid rows after validation. Synthetic data is used instead.")
            return synthetic.copy(), "Synthetic"
        st.success(f"Loaded {len(df)} rows from {up.name}.")
        return df, f"Uploaded file {up.name}"
    return synthetic.copy(), "Synthetic"


def export_panel(key: str, title: str, sections: list, tables: dict):
    st.markdown("Download the complete results of this use case. Every format contains the same "
                "reasoning trace and result tables.")
    c1, c2, c3, c4 = st.columns(4)
    base = key.lower()
    with c1:
        st.download_button("Download PDF", X.to_pdf(title, sections, tables), f"{base}_report.pdf",
                           "application/pdf", key=f"{key}_pdf")
    with c2:
        st.download_button("Download Word", X.to_docx(title, sections, tables), f"{base}_report.docx",
                           "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                           key=f"{key}_docx")
    with c3:
        st.download_button("Download Text", X.to_text(title, sections, tables), f"{base}_report.txt",
                           "text/plain", key=f"{key}_txt")
    with c4:
        st.download_button("Download CSV", X.to_csv(tables), f"{base}_results.csv", "text/csv",
                           key=f"{key}_csv")
    st.markdown("**Tables included in the export**")
    st.dataframe(pd.DataFrame([{"Table": k, "Rows": 0 if v is None else len(v),
                                "Columns": 0 if v is None else len(v.columns)} for k, v in tables.items()]),
                 hide_index=True)


def flow_dot(steps: list, color: str = BLUE, loop_back: tuple | None = None, rankdir: str = "TB",
             human: set | None = None) -> str:
    human = human or set()
    lines = [f'digraph G {{ rankdir={rankdir}; bgcolor="transparent"; nodesep=0.3; ranksep=0.32;',
             'node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, '
             f'fillcolor="#E3F2FD", color="{color}", penwidth=1.6];',
             f'edge [color="{color}", penwidth=1.4];']
    for i, s in enumerate(steps):
        fill = "#FFE0B2" if s in human else ("#0D47A1" if i == 0 else "#E3F2FD")
        font = "white" if i == 0 and s not in human else "black"
        lines.append(f'n{i} [label="{s}", fillcolor="{fill}", fontcolor="{font}"];')
    if rankdir == "LR" and len(steps) > 6:
        # wrap long workflows into rows of five so labels stay readable
        lines[0] = lines[0].replace("rankdir=LR", "rankdir=TB")
        lines[1] = lines[1].replace("fontsize=11", "fontsize=13").replace("shape=box,", "shape=box, width=3.6,")
    for i in range(len(steps) - 1):
        lines.append(f"n{i} -> n{i + 1};")
    if loop_back:
        a, b = loop_back
        lines.append(f'n{a} -> n{b} [style=dashed, color="#C62828", label="  learn and improve", fontsize=9, constraint=false];')
    lines.append("}")
    return "\n".join(lines)


def trace_view(trace: E.ReasoningTrace):
    st.markdown("**AGI reasoning trace**")
    for s in trace.steps:
        st.markdown(f'<div class="step-box"><b>Step {s["Step"]}. {s["Stage"]}</b><br>{s["Reasoning"]}</div>',
                    unsafe_allow_html=True)


def formula(title: str, latex: str, explanation: str):
    st.markdown(f"**{title}**")
    st.latex(latex)
    st.markdown(explanation)
    st.markdown("---")


def tabs6():
    return st.tabs(["Why AGI", "Synthetic Data Bar", "AGI Reasoning and Results", "Diagrams and Charts",
                    "Formulas Explained", "Export Results"])


# =============================================================================
# Overview
# =============================================================================
def page_overview():
    st.header("Overview of Artificial General Intelligence use cases")
    st.markdown('<div class="why-box"><b>What makes AGI different.</b> Narrow AI solves one task, such as '
                'classifying an alert or reading a lab value. Artificial General Intelligence understands the '
                'overall objective, reasons across many kinds of data, plans multi step work, uses tools, checks '
                'its own results and learns, while a human keeps decision authority for high impact actions. '
                'This application demonstrates that general loop in six domains.</div>', unsafe_allow_html=True)
    st.subheader("The general intelligence loop used in every use case")
    st.graphviz_chart(flow_dot(["Objective or event", "Observe all relevant data", "Understand context and intent",
                                "Reason across sources", "Plan options", "Human approval",
                                "Act with tools", "Verify results", "Learn"],
                               loop_back=(8, 2), rankdir="LR", human={"Human approval"}), width="content")
    st.subheader("Use cases in this application")
    st.dataframe(pd.DataFrame([
        ("Healthcare", "Patient information, labs, history", "Risk scores, possible conditions, physician questions, care plans, appointments, insurance actions", "Physician"),
        ("Cybersecurity", "SIEM alerts, threat intelligence, behavior analytics", "Risk ranked alerts, attack graph, likely attack path, SOAR playbooks, learning", "SOC analyst"),
        ("Software Development", "Plain language requirement, module plan", "Architecture, code scaffold, build order, effort, automated test and fix loop, documentation", "Engineering lead"),
        ("Government and DoD", "Mission statement, risk register, courses of action", "Fused risk picture, scored and simulated COAs, recommendation, execution monitoring", "Decision authority"),
        ("AGI and Knowledge Graph", "Entities and relationships", "Blast radius, mission impact paths, best mitigation by what if reasoning", "Security architect"),
        ("Everyday Life Travel", "Family, budget, activities, hotels, flights", "Day by day itinerary, budget in USD and INR, flight adaptation, intent based replanning", "Traveler"),
    ], columns=["Use case", "Inputs", "AGI outputs", "Human decision authority"]), hide_index=True)
    st.subheader("Narrow AI compared with AGI")
    cats = ["Breadth of tasks", "Cross domain reasoning", "Planning", "Tool use", "Self verification", "Learning from outcomes"]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=[3, 2, 2, 3, 2, 3], theta=cats, fill="toself", name="Narrow AI", line_color="#90A4AE"))
    fig.add_trace(go.Scatterpolar(r=[9, 9, 8, 9, 8, 8], theta=cats, fill="toself", name="AGI approach", line_color=BLUE))
    fig.update_layout(polar=dict(radialaxis=dict(range=[0, 10])), height=420, margin=dict(t=30, b=30))
    st.plotly_chart(fig)
    st.caption("Illustrative capability profile on a 0 to 10 scale.")
    st.subheader("How to use this application")
    for s in ["Pick a use case on the left navigation bar.",
              "Read Why AGI to see the business case.",
              "Open Synthetic Data Bar to see every synthetic record and an explanation of each field, or switch to Upload my own data.",
              "Open AGI Reasoning and Results to run the agent and inspect its reasoning trace.",
              "Open Diagrams and Charts and Formulas Explained to understand how each result is produced.",
              "Open Export Results to download PDF, Word, Text or CSV reports."]:
        st.markdown(f'<div class="step-box">{s}</div>', unsafe_allow_html=True)


# =============================================================================
# Healthcare
# =============================================================================
HC_NUM = ["Age", "HeightCm", "WeightKg", "SystolicBP", "DiastolicBP", "HeartRate", "FastingGlucose", "HbA1c",
          "LDL", "HDL", "Creatinine", "ActiveMedications", "LastVisitDaysAgo"]


def page_healthcare():
    st.header("Healthcare: AGI medical research and administrative assistant")
    t = tabs6()
    with t[0]:
        why_agi("An AGI assistant moves from <b>patient information to reasoning to recommendations</b> in one "
                "connected workflow. It reviews records, analyzes labs, consults medical knowledge, proposes "
                "possible conditions, prepares questions for the physician, builds a personalized care plan, "
                "monitors trends and coordinates appointments and insurance. <b>The physician remains "
                "responsible for every medical decision.</b>", [
            ("Record review", "Clinician reads each chart manually", "Reads every record and lab in seconds", "More time for patient care"),
            ("Lab analysis", "Isolated reference ranges per test", "Combines BP, glucose, lipids, kidney and BMI into one risk view", "Fewer missed combined risks"),
            ("Literature research", "Separate search tools", "Links each finding to guideline evidence automatically", "Evidence at the point of care"),
            ("Possible diagnoses", "Clinician memory and checklists", "Systematic screening of every flag", "Consistent, explainable flags"),
            ("Care plans", "Generic templates", "Personalized to each patient's findings", "Better adherence"),
            ("Trend monitoring", "Reviewed only at visits", "Continuous slope tracking with projections", "Earlier intervention"),
            ("Appointments and insurance", "Separate admin staff and systems", "Scheduled by clinical urgency and preference; coverage issues flagged", "Less administrative burden"),
        ])
    with t[1]:
        df, src = data_source("healthcare", E.synthetic_healthcare(), E.HC_REQUIRED, "Patient records", HC_NUM)
        st.markdown(f"**Data in use: {src}. {len(df)} patients, {len(df.columns)} fields. All rows shown.**")
        full_table(df, key="hc_data")
        st.markdown("**Field explanations**")
        field_dictionary(E.HC_FIELDS, df)
    res, trace = E.analyze_healthcare(df, TODAY)
    merged = df.merge(res, on="PatientID", how="left")
    with t[2]:
        c = st.columns(6)
        c[0].metric("Patients", len(res))
        c[1].metric("High priority", int((res.PriorityLevel == "High").sum()))
        c[2].metric("Medium priority", int((res.PriorityLevel == "Medium").sum()))
        c[3].metric("Low priority", int((res.PriorityLevel == "Low").sum()))
        c[4].metric("Overdue visits", int((res.Overdue == "Yes").sum()))
        c[5].metric("Insurance follow ups", int((res.InsuranceAction != "Verified, no action").sum()))
        trace_view(trace)
        st.subheader("Prioritized patient results (all patients)")
        full_table(res, key="hc_res")
        st.subheader("Patient drill down")
        pid = st.selectbox("Select patient", list(res.PatientID), key="hc_pid")
        row = res[res.PatientID == pid].iloc[0]
        prow = df[df.PatientID == pid].iloc[0]
        a, b = st.columns(2)
        with a:
            st.markdown(f"**Priority:** {row.PriorityLevel} ({row.PriorityScore})")
            st.markdown(f"**Possible conditions for physician review:** {row.PossibleConditions}")
            st.markdown(f"**Next appointment:** {row.NextAppointment}")
            st.markdown(f"**Insurance:** {row.InsuranceAction}")
            st.markdown("**Questions to ask the physician**")
            for q in row.PhysicianQuestions.split(" | "):
                st.markdown(f"- {q}")
            st.markdown("**Personalized care plan**")
            for p in row.CarePlan.split(" | "):
                st.markdown(f"- {p}")
        with b:
            st.markdown("**Literature and guideline evidence**")
            lit = E.literature_for(row.PossibleConditions)
            if len(lit):
                st.dataframe(lit, hide_index=True)
            else:
                st.markdown("No guideline flags for this patient.")
            st.markdown('<div class="warn-box">Decision support only. Diagnosis and treatment decisions are made '
                        'by the physician.</div>', unsafe_allow_html=True)
        st.markdown("**Trend monitoring for the selected patient (12 months)**")
        trend = E.patient_trend(prow)
        slopes = E.trend_slopes(trend)
        st.dataframe(slopes, hide_index=True)
        fig = px.line(trend.melt("Month", var_name="Measure", value_name="Value"), x="Month", y="Value",
                      color="Measure", facet_row="Measure", markers=True, color_discrete_sequence=PALETTE, height=520)
        fig.update_yaxes(matches=None)
        st.plotly_chart(fig, key="hc_trend")
    with t[3]:
        st.subheader("Workflow: patient information to reasoning to recommendations")
        st.graphviz_chart(flow_dot(["Patient information", "Review medical records", "Analyze lab results",
                                    "Research medical literature", "Identify possible diagnoses",
                                    "Suggest physician questions", "Personalized care plan", "Monitor trends",
                                    "Coordinate appointments and insurance", "Physician decision"],
                                   loop_back=(7, 2), rankdir="LR", human={"Physician decision"}), width="content")
        st.subheader("Data sources fused by the AGI assistant")
        st.graphviz_chart("""digraph { rankdir=LR; bgcolor="transparent"; node [shape=box, style="rounded,filled", fontname=Helvetica, fillcolor="#E3F2FD", color="#0D47A1"];
            EHR [label="Electronic health record"]; LAB [label="Lab results"]; KB [label="Medical literature"]; SCH [label="Scheduling system"]; INS [label="Insurance system"];
            AGI [label="AGI clinical reasoning agent", fillcolor="#0D47A1", fontcolor=white];
            DOC [label="Physician", fillcolor="#FFE0B2"];
            EHR->AGI; LAB->AGI; KB->AGI; SCH->AGI; INS->AGI; AGI->DOC [label=" recommendations"]; DOC->AGI [label=" decisions", style=dashed]; }""",
                          width="content")
        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(res, x="PatientID", y="PriorityScore", color="PriorityLevel", title="Priority score by patient",
                         color_discrete_map={"High": "#C62828", "Medium": "#F57C00", "Low": "#2E7D32"})
            fig.add_hline(y=60, line_dash="dash", annotation_text="High threshold 60")
            fig.add_hline(y=35, line_dash="dot", annotation_text="Medium threshold 35")
            st.plotly_chart(fig, key="hc_c1")
        with c2:
            fig = px.scatter(merged, x="Age", y="CVRiskPercent", size="PriorityScore", color="BPStage",
                             hover_data=["PatientID"], title="Age compared with estimated cardiovascular risk",
                             color_discrete_sequence=PALETTE)
            st.plotly_chart(fig, key="hc_c2")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.plotly_chart(px.pie(res, names="BPStage", title="Blood pressure stages", hole=0.4,
                                   color_discrete_sequence=PALETTE), key="hc_c3")
        with c2:
            st.plotly_chart(px.pie(res, names="GlycemicStatus", title="Glycemic status", hole=0.4,
                                   color_discrete_sequence=PALETTE), key="hc_c4")
        with c3:
            fig = px.histogram(res, x="eGFR", nbins=12, title="Kidney function (eGFR) distribution",
                               color_discrete_sequence=[BLUE])
            fig.add_vline(x=60, line_dash="dash", annotation_text="60")
            st.plotly_chart(fig, key="hc_c5")
        comp = merged[["PatientID"]].copy()
        comp["Cardiovascular"] = [30 * min(r / 30, 1) for r in merged.CVRiskPercent]
        comp["Blood pressure"] = [20 * E._BP_SCORE[s] for s in merged.BPStage]
        comp["Glycemic"] = [20 * E._GLY_SCORE[s] for s in merged.GlycemicStatus]
        comp["Kidney"] = [15 * E._kid_score(v) for v in merged.eGFR]
        comp["BMI"] = [15 * E._BMI_SCORE[s] for s in merged.BMICategory]
        fig = px.bar(comp.melt("PatientID", var_name="Component", value_name="Points"), x="PatientID", y="Points",
                     color="Component", title="How each priority score is built (stacked components)",
                     color_discrete_sequence=PALETTE)
        st.plotly_chart(fig, key="hc_c6")
    with t[4]:
        formula("Body Mass Index", r"BMI = \frac{Weight_{kg}}{(Height_{cm}/100)^2}",
                "Measures weight relative to height. Categories: below 18.5 Underweight, 18.5 to 24.9 Normal, "
                "25 to 29.9 Overweight, 30 or more Obesity. Used for the care plan and 15 points of the priority score.")
        formula("Kidney function, CKD EPI 2021 eGFR",
                r"eGFR = 142 \times \min\left(\tfrac{S_{cr}}{\kappa},1\right)^{\alpha} \times \max\left(\tfrac{S_{cr}}{\kappa},1\right)^{-1.200} \times 0.9938^{Age} \times 1.012_{[female]}",
                "Scr is serum creatinine. For females kappa is 0.7 and alpha is minus 0.241; for males kappa is 0.9 "
                "and alpha is minus 0.302. Result in mL per minute per 1.73 square meters. Below 60 suggests chronic "
                "kidney disease and triggers a medication dosing question.")
        formula("Estimated cardiovascular risk (illustrative logistic model)",
                r"z = -9.0 + 0.065\,Age + 0.018\,SBP + 0.007\,LDL - 0.025\,HDL + 0.65\,Smoker + 0.45\,FamHx + 0.50\,Diabetes",
                "")
        st.latex(r"Risk = \frac{1}{1 + e^{-z}}")
        st.markdown("The logistic function turns the weighted sum into a probability between 0 and 1. Positive "
                    "weights raise risk; HDL has a negative weight because it is protective. This is an educational "
                    "model built for demonstration, not a validated clinical calculator.")
        st.markdown("---")
        formula("Priority score",
                r"P = 100\left(0.30\min\left(\tfrac{Risk}{0.30},1\right) + 0.20\,S_{BP} + 0.20\,S_{Gly} + 0.15\,S_{Kid} + 0.15\,S_{BMI}\right)",
                "Each S is a 0 to 1 severity for that domain (for example Stage 2 Hypertension is 0.85). Weights sum to 1, "
                "so P runs 0 to 100. High is 60 or more (visit within 7 days), Medium is 35 to 59 (within 30 days), "
                "Low is below 35 (within 90 days). A hypertensive crisis is always scheduled next day.")
        st.markdown("**Severity values used**")
        st.dataframe(pd.DataFrame(
            [("Blood pressure", k, v) for k, v in E._BP_SCORE.items()] +
            [("Glycemic", k, v) for k, v in E._GLY_SCORE.items()] +
            [("BMI", k, v) for k, v in E._BMI_SCORE.items()] +
            [("Kidney", "eGFR 90 or more", 0.0), ("Kidney", "60 to 89", 0.15), ("Kidney", "45 to 59", 0.55),
             ("Kidney", "30 to 44", 0.75), ("Kidney", "below 30", 1.0)],
            columns=["Domain", "Category", "Severity S"]), hide_index=True)
        formula("Blood pressure staging (ACC AHA 2017)", r"\text{Stage 2 if } SBP \geq 140 \text{ or } DBP \geq 90",
                "Normal below 120 and below 80; Elevated 120 to 129 and below 80; Stage 1 130 to 139 or 80 to 89; "
                "Stage 2 140 or more or 90 or more; Crisis 180 or more or 120 or more.")
        formula("Glycemic status", r"\text{Diabetes if } HbA1c \geq 6.5 \text{ or } Glucose \geq 126",
                "Prediabetes if HbA1c 5.7 to 6.4 or fasting glucose 100 to 125. Repeat testing confirms.")
        formula("Trend slope (least squares)", r"b = \frac{\sum (x_i-\bar{x})(y_i-\bar{y})}{\sum (x_i-\bar{x})^2},\quad \hat{y}_{t+3} = a + b\,(t+3)",
                "x is the month and y the measurement. A slope above 1 mmHg per month for systolic BP, 1.5 for glucose "
                "or 0.3 kg for weight is flagged as Rising.")
    with t[5]:
        export_panel("Healthcare", "Healthcare AGI Assistant Report",
                     [("Data source", src), ("Summary", f"{len(res)} patients analyzed. "
                       f"{int((res.PriorityLevel == 'High').sum())} High priority.")] +
                     [(f"{s['Step']}. {s['Stage']}", s["Reasoning"]) for s in trace.steps],
                     {"Patient results": res, "Reasoning trace": trace.to_df(), "Input data": df})


# =============================================================================
# Cybersecurity
# =============================================================================
CY_NUM = ["Severity", "AssetCriticality", "ThreatIntelScore", "AnomalyScore", "DetectionConfidence"]


def graph_dot(g, highlight_path: list | None = None, colors: dict | None = None, label_attr: str | None = None,
              edge_label: str = "p", rankdir: str = "LR", reach: set | None = None) -> str:
    hp = set(zip(highlight_path[:-1], highlight_path[1:])) if highlight_path and len(highlight_path) > 1 else set()
    hn = set(highlight_path or [])
    lines = [f'digraph G {{ rankdir={rankdir}; bgcolor="transparent"; nodesep=0.35; ranksep=0.5;',
             'node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=10];',
             'edge [fontname="Helvetica", fontsize=8];']
    for n, d in g.nodes(data=True):
        lab = d.get(label_attr, n) if label_attr else n
        fill = (colors or {}).get(d.get("type", ""), "#E3F2FD")
        if reach is not None and n not in reach and n not in hn:
            fill = "#ECEFF1"
        pen = "3" if n in hn else "1"
        col = "#C62828" if n in hn else "#0D47A1"
        lines.append(f'"{n}" [label="{lab}", fillcolor="{fill}", color="{col}", penwidth={pen}];')
    for u, v, d in g.edges(data=True):
        val = d.get(edge_label, "")
        lab = f"{val:.2f}" if isinstance(val, float) else str(val)
        if (u, v) in hp:
            lines.append(f'"{u}" -> "{v}" [label="{lab}", color="#C62828", penwidth=3, fontcolor="#C62828"];')
        else:
            lines.append(f'"{u}" -> "{v}" [label="{lab}", color="#607D8B"];')
    lines.append("}")
    return "\n".join(lines)


def page_cyber():
    st.header("Cybersecurity: AGI coordinated SIEM, SOAR, Graph DB, Threat Intelligence and AI agents")
    t = tabs6()
    with t[0]:
        why_agi("Today a security operations center uses separate tools for each step: the SIEM raises alerts, "
                "analysts pivot manually, threat intelligence lives in another console, SOAR playbooks run in "
                "isolation and lessons learned are rarely fed back. An AGI agent <b>coordinates the entire chain</b>: "
                "it understands the alert, investigates related users and systems, builds an attack graph, finds the "
                "most likely attack path, decides the response, executes approved playbooks, verifies recovery and "
                "learns from the incident.", [
            ("Alert triage", "Static severity, alert fatigue", "Context weighted risk using severity, asset value, intel and behavior", "Focus on what matters"),
            ("Investigation", "Manual pivots across consoles", "Automatic pivot on users and hosts", "Minutes instead of hours"),
            ("Attack graph", "Rarely built during an incident", "Built live from alert evidence", "See the whole campaign"),
            ("Attack path", "Analyst intuition", "Most probable path by graph search", "Protect the next hop first"),
            ("Response", "Playbooks chosen by hand", "Playbook matched to tactic with approval gates", "Fast and controlled"),
            ("Recovery", "Assumed after action", "Residual risk verified", "Proof of containment"),
            ("Learning", "After action report on file", "Detection confidence retuned from verdicts", "Fewer false positives next time"),
        ])
    with t[1]:
        df, src = data_source("cyber", E.synthetic_cyber(), E.CY_REQUIRED, "SIEM alerts", CY_NUM)
        if "MitreTechnique" not in df.columns:
            df["MitreTechnique"] = "Unknown"
        st.markdown(f"**Data in use: {src}. {len(df)} alerts. All rows shown.**")
        full_table(df, key="cy_data")
        st.markdown("**Field explanations**")
        field_dictionary(E.CY_FIELDS, df)
    with t[2]:
        with st.expander("Risk weights (must be tuned to your environment)"):
            w1 = st.slider("Severity weight", 0.0, 1.0, 0.35, 0.05, key="cy_w1")
            w2 = st.slider("Asset criticality weight", 0.0, 1.0, 0.25, 0.05, key="cy_w2")
            w3 = st.slider("Threat intelligence weight", 0.0, 1.0, 0.20, 0.05, key="cy_w3")
            w4 = st.slider("Anomaly weight", 0.0, 1.0, 0.20, 0.05, key="cy_w4")
            tot = w1 + w2 + w3 + w4 or 1
            weights = (w1 / tot, w2 / tot, w3 / tot, w4 / tot)
            st.caption("Weights are normalized so they sum to 1.")
        approved = st.checkbox("Human analyst approves execution of Critical playbooks", key="cy_appr")
    if "weights" not in locals():
        weights = (0.35, 0.25, 0.20, 0.20)
    scored, g, path, prob, entry, target, resp, learn, trace = E.analyze_cyber(df, approved, weights)
    with t[2]:
        c = st.columns(5)
        c[0].metric("Alerts", len(scored))
        c[1].metric("Critical", int((scored.RiskTier == "Critical").sum()))
        c[2].metric("High", int((scored.RiskTier == "High").sum()))
        c[3].metric("Attack path probability", f"{prob:.3f}")
        c[4].metric("Playbooks recovered", f"{int((resp.Recovered == 'Yes').sum())} of {len(resp)}")
        trace_view(trace)
        st.subheader("Risk ranked alerts (all)")
        full_table(scored, key="cy_scored")
        top = scored.iloc[0]
        st.subheader(f"Investigation of top alert {top.AlertID}")
        keys = {top.SourceHost, top.DestinationHost}
        rel = scored[(scored.UserAccount == top.UserAccount) | scored.SourceHost.isin(keys) | scored.DestinationHost.isin(keys)]
        st.dataframe(rel, hide_index=True)
        st.subheader("Most likely attack path")
        if path:
            st.markdown(f'<div class="warn-box">Entry point <b>{entry}</b> to highest value target <b>{target}</b>: '
                        f'{" then ".join(path)}. Joint probability {prob:.3f}.</div>', unsafe_allow_html=True)
        st.subheader("Response decisions and recovery verification")
        st.dataframe(resp, hide_index=True)
        if not approved and (resp.Status == "Awaiting human approval").any():
            st.warning("Critical playbooks are waiting for analyst approval. Tick the approval box above to execute them.")
        st.subheader("Learning from the incident")
        st.dataframe(learn, hide_index=True)
    with t[3]:
        st.subheader("AGI incident workflow")
        st.graphviz_chart(flow_dot(["Cyber alert", "Understand the alert", "Investigate related systems and users",
                                    "Build attack graph", "Determine likely attack path", "Decide response",
                                    "Human approval", "Execute approved playbook", "Verify recovery",
                                    "Learn from incident"], loop_back=(9, 1), rankdir="LR",
                                   human={"Human approval"}), width="content")
        st.subheader("Integrated architecture: one AGI coordinating every tool")
        st.graphviz_chart("""digraph { rankdir=TB; bgcolor="transparent"; node [shape=box, style="rounded,filled", fontname=Helvetica, fillcolor="#E3F2FD", color="#0D47A1"];
            AGI [label="AGI security agent", fillcolor="#0D47A1", fontcolor=white];
            SIEM [label="SIEM alerts and logs"]; TI [label="Threat intelligence"]; GDB [label="Graph database"]; SOAR [label="SOAR playbooks"]; AG [label="Specialist AI agents"]; H [label="SOC analyst approval", fillcolor="#FFE0B2"];
            SIEM->AGI; TI->AGI; AGI->GDB [dir=both]; AGI->AG [dir=both]; AGI->H; H->AGI [style=dashed]; AGI->SOAR [label=" approved actions"]; SOAR->SIEM [label=" verification", style=dashed]; }""",
                          width="content")
        st.subheader("Live attack graph (most likely path in red, edge labels are step probabilities)")
        st.graphviz_chart(graph_dot(g, path), width="content")
        c1, c2 = st.columns(2)
        with c1:
            tl = scored.copy()
            tl["Time"] = pd.to_datetime(tl.Timestamp)
            fig = px.scatter(tl, x="Time", y="AlertType", size="RiskScore", color="RiskTier",
                             title="Alert timeline (kill chain progression)", hover_data=["AlertID", "SourceHost", "DestinationHost"],
                             color_discrete_map={"Critical": "#C62828", "High": "#F57C00", "Medium": "#FBC02D", "Low": "#2E7D32"})
            st.plotly_chart(fig, key="cy_c1")
        with c2:
            fig = px.box(scored, x="AlertType", y="RiskScore", color="AlertType", title="Risk score by alert type",
                         color_discrete_sequence=PALETTE, points="all")
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, key="cy_c2")
        c1, c2 = st.columns(2)
        with c1:
            m = resp.melt(id_vars="AlertType", value_vars=["MaxRiskBefore", "ResidualRiskAfter"], var_name="Stage", value_name="Risk")
            st.plotly_chart(px.bar(m, x="AlertType", y="Risk", color="Stage", barmode="group",
                                   title="Recovery verification: risk before and after playbooks",
                                   color_discrete_sequence=["#C62828", "#2E7D32"]), key="cy_c3")
        with c2:
            mt = pd.DataFrame({"Step": ["Understand", "Investigate", "Graph", "Path", "Decide", "Execute", "Verify", "Learn"],
                               "Manual minutes": [15, 60, 45, 30, 20, 25, 30, 60],
                               "AGI minutes": [1, 3, 1, 1, 2, 5, 3, 2]})
            fig = px.bar(mt.melt("Step", var_name="Approach", value_name="Minutes"), x="Step", y="Minutes",
                         color="Approach", barmode="group", title="Illustrative time per step: manual compared with AGI",
                         color_discrete_sequence=["#90A4AE", BLUE])
            st.plotly_chart(fig, key="cy_c4")
            st.caption(f"Illustrative totals: manual {mt['Manual minutes'].sum()} minutes, AGI {mt['AGI minutes'].sum()} minutes.")
        st.plotly_chart(px.bar(learn, x="AlertType", y=["Precision", "ConfidenceMultiplier"], barmode="group",
                               title="Learning: precision and new confidence multiplier by alert type",
                               color_discrete_sequence=[BLUE, "#00897B"]), key="cy_c5")
    with t[4]:
        formula("Alert risk score", r"Risk = 100 \times C \times \left(w_1\frac{Sev}{10} + w_2\frac{Crit}{5} + w_3\,TI + w_4\,Anom\right)",
                "C is detection confidence. Severity and criticality are scaled to 0 to 1. Default weights 0.35, 0.25, "
                "0.20, 0.20 sum to 1, so Risk runs 0 to 100. Tiers: Critical 60 or more, High 40 to 59, Medium 20 to 39, Low below 20.")
        formula("Probability an observed step is real attacker progress", r"p = clip\left(C(0.5\,TI + 0.5\,Anom) + 0.1,\; 0.01,\; 0.99\right)",
                "Confident alerts with intelligence matches and abnormal behavior produce likely steps. The floor of 0.1 "
                "keeps weak evidence from vanishing.")
        formula("Fusing repeated evidence on the same edge", r"p_{edge} = 1 - (1-p_1)(1-p_2)\cdots(1-p_k)",
                "Two independent alerts on the same link make the link more likely than either alone.")
        formula("Most likely attack path", r"w_{edge} = -\ln p_{edge}, \qquad P(path) = \prod p_{edge} = e^{-\sum w_{edge}}",
                "Taking the negative logarithm turns the product of probabilities into a sum, so Dijkstra's shortest path "
                "algorithm finds the path with the highest joint probability.")
        formula("Residual risk after a playbook", r"Risk_{after} = Risk_{before} \times (1 - Effectiveness)",
                "Recovery is verified when residual risk falls below 20. Critical playbooks only execute after human approval.")
        formula("Learning from analyst verdicts", r"Precision = \frac{TP}{TP + FP}, \qquad Multiplier = 0.5 + 0.5 \times Precision",
                "Alert types that are often false positives get their future confidence reduced, cutting alert fatigue.")
    with t[5]:
        export_panel("Cybersecurity", "Cybersecurity AGI Incident Report",
                     [("Data source", src), ("Attack path", " then ".join(path) + f" (probability {prob:.3f})" if path else "None")] +
                     [(f"{s['Step']}. {s['Stage']}", s["Reasoning"]) for s in trace.steps],
                     {"Risk ranked alerts": scored, "Response and recovery": resp, "Learning": learn,
                      "Reasoning trace": trace.to_df()})


# =============================================================================
# Software Development
# =============================================================================
SW_NUM = ["EstimatedKLOC", "Complexity", "RequirementsCount", "TestCases", "DefectsFound"]
DEFAULT_REQ = ("Build a Streamlit cybersecurity application that uses a graph database, synthetic data, "
               "AI reasoning, CSV/PDF export and user authentication.")


def page_software():
    st.header("Software Development: AGI that designs, builds, tests, fixes, documents and deploys")
    t = tabs6()
    with t[0]:
        why_agi("Today's coding assistants complete a function or a file. An AGI software agent takes a "
                "<b>plain language goal</b> and carries it through the whole life cycle: architecture, code, "
                "database, test data, automated tests, error finding and fixing, documentation and deployment, "
                "keeping every artifact consistent with the original intent.", [
            ("Architecture", "Architect drafts diagrams by hand", "Derived directly from the requirement", "Days to minutes"),
            ("Code", "Line by line suggestions", "Complete module scaffold in dependency order", "Consistent structure"),
            ("Database and test data", "Separate scripts", "Generated with the schema", "Realistic testing from day one"),
            ("Testing", "Written late or skipped", "Generated per requirement", "Higher coverage"),
            ("Find and fix errors", "Manual debug cycle", "Autonomous test and fix loop", "Defects drop geometrically"),
            ("Documentation", "Often out of date", "Generated from the same model as the code", "Always current"),
            ("Deployment", "Manual checklist", "Quality gate plus human release approval", "Safer releases"),
        ])
    with t[1]:
        df, src = data_source("software", E.synthetic_software(), E.SW_REQUIRED, "Module plan", SW_NUM)
        st.markdown(f"**Data in use: {src}. {len(df)} modules. All rows shown.**")
        full_table(df, key="sw_data")
        st.markdown("**Field explanations**")
        field_dictionary(E.SW_FIELDS, df)
    with t[2]:
        req = st.text_area("Tell the AGI what to build", DEFAULT_REQ, key="sw_req", height=90)
        c1, c2 = st.columns(2)
        fix = c1.slider("Autonomous fix rate per iteration", 0.2, 0.9, 0.6, 0.05, key="sw_fix")
        mode = c2.selectbox("COCOMO project mode", ["Organic", "Semi detached", "Embedded"], key="sw_mode")
    if "fix" not in locals():
        fix, mode, req = 0.6, "Organic", DEFAULT_REQ
    try:
        mods, dg, order, iters, summ, trace = E.analyze_software(df, fix, mode)
        err = None
    except ValueError as ex:
        err = str(ex)
        mods, dg, order, iters, summ, trace = E.analyze_software(E.synthetic_software(), fix, mode)
    comps = E.parse_requirement(req)
    code = E.generate_scaffold(comps, "kalsnet_cyber_app")
    with t[2]:
        if err:
            st.error(err + " Synthetic modules are used until the cycle is fixed.")
        st.subheader("Understanding the requirement")
        st.dataframe(comps, hide_index=True)
        c = st.columns(5)
        c[0].metric("Total KLOC", summ["TotalKLOC"])
        c[1].metric("Effort person months", summ["EffortPM"])
        c[2].metric("Schedule months", summ["ScheduleMonths"])
        c[3].metric("Team size", summ["TeamSize"])
        c[4].metric("Defects remaining", f"{summ['InitialDefects']} to {summ['FinalDefects']}")
        trace_view(trace)
        st.subheader("Module plan with build order, effort and quality gate")
        full_table(mods, key="sw_mods")
        st.subheader("Autonomous test and fix iterations")
        st.dataframe(iters, hide_index=True)
        st.subheader("Generated code scaffold")
        st.code(code, language="python")
        st.download_button("Download generated scaffold", code.encode(), "generated_app.py", "text/x-python", key="sw_code")
        st.subheader("Generated documentation")
        doc = "\n".join(f"{r.ModuleID} {r.ModuleName} ({r.Layer}): depends on {r.DependsOn or 'nothing'}; "
                        f"{r.TestCases} tests; quality {r.QualityScore}; {r.Status}." for r in mods.itertuples())
        st.text(doc)
        st.subheader("Deployment checklist")
        st.dataframe(pd.DataFrame([
            ("All modules pass quality gate of 70", "Yes" if (mods.Status == "Ready to deploy").all() else "No"),
            ("Remaining defects below 1", "Yes" if summ["FinalDefects"] < 1 else "No"),
            ("Dependency graph has no cycles", "Yes" if err is None else "No"),
            ("Human release approval", "Required"),
        ], columns=["Check", "Result"]), hide_index=True)
    with t[3]:
        st.subheader("AGI software life cycle")
        st.graphviz_chart(flow_dot(["Requirement in plain language", "Design the architecture", "Write the Python code",
                                    "Create the database", "Generate test data", "Test the application", "Find errors",
                                    "Fix the errors", "Document the system", "Human release approval", "Deploy"],
                                   loop_back=(7, 5), rankdir="LR", human={"Human release approval"}), width="content")
        st.subheader("Generated layered architecture")
        layers = ["UI", "Security", "Logic", "Integration", "Data", "Test"]
        colors = {"UI": "#BBDEFB", "Security": "#FFCDD2", "Logic": "#C8E6C9", "Integration": "#FFE0B2", "Data": "#D1C4E9", "Test": "#F0F4C3"}
        dot = ['digraph { rankdir=TB; bgcolor="transparent"; compound=true; node [shape=box, style="rounded,filled", fontname=Helvetica, fontsize=10];']
        for L in layers:
            sub = mods[mods.Layer == L]
            if len(sub) == 0:
                continue
            dot.append(f'subgraph cluster_{L} {{ label="{L} layer"; style="rounded,filled"; fillcolor="{colors[L]}55"; color="#0D47A1"; fontname=Helvetica;')
            for r in sub.itertuples():
                dot.append(f'{r.ModuleID} [label="{r.ModuleName}", fillcolor="{colors[L]}"];')
            dot.append("}")
        for u, v in dg.edges:
            if u in set(mods.ModuleID):
                dot.append(f"{u} -> {v} [color=\"#607D8B\"];")
        dot.append("}")
        st.graphviz_chart("\n".join(dot), width="content")
        c1, c2 = st.columns(2)
        with c1:
            fig = px.line(iters, x="Iteration", y="DefectsRemaining", markers=True, title="Defect burn down in the test and fix loop",
                          color_discrete_sequence=["#C62828"])
            st.plotly_chart(fig, key="sw_c1")
        with c2:
            st.plotly_chart(px.bar(mods, x="ModuleName", y="EffortPM", color="Layer", title="Effort by module (person months)",
                                   color_discrete_sequence=PALETTE), key="sw_c2")
        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(mods, x="ModuleName", y="QualityScore", color="Status", title="Quality score by module",
                         color_discrete_map={"Ready to deploy": "#2E7D32", "Needs review": "#F57C00"})
            fig.add_hline(y=70, line_dash="dash", annotation_text="Quality gate 70")
            st.plotly_chart(fig, key="sw_c3")
        with c2:
            g2 = mods.sort_values("BuildOrder").copy()
            scale = summ["ScheduleMonths"] * 30 / max(g2.EffortPM.sum(), 1e-9)
            g2["StartDay"] = (g2.EffortPM.cumsum() - g2.EffortPM) * scale
            g2["Start"] = pd.Timestamp(TODAY) + pd.to_timedelta(g2.StartDay, unit="D")
            g2["Finish"] = g2.Start + pd.to_timedelta(g2.EffortPM * scale, unit="D")
            fig = px.timeline(g2, x_start="Start", x_end="Finish", y="ModuleName", color="Layer",
                              title="Build schedule in dependency order", color_discrete_sequence=PALETTE)
            fig.update_yaxes(autorange="reversed")
            st.plotly_chart(fig, key="sw_c4")
    with t[4]:
        formula("Basic COCOMO effort and schedule", r"E = a \times KLOC^{\,b}, \qquad T = c \times E^{\,d}, \qquad Team = \frac{E}{T}",
                "E is person months and T is calendar months. Organic: a 2.4, b 1.05, c 2.5, d 0.38. "
                "Semi detached: 3.0, 1.12, 2.5, 0.35. Embedded: 3.6, 1.20, 2.5, 0.32.")
        formula("Effort share per module", r"Share_i = \frac{KLOC_i \times Complexity_i}{\sum_j KLOC_j \times Complexity_j}, \qquad E_i = Share_i \times E",
                "Larger and more complex modules receive proportionally more effort.")
        formula("Defect density", r"DD_i = \frac{Defects_i}{KLOC_i}", "Defects per thousand lines of code.")
        formula("Test coverage estimate", r"Coverage_i = \min\left(1, \frac{TestCases_i}{3 \times Requirements_i}\right)",
                "Assumes three tests per requirement (normal, edge and error case) gives full coverage.")
        formula("Autonomous test and fix loop", r"D_n = D_0 (1 - f)^n",
                "Each iteration fixes fraction f of remaining defects. The loop stops when fewer than 0.5 defects remain or after 10 iterations.")
        formula("Quality score", r"Q_i = 100\left(0.4\,Coverage_i + 0.3\left(1 - \frac{D_{i,final}}{D_{i,0}}\right) + 0.3\left(1 - \min\left(\frac{DD_i}{10},1\right)\right)\right)",
                "Modules at 70 or above pass the deployment quality gate.")
        formula("Build order", r"\text{Topological sort of the dependency graph}",
                "A module is built only after every module it depends on. A dependency cycle is reported as an error.")
    with t[5]:
        export_panel("Software", "Software Development AGI Report",
                     [("Data source", src), ("Requirement", req), ("Generated scaffold", code)] +
                     [(f"{s['Step']}. {s['Stage']}", s["Reasoning"]) for s in trace.steps],
                     {"Requirement components": comps, "Module plan": mods, "Test and fix iterations": iters,
                      "Reasoning trace": trace.to_df()})


# =============================================================================
# Government and DoD
# =============================================================================
DEFAULT_MISSION = ("Ensure secure, resilient command and control communications for a coalition mission "
                   "within 120 days while defending against an active cyber threat.")


def page_gov():
    st.header("Government and DoD: AGI mission support assistant")
    t = tabs6()
    with t[0]:
        why_agi("For a large organization such as DISA, information lives in separate silos: network operations, "
                "cybersecurity, logistics, mission systems, policies, incident management, asset inventories, "
                "threat intelligence and knowledge graphs. An AGI mission assistant <b>connects all of them</b>, "
                "understands the mission, identifies risks, develops and simulates courses of action and recommends "
                "the best option. <b>The human remains the decision authority</b>, particularly for high impact actions.", [
            ("Mission analysis", "Staff reads many reports", "Mission text mapped to relevant domains automatically", "Faster mission analysis"),
            ("Risk picture", "Separate registers per office", "One fused, mission weighted register", "Common operating picture"),
            ("Courses of action", "Briefed qualitatively", "Scored on transparent weighted criteria", "Defensible choices"),
            ("Outcome simulation", "Rarely done", "Thousands of Monte Carlo trials per COA", "Risk aware decisions"),
            ("Recommendation", "Depends on who briefs", "Best option with evidence", "Consistency"),
            ("Approval and execution", "Manual tasking", "Approval gate then tracked execution", "Accountability"),
            ("Monitoring", "Periodic status slides", "Continuous planned versus actual tracking", "Early warning"),
        ])
    with t[1]:
        risks, s1 = data_source("gov_risks", E.synthetic_gov_risks(), E.GOV_RISK_REQUIRED, "Risk register",
                                ["Likelihood", "Impact", "ControlEffectiveness", "MissionDependency"])
        st.markdown(f"**Data in use: {s1}. {len(risks)} risks. All rows shown.**")
        full_table(risks, key="gv_r")
        coas, s2 = data_source("gov_coas", E.synthetic_gov_coas(), E.GOV_COA_REQUIRED, "Courses of action",
                               ["Effectiveness", "CostMillions", "TimeDays", "RiskLevel", "PolicyCompliance",
                                "SuccessProbability", "Uncertainty"])
        st.markdown(f"**Data in use: {s2}. {len(coas)} courses of action. All rows shown.**")
        full_table(coas, key="gv_c")
        st.markdown("**Field explanations**")
        field_dictionary(E.GOV_FIELDS, risks.merge(coas, how="cross") if len(risks) and len(coas) else None)
    if "Owner" not in risks.columns:
        risks["Owner"] = "Not provided"
    with t[2]:
        mission = st.text_area("Mission requirement", DEFAULT_MISSION, key="gv_mission", height=80)
        st.markdown("**Decision criteria weights**")
        c = st.columns(5)
        w = {"Effectiveness": c[0].slider("Effectiveness", 0.0, 1.0, 0.30, 0.05, key="gv_w1"),
             "CostMillions": c[1].slider("Cost", 0.0, 1.0, 0.20, 0.05, key="gv_w2"),
             "TimeDays": c[2].slider("Time", 0.0, 1.0, 0.15, 0.05, key="gv_w3"),
             "RiskLevel": c[3].slider("Risk", 0.0, 1.0, 0.20, 0.05, key="gv_w4"),
             "PolicyCompliance": c[4].slider("Policy", 0.0, 1.0, 0.15, 0.05, key="gv_w5")}
        if sum(w.values()) == 0:
            w["Effectiveness"] = 1.0
        thr = st.slider("Mission success threshold (effectiveness points)", 30, 90, 60, 5, key="gv_thr")
        c1, c2 = st.columns(2)
        approver = c1.text_input("Decision authority name", "Mission Commander", key="gv_name")
        approved = c2.checkbox("Decision authority approves the recommended course of action", key="gv_appr")
    if "mission" not in locals():
        mission, thr, approved, approver = DEFAULT_MISSION, 60, False, "Mission Commander"
        w = {"Effectiveness": 0.30, "CostMillions": 0.20, "TimeDays": 0.15, "RiskLevel": 0.20, "PolicyCompliance": 0.15}
    reg, ranked, monitor, doms, trace = E.analyze_gov(risks, coas, mission, w, thr, approved)
    best = ranked.iloc[0]
    with t[2]:
        st.markdown(f"**Domains the AGI linked to this mission:** {', '.join(doms)}")
        c = st.columns(4)
        c[0].metric("Risks analyzed", len(reg))
        c[1].metric("Mission relevant risks", int((reg.RelevantToMission == "Yes").sum()))
        c[2].metric("Recommended", best.COA)
        c[3].metric("Probability above threshold", f"{best.ProbAboveThreshold:.0%}".replace("%", " percent"))
        trace_view(trace)
        st.subheader("Fused mission risk register (all risks)")
        full_table(reg, key="gv_reg")
        st.subheader("Course of action evaluation and simulation")
        st.dataframe(ranked[["Rank", "COA", "Description", "MCDAScore", "SimMean", "P10", "P90",
                             "ProbAboveThreshold", "CombinedScore"]], hide_index=True)
        st.markdown(f'<div class="why-box"><b>Recommendation:</b> {best.COA}, {best.Description}. Combined score '
                    f'{best.CombinedScore}. Simulated mean outcome {best.SimMean} with a 10th to 90th percentile range '
                    f'of {best.P10} to {best.P90}.</div>', unsafe_allow_html=True)
        if approved:
            st.success(f"Approved by {approver}. Execution started and is being monitored.")
            st.dataframe(monitor, hide_index=True)
        else:
            st.warning("Execution is blocked until the decision authority approves.")
    with t[3]:
        st.subheader("AGI mission workflow")
        st.graphviz_chart(flow_dot(["Mission requirement", "Understand mission", "Analyze systems and data",
                                    "Identify risks", "Develop courses of action", "Simulate outcomes",
                                    "Recommend best option", "Human approval", "Execute", "Monitor"],
                                   loop_back=(9, 3), rankdir="LR", human={"Human approval"}), width="content")
        st.subheader("Enterprise data fusion for a large organization such as DISA")
        srcs = ["Network operations", "Cybersecurity", "Logistics", "Mission systems", "Policies",
                "Incident management", "Asset inventories", "Threat intelligence", "Knowledge graphs"]
        dot = ['digraph { layout=circo; bgcolor="transparent"; node [shape=box, style="rounded,filled", fontname=Helvetica, fontsize=10, fillcolor="#E3F2FD", color="#0D47A1"];',
               'AGI [label="AGI mission assistant\\nSIEM, SOAR, Graph DB,\\nThreat Intel, AI Agents", fillcolor="#0D47A1", fontcolor=white];',
               'H [label="Decision authority", fillcolor="#FFE0B2"];']
        for i, s in enumerate(srcs):
            dot.append(f'S{i} [label="{s}"]; S{i} -> AGI [color="#1E88E5"];')
        dot.append('AGI -> H [color="#F57C00", penwidth=2]; }')
        st.graphviz_chart("\n".join(dot), width="content")
        c1, c2 = st.columns(2)
        with c1:
            grid = np.zeros((5, 5), dtype=int)
            labels = [["" for _ in range(5)] for _ in range(5)]
            for r in reg.itertuples():
                li, ii = int(r.Likelihood) - 1, int(r.Impact) - 1
                if 0 <= li < 5 and 0 <= ii < 5:
                    grid[li][ii] += 1
                    labels[li][ii] += (" " if labels[li][ii] else "") + str(r.RiskID)
            score = np.array([[(l + 1) * (i + 1) for i in range(5)] for l in range(5)])
            fig = go.Figure(go.Heatmap(z=score, x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5], text=labels, texttemplate="%{text}",
                                       colorscale=[[0, "#2E7D32"], [0.4, "#FBC02D"], [0.7, "#F57C00"], [1, "#C62828"]],
                                       showscale=False))
            fig.update_layout(title="Inherent risk heat map (risk IDs placed by likelihood and impact)",
                              xaxis_title="Impact", yaxis_title="Likelihood", height=430)
            st.plotly_chart(fig, key="gv_c1")
        with c2:
            agg = reg.groupby("Domain")[["InherentRisk", "ResidualRisk", "MissionWeightedRisk"]].sum().reset_index()
            st.plotly_chart(px.bar(agg.melt("Domain", var_name="Measure", value_name="Score"), y="Domain", x="Score",
                                   color="Measure", barmode="group", orientation="h", height=430,
                                   title="Risk by domain: inherent, residual and mission weighted",
                                   color_discrete_sequence=["#C62828", "#F57C00", BLUE]), key="gv_c2")
        c1, c2 = st.columns(2)
        with c1:
            cats = ["n_Effectiveness", "n_CostMillions", "n_TimeDays", "n_RiskLevel", "n_PolicyCompliance"]
            names = ["Effectiveness", "Cost", "Time", "Risk", "Policy"]
            fig = go.Figure()
            for i, r in ranked.iterrows():
                fig.add_trace(go.Scatterpolar(r=[r[c] for c in cats] + [r[cats[0]]], theta=names + [names[0]],
                                              fill="toself", name=r.COA, line_color=PALETTE[i % len(PALETTE)]))
            fig.update_layout(title="Normalized criteria per COA (1 is best)", polar=dict(radialaxis=dict(range=[0, 1])), height=430)
            st.plotly_chart(fig, key="gv_c3")
        with c2:
            draws = E.simulate_draws(coas)
            fig = go.Figure()
            for i, (k, v) in enumerate(draws.items()):
                fig.add_trace(go.Histogram(x=v, name=k, opacity=0.55, nbinsx=40, marker_color=PALETTE[i % len(PALETTE)]))
            fig.add_vline(x=thr, line_dash="dash", annotation_text="Threshold")
            fig.update_layout(barmode="overlay", title="Monte Carlo outcome distributions (5000 trials each)",
                              xaxis_title="Simulated effectiveness", height=430)
            st.plotly_chart(fig, key="gv_c4")
        if monitor is not None:
            st.plotly_chart(px.line(monitor, x="Week", y=["PlannedProgress", "ActualProgress"], markers=True,
                                    title="Execution monitoring: planned compared with actual progress",
                                    color_discrete_sequence=["#90A4AE", BLUE]), key="gv_c5")
    with t[4]:
        formula("Inherent risk", r"R_{inh} = Likelihood \times Impact", "Range 1 to 25. Low 1 to 4, Moderate 5 to 9, High 10 to 14, Very High 15 to 25.")
        formula("Residual risk", r"R_{res} = R_{inh} \times (1 - ControlEffectiveness)", "Risk that remains after existing controls.")
        formula("Mission weighted risk", r"R_{mission} = R_{res} \times \frac{MissionDependency}{5}", "Ranks risks by how much the mission depends on the system.")
        formula("Criteria normalization", r"n_{benefit} = \frac{x}{\max(x)}, \qquad n_{cost} = \frac{\min(x)}{x}",
                "Effectiveness and policy compliance are benefits (higher is better). Cost, time and risk are costs (lower is better). Every normalized value is 0 to 1 with 1 best.")
        formula("Weighted sum decision score", r"MCDA = 100 \times \frac{\sum_j w_j\, n_j}{\sum_j w_j}", "Weights come from the sliders and express command priorities.")
        formula("Monte Carlo outcome simulation", r"S \sim Bernoulli(p), \quad Y \sim \mathcal{N}(\mu_S, \sigma), \quad \mu_1 = Eff,\; \mu_0 = 0.35\,Eff",
                "Each trial decides success with the COA's probability, then draws an outcome around full or partial effectiveness. Reported: mean, 10th and 90th percentiles and probability of exceeding the threshold.")
        formula("Combined recommendation score", r"Combined = 0.6 \times MCDA + 0.4 \times \bar{Y}", "Balances stated priorities with simulated real world performance.")
    with t[5]:
        export_panel("Government", "Government and DoD AGI Mission Support Report",
                     [("Mission", mission), ("Domains", ", ".join(doms)),
                      ("Recommendation", f"{best.COA}: {best.Description}"),
                      ("Approval", f"Approved by {approver}" if approved else "Pending approval")] +
                     [(f"{s['Step']}. {s['Stage']}", s["Reasoning"]) for s in trace.steps],
                     {"Risk register": reg, "COA evaluation": ranked.drop(columns=[c for c in ranked.columns if c.startswith("n_")]),
                      "Execution monitoring": monitor, "Reasoning trace": trace.to_df()})


# =============================================================================
# AGI and Knowledge Graph
# =============================================================================
KG_COLORS = {"Employee": "#BBDEFB", "Device": "#C8E6C9", "Network": "#FFF9C4", "Application": "#FFE0B2",
             "Server": "#FFE0B2", "Database": "#D1C4E9", "MissionSystem": "#FFCDD2", "Vulnerability": "#F8BBD0",
             "Threat": "#CFD8DC"}
DEFAULT_Q = "If this employee's laptop is compromised, what critical systems could ultimately be affected?"


def page_kg():
    st.header("AGI and Knowledge Graph: reasoning across connected entities")
    t = tabs6()
    with t[0]:
        why_agi("A knowledge graph stores how things connect: <b>User to Device to Network to Application to "
                "Vulnerability to Threat</b>. Traditional tools answer questions about one table at a time. An AGI "
                "reasons across the whole graph, so it can answer a question such as <i>if this employee's laptop is "
                "compromised, what critical systems could ultimately be affected?</i> by traversing every path, "
                "estimating how likely each is, ranking impact and finding the single change that reduces risk the most.", [
            ("Question answering", "Query languages and experts", "Plain language question resolved to graph entities", "Anyone can ask"),
            ("Reachability", "Manual whiteboard tracing", "Full traversal of every path", "No blind spots"),
            ("Likelihood", "Not quantified", "Path probability as product of link probabilities", "Prioritized exposure"),
            ("Impact", "Asset lists", "Probability multiplied by criticality", "Mission focused ranking"),
            ("Mitigation", "Best guess", "What if removal of every link, ranked by impact reduction", "Highest return fix first"),
        ])
    with t[1]:
        sn, se = E.synthetic_kg()
        nodes, s1 = data_source("kg_nodes", sn, E.KG_NODE_REQUIRED, "Graph nodes (entities)", ["Criticality"])
        st.markdown(f"**Data in use: {s1}. {len(nodes)} nodes. All rows shown.**")
        full_table(nodes, key="kg_n")
        edges, s2 = data_source("kg_edges", se, E.KG_EDGE_REQUIRED, "Graph edges (relationships)", ["CompromiseProbability"])
        st.markdown(f"**Data in use: {s2}. {len(edges)} edges. All rows shown.**")
        full_table(edges, key="kg_e")
        st.markdown("**Field explanations**")
        field_dictionary(E.KG_FIELDS, nodes.merge(edges, left_on="NodeID", right_on="SourceID") if len(edges) else nodes)
    bad = set(edges.SourceID.astype(str)) | set(edges.TargetID.astype(str))
    bad -= set(nodes.NodeID.astype(str))
    if bad:
        st.error("Edges reference unknown nodes: " + ", ".join(sorted(bad)) + ". Synthetic graph is used instead.")
        nodes, edges = E.synthetic_kg()
    with t[2]:
        q = st.text_input("Ask the graph a question", DEFAULT_Q, key="kg_q")
    if "q" not in locals():
        q = DEFAULT_Q
    resolved = E.resolve_question(q, nodes) or str(nodes.NodeID.iloc[0])
    ids = list(nodes.NodeID.astype(str))
    name_of = dict(zip(nodes.NodeID.astype(str), nodes.NodeName))
    with t[2]:
        start = st.selectbox("Compromised entity (resolved from your question, you can change it)", ids,
                             index=ids.index(resolved), format_func=lambda x: f"{x} {name_of[x]}", key=f"kg_start_{resolved}")
    if "start" not in locals():
        start = resolved
    g, br, mit, trace = E.analyze_kg(nodes, edges, start)
    mission = br[br.NodeType == "MissionSystem"]
    crit_path = []
    if len(mission):
        import networkx as nx
        crit_path = nx.dijkstra_path(g, start, mission.iloc[0].NodeID, weight="weight")
    with t[2]:
        c = st.columns(4)
        c[0].metric("Entities reachable", len(br))
        c[1].metric("Mission systems at risk", len(mission))
        c[2].metric("Total expected impact", round(br.ExpectedImpact.sum(), 2))
        c[3].metric("Best mitigation cuts impact by", f"{mit.ReductionPercent.iloc[0] if len(mit) else 0} percent")
        trace_view(trace)
        st.subheader("Answer")
        if len(mission):
            ans = "; ".join(f"{r.NodeName} (probability {r.ReachProbability}, {r.Hops} hops)" for r in mission.itertuples())
            st.markdown(f'<div class="warn-box">If <b>{name_of[start]}</b> is compromised, these mission systems '
                        f'could ultimately be affected: {ans}. Most likely route: {mission.iloc[0].Path}.</div>',
                        unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="step-box">No mission system is reachable from {name_of[start]}.</div>',
                        unsafe_allow_html=True)
        st.subheader("Blast radius (every reachable entity)")
        full_table(br, key="kg_br")
        st.subheader("What if mitigation analysis (top 10 links to break)")
        st.dataframe(mit.head(10), hide_index=True)
    with t[3]:
        st.subheader("Knowledge graph concept")
        st.graphviz_chart(flow_dot(["User", "Device", "Network", "Application", "Vulnerability", "Threat"], rankdir="LR"),
                          width="content")
        st.subheader("Example traversal for a compromised laptop")
        st.graphviz_chart(flow_dot(["Employee", "Laptop", "VPN", "Application Server", "Database", "Mission System"],
                                   color="#C62828", rankdir="LR"), width="content")
        st.subheader("Full knowledge graph (grey is unreachable, red is the most likely path to a mission system)")
        reach = set(br.NodeID) | {start}
        st.graphviz_chart(graph_dot(g, crit_path, KG_COLORS, label_attr="name", edge_label="p", reach=reach),
                          width="content")
        st.dataframe(pd.DataFrame([(k, v) for k, v in KG_COLORS.items()], columns=["Node type", "Color code"]), hide_index=True)
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(px.bar(br.head(12), y="NodeName", x="ExpectedImpact", color="NodeType", orientation="h",
                                   title="Expected impact of reachable entities", color_discrete_sequence=PALETTE,
                                   height=450), key="kg_c1")
        with c2:
            st.plotly_chart(px.scatter(br, x="Hops", y="ReachProbability", size="Criticality", color="NodeType",
                                       hover_data=["NodeName"], title="Probability decays with distance",
                                       color_discrete_sequence=PALETTE, height=450), key="kg_c2")
        c1, c2 = st.columns(2)
        with c1:
            if len(br):
                st.plotly_chart(px.treemap(br, path=["NodeType", "NodeName"], values="ExpectedImpact",
                                           title="Impact by entity type", color="ExpectedImpact",
                                           color_continuous_scale="Blues"), key="kg_c3")
        with c2:
            st.plotly_chart(px.bar(mit.head(8), y="BreakLink", x="ReductionPercent", orientation="h",
                                   title="Impact reduction if this link is broken (percent)",
                                   color_discrete_sequence=["#00897B"], height=450), key="kg_c4")
    with t[4]:
        formula("Edge weight", r"w_{uv} = -\ln p_{uv}", "p is the probability that compromise spreads across the link. Low probability links become long distances.")
        formula("Path probability", r"P(path) = \prod_{(u,v) \in path} p_{uv} = e^{-\sum w_{uv}}",
                "Dijkstra's algorithm finds the minimum total weight, which is the maximum probability path to every node.")
        formula("Expected impact", r"Impact_n = P_{max}(start \to n) \times Criticality_n", "Combines how likely and how bad.")
        formula("Total exposure", r"I_{total} = \sum_{n \neq start} Impact_n", "Single number describing the blast radius.")
        formula("Mitigation value", r"Reduction_e = 100 \times \frac{I_{total} - I_{total}^{(-e)}}{I_{total}}",
                "The agent removes each link e in turn, recomputes total exposure and ranks links by percent reduction. "
                "Removing the first link from the compromised entity is often trivially 100 percent; the next items show the most practical controls.")
        formula("Entity resolution from the question", r"Score = |Q \cap T| + 0.5\,[Type \in Q] + 3\,[Focus \in T]",
                "Q is the set of question words, T the words in an entity name and type, and Focus the word right before compromised.")
    with t[5]:
        export_panel("KnowledgeGraph", "AGI Knowledge Graph Impact Report",
                     [("Question", q), ("Resolved start", f"{start} {name_of[start]}")] +
                     [(f"{s['Step']}. {s['Stage']}", s["Reasoning"]) for s in trace.steps],
                     {"Blast radius": br, "Mitigation analysis": mit, "Nodes": nodes, "Edges": edges,
                      "Reasoning trace": trace.to_df()})


# =============================================================================
# Everyday Life Travel
# =============================================================================
TR_NUM = ["DurationHours", "CostUSD", "EnergyLevel", "FamilyRating"]


def page_travel():
    st.header("Everyday Life: AGI two week India trip planner")
    t = tabs6()
    with t[0]:
        why_agi("Ask a normal assistant to plan a two week India trip and you receive a list. An AGI "
                "<b>understands the family, the budget and the preferences</b>, plans flights, transport and hotels, "
                "calculates currency needs, builds a day by day itinerary, monitors flight changes, communicates with "
                "hotels and drivers, tracks expenses and adapts. If you say <i>we are tired, change tomorrow's "
                "schedule</i>, it understands the objective (recovery without losing the trip) and redesigns the day "
                "rather than answering the sentence literally.", [
            ("Family understanding", "One size fits all lists", "Interests, ages and children shape every choice", "Everyone enjoys the trip"),
            ("Budget and currency", "Manual spreadsheet", "Live total in USD and INR with cash estimate", "No surprises"),
            ("Itinerary", "Static list", "Optimized by enjoyment, time and energy", "Realistic days"),
            ("Flights", "Check apps yourself", "Delays absorbed into the day plan", "Less stress"),
            ("Communication", "Many calls and messages", "Drafted messages to hotels and drivers", "Time saved"),
            ("Adapting", "Literal answer to a sentence", "Understands intent and replans the whole day", "True assistant"),
        ])
    with t[1]:
        acts, src = data_source("travel", E.synthetic_travel_activities(), E.TR_REQUIRED, "Activities", TR_NUM)
        st.markdown(f"**Data in use: {src}. {len(acts)} activities. All rows shown.**")
        full_table(acts, key="tr_a")
        st.markdown("**Family (editable)**")
        family = st.data_editor(E.synthetic_family(), num_rows="dynamic", key="tr_fam", hide_index=True)
        st.markdown("**Hotels (editable)**")
        hotels = st.data_editor(E.synthetic_hotels(), num_rows="dynamic", key="tr_hot", hide_index=True)
        st.markdown("**Flights being monitored (editable, change DelayHours to see the plan adapt)**")
        flights = st.data_editor(E.synthetic_flights(), num_rows="dynamic", key="tr_fl", hide_index=True)
        st.markdown("**Field explanations**")
        field_dictionary(E.TR_FIELDS, acts.merge(hotels, on="City", how="left"))
    family = family.dropna(subset=["Name"]) if len(family) else E.synthetic_family()
    if len(family) == 0:
        family = E.synthetic_family()
    with t[2]:
        c = st.columns(4)
        start = c[0].date_input("Trip start date", date(2026, 12, 18), key="tr_start")
        days = c[1].slider("Trip length (days)", 7, 21, 14, key="tr_days")
        budget = c[2].number_input("Budget in USD", 1000, 200000, 22000, 500, key="tr_budget")
        fx = c[3].number_input("Exchange rate INR per USD (verify the current rate)", 50.0, 150.0, 88.0, 0.5, key="tr_fx")
        c = st.columns(3)
        dh = c[0].slider("Normal daily activity hours", 4, 10, 8, key="tr_h")
        de = c[1].slider("Normal daily energy budget", 4, 15, 10, key="tr_e")
        cur = c[2].number_input("Today is trip day", 1, days, 1, key="tr_cur")
        req = st.text_input("Tell the assistant what changed", "We are tired. Change tomorrow's schedule.", key="tr_req")
    if "start" not in locals():
        start, days, budget, fx, dh, de, cur, req = date(2026, 12, 18), 14, 22000, 88.0, 8, 10, 1, "We are tired. Change tomorrow's schedule."
    base, adj, target, expl, lines, total, cash, alloc, trace = E.analyze_travel(
        acts, family, hotels, flights, days, start, budget, fx, req, int(cur), dh, de)
    with t[2]:
        c = st.columns(5)
        c[0].metric("Travelers", len(family))
        c[1].metric("Cities", len(alloc))
        c[2].metric("Estimated total USD", f"{total:,.0f}")
        c[3].metric("Budget status", "Within budget" if total <= budget else "Over budget")
        c[4].metric("Cash to carry INR", f"{cash:,.0f}")
        trace_view(trace)
        if adj is not None:
            st.subheader(f"Replanned day {target}")
            st.markdown(f'<div class="why-box"><b>What the assistant understood:</b> {expl}</div>', unsafe_allow_html=True)
            a, b = st.columns(2)
            cols = ["Time", "Activity", "Category", "DurationHours", "EnergyLevel", "CostUSD"]
            with a:
                st.markdown("**Before**")
                st.dataframe(base[base.Day == target][cols], hide_index=True)
            with b:
                st.markdown("**After**")
                st.dataframe(adj[adj.Day == target][cols], hide_index=True)
        final = adj if adj is not None else base
        st.subheader("Day by day itinerary (final, all days)")
        full_table(final, key="tr_it")
        st.subheader("Budget and currency")
        st.dataframe(lines, hide_index=True)
        st.subheader("Flight monitoring")
        st.dataframe(flights, hide_index=True)
        st.subheader("Messages drafted for hotels and drivers")
        st.text(E.draft_messages(final, hotels))
        st.subheader("Expense tracker (enter actual spending)")
        tracker = lines[["Category", "USD"]].rename(columns={"USD": "PlannedUSD"}).assign(ActualUSD=0.0)
        tracked = st.data_editor(tracker, key="tr_exp", hide_index=True, disabled=["Category", "PlannedUSD"])
        tracked["RemainingUSD"] = tracked.PlannedUSD - tracked.ActualUSD
        st.dataframe(tracked, hide_index=True)
    with t[3]:
        st.subheader("AGI travel planning loop")
        st.graphviz_chart(flow_dot(["Plan my two week India trip", "Understand family and budget", "Check flights",
                                    "Plan transportation", "Reserve hotels", "Calculate currency needs",
                                    "Build day by day itinerary", "Monitor flights and changes",
                                    "Communicate with hotels and drivers", "Track expenses"],
                                   loop_back=(7, 6), rankdir="LR"), width="content")
        st.subheader("Understanding intent, not just words")
        st.graphviz_chart("""digraph { rankdir=LR; bgcolor="transparent"; node [shape=box, style="rounded,filled", fontname=Helvetica, fillcolor="#E3F2FD", color="#0D47A1"];
            A [label="We are tired.\\nChange tomorrow's schedule.", fillcolor="#FFE0B2"]; B [label="Intent: recover energy\\nwhile keeping the trip enjoyable"];
            C [label="Later start\\nfewer hours\\nlower energy"]; D [label="Prefer relaxation\\nand low effort sights"]; E [label="Move skipped sights\\nto later days"]; F [label="Redesigned day", fillcolor="#0D47A1", fontcolor=white];
            A->B; B->C; B->D; B->E; C->F; D->F; E->F; }""", width="content")
        st.subheader("Route")
        dot = ['digraph { rankdir=LR; bgcolor="transparent"; node [shape=ellipse, style=filled, fontname=Helvetica, fillcolor="#BBDEFB", color="#0D47A1"];']
        for i, (cty, nd) in enumerate(alloc):
            dot.append(f'C{i} [label="{cty}\\n{nd} days"];')
            if i:
                dot.append(f"C{i - 1} -> C{i};")
        dot.append("}")
        st.graphviz_chart("\n".join(dot), width="content")
        c1, c2 = st.columns(2)
        with c1:
            per = final.groupby("Day").agg(Hours=("DurationHours", "sum"), Energy=("EnergyLevel", "sum")).reset_index()
            fig = px.bar(per, x="Day", y=["Hours", "Energy"], barmode="group", title="Daily load (final plan)",
                         color_discrete_sequence=[BLUE, "#F57C00"])
            st.plotly_chart(fig, key="tr_c1")
        with c2:
            st.plotly_chart(px.pie(lines, names="Category", values="USD", hole=0.4, title="Budget split",
                                   color_discrete_sequence=PALETTE), key="tr_c2")
        c1, c2 = st.columns(2)
        with c1:
            if adj is not None:
                cmp = pd.DataFrame({"Plan": ["Before", "After"],
                                    "Hours": [base[base.Day == target].DurationHours.sum(), adj[adj.Day == target].DurationHours.sum()],
                                    "Energy": [base[base.Day == target].EnergyLevel.sum(), adj[adj.Day == target].EnergyLevel.sum()]})
                st.plotly_chart(px.bar(cmp.melt("Plan", var_name="Measure", value_name="Value"), x="Measure", y="Value",
                                       color="Plan", barmode="group", title=f"Day {target} before and after replanning",
                                       color_discrete_sequence=["#90A4AE", "#2E7D32"]), key="tr_c3")
        with c2:
            st.plotly_chart(px.histogram(final[final.ActivityID != ""], x="Category", color="City",
                                         title="Activity mix by category and city", color_discrete_sequence=PALETTE),
                            key="tr_c4")
        if adj is not None:
            dd = adj[(adj.Day == target) & (adj.ActivityID != "")].copy()
            if len(dd):
                dd["Start"] = pd.to_datetime(dd.Date + " " + dd.Time)
                dd["Finish"] = dd.Start + pd.to_timedelta(dd.DurationHours, unit="h")
                fig = px.timeline(dd, x_start="Start", x_end="Finish", y="Activity", color="Category",
                                  title=f"Redesigned schedule for day {target}", color_discrete_sequence=PALETTE)
                fig.update_yaxes(autorange="reversed")
                st.plotly_chart(fig, key="tr_c5")
    with t[4]:
        formula("Day allocation by city (largest remainder method)",
                r"q_c = \frac{W_c}{\sum W}(D - N), \qquad Days_c = 1 + \lfloor q_c \rfloor + [c \in \text{largest remainders}]",
                "W is the total family rating of activities in the city, D the trip length and N the number of cities. "
                "Each city gets at least one day and the remaining days follow enjoyment weight. The total always equals D.")
        formula("Activity score", r"S_a = Rating_a + 1.0\,[Category_a \in Interests] + 1.5\,[Rest \wedge Relaxation] - 0.01\,Cost_a[Budget]",
                "Bracketed terms are 1 when the condition holds. Rest and budget terms only apply in those replanning modes.")
        formula("Daily selection (greedy constrained knapsack)",
                r"\text{choose by } \frac{S_a}{Energy_a} \text{ subject to } \sum Hours \le H,\; \sum Energy \le E",
                "Activities with the best enjoyment per unit of energy are taken first while time and energy budgets allow. "
                "Travel days lose 3 hours and start at noon. Flight delays shift the start time.")
        formula("Fatigue replanning", r"H' = \min(H,5), \quad E' = \min(E,5), \quad Start' = \max(Start, 10{:}30), \quad Energy_a \le 2",
                "The assistant interprets tiredness as an objective to recover, not a literal edit.")
        formula("Trip budget", r"Total = Flights \times n + \sum_c Nights_c \times Rate_c \times \lceil n/3 \rceil + \sum_a Cost_a \times n + 60\,D + 15\,n\,D",
                "n is the number of travelers. Ground transport is 60 USD per day and food 15 USD per person per day (adjustable assumptions).")
        formula("Currency", r"INR = USD \times Rate, \qquad Cash_{INR} = 0.20 \times LocalSpend_{USD} \times Rate",
                "Local spend excludes flights. Twenty percent in cash covers markets, tips and small vendors.")
    with t[5]:
        final = adj if adj is not None else base
        export_panel("Travel", "AGI India Trip Plan",
                     [("Request", req), ("Understanding", expl or "No change requested"),
                      ("Totals", f"Estimated {total:,.0f} USD; budget {budget:,.0f} USD; cash {cash:,.0f} INR"),
                      ("Messages", E.draft_messages(final, hotels))] +
                     [(f"{s['Step']}. {s['Stage']}", s["Reasoning"]) for s in trace.steps],
                     {"Final itinerary": final, "Original itinerary": base if adj is not None else None,
                      "Budget": lines, "Flights": flights, "Family": family, "Reasoning trace": trace.to_df()})


ROUTER = {"Overview": page_overview, "Healthcare": page_healthcare, "Cybersecurity": page_cyber,
          "Software Development": page_software, "Government and DoD": page_gov,
          "AGI and Knowledge Graph": page_kg, "Everyday Life Travel Planner": page_travel}
ROUTER[page]()
