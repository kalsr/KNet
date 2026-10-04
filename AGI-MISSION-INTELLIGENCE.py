"""
AGI Mission Intelligence Suite
Developed by Randy Singh from Kalsnet (KNet) Consulting Group

Run with:  streamlit run AGI-MISSION-INTELLIGENCE.py
Single self-contained file: the AGI engine and report exporters are built in.
Install packages with:  pip install -r requirements.txt
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

import re as _re
from datetime import timedelta as _td
from types import SimpleNamespace as _SimpleNamespace

import networkx as nx


# =============================================================================
# AGI ENGINE  (built in - replaces the separate agi_engine.py module)
# =============================================================================
class ReasoningTrace:
    """Ordered record of every reasoning step the agent takes."""

    def __init__(self):
        self.steps = []

    def add(self, stage: str, reasoning: str):
        self.steps.append({"Step": len(self.steps) + 1, "Stage": stage, "Reasoning": reasoning})
        return self

    def to_df(self) -> pd.DataFrame:
        return pd.DataFrame(self.steps, columns=["Step", "Stage", "Reasoning"])


def validate_columns(df: pd.DataFrame, required: list) -> list:
    return [c for c in required if c not in df.columns]


def _yes(v) -> bool:
    return str(v).strip().lower() in ("yes", "y", "true", "1", "1.0")


def _num(v, default=0.0) -> float:
    try:
        f = float(v)
        return default if math.isnan(f) else f
    except (TypeError, ValueError):
        return default


_WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# ----------------------------------------------------------------------------- Healthcare
HC_REQUIRED = ["PatientID", "Age", "Sex", "HeightCm", "WeightKg", "SystolicBP", "DiastolicBP", "HeartRate",
               "FastingGlucose", "HbA1c", "LDL", "HDL", "Creatinine", "Smoker", "FamilyHistoryCVD",
               "ActiveMedications", "LastVisitDaysAgo", "InsuranceStatus", "PreferredDay"]

HC_FIELDS = {
    "PatientID": "Unique patient identifier. Links results back to the record.",
    "Age": "Age in years. Drives cardiovascular risk and kidney function (eGFR).",
    "Sex": "F or M. Needed by the CKD EPI 2021 eGFR formula and the HDL threshold.",
    "HeightCm": "Height in centimeters. Used to compute BMI.",
    "WeightKg": "Weight in kilograms. Used to compute BMI and weight trends.",
    "SystolicBP": "Top blood pressure number (mmHg). Used for BP stage and cardiovascular risk.",
    "DiastolicBP": "Bottom blood pressure number (mmHg). Used for BP stage.",
    "HeartRate": "Resting heart rate (beats per minute). Above 100 is flagged.",
    "FastingGlucose": "Fasting blood sugar (mg/dL). Used for glycemic status.",
    "HbA1c": "Three month average blood sugar (percent). Used for glycemic status.",
    "LDL": "LDL ('bad') cholesterol (mg/dL). Raises cardiovascular risk.",
    "HDL": "HDL ('good') cholesterol (mg/dL). Protective, lowers cardiovascular risk.",
    "Creatinine": "Serum creatinine (mg/dL). Used to estimate kidney function (eGFR).",
    "Smoker": "Yes or No. Raises cardiovascular risk.",
    "FamilyHistoryCVD": "Yes or No for early heart disease in the family. Raises cardiovascular risk.",
    "ActiveMedications": "Number of current medications. Five or more triggers a polypharmacy review.",
    "LastVisitDaysAgo": "Days since the last visit. Used to flag overdue follow up.",
    "InsuranceStatus": "Active, Prior authorization needed, Pending verification or Expired. Drives insurance actions.",
    "PreferredDay": "Weekday the patient prefers for appointments. Used for scheduling.",
}

_BP_SCORE = {"Normal": 0.0, "Elevated": 0.3, "Stage 1 Hypertension": 0.6, "Stage 2 Hypertension": 0.85,
             "Hypertensive Crisis": 1.0}
_GLY_SCORE = {"Normal": 0.0, "Prediabetes range": 0.5, "Diabetes range": 1.0}
_BMI_SCORE = {"Underweight": 0.4, "Normal": 0.0, "Overweight": 0.4, "Obesity": 0.8}


def _kid_score(egfr: float) -> float:
    if egfr >= 90:
        return 0.0
    if egfr >= 60:
        return 0.15
    if egfr >= 45:
        return 0.55
    if egfr >= 30:
        return 0.75
    return 1.0


def _bp_stage(s: float, d: float) -> str:
    if s >= 180 or d >= 120:
        return "Hypertensive Crisis"
    if s >= 140 or d >= 90:
        return "Stage 2 Hypertension"
    if s >= 130 or d >= 80:
        return "Stage 1 Hypertension"
    if s >= 120:
        return "Elevated"
    return "Normal"


def _gly_status(a1c: float, glu: float) -> str:
    if a1c >= 6.5 or glu >= 126:
        return "Diabetes range"
    if a1c >= 5.7 or glu >= 100:
        return "Prediabetes range"
    return "Normal"


def _bmi_cat(b: float) -> str:
    if b < 18.5:
        return "Underweight"
    if b < 25:
        return "Normal"
    if b < 30:
        return "Overweight"
    return "Obesity"


def egfr_ckd_epi_2021(scr: float, age: float, sex: str) -> float:
    female = str(sex).strip().upper().startswith("F")
    k, a = (0.7, -0.241) if female else (0.9, -0.302)
    r = max(scr, 0.1) / k
    v = 142 * min(r, 1) ** a * max(r, 1) ** -1.200 * 0.9938 ** age
    return v * 1.012 if female else v


def synthetic_healthcare(n: int = 24, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    ins = ["Active", "Active", "Active", "Prior authorization needed", "Pending verification", "Expired"]
    rows = []
    for i in range(n):
        profile = i % 4                 # 0 healthy, 1 metabolic, 2 cardiovascular, 3 kidney / older
        sex = "F" if i % 2 == 0 else "M"
        age = int(rng.integers(28, 50)) if profile == 0 else int(rng.integers(45, 82))
        h = float(rng.normal(163 if sex == "F" else 177, 7))
        bmi = float(rng.normal(*{0: (23, 2), 1: (33, 3), 2: (28, 3), 3: (26, 3)}[profile]))
        sbp = float(rng.normal(*{0: (116, 6), 1: (134, 8), 2: (152, 14), 3: (138, 10)}[profile]))
        dbp = sbp * 0.6 + float(rng.normal(4, 4))
        if i == 6:
            sbp, dbp = 186.0, 118.0     # one hypertensive crisis for demonstration
        glu = float(rng.normal(*{0: (88, 6), 1: (138, 18), 2: (104, 8), 3: (112, 14)}[profile]))
        a1c = 2.6 + 0.032 * glu + float(rng.normal(0, 0.15))
        rows.append({
            "PatientID": f"P{i + 1:03d}", "Age": age, "Sex": sex, "HeightCm": round(h, 1),
            "WeightKg": round(bmi * (h / 100) ** 2, 1), "SystolicBP": int(round(sbp)), "DiastolicBP": int(round(dbp)),
            "HeartRate": int(round(rng.normal(74 + (10 if profile == 2 else 0), 9))),
            "FastingGlucose": int(round(glu)), "HbA1c": round(a1c, 1),
            "LDL": int(round(rng.normal(*{0: (105, 15), 1: (140, 20), 2: (165, 20), 3: (125, 20)}[profile]))),
            "HDL": int(round(rng.normal(*{0: (58, 8), 1: (40, 6), 2: (42, 6), 3: (48, 7)}[profile]))),
            "Creatinine": round(max(0.5, float(rng.normal(1.9, 0.4)) if profile == 3
                                    else float(rng.normal(0.8 if sex == "F" else 1.0, 0.12))), 2),
            "Smoker": "Yes" if rng.random() < (0.1, 0.25, 0.45, 0.2)[profile] else "No",
            "FamilyHistoryCVD": "Yes" if rng.random() < (0.2, 0.35, 0.5, 0.3)[profile] else "No",
            "ActiveMedications": int(rng.integers(0, 2)) if profile == 0 else int(rng.integers(2, 8)),
            "LastVisitDaysAgo": int(rng.integers(20, 500)),
            "InsuranceStatus": ins[int(rng.integers(0, len(ins)))],
            "PreferredDay": _WEEKDAYS[int(rng.integers(0, 5))],
        })
    return pd.DataFrame(rows)


_LIT = [
    ("ypertens", "High blood pressure",
     "2017 ACC/AHA Guideline for the Prevention, Detection, Evaluation and Management of High Blood Pressure in Adults",
     "Confirm with repeated and out of office readings; lifestyle therapy for everyone, medication guided by stage and cardiovascular risk."),
    ("iabetes", "Diabetes",
     "American Diabetes Association Standards of Care in Diabetes (updated each year)",
     "A diagnosis needs confirmation by repeat testing unless symptoms are clear; HbA1c targets are individualized."),
    ("rediabetes", "Prediabetes",
     "American Diabetes Association Standards of Care in Diabetes (updated each year)",
     "Lifestyle programs reduce progression to type 2 diabetes; retest at least yearly."),
    ("kidney", "Chronic kidney disease",
     "KDIGO Clinical Practice Guideline for the Evaluation and Management of CKD (2024)",
     "Confirm reduced eGFR over at least 3 months, check urine albumin, and review doses of renally cleared drugs."),
    ("ipid", "Cholesterol",
     "2018 AHA/ACC Guideline on the Management of Blood Cholesterol",
     "LDL of 190 or more usually warrants high intensity statin therapy; otherwise treatment follows overall risk."),
    ("HDL", "Low HDL",
     "2018 AHA/ACC Guideline on the Management of Blood Cholesterol",
     "Low HDL is a risk enhancer; focus on overall risk reduction rather than raising HDL alone."),
    ("Obesity", "Obesity",
     "US Preventive Services Task Force: behavioral weight loss interventions for adults (2018)",
     "Offer or refer adults with BMI 30 or more to intensive, multicomponent behavioral programs."),
    ("ardiovascular", "Cardiovascular risk",
     "2019 ACC/AHA Guideline on the Primary Prevention of Cardiovascular Disease",
     "Use a validated 10 year risk estimate plus risk enhancers to guide statin and lifestyle decisions."),
    ("achycardia", "Fast resting heart rate",
     "Clinical evaluation (no single guideline)",
     "A resting rate above 100 deserves an ECG and review of causes such as anemia, thyroid or medication effects."),
]


def literature_for(conditions: str) -> pd.DataFrame:
    rows = [{"Finding": t, "Guideline or source": g, "Key point": k}
            for key, t, g, k in _LIT if key in str(conditions)]
    df = pd.DataFrame(rows, columns=["Finding", "Guideline or source", "Key point"])
    return df.drop_duplicates("Finding").reset_index(drop=True)


def analyze_healthcare(df: pd.DataFrame, today):
    trace = ReasoningTrace()
    out = []
    for r in df.to_dict("records"):
        age, sex = _num(r["Age"]), str(r["Sex"])
        h, w = _num(r["HeightCm"], 170), _num(r["WeightKg"], 70)
        sbp, dbp, hr = _num(r["SystolicBP"]), _num(r["DiastolicBP"]), _num(r["HeartRate"])
        glu, a1c = _num(r["FastingGlucose"]), _num(r["HbA1c"])
        ldl, hdl, scr = _num(r["LDL"]), _num(r["HDL"]), _num(r["Creatinine"], 1.0)
        meds, last = _num(r["ActiveMedications"]), _num(r["LastVisitDaysAgo"])
        smoker, fam = _yes(r.get("Smoker", "No")), _yes(r.get("FamilyHistoryCVD", "No"))

        bmi = w / ((h / 100) ** 2) if h > 0 else 0
        bmic, bps, gly = _bmi_cat(bmi), _bp_stage(sbp, dbp), _gly_status(a1c, glu)
        egfr = egfr_ckd_epi_2021(scr, age, sex)
        z = (-9.0 + 0.065 * age + 0.018 * sbp + 0.007 * ldl - 0.025 * hdl + 0.65 * smoker + 0.45 * fam
             + 0.50 * (gly == "Diabetes range"))
        risk = 1 / (1 + math.exp(-z))
        score = 100 * (0.30 * min(risk / 0.30, 1) + 0.20 * _BP_SCORE[bps] + 0.20 * _GLY_SCORE[gly]
                       + 0.15 * _kid_score(egfr) + 0.15 * _BMI_SCORE[bmic])
        level = "High" if score >= 60 else "Medium" if score >= 35 else "Low"
        crisis = bps == "Hypertensive Crisis"

        conds, qs, plan = [], [], []
        if crisis:
            conds.append("Hypertensive crisis")
            qs.append("Does this reading need same day evaluation for end organ damage?")
            plan.append("Same day clinical assessment and repeat blood pressure measurement")
        elif bps in ("Stage 1 Hypertension", "Stage 2 Hypertension"):
            conds.append(f"Hypertension ({bps.replace(' Hypertension', '').lower()})")
            qs.append("Should home blood pressure monitoring confirm the diagnosis before starting or changing medication?")
            plan.append("Home blood pressure log twice daily for 2 weeks; reduce sodium; 150 minutes of activity per week")
        if gly == "Diabetes range":
            conds.append("Possible type 2 diabetes")
            qs.append("Should HbA1c or fasting glucose be repeated to confirm diabetes?")
            plan.append("Repeat HbA1c; referral to diabetes self management education")
        elif gly == "Prediabetes range":
            conds.append("Prediabetes")
            qs.append("Is a structured lifestyle program appropriate to prevent progression?")
            plan.append("Lifestyle program; recheck glucose in 12 months")
        if egfr < 60:
            conds.append("Possible chronic kidney disease")
            qs.append(f"Should renally cleared medications be dose adjusted for an eGFR of {egfr:.0f}?")
            plan.append("Repeat creatinine and urine albumin in 3 months; avoid NSAIDs")
        if ldl >= 160:
            conds.append("Hyperlipidemia")
            qs.append("Is statin therapy indicated given LDL and overall cardiovascular risk?")
            plan.append("Heart healthy diet; repeat lipid panel")
        if hdl < (50 if sex.upper().startswith("F") else 40):
            conds.append("Low HDL")
        if bmi >= 30:
            conds.append("Obesity")
            plan.append("Refer to an intensive behavioral weight management program")
        if hr > 100:
            conds.append("Tachycardia")
            qs.append("Is an ECG needed to evaluate the resting heart rate above 100?")
        if risk >= 0.20:
            conds.append("Elevated cardiovascular risk")
            qs.append("Should cardiovascular prevention therapy be discussed?")
        if smoker:
            plan.append("Offer smoking cessation counselling and pharmacotherapy")
        if meds >= 5:
            qs.append(f"Should the {int(meds)} active medications be reviewed for interactions (polypharmacy)?")
        if not qs:
            qs.append("Are routine preventive screenings up to date?")
        plan.append("Follow up as scheduled and continue trend monitoring")

        interval = 1 if crisis else {"High": 7, "Medium": 30, "Low": 90}[level]
        due = today + _td(days=interval)
        appt = due
        pref = str(r.get("PreferredDay", "")).strip().title()
        if not crisis and pref in _WEEKDAYS:
            for back in range(7):
                cand = due - _td(days=back)
                if cand <= today:
                    break
                if cand.weekday() == _WEEKDAYS.index(pref):
                    appt = cand
                    break
        appt_txt = f"{appt.isoformat()} ({appt.strftime('%A')})" + (" URGENT" if crisis else "")
        overdue = last > {"High": 90, "Medium": 180, "Low": 365}[level]
        status = str(r.get("InsuranceStatus", "Active")).strip()
        ins = {"active": "Verified, no action",
               "prior authorization needed": "Submit prior authorization before the next appointment",
               "pending verification": "Verify coverage with the payer before the visit",
               "expired": "Coverage expired: contact the patient and a financial counselor"}.get(
            status.lower(), f"Review insurance status: {status}")

        out.append({"PatientID": r["PatientID"], "BMI": round(bmi, 1), "BMICategory": bmic, "BPStage": bps,
                    "GlycemicStatus": gly, "eGFR": round(egfr, 1), "CVRiskPercent": round(100 * risk, 1),
                    "PriorityScore": round(score, 1), "PriorityLevel": level,
                    "PossibleConditions": "; ".join(conds) if conds else "No flags",
                    "PhysicianQuestions": " | ".join(qs), "CarePlan": " | ".join(plan),
                    "NextAppointment": appt_txt, "Overdue": "Yes" if overdue else "No", "InsuranceAction": ins})
    res = pd.DataFrame(out).sort_values("PriorityScore", ascending=False).reset_index(drop=True)
    n_hi = int((res.PriorityLevel == "High").sum())
    trace.add("Observe", f"Loaded {len(res)} patient records with vitals, labs, history and insurance status.")
    trace.add("Review medical records", "Computed BMI, blood pressure stage (ACC AHA 2017) and glycemic status for every patient.")
    trace.add("Analyze lab results", f"Estimated kidney function with CKD EPI 2021; {int((res.eGFR < 60).sum())} patients have eGFR below 60.")
    trace.add("Reason across sources", "Combined age, blood pressure, cholesterol, smoking, family history and diabetes into an illustrative cardiovascular risk.")
    trace.add("Research literature", "Linked each finding to the relevant clinical guideline for the physician to review.")
    trace.add("Prioritize", f"Weighted five severity domains into a 0 to 100 priority score: {n_hi} High, "
                            f"{int((res.PriorityLevel == 'Medium').sum())} Medium, {int((res.PriorityLevel == 'Low').sum())} Low.")
    trace.add("Plan and coordinate", "Drafted physician questions and care plans, scheduled visits by urgency and preferred weekday, and flagged insurance follow ups.")
    trace.add("Human decision authority", "All outputs are decision support. The physician confirms every diagnosis and treatment.")
    return res, trace


def patient_trend(prow) -> pd.DataFrame:
    rng = np.random.default_rng(sum(ord(c) for c in str(prow["PatientID"])))
    months = list(range(1, 13))
    out = {"Month": months}
    for col, sd, noise in [("SystolicBP", 1.2, 3.0), ("FastingGlucose", 1.6, 4.0), ("WeightKg", 0.3, 0.6),
                           ("HbA1c", 0.04, 0.08)]:
        cur = _num(prow[col])
        drift = float(rng.normal(0.4 * sd, sd))
        out[col] = [round(cur - drift * (12 - m) + (float(rng.normal(0, noise)) if m < 12 else 0.0), 2) for m in months]
    return pd.DataFrame(out)


def trend_slopes(trend: pd.DataFrame) -> pd.DataFrame:
    thr = {"SystolicBP": 1.0, "FastingGlucose": 1.5, "WeightKg": 0.3, "HbA1c": 0.05}
    x = trend["Month"].to_numpy(dtype=float)
    rows = []
    for col in [c for c in trend.columns if c != "Month"]:
        y = trend[col].to_numpy(dtype=float)
        b = float(((x - x.mean()) * (y - y.mean())).sum() / ((x - x.mean()) ** 2).sum())
        a = float(y.mean() - b * x.mean())
        t = thr.get(col, 0.5)
        rows.append({"Measure": col, "SlopePerMonth": round(b, 3), "Current": round(y[-1], 2),
                     "Projected3Months": round(a + b * (x[-1] + 3), 2),
                     "Trend": "Rising" if b > t else "Falling" if b < -t else "Stable"})
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- Cybersecurity
CY_REQUIRED = ["AlertID", "Timestamp", "AlertType", "SourceHost", "DestinationHost", "UserAccount", "Severity",
               "AssetCriticality", "ThreatIntelScore", "AnomalyScore", "DetectionConfidence"]

CY_FIELDS = {
    "AlertID": "Unique SIEM alert identifier.",
    "Timestamp": "When the alert fired. Orders the kill chain timeline.",
    "AlertType": "Kind of detection. Selects the SOAR playbook and groups learning.",
    "SourceHost": "Where the activity came from. Start of an attack graph edge.",
    "DestinationHost": "Where the activity went. End of an attack graph edge.",
    "UserAccount": "Account involved. Used to pivot to related alerts.",
    "Severity": "SIEM severity from 1 to 10.",
    "AssetCriticality": "Business value of the destination from 1 to 5.",
    "ThreatIntelScore": "0 to 1 match with known threat intelligence indicators.",
    "AnomalyScore": "0 to 1 deviation from normal behavior (UEBA).",
    "DetectionConfidence": "0 to 1 confidence of the detection rule. Multiplies the risk score.",
    "MitreTechnique": "Optional MITRE ATT&CK technique ID for context.",
    "AnalystVerdict": "Optional True positive or False positive. Used for learning.",
}

_PLAYBOOKS = {
    "Phishing email clicked": ("Quarantine the email, block the sender and reset the user password", 0.85),
    "Malicious PowerShell": ("Isolate the endpoint and kill the process tree", 0.90),
    "Command and control beacon": ("Block the C2 address at proxy and firewall", 0.90),
    "Credential access": ("Disable compromised accounts and rotate service credentials", 0.85),
    "Lateral movement": ("Segment hosts and block SMB and RDP between zones", 0.80),
    "Privilege escalation": ("Revoke elevated rights and reset privileged credentials", 0.85),
    "Data exfiltration": ("Block egress, preserve evidence and notify legal", 0.88),
    "Brute force login": ("Lock the account and enforce MFA", 0.80),
    "Port scan": ("Confirm scanner authorization and tune the rule", 0.70),
    "Impossible travel": ("Force re-authentication with MFA", 0.75),
    "Malware quarantined": ("Confirm quarantine and run a full scan", 0.80),
    "DNS tunneling": ("Sinkhole the domain and isolate the host", 0.85),
}
_DEFAULT_PLAYBOOK = ("Generic containment: isolate the host and reset credentials", 0.60)


def synthetic_cyber() -> pd.DataFrame:
    rows = [
        ("Phishing email clicked", "MAIL-RELAY", "WS-ACCT-07", "jsmith", 6, 2, 0.80, 0.60, 0.85, "T1566", "True positive"),
        ("Brute force login", "VPN-GW", "WS-HR-03", "tlee", 4, 2, 0.10, 0.30, 0.50, "T1110", "False positive"),
        ("Malicious PowerShell", "WS-ACCT-07", "C2-203.0.113.45", "jsmith", 8, 2, 0.90, 0.85, 0.90, "T1059", "True positive"),
        ("Command and control beacon", "WS-ACCT-07", "C2-203.0.113.45", "jsmith", 8, 2, 0.95, 0.80, 0.85, "T1071", "True positive"),
        ("Port scan", "SCANNER-01", "APP-ERP-02", "svc_scan", 4, 4, 0.00, 0.20, 0.40, "T1046", "False positive"),
        ("Credential access", "WS-ACCT-07", "AUTH-SRV-01", "jsmith", 8, 4, 0.70, 0.80, 0.80, "T1558", "True positive"),
        ("Lateral movement", "WS-ACCT-07", "FS-01", "svc_backup", 7, 3, 0.60, 0.85, 0.80, "T1021", "True positive"),
        ("Lateral movement", "WS-ACCT-07", "FS-01", "svc_backup", 6, 3, 0.50, 0.70, 0.75, "T1021", "True positive"),
        ("Impossible travel", "VPN-GW", "WS-SALES-11", "mlee", 5, 2, 0.20, 0.60, 0.55, "T1078", "False positive"),
        ("Lateral movement", "FS-01", "APP-ERP-02", "svc_backup", 7, 4, 0.60, 0.80, 0.80, "T1021", "True positive"),
        ("Malware quarantined", "WS-SALES-11", "WS-SALES-11", "mlee", 5, 2, 0.30, 0.20, 0.70, "T1204", "False positive"),
        ("Privilege escalation", "APP-ERP-02", "DC-01", "svc_backup", 9, 5, 0.75, 0.90, 0.85, "T1068", "True positive"),
        ("DNS tunneling", "WS-ENG-04", "EXT-DNS", "achen", 6, 3, 0.40, 0.70, 0.60, "T1071.004", "False positive"),
        ("Lateral movement", "DC-01", "DB-FIN-01", "adm_jsmith", 9, 5, 0.70, 0.90, 0.85, "T1021", "True positive"),
        ("Brute force login", "VPN-GW", "WS-HR-03", "tlee", 3, 2, 0.05, 0.25, 0.45, "T1110", "False positive"),
        ("Data exfiltration", "DB-FIN-01", "EXT-203.0.113.77", "adm_jsmith", 10, 3, 0.85, 0.95, 0.90, "T1041", "True positive"),
    ]
    start = pd.Timestamp("2026-10-03 08:05")
    recs = []
    for i, r in enumerate(rows):
        recs.append({"AlertID": f"A{i + 1:03d}", "Timestamp": (start + pd.Timedelta(minutes=17 * i)).strftime("%Y-%m-%d %H:%M"),
                     "AlertType": r[0], "SourceHost": r[1], "DestinationHost": r[2], "UserAccount": r[3],
                     "Severity": r[4], "AssetCriticality": r[5], "ThreatIntelScore": r[6], "AnomalyScore": r[7],
                     "DetectionConfidence": r[8], "MitreTechnique": r[9], "AnalystVerdict": r[10]})
    return pd.DataFrame(recs)


def _risk_tier(x: float) -> str:
    return "Critical" if x >= 60 else "High" if x >= 40 else "Medium" if x >= 20 else "Low"


def analyze_cyber(df: pd.DataFrame, approved: bool = False, weights=(0.35, 0.25, 0.20, 0.20)):
    trace = ReasoningTrace()
    d = df.copy()
    for c in ["AlertID", "AlertType", "SourceHost", "DestinationHost", "UserAccount"]:
        d[c] = d[c].astype(str)
    w1, w2, w3, w4 = weights
    sev, crit = d.Severity.clip(0, 10) / 10, d.AssetCriticality.clip(0, 5) / 5
    ti, an, conf = d.ThreatIntelScore.clip(0, 1), d.AnomalyScore.clip(0, 1), d.DetectionConfidence.clip(0, 1)
    d["RiskScore"] = (100 * conf * (w1 * sev + w2 * crit + w3 * ti + w4 * an)).round(1)
    d["RiskTier"] = d.RiskScore.map(_risk_tier)
    d["StepProbability"] = (conf * (0.5 * ti + 0.5 * an) + 0.1).clip(0.01, 0.99).round(3)
    scored = d.sort_values("RiskScore", ascending=False).reset_index(drop=True)

    g = nx.DiGraph()
    crit_of = {}
    for r in d.itertuples():
        crit_of[r.DestinationHost] = max(crit_of.get(r.DestinationHost, 0.0), float(r.AssetCriticality))
        crit_of.setdefault(r.SourceHost, 0.0)
        if r.SourceHost == r.DestinationHost:
            g.add_node(r.SourceHost)
            continue
        p = float(r.StepProbability)
        if g.has_edge(r.SourceHost, r.DestinationHost):
            e = g[r.SourceHost][r.DestinationHost]
            e["p"] = round(1 - (1 - e["p"]) * (1 - p), 3)
            e["alerts"] += 1
        else:
            g.add_edge(r.SourceHost, r.DestinationHost, p=round(p, 3), alerts=1)
    for _, _, e in g.edges(data=True):
        e["weight"] = -math.log(max(e["p"], 1e-6))
    for n in g.nodes:
        g.nodes[n]["type"] = "host"
        g.nodes[n]["criticality"] = crit_of.get(n, 0.0)

    risk_in = d.groupby("DestinationHost").RiskScore.max().to_dict()
    sources = [n for n in g.nodes if g.in_degree(n) == 0] or list(g.nodes)
    best = (0.0, [], None, None)
    for t in sorted(g.nodes, key=lambda n: (crit_of.get(n, 0.0), risk_in.get(n, 0.0)), reverse=True):
        for s in sources:
            if s == t:
                continue
            try:
                length, p_nodes = nx.single_source_dijkstra(g, s, t, weight="weight")
            except nx.NetworkXNoPath:
                continue
            prob = math.exp(-length)
            if prob > best[0]:
                best = (prob, p_nodes, s, t)
        if best[1]:
            break
    prob, path, entry, target = best

    resp_rows = []
    for at, grp in scored.groupby("AlertType", sort=False):
        mx = float(grp.RiskScore.max())
        tier = _risk_tier(mx)
        pb, eff = _PLAYBOOKS.get(at, _DEFAULT_PLAYBOOK)
        if tier == "Critical" and not approved:
            status, after = "Awaiting human approval", mx
        else:
            status = "Executed after human approval" if tier == "Critical" else "Executed automatically"
            after = round(mx * (1 - eff), 1)
        resp_rows.append({"AlertType": at, "Alerts": len(grp), "HighestTier": tier, "Playbook": pb,
                          "Effectiveness": eff, "Status": status, "MaxRiskBefore": round(mx, 1),
                          "ResidualRiskAfter": after,
                          "Recovered": "Yes" if status != "Awaiting human approval" and after < 20 else "No"})
    resp = pd.DataFrame(resp_rows)

    if "AnalystVerdict" in d.columns:
        verdict = d.AnalystVerdict.astype(str).str.strip().str.lower()
        tp_mask = verdict.str.contains("true") | verdict.isin(["tp", "yes", "malicious"])
        basis = "analyst verdicts"
    else:
        tp_mask = d.RiskScore >= 40
        basis = "risk score of 40 or more as a proxy (no AnalystVerdict column)"
    learn_rows = []
    for at, idx in d.groupby("AlertType").groups.items():
        tp = int(tp_mask.loc[idx].sum())
        fp = len(idx) - tp
        prec = tp / (tp + fp) if tp + fp else 0.0
        old = float(d.loc[idx, "DetectionConfidence"].mean())
        mult = 0.5 + 0.5 * prec
        learn_rows.append({"AlertType": at, "TruePositives": tp, "FalsePositives": fp, "Precision": round(prec, 2),
                           "OldConfidence": round(old, 2), "ConfidenceMultiplier": round(mult, 2),
                           "NewConfidence": round(min(1.0, old * mult), 2)})
    learn = pd.DataFrame(learn_rows)

    trace.add("Understand the alert", f"Scored {len(d)} alerts with severity, asset value, threat intelligence and behavior; "
                                      f"{int((d.RiskTier == 'Critical').sum())} are Critical.")
    top = scored.iloc[0] if len(scored) else None
    if top is not None:
        trace.add("Investigate", f"Top alert {top.AlertID} ({top.AlertType}) pivoted on user {top.UserAccount} and hosts "
                                 f"{top.SourceHost} and {top.DestinationHost}.")
    trace.add("Build attack graph", f"Built a graph of {g.number_of_nodes()} hosts and {g.number_of_edges()} observed steps; "
                                    "repeated evidence on a link is fused.")
    trace.add("Determine attack path", ("Most likely path " + " then ".join(path) + f" with probability {prob:.3f}.")
              if path else "No connected path to a high value asset was found.")
    trace.add("Decide response", f"Matched {len(resp)} alert types to SOAR playbooks. Critical playbooks need human approval.")
    trace.add("Verify recovery", f"{int((resp.Recovered == 'Yes').sum())} of {len(resp)} playbooks bring residual risk below 20.")
    trace.add("Learn", f"Retuned detection confidence per alert type using {basis}.")
    return scored, g, path, prob, entry, target, resp, learn, trace


# ----------------------------------------------------------------------------- Software development
SW_REQUIRED = ["ModuleID", "ModuleName", "Layer", "DependsOn", "EstimatedKLOC", "Complexity", "RequirementsCount",
               "TestCases", "DefectsFound"]

SW_FIELDS = {
    "ModuleID": "Unique module code. Used in the dependency graph.",
    "ModuleName": "Human readable module name.",
    "Layer": "Architecture layer: UI, Security, Logic, Integration, Data or Test.",
    "DependsOn": "Module IDs this module needs first, separated by semicolons. Drives the build order.",
    "EstimatedKLOC": "Estimated size in thousands of lines of code. Drives COCOMO effort.",
    "Complexity": "1 (simple) to 5 (very complex). Weights the effort share.",
    "RequirementsCount": "Number of requirements the module implements. Used for test coverage.",
    "TestCases": "Generated test cases. Coverage assumes three tests per requirement.",
    "DefectsFound": "Defects found by the first automated test run. Feeds the test and fix loop.",
}

_COCOMO = {"Organic": (2.4, 1.05, 2.5, 0.38), "Semi detached": (3.0, 1.12, 2.5, 0.35),
           "Embedded": (3.6, 1.20, 2.5, 0.32)}


def synthetic_software() -> pd.DataFrame:
    rows = [
        ("M01", "Authentication", "Security", "", 1.8, 4, 8, 22, 6),
        ("M02", "Data model", "Data", "", 1.2, 2, 6, 16, 3),
        ("M03", "Graph database connector", "Integration", "M02", 2.0, 4, 7, 15, 7),
        ("M04", "Synthetic data generator", "Data", "M02", 1.0, 2, 5, 15, 2),
        ("M05", "Threat intelligence ingest", "Integration", "M03", 1.6, 3, 6, 12, 5),
        ("M06", "AI reasoning engine", "Logic", "M03;M05", 3.2, 5, 10, 24, 11),
        ("M07", "Risk scoring", "Logic", "M06", 1.4, 3, 6, 18, 4),
        ("M08", "CSV and PDF export", "Logic", "M07", 1.1, 2, 5, 15, 3),
        ("M09", "Dashboard UI", "UI", "M01;M07;M08", 2.6, 3, 9, 20, 8),
        ("M10", "End to end test suite", "Test", "M09", 1.5, 2, 6, 18, 2),
    ]
    return pd.DataFrame(rows, columns=SW_REQUIRED)


def analyze_software(df: pd.DataFrame, fix: float = 0.6, mode: str = "Organic"):
    trace = ReasoningTrace()
    d = df.copy()
    d["ModuleID"] = d.ModuleID.astype(str).str.strip()
    d["DependsOn"] = d.DependsOn.fillna("").astype(str).replace("nan", "")
    ids = set(d.ModuleID)
    dg = nx.DiGraph()
    dg.add_nodes_from(d.ModuleID)
    for r in d.itertuples():
        for dep in [x.strip() for x in _re.split(r"[;,|]", r.DependsOn) if x.strip()]:
            if dep in ids and dep != r.ModuleID:
                dg.add_edge(dep, r.ModuleID)
    if not nx.is_directed_acyclic_graph(dg):
        cyc = nx.find_cycle(dg)
        raise ValueError("Dependency cycle detected: " + " -> ".join([u for u, _ in cyc] + [cyc[0][0]]) + ".")
    order = list(nx.lexicographical_topological_sort(dg))

    a, b, c, dd = _COCOMO.get(mode, _COCOMO["Organic"])
    kloc = d.EstimatedKLOC.clip(lower=0.01)
    total = float(kloc.sum())
    effort = a * total ** b
    sched = c * effort ** dd
    team = effort / sched
    wt = kloc * d.Complexity.clip(lower=0.1)
    d["EffortPM"] = (wt / wt.sum() * effort).round(2)

    d0 = d.DefectsFound.clip(lower=0)
    D0 = float(d0.sum())
    n, series = 0, [D0]
    while series[-1] >= 0.5 and n < 10:
        n += 1
        series.append(D0 * (1 - fix) ** n)
    final = d0 * (1 - fix) ** n
    cov = (d.TestCases / (3 * d.RequirementsCount.clip(lower=1))).clip(upper=1)
    dens = d0 / kloc
    fixed_frac = np.where(d0 > 0, 1 - final / d0.replace(0, 1), 1.0)
    q = 100 * (0.4 * cov + 0.3 * fixed_frac + 0.3 * (1 - np.minimum(dens / 10, 1)))

    d["BuildOrder"] = [order.index(m) + 1 for m in d.ModuleID]
    d["DefectDensity"] = dens.round(2)
    d["TestCoverage"] = cov.round(2)
    d["DefectsAfterFixing"] = final.round(2)
    d["QualityScore"] = np.round(q, 1)
    d["Status"] = np.where(d.QualityScore >= 70, "Ready to deploy", "Needs review")
    cols = ["BuildOrder"] + [x for x in SW_REQUIRED] + ["EffortPM", "DefectDensity", "TestCoverage",
                                                        "DefectsAfterFixing", "QualityScore", "Status"]
    mods = d[cols + [x for x in d.columns if x not in cols]].sort_values("BuildOrder").reset_index(drop=True)

    iters = pd.DataFrame({"Iteration": list(range(len(series))),
                          "DefectsRemaining": [round(v, 2) for v in series],
                          "FixedThisIteration": [0.0] + [round(series[i - 1] - series[i], 2) for i in range(1, len(series))]})
    summ = {"TotalKLOC": round(total, 2), "EffortPM": round(effort, 1), "ScheduleMonths": round(sched, 1),
            "TeamSize": round(team, 1), "InitialDefects": int(round(D0)), "FinalDefects": round(series[-1], 1)}

    trace.add("Understand the requirement", f"Read the plan of {len(d)} modules totalling {total:.1f} KLOC.")
    trace.add("Design the architecture", f"Grouped modules into {d.Layer.nunique()} layers and built a dependency graph with {dg.number_of_edges()} links.")
    trace.add("Plan the build", "Topological sort gives the build order: " + ", ".join(order) + ".")
    trace.add("Estimate effort", f"Basic COCOMO ({mode}): {effort:.1f} person months over {sched:.1f} months with about {team:.1f} people.")
    trace.add("Test, find and fix", f"Autonomous loop fixing {fix:.0%} per iteration reduced defects from {D0:.0f} to {series[-1]:.1f} in {n} iterations.")
    trace.add("Quality gate", f"{int((d.Status == 'Ready to deploy').sum())} of {len(d)} modules pass the quality gate of 70.")
    trace.add("Document and deploy", "Generated documentation from the same model. Release requires human approval.")
    return mods, dg, order, iters, summ, trace


_REQ_MAP = [
    (("streamlit", "web app", "ui", "interface", "dashboard"), "User interface", "UI", "Streamlit pages, navigation and charts"),
    (("authentication", "login", "sign in", "auth", "user management"), "User authentication", "Security", "Login form, password hashing and session handling"),
    (("graph database", "graph db", "neo4j", "knowledge graph"), "Graph database", "Integration", "Graph connector, node and edge schema, traversal queries"),
    (("synthetic data", "test data", "sample data"), "Synthetic data generator", "Data", "Seeded generator producing realistic records"),
    (("ai reasoning", "reasoning", "machine learning", "llm"), "AI reasoning engine", "Logic", "Scoring and explanation functions with a reasoning trace"),
    (("csv", "pdf", "export", "report"), "Export service", "Logic", "CSV and PDF report builders"),
    (("cybersecurity", "threat", "siem", "alert", "security"), "Security analytics", "Logic", "Alert model, risk scoring and threat logic"),
    (("sql", "postgres", "sqlite", "relational database"), "Relational database", "Data", "Tables and data access layer"),
    (("api", "rest", "endpoint"), "API layer", "Integration", "REST endpoints"),
]


def parse_requirement(req: str) -> pd.DataFrame:
    text = str(req).lower()
    rows = []
    for keys, comp, layer, art in _REQ_MAP:
        hit = next((k for k in keys if _re.search(r"\b" + _re.escape(k) + r"\b", text)), None)
        if hit:
            rows.append({"Component": comp, "Layer": layer, "DetectedFrom": hit, "GeneratedArtifact": art})
    if not rows:
        rows.append({"Component": "Core application", "Layer": "Logic", "DetectedFrom": "(general request)",
                     "GeneratedArtifact": "Application skeleton"})
    rows.append({"Component": "Automated tests", "Layer": "Test", "DetectedFrom": "(always added)",
                 "GeneratedArtifact": "Unit tests for every component"})
    return pd.DataFrame(rows)


def generate_scaffold(comps: pd.DataFrame, app_name: str = "generated_app") -> str:
    out = [f'"""{app_name}: application scaffold generated by the AGI software agent."""', "",
           "import pandas as pd", "import streamlit as st", "", ""]
    funcs = []
    for r in comps.itertuples():
        fn = _re.sub(r"[^a-z0-9]+", "_", str(r.Component).lower()).strip("_") or "component"
        funcs.append(fn)
        out += [f"def {fn}():",
                f'    """{r.Component} ({r.Layer} layer): {r.GeneratedArtifact}."""',
                f"    # TODO: implement the {str(r.Component).lower()}",
                f'    return {{"component": "{r.Component}", "layer": "{r.Layer}", "status": "scaffolded"}}',
                "", ""]
    out += ["def main():",
            f'    st.title("{app_name}")',
            "    results = [" + ", ".join(f"{f}()" for f in funcs) + "]",
            "    st.dataframe(pd.DataFrame(results))", "", "",
            'if __name__ == "__main__":', "    main()", ""]
    return "\n".join(out)


# ----------------------------------------------------------------------------- Government and DoD
GOV_RISK_REQUIRED = ["RiskID", "Domain", "System", "Description", "Likelihood", "Impact", "ControlEffectiveness",
                     "MissionDependency"]
GOV_COA_REQUIRED = ["COA", "Description", "Effectiveness", "CostMillions", "TimeDays", "RiskLevel",
                    "PolicyCompliance", "SuccessProbability", "Uncertainty"]

GOV_FIELDS = {
    "RiskID": "Unique risk identifier.",
    "Domain": "Enterprise domain the risk belongs to (network operations, cybersecurity, logistics ...).",
    "System": "System or capability affected.",
    "Description": "Plain language description of the risk or course of action.",
    "Likelihood": "1 (rare) to 5 (almost certain).",
    "Impact": "1 (minor) to 5 (severe).",
    "ControlEffectiveness": "0 to 1 share of the risk already reduced by existing controls.",
    "MissionDependency": "1 to 5, how much the mission depends on this system.",
    "Owner": "Optional accountable office.",
    "COA": "Course of action identifier.",
    "Effectiveness": "Expected mission effectiveness if it succeeds, 0 to 100.",
    "CostMillions": "Estimated cost in millions of dollars (lower is better).",
    "TimeDays": "Days to implement (lower is better).",
    "RiskLevel": "Implementation risk 1 to 5 (lower is better).",
    "PolicyCompliance": "0 to 100 compliance with policy and authorities.",
    "SuccessProbability": "0 to 1 probability of full success. Used in the simulation.",
    "Uncertainty": "Standard deviation of the outcome in effectiveness points. Used in the simulation.",
}

_GOV_KEYWORDS = {
    "Network operations": ["network", "communication", "comms", "link", "bandwidth", "resilient", "connectivity"],
    "Cybersecurity": ["cyber", "secure", "security", "intrusion", "defend", "attack"],
    "Logistics": ["logistic", "supply", "parts", "fuel", "transport", "sustain"],
    "Mission systems": ["mission", "command and control", "c2", "system"],
    "Policy": ["policy", "coalition", "compliance", "authority", "partner"],
    "Incident management": ["incident", "response", "recover"],
    "Asset inventory": ["asset", "inventory", "endpoint", "device"],
    "Threat intelligence": ["threat", "intelligence", "adversary", "actor"],
    "Knowledge graph": ["dependency", "dependencies", "knowledge", "relationship"],
}


def synthetic_gov_risks() -> pd.DataFrame:
    rows = [
        ("R01", "Network operations", "Coalition WAN backbone", "Single fiber path between two hubs", 3, 5, 0.30, 5, "Network operations center"),
        ("R02", "Cybersecurity", "C2 enclave", "Active intrusion attempts by a persistent threat actor", 4, 5, 0.50, 5, "Cyber defense"),
        ("R03", "Cybersecurity", "Identity services", "Legacy accounts without phishing resistant MFA", 4, 4, 0.40, 4, "Identity office"),
        ("R04", "Logistics", "SATCOM spares", "Long lead time for modem replacements", 3, 3, 0.20, 3, "Logistics"),
        ("R05", "Mission systems", "C2 application", "Unpatched mission application server", 3, 5, 0.35, 5, "Program office"),
        ("R06", "Policy", "Coalition data sharing", "Releasability rules slow partner onboarding", 3, 3, 0.50, 4, "Policy office"),
        ("R07", "Incident management", "Security operations", "After hours incident response staffing gap", 3, 4, 0.30, 4, "SOC"),
        ("R08", "Asset inventory", "Deployed endpoints", "Incomplete inventory of deployed endpoints", 4, 3, 0.25, 3, "Asset management"),
        ("R09", "Threat intelligence", "Partner feeds", "Indicators shared late by partners", 3, 3, 0.30, 3, "Intelligence cell"),
        ("R10", "Knowledge graph", "Dependency map", "Mission to system dependencies not fully mapped", 3, 4, 0.20, 4, "Enterprise architecture"),
        ("R11", "Network operations", "SATCOM link", "Jamming risk in the contested area", 3, 5, 0.35, 5, "Network operations center"),
        ("R12", "Logistics", "Forward site power", "Generator fuel resupply delays", 2, 4, 0.30, 4, "Logistics"),
    ]
    return pd.DataFrame(rows, columns=GOV_RISK_REQUIRED + ["Owner"])


def synthetic_gov_coas() -> pd.DataFrame:
    rows = [
        ("COA-1", "Harden existing links with zero trust segmentation and MFA everywhere", 72, 18, 75, 2, 92, 0.80, 8),
        ("COA-2", "Add redundant commercial LEO satellite paths with encrypted overlay", 84, 42, 110, 3, 80, 0.70, 12),
        ("COA-3", "Stand up a monitored coalition mission network enclave", 78, 30, 95, 3, 88, 0.75, 10),
        ("COA-4", "Fast migration of C2 to a cloud hosted platform with managed SOC", 88, 55, 160, 4, 70, 0.55, 15),
    ]
    return pd.DataFrame(rows, columns=GOV_COA_REQUIRED)


def _sim_coa(row, i: int, n: int = 5000) -> np.ndarray:
    rng = np.random.default_rng(1000 + i)
    p = _num(row.SuccessProbability, 0.5)
    p = p / 100 if p > 1 else p
    eff, sd = _num(row.Effectiveness), max(_num(row.Uncertainty, 5), 0.1)
    success = rng.random(n) < min(max(p, 0.0), 1.0)
    mu = np.where(success, eff, 0.35 * eff)
    return np.clip(rng.normal(mu, sd), 0, 100)


def simulate_draws(coas: pd.DataFrame) -> dict:
    return {str(r.COA): _sim_coa(r, i) for i, r in enumerate(coas.itertuples())}


def analyze_gov(risks: pd.DataFrame, coas: pd.DataFrame, mission: str, weights: dict, threshold: float,
                approved: bool):
    trace = ReasoningTrace()
    text = str(mission).lower()
    doms = [dname for dname, keys in _GOV_KEYWORDS.items() if any(k in text for k in keys)]
    if not doms:
        doms = list(_GOV_KEYWORDS)

    reg = risks.copy()
    ce = reg.ControlEffectiveness.astype(float)
    ce = np.where(ce > 1, ce / 100, ce).clip(0, 1)
    reg["InherentRisk"] = (reg.Likelihood * reg.Impact).astype(float)
    reg["ResidualRisk"] = (reg.InherentRisk * (1 - ce)).round(2)
    reg["MissionWeightedRisk"] = (reg.ResidualRisk * reg.MissionDependency / 5).round(2)
    reg["RiskBand"] = pd.cut(reg.InherentRisk, [0, 4, 9, 14, 25], labels=["Low", "Moderate", "High", "Very High"],
                             include_lowest=True).astype(str)
    reg["RelevantToMission"] = np.where(reg.Domain.astype(str).isin(doms) | (reg.MissionDependency >= 4), "Yes", "No")
    reg = reg.sort_values("MissionWeightedRisk", ascending=False).reset_index(drop=True)

    c = coas.copy().reset_index(drop=True)
    benefit, cost = ["Effectiveness", "PolicyCompliance"], ["CostMillions", "TimeDays", "RiskLevel"]
    for col in benefit:
        mx = c[col].max()
        c["n_" + col] = (c[col] / mx).round(3) if mx > 0 else 0.0
    for col in cost:
        mn = c[col].min()
        c["n_" + col] = [round(mn / x, 3) if x > 0 else 1.0 for x in c[col]]
    wsum = sum(weights.values()) or 1
    c["MCDAScore"] = (100 * sum(weights[k] * c["n_" + k] for k in weights) / wsum).round(1)
    sims = [_sim_coa(r, i) for i, r in enumerate(c.itertuples())]
    c["SimMean"] = [round(float(s.mean()), 1) for s in sims]
    c["P10"] = [round(float(np.percentile(s, 10)), 1) for s in sims]
    c["P90"] = [round(float(np.percentile(s, 90)), 1) for s in sims]
    c["ProbAboveThreshold"] = [round(float((s >= threshold).mean()), 3) for s in sims]
    c["CombinedScore"] = (0.6 * c.MCDAScore + 0.4 * c.SimMean).round(1)
    ranked = c.sort_values("CombinedScore", ascending=False).reset_index(drop=True)
    ranked.insert(0, "Rank", range(1, len(ranked) + 1))
    best = ranked.iloc[0]

    monitor = None
    if approved:
        weeks = int(min(max(math.ceil(_num(best.TimeDays, 60) / 7), 4), 26))
        elapsed = max(2, weeks // 2)
        rows = []
        for wk in range(1, weeks + 1):
            planned = round(100 * wk / weeks, 1)
            actual = round(min(100.0, planned * (0.9 + 0.05 * math.sin(wk))), 1) if wk <= elapsed else np.nan
            status = "" if np.isnan(actual) else ("On track" if actual >= planned - 5 else "Behind plan")
            rows.append({"Week": wk, "PlannedProgress": planned, "ActualProgress": actual, "Status": status})
        monitor = pd.DataFrame(rows)

    trace.add("Understand mission", "Mapped the mission statement to these domains: " + ", ".join(doms) + ".")
    trace.add("Analyze systems and data", f"Fused {len(reg)} risks from {reg.Domain.nunique()} domains into one register.")
    trace.add("Identify risks", f"{int((reg.RelevantToMission == 'Yes').sum())} risks are mission relevant; top risk "
                                f"{reg.iloc[0].RiskID} ({reg.iloc[0].Description}).")
    trace.add("Develop courses of action", f"Normalized {len(c)} courses of action on five criteria and applied command weights.")
    trace.add("Simulate outcomes", "Ran 5000 Monte Carlo trials per course of action.")
    trace.add("Recommend best option", f"{best.COA} has the best combined score {best.CombinedScore} and a "
                                       f"{best.ProbAboveThreshold:.0%} chance of exceeding {threshold} effectiveness points.")
    trace.add("Human approval", "Approved by the decision authority. Execution is being monitored." if approved
              else "Waiting for the decision authority. No action is taken without approval.")
    return reg, ranked, monitor, doms, trace


# ----------------------------------------------------------------------------- Knowledge graph
KG_NODE_REQUIRED = ["NodeID", "NodeName", "NodeType", "Criticality"]
KG_EDGE_REQUIRED = ["SourceID", "TargetID", "Relationship", "CompromiseProbability"]

KG_FIELDS = {
    "NodeID": "Unique entity identifier.",
    "NodeName": "Entity name used in answers and diagrams.",
    "NodeType": "Employee, Device, Network, Application, Server, Database, MissionSystem, Vulnerability or Threat.",
    "Criticality": "1 to 10 business or mission value. Multiplies reach probability into expected impact.",
    "SourceID": "Entity the relationship starts from.",
    "TargetID": "Entity the relationship points to.",
    "Relationship": "How the two connect (uses, connects to, hosts ...).",
    "CompromiseProbability": "0 to 1 probability that a compromise spreads across this link.",
}


def synthetic_kg():
    nodes = pd.DataFrame([
        ("EMP01", "Employee A. Rivera", "Employee", 3), ("EMP02", "Administrator K. Osei", "Employee", 5),
        ("DEV01", "Rivera laptop", "Device", 4), ("DEV02", "Admin workstation", "Device", 6),
        ("DEV03", "Rivera mobile phone", "Device", 2), ("NET01", "Corporate VPN", "Network", 7),
        ("NET02", "Internal LAN", "Network", 6), ("NET03", "Mission network enclave", "Network", 8),
        ("APP01", "Email and collaboration suite", "Application", 5), ("APP02", "HR self service portal", "Application", 4),
        ("SRV01", "Application server", "Server", 7), ("SRV02", "Identity server", "Server", 9),
        ("DB01", "Finance database", "Database", 8), ("DB02", "Mission data store", "Database", 9),
        ("MS01", "Command and control system", "MissionSystem", 10), ("MS02", "Logistics planning system", "MissionSystem", 9),
        ("VUL01", "Unpatched VPN appliance", "Vulnerability", 6), ("THR01", "Ransomware affiliate group", "Threat", 5),
    ], columns=KG_NODE_REQUIRED)
    edges = pd.DataFrame([
        ("EMP01", "DEV01", "uses", 0.90), ("EMP01", "DEV03", "uses", 0.90), ("DEV03", "APP01", "accesses", 0.50),
        ("DEV01", "NET01", "connects through", 0.80), ("DEV01", "APP01", "accesses", 0.70),
        ("APP01", "NET02", "runs on", 0.30), ("NET01", "NET02", "routes to", 0.70), ("NET02", "SRV01", "reaches", 0.60),
        ("NET02", "APP02", "reaches", 0.50), ("SRV01", "DB01", "queries", 0.70), ("SRV01", "SRV02", "authenticates via", 0.40),
        ("SRV02", "NET03", "grants access to", 0.50), ("DB01", "DB02", "replicates to", 0.35),
        ("NET03", "DB02", "reaches", 0.60), ("DB02", "MS01", "feeds", 0.80), ("NET03", "MS02", "reaches", 0.55),
        ("SRV01", "MS02", "integrates with", 0.45), ("EMP02", "DEV02", "uses", 0.90), ("DEV02", "SRV02", "administers", 0.80),
        ("THR01", "VUL01", "exploits", 0.60), ("VUL01", "NET01", "affects", 0.70),
    ], columns=KG_EDGE_REQUIRED)
    return nodes, edges


_STOP = {"if", "this", "the", "a", "an", "is", "was", "are", "be", "been", "gets", "got", "what", "which", "could",
         "would", "ultimately", "be", "affected", "s", "of", "to", "and", "or", "my", "our", "systems", "critical"}


def resolve_question(q: str, nodes: pd.DataFrame):
    words = _re.findall(r"[a-z0-9]+", str(q).lower())
    qset = {w for w in words if w not in _STOP}
    focus = None
    if "compromised" in words:
        for w in reversed(words[:words.index("compromised")]):
            if w not in _STOP:
                focus = w
                break
    best, best_score = None, 0.0
    for r in nodes.itertuples():
        tset = set(_re.findall(r"[a-z0-9]+", f"{r.NodeName} {r.NodeType}".lower()))
        score = len(qset & tset) + 0.5 * (str(r.NodeType).lower() in qset) + 3 * (focus in tset if focus else 0)
        if score > best_score:
            best, best_score = str(r.NodeID), score
    return best


def _blast(g, start):
    if start not in g:
        return [], 0.0
    dist, paths = nx.single_source_dijkstra(g, start, weight="weight")
    rows = []
    for n, dval in dist.items():
        if n == start:
            continue
        p = math.exp(-dval)
        crit = float(g.nodes[n].get("criticality", 0))
        rows.append({"NodeID": n, "NodeName": g.nodes[n].get("name", n), "NodeType": g.nodes[n].get("type", ""),
                     "Criticality": crit, "ReachProbability": round(p, 3), "Hops": len(paths[n]) - 1,
                     "ExpectedImpact": round(p * crit, 2),
                     "Path": " -> ".join(g.nodes[x].get("name", x) for x in paths[n])})
    return rows, sum(r["ExpectedImpact"] for r in rows)


def analyze_kg(nodes: pd.DataFrame, edges: pd.DataFrame, start):
    trace = ReasoningTrace()
    g = nx.DiGraph()
    for r in nodes.itertuples():
        g.add_node(str(r.NodeID), name=str(r.NodeName), type=str(r.NodeType), criticality=_num(r.Criticality))
    for r in edges.itertuples():
        p = min(max(_num(r.CompromiseProbability, 0.5), 0.01), 0.99)
        g.add_edge(str(r.SourceID), str(r.TargetID), p=round(p, 3), weight=-math.log(p),
                   rel=str(getattr(r, "Relationship", "")))
    start = str(start)
    rows, total = _blast(g, start)
    cols = ["NodeID", "NodeName", "NodeType", "Criticality", "ReachProbability", "Hops", "ExpectedImpact", "Path"]
    br = pd.DataFrame(rows, columns=cols).sort_values("ExpectedImpact", ascending=False).reset_index(drop=True)

    reach = set(br.NodeID) | {start}
    mrows = []
    for u, v, e in list(g.edges(data=True)):
        if u not in reach:
            continue
        h = g.copy()
        h.remove_edge(u, v)
        _, t2 = _blast(h, start)
        mrows.append({"BreakLink": f"{g.nodes[u]['name']} -> {g.nodes[v]['name']}", "Relationship": e.get("rel", ""),
                      "ExposureAfter": round(t2, 2),
                      "ReductionPercent": round(100 * (total - t2) / total, 1) if total > 0 else 0.0})
    mit = pd.DataFrame(mrows, columns=["BreakLink", "Relationship", "ExposureAfter", "ReductionPercent"])
    mit = mit.sort_values("ReductionPercent", ascending=False).reset_index(drop=True)

    name = g.nodes[start]["name"] if start in g else start
    ms = br[br.NodeType == "MissionSystem"]
    trace.add("Understand the question", f"Resolved the compromised entity to {start} ({name}).")
    trace.add("Traverse the graph", f"{len(br)} entities are reachable from {name}.")
    trace.add("Estimate likelihood", "Path probability is the product of link probabilities; Dijkstra on -ln p finds the most likely path to each entity.")
    trace.add("Rank impact", f"Total expected impact {total:.2f}; {len(ms)} mission systems are at risk.")
    trace.add("What if mitigation", (f"Breaking '{mit.iloc[0].BreakLink}' cuts exposure by {mit.iloc[0].ReductionPercent} percent."
                                     if len(mit) else "No links to break."))
    trace.add("Human decision authority", "The security architect chooses which mitigation to implement.")
    return g, br, mit, trace


# ----------------------------------------------------------------------------- Everyday life travel
TR_REQUIRED = ["ActivityID", "City", "Activity", "Category", "DurationHours", "CostUSD", "EnergyLevel", "FamilyRating"]

TR_FIELDS = {
    "ActivityID": "Unique activity code.",
    "City": "City where the activity happens. Cities are visited in the order they first appear.",
    "Activity": "What the family will do.",
    "Category": "History, Culture, Food, Shopping, Nature, Relaxation, Adventure or Spiritual. Matched to interests.",
    "DurationHours": "Hours needed. Limited by the daily activity hours.",
    "CostUSD": "Cost per person in US dollars.",
    "EnergyLevel": "1 (easy) to 5 (tiring). Limited by the daily energy budget.",
    "FamilyRating": "1 to 5 expected enjoyment. Drives city day allocation and selection.",
    "HotelName": "Hotel booked in the city.",
    "RateUSDPerNight": "Room rate per night in US dollars (one room per three travelers).",
    "CheckInTime": "Hotel check in time, used in drafted messages.",
}


def synthetic_travel_activities() -> pd.DataFrame:
    rows = [
        ("D01", "Delhi", "Red Fort tour", "History", 3, 8, 3, 5), ("D02", "Delhi", "Humayun's Tomb", "History", 2, 7, 2, 4),
        ("D03", "Delhi", "Chandni Chowk food walk", "Food", 3, 15, 3, 5), ("D04", "Delhi", "Lotus Temple visit", "Spiritual", 1.5, 0, 1, 4),
        ("D05", "Delhi", "Dilli Haat crafts market", "Shopping", 2, 10, 2, 4), ("D06", "Delhi", "National Rail Museum", "Culture", 2, 3, 2, 4),
        ("D07", "Delhi", "Lodhi Garden walk", "Nature", 1.5, 0, 1, 3), ("D08", "Delhi", "Qutub Minar", "History", 2, 7, 2, 5),
        ("A01", "Agra", "Taj Mahal at sunrise", "History", 3, 15, 3, 5), ("A02", "Agra", "Agra Fort", "History", 2.5, 8, 2, 4),
        ("A03", "Agra", "Mehtab Bagh sunset view", "Nature", 1.5, 3, 1, 4), ("A04", "Agra", "Marble inlay workshop", "Culture", 1.5, 0, 1, 3),
        ("J01", "Jaipur", "Amber Fort", "History", 3.5, 7, 4, 5), ("J02", "Jaipur", "City Palace and Jantar Mantar", "History", 3, 10, 2, 4),
        ("J03", "Jaipur", "Hawa Mahal photo stop", "Culture", 1, 3, 1, 4), ("J04", "Jaipur", "Johari Bazaar shopping", "Shopping", 2.5, 20, 2, 4),
        ("J05", "Jaipur", "Ethical elephant sanctuary visit", "Nature", 3, 45, 3, 5), ("J06", "Jaipur", "Rajasthani thali and folk dance", "Food", 2.5, 25, 1, 5),
        ("J07", "Jaipur", "Spa and pool afternoon", "Relaxation", 3, 30, 1, 3), ("J08", "Jaipur", "Nahargarh Fort sunset", "Nature", 2, 4, 3, 4),
        ("U01", "Udaipur", "Lake Pichola boat ride", "Relaxation", 1.5, 10, 1, 5), ("U02", "Udaipur", "City Palace Udaipur", "History", 2.5, 9, 2, 4),
        ("U03", "Udaipur", "Rajasthani cooking class", "Food", 3, 30, 2, 5), ("U04", "Udaipur", "Monsoon Palace sunset", "Nature", 2, 5, 2, 4),
        ("U05", "Udaipur", "Bagore ki Haveli dance show", "Culture", 1.5, 4, 1, 4), ("U06", "Udaipur", "Lakeside cafe and rooftop rest", "Relaxation", 2, 12, 1, 4),
        ("U07", "Udaipur", "Hilltop zipline adventure", "Adventure", 2, 25, 4, 3),
        ("M01", "Mumbai", "Gateway of India and harbour cruise", "History", 2, 8, 2, 4), ("M02", "Mumbai", "Elephanta Caves ferry trip", "History", 5, 15, 4, 4),
        ("M03", "Mumbai", "Marine Drive and Chowpatty street food", "Food", 2, 10, 1, 5), ("M04", "Mumbai", "Colaba Causeway shopping", "Shopping", 2, 25, 2, 4),
        ("M05", "Mumbai", "Sanjay Gandhi National Park", "Nature", 4, 6, 4, 3), ("M06", "Mumbai", "Dharavi community tour", "Culture", 2.5, 15, 2, 4),
        ("M07", "Mumbai", "Juhu Beach evening", "Relaxation", 2, 0, 1, 4), ("M08", "Mumbai", "Film studio tour", "Culture", 3, 40, 2, 5),
    ]
    return pd.DataFrame(rows, columns=TR_REQUIRED)


def synthetic_family() -> pd.DataFrame:
    return pd.DataFrame([("Raj", 45, "Parent", "History;Food"), ("Priya", 42, "Parent", "Culture;Shopping;Relaxation"),
                         ("Arjun", 14, "Child", "Adventure;History"), ("Anaya", 9, "Child", "Nature;Food")],
                        columns=["Name", "Age", "Role", "Interests"])


def synthetic_hotels() -> pd.DataFrame:
    return pd.DataFrame([("Delhi", "Central Delhi family hotel", 140, "14:00"), ("Agra", "Taj view guest house", 110, "13:00"),
                         ("Jaipur", "Heritage haveli Jaipur", 130, "14:00"), ("Udaipur", "Lakeside palace hotel", 170, "14:00"),
                         ("Mumbai", "Seafront hotel Mumbai", 180, "15:00")],
                        columns=["City", "HotelName", "RateUSDPerNight", "CheckInTime"])


def _city_alloc(acts: pd.DataFrame, days: int):
    cities = list(dict.fromkeys(acts.City.astype(str)))
    if not cities:
        return []
    if days <= len(cities):
        return [(c, 1) for c in cities[:max(days, 1)]]
    w = {c: float(acts.loc[acts.City.astype(str) == c, "FamilyRating"].sum()) for c in cities}
    tot = sum(w.values()) or 1.0
    extra = days - len(cities)
    q = {c: w[c] / tot * extra for c in cities}
    base = {c: int(math.floor(q[c])) for c in cities}
    left = extra - sum(base.values())
    for c in sorted(cities, key=lambda c: q[c] - base[c], reverse=True)[:left]:
        base[c] += 1
    return [(c, 1 + base[c]) for c in cities]


def synthetic_flights(start=date(2026, 12, 18), days: int = 14) -> pd.DataFrame:
    alloc = _city_alloc(synthetic_travel_activities(), days)
    first = {}
    d = 0
    for c, nd in alloc:
        first[c] = start + _td(days=d)
        d += nd
    end = start + _td(days=days - 1)
    return pd.DataFrame([
        ("INTL-101", "Washington DC", "Delhi", (start - _td(days=1)).isoformat(), "22:00", 0, 1100),
        ("DOM-215", "Jaipur", "Udaipur", first.get("Udaipur", start).isoformat(), "10:30", 0, 70),
        ("DOM-322", "Udaipur", "Mumbai", first.get("Mumbai", start).isoformat(), "11:15", 0, 85),
        ("INTL-102", "Mumbai", "Washington DC", end.isoformat(), "23:30", 0, 1100),
    ], columns=["FlightID", "FromCity", "ToCity", "Date", "DepartTime", "DelayHours", "PriceUSDPerPerson"])


def _fmt_time(h: float) -> str:
    h = max(0.0, min(h, 23.99))
    hh = int(h)
    mm = int(round((h - hh) * 60))
    if mm == 60:
        hh, mm = hh + 1, 0
    return f"{hh:02d}:{mm:02d}"


def _select(pool: pd.DataFrame, hours: float, energy: float, interests: set, mode=None) -> list:
    cand = pool.copy()
    if mode == "rest":
        cand = cand[cand.EnergyLevel <= 2]
    if mode == "indoor":
        cand = cand[~cand.Category.isin(["Nature", "Adventure"])]
    if cand.empty:
        return []
    score = cand.FamilyRating + 1.0 * cand.Category.str.lower().isin(interests)
    if mode == "rest":
        score = score + 1.5 * (cand.Category == "Relaxation")
    if mode == "budget":
        score = score - 0.01 * cand.CostUSD
    cand = cand.assign(_key=score / cand.EnergyLevel.clip(lower=0.5)).sort_values(["_key", "ActivityID"],
                                                                                 ascending=[False, True])
    chosen, h_used, e_used = [], 0.0, 0.0
    for r in cand.itertuples():
        if h_used + r.DurationHours <= hours and e_used + r.EnergyLevel <= energy:
            chosen.append(r.ActivityID)
            h_used += r.DurationHours + 0.5
            e_used += r.EnergyLevel
    return chosen


def _day_rows(spec: dict, acts_by_id: dict) -> list:
    rows = []
    date_s = spec["date"].isoformat()
    if spec["travel"]:
        label = (f"Arrive in {spec['city']} and check in" if spec["day"] == 1
                 else f"Travel to {spec['city']} and check in")
        if spec["delay"]:
            label += f" (flight delayed {spec['delay']:g} h)"
        rows.append({"Day": spec["day"], "Date": date_s, "City": spec["city"], "Time": _fmt_time(spec["start"] - 1),
                     "Activity": label, "ActivityID": "", "Category": "Travel", "DurationHours": 0.0,
                     "EnergyLevel": 0.0, "CostUSD": 0.0})
    t = spec["start"]
    for aid in spec["chosen"]:
        a = acts_by_id[aid]
        rows.append({"Day": spec["day"], "Date": date_s, "City": spec["city"], "Time": _fmt_time(t),
                     "Activity": a["Activity"], "ActivityID": aid, "Category": a["Category"],
                     "DurationHours": float(a["DurationHours"]), "EnergyLevel": float(a["EnergyLevel"]),
                     "CostUSD": float(a["CostUSD"])})
        t += float(a["DurationHours"]) + 0.5
    if not spec["chosen"]:
        rows.append({"Day": spec["day"], "Date": date_s, "City": spec["city"], "Time": _fmt_time(spec["start"]),
                     "Activity": "Free time and rest at the hotel", "ActivityID": "", "Category": "Rest",
                     "DurationHours": 0.0, "EnergyLevel": 0.0, "CostUSD": 0.0})
    return rows


def _build(specs, acts_by_id) -> pd.DataFrame:
    rows = []
    for s in specs:
        rows += _day_rows(s, acts_by_id)
    return pd.DataFrame(rows, columns=["Day", "Date", "City", "Time", "Activity", "ActivityID", "Category",
                                       "DurationHours", "EnergyLevel", "CostUSD"])


_MODES = {
    "rest": (["tired", "exhausted", "rest", "relax", "slow", "sleep", "jet lag", "jetlag", "sick", "unwell"],
             "recover energy while keeping the trip enjoyable"),
    "budget": (["budget", "cheap", "cheaper", "expensive", "money", "save", "cost"],
               "spend less without losing the highlights"),
    "indoor": (["rain", "raining", "weather", "heat", "too hot", "storm", "indoor"],
               "avoid outdoor activities because of the weather"),
}


def analyze_travel(acts, family, hotels, flights, days, start, budget, fx, req, cur, dh, de):
    trace = ReasoningTrace()
    a = acts.copy()
    a["ActivityID"] = a.ActivityID.astype(str)
    a["City"] = a.City.astype(str)
    a["Category"] = a.Category.astype(str)
    acts_by_id = {r["ActivityID"]: r for r in a.to_dict("records")}
    n = max(len(family), 1)
    interests = set()
    for v in family.get("Interests", pd.Series(dtype=str)).fillna("").astype(str):
        interests |= {x.strip().lower() for x in v.replace(",", ";").split(";") if x.strip()}

    alloc = _city_alloc(a, days)
    delays = {}
    if flights is not None and len(flights) and "ToCity" in flights.columns:
        for r in flights.itertuples():
            delays[str(r.ToCity)] = max(delays.get(str(r.ToCity), 0.0), _num(getattr(r, "DelayHours", 0)))

    specs, used, day = [], set(), 1
    for city, nd in alloc:
        for k in range(nd):
            travel = k == 0
            delay = delays.get(city, 0.0) if travel else 0.0
            st_h = min(12.0 + delay, 20.0) if travel else 9.0
            hrs = max(1.0, dh - 3 - delay) if travel else float(dh)
            en = max(2.0, de * 0.6) if travel else float(de)
            pool = a[(a.City == city) & (~a.ActivityID.isin(used))]
            chosen = _select(pool, hrs, en, interests)
            used |= set(chosen)
            specs.append({"day": day, "date": start + _td(days=day - 1), "city": city, "travel": travel,
                          "delay": delay, "start": st_h, "hours": hrs, "energy": en, "chosen": chosen})
            day += 1
    base = _build(specs, acts_by_id)

    adj, target, expl = None, None, ""
    text = str(req).lower()
    mode = next((m for m, (keys, _) in _MODES.items() if any(k in text for k in keys)), None)
    if mode and specs:
        m = _re.search(r"day\s*(\d+)", text)
        target = int(m.group(1)) if m else (cur if "today" in text else cur + 1)
        target = min(max(target, 1), len(specs))
        new = [dict(s, chosen=list(s["chosen"])) for s in specs]
        s = new[target - 1]
        other_used = {x for t in new if t is not s for x in t["chosen"]}
        cand = a[(a.City == s["city"]) & (~a.ActivityID.isin(other_used))]
        h0 = sum(acts_by_id[x]["DurationHours"] for x in s["chosen"])
        e0 = sum(acts_by_id[x]["EnergyLevel"] for x in s["chosen"])
        if mode == "rest":
            s["hours"], s["energy"] = min(s["hours"], 5.0), min(s["energy"], 5.0)
            s["start"] = max(s["start"], 10.5)
        new_ch = _select(cand, s["hours"], s["energy"], interests, mode)
        dropped = [x for x in s["chosen"] if x not in new_ch]
        s["chosen"] = new_ch
        moved, skipped = [], []
        for x in dropped:
            placed = False
            for t in new[target:]:
                if t["city"] != s["city"]:
                    continue
                hh = sum(acts_by_id[y]["DurationHours"] + 0.5 for y in t["chosen"])
                ee = sum(acts_by_id[y]["EnergyLevel"] for y in t["chosen"])
                if hh + acts_by_id[x]["DurationHours"] <= dh and ee + acts_by_id[x]["EnergyLevel"] <= de:
                    t["chosen"].append(x)
                    moved.append(f"{acts_by_id[x]['Activity']} (day {t['day']})")
                    placed = True
                    break
            if not placed:
                skipped.append(acts_by_id[x]["Activity"])
        adj = _build(new, acts_by_id)
        h1 = sum(acts_by_id[x]["DurationHours"] for x in new_ch)
        e1 = sum(acts_by_id[x]["EnergyLevel"] for x in new_ch)
        expl = (f"You said \"{req}\". I read this as a request to {_MODES[mode][1]}, not a literal edit. "
                f"Day {target} in {s['city']} now starts at {_fmt_time(s['start'])} with {h1:g} activity hours "
                f"(was {h0:g}) and an energy load of {e1:g} (was {e0:g}). "
                + (f"Moved to later days: {', '.join(moved)}. " if moved else "")
                + (f"Not rescheduled: {', '.join(skipped)}." if skipped else ""))
    final = adj if adj is not None else base

    rooms = math.ceil(n / 3)
    rate = {}
    if hotels is not None and len(hotels):
        for r in hotels.itertuples():
            rate[str(r.City)] = _num(getattr(r, "RateUSDPerNight", 120), 120)
    hotel_usd = 0.0
    for i, (city, nd) in enumerate(alloc):
        nights = nd - 1 if i == len(alloc) - 1 else nd
        hotel_usd += max(nights, 0) * rate.get(city, 120.0) * rooms
    flights_usd = (pd.to_numeric(flights.get("PriceUSDPerPerson", pd.Series(dtype=float)), errors="coerce").fillna(0).sum()
                   * n if flights is not None else 0.0)
    act_usd = float(final.CostUSD.sum()) * n
    lines = pd.DataFrame([("Flights", flights_usd), ("Hotels", hotel_usd), ("Activities and entry fees", act_usd),
                          ("Ground transport", 60.0 * days), ("Food", 15.0 * n * days)], columns=["Category", "USD"])
    lines["USD"] = lines.USD.round(0)
    lines["INR"] = (lines.USD * fx).round(0)
    total = float(lines.USD.sum())
    cash = 0.20 * (total - flights_usd) * fx

    trace.add("Understand family and budget", f"{n} travelers; shared interests: {', '.join(sorted(interests)) or 'none given'}; "
                                              f"budget {budget:,.0f} USD.")
    trace.add("Allocate days", "Days per city by enjoyment weight: " + ", ".join(f"{c} {d}" for c, d in alloc) + ".")
    trace.add("Check flights", ("Delays absorbed: " + ", ".join(f"{c} +{v:g} h" for c, v in delays.items() if v) + ".")
              if any(delays.values()) else "No flight delays reported.")
    trace.add("Build itinerary", f"Selected activities by enjoyment per unit of energy within {dh} hours and energy {de} per day.")
    trace.add("Calculate budget and currency", f"Estimated {total:,.0f} USD ({'within' if total <= budget else 'over'} budget) "
                                               f"at {fx} INR per USD; carry about {cash:,.0f} INR in cash.")
    trace.add("Adapt to the request", expl if expl else "No change requested, so the base plan stands.")
    return base, adj, target, expl, lines, total, cash, alloc, trace


def draft_messages(final: pd.DataFrame, hotels: pd.DataFrame) -> str:
    hmap = {}
    if hotels is not None and len(hotels):
        for r in hotels.itertuples():
            hmap[str(r.City)] = (str(getattr(r, "HotelName", "the hotel")), str(getattr(r, "CheckInTime", "14:00")))
    out = []
    for city, grp in final.groupby("City", sort=False):
        name, cin = hmap.get(city, ("the hotel", "14:00"))
        out.append(f"To {name}: Hello, this is to confirm our family booking from {grp.Date.min()} for "
                   f"{grp.Day.nunique()} night(s). We expect to arrive around check in ({cin}). Please let us know "
                   "if an early breakfast is possible on days with early sightseeing. Thank you.")
    for d, grp in final.groupby("Day"):
        acts = grp[grp.ActivityID != ""]
        if acts.empty:
            continue
        first = acts.iloc[0]
        hh, mm = map(int, first.Time.split(":"))
        pick = _fmt_time(max(hh + mm / 60 - 0.5, 0))
        out.append(f"To driver, day {d} ({first.Date}, {first.City}): please pick us up at {pick} for {first.Activity}.")
    return "\n".join(out)


# =============================================================================
# REPORT EXPORTS  (built in - replaces the separate exports.py module)
# =============================================================================
_DEV_LINE = "Developed by Randy Singh from Kalsnet (KNet) Consulting Group"


def _clean(x) -> str:
    if x is None:
        return ""
    if isinstance(x, float) and math.isnan(x):
        return ""
    s = str(x)
    for k, v in {"→": "->", "—": "-", "–": "-", "≥": ">=", "≤": "<=", "…": "...",
                 "₹": "INR "}.items():
        s = s.replace(k, v)
    return s


def _latin(x) -> str:
    return _clean(x).encode("latin-1", "replace").decode("latin-1")


def _esc(x) -> str:
    return _latin(x).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _cut(x, n: int = 90) -> str:
    s = _clean(x)
    return s if len(s) <= n else s[: n - 3] + "..."


def to_pdf(title: str, sections: list, tables: dict) -> bytes:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import landscape, letter
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle

    buf = io.BytesIO()
    page = landscape(letter)
    doc = SimpleDocTemplate(buf, pagesize=page, leftMargin=0.5 * inch, rightMargin=0.5 * inch,
                            topMargin=0.5 * inch, bottomMargin=0.5 * inch, title=_latin(title))
    ss = getSampleStyleSheet()
    blue = colors.HexColor("#0D47A1")
    h1 = ParagraphStyle("h1", parent=ss["Title"], textColor=blue, fontSize=22, leading=26)
    dev = ParagraphStyle("dev", parent=ss["Title"], textColor=blue, fontSize=14, leading=18)
    h2 = ParagraphStyle("h2", parent=ss["Heading2"], textColor=blue)
    body = ParagraphStyle("b", parent=ss["BodyText"], fontSize=9.5, leading=12.5)
    cell = ParagraphStyle("c", parent=ss["BodyText"], fontSize=7, leading=8.5)
    hcell = ParagraphStyle("hc", parent=cell, textColor=colors.white, fontName="Helvetica-Bold")
    code = ParagraphStyle("code", parent=ss["Code"], fontSize=7, leading=8.5)

    story = [Paragraph(_esc(title), h1), Paragraph(_esc(_DEV_LINE), dev),
             Paragraph(f"Generated {date.today().isoformat()}", body), Spacer(1, 8)]
    for head, text in sections:
        story.append(Paragraph(_esc(head), h2))
        t = _latin(text)
        if "\n" in t and ("def " in t or t.lstrip().startswith('"""')):
            story.append(Preformatted(t, code))
        else:
            for para in t.split("\n"):
                if para.strip():
                    story.append(Paragraph(_esc(para), body))
    avail = page[0] - 1.0 * inch
    for name, df in tables.items():
        story.append(Paragraph(_esc(name), h2))
        if df is None or len(df) == 0:
            story.append(Paragraph("No rows.", body))
            continue
        cols = list(df.columns)[:10]
        sub = df[cols].head(60)
        data = [[Paragraph(_esc(c), hcell) for c in cols]]
        data += [[Paragraph(_esc(_cut(v)), cell) for v in row] for row in sub.itertuples(index=False)]
        tb = Table(data, colWidths=[avail / len(cols)] * len(cols), repeatRows=1)
        tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), blue),
                                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#E3F2FD")]),
                                ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#90CAF9")),
                                ("VALIGN", (0, 0), (-1, -1), "TOP")]))
        story.append(tb)
        notes = []
        if len(df) > 60:
            notes.append(f"first 60 of {len(df)} rows")
        if len(df.columns) > 10:
            notes.append(f"first 10 of {len(df.columns)} columns")
        if notes:
            story.append(Paragraph(f"<i>Showing {' and '.join(notes)}. The CSV export has everything.</i>", body))
    doc.build(story)
    return buf.getvalue()


def to_docx(title: str, sections: list, tables: dict) -> bytes:
    from docx import Document
    from docx.enum.section import WD_ORIENT
    from docx.shared import Inches, Pt, RGBColor

    doc = Document()
    sec = doc.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = sec.page_height, sec.page_width
    for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, side, Inches(0.6))
    blue = RGBColor(0x0D, 0x47, 0xA1)

    def para(text, size=10.5, bold=False, color=None, font=None):
        p = doc.add_paragraph()
        r = p.add_run(_clean(text))
        r.font.size, r.bold = Pt(size), bold
        if color is not None:
            r.font.color.rgb = color
        if font:
            r.font.name = font
        return p

    para(title, 22, True, blue)
    para(_DEV_LINE, 14, True, blue)
    para(f"Generated {date.today().isoformat()}", 9)
    for head, text in sections:
        para(head, 13, True, blue)
        t = _clean(text)
        is_code = "\n" in t and ("def " in t or t.lstrip().startswith('"""'))
        if is_code:
            para(t, 8, font="Consolas")
        else:
            for line in t.split("\n"):
                if line.strip():
                    para(line)
    for name, df in tables.items():
        para(name, 13, True, blue)
        if df is None or len(df) == 0:
            para("No rows.")
            continue
        cols = list(df.columns)[:12]
        sub = df[cols].head(100)
        tb = doc.add_table(rows=1, cols=len(cols))
        tb.style = "Table Grid"
        for i, c in enumerate(cols):
            run = tb.rows[0].cells[i].paragraphs[0].add_run(str(c))
            run.bold, run.font.size = True, Pt(8)
        for row in sub.itertuples(index=False):
            cells = tb.add_row().cells
            for i, v in enumerate(row):
                run = cells[i].paragraphs[0].add_run(_cut(v, 120))
                run.font.size = Pt(8)
        if len(df) > 100 or len(df.columns) > 12:
            para("Table truncated in Word. The CSV export has every row and column.", 9)
    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()


def to_text(title: str, sections: list, tables: dict) -> bytes:
    bar = "=" * 100
    out = [bar, _clean(title), _DEV_LINE, f"Generated {date.today().isoformat()}", bar, ""]
    for head, text in sections:
        out += [_clean(head).upper(), "-" * len(_clean(head)), _clean(text), ""]
    for name, df in tables.items():
        out += [f"TABLE: {_clean(name)}", "-" * (7 + len(_clean(name)))]
        if df is None or len(df) == 0:
            out += ["No rows.", ""]
            continue
        with pd.option_context("display.max_columns", None, "display.width", 250, "display.max_colwidth", 45):
            out += [df.to_string(index=False, max_rows=300), ""]
    return "\n".join(out).encode("utf-8")


def to_csv(tables: dict) -> bytes:
    buf = io.StringIO()
    for name, df in tables.items():
        if df is None:
            continue
        buf.write(f"# {_clean(name)}\n")
        df.to_csv(buf, index=False)
        buf.write("\n")
    return buf.getvalue().encode("utf-8-sig")


# Namespaces so the user interface below can keep calling E.<name> and X.<name>.
E = _SimpleNamespace(**{k: v for k, v in dict(globals()).items() if not k.startswith("__")})
X = E

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
                dot.append(f'"{r.ModuleID}" [label="{r.ModuleName}", fillcolor="{colors[L]}"];')
            dot.append("}")
        for u, v in dg.edges:
            if u in set(mods.ModuleID):
                dot.append(f"\"{u}\" -> \"{v}\" [color=\"#607D8B\"];")
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
