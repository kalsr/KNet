

# KNet ASI Decision Intelligence Platform
# Developed by Randy Singh from Kalsnet (KNet) Consulting Group

#  single Streamlit application that demonstrates six enterprise use cases of an
# Artificial Super Intelligence (ASI) style decision engine. Every use case supports
# synthetic data and real data upload, explains each field, formula and benefit,
# draws workflow and decision flow charts, and exports results as PDF, TXT and CSV.

# Run with:  streamlit run app.py

import io
import datetime as dt
from statistics import NormalDist

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from fpdf import FPDF  # noqa: E402
from sklearn.cluster import KMeans  # noqa: E402
from sklearn.decomposition import PCA  # noqa: E402
from sklearn.ensemble import (  # noqa: E402
    GradientBoostingClassifier,
    GradientBoostingRegressor,
    IsolationForest,
    RandomForestClassifier,
)
from sklearn.linear_model import LinearRegression, LogisticRegression  # noqa: E402
from sklearn.metrics import (  # noqa: E402
    accuracy_score,
    confusion_matrix,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
    silhouette_score,
)
from sklearn.model_selection import train_test_split  # noqa: E402
from sklearn.pipeline import Pipeline  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402

# ----------------------------------------------------------------------------
# Global identity and theme
# ----------------------------------------------------------------------------
APP_TITLE = "Kalsnet (KNet) ASI Decision Intelligence Platform"
APP_TAGLINE = "Artificial Super Intelligence for Predictive, Prescriptive and Explainable Enterprise Decisions"
DEVELOPER = "Developed by Randy Singh from Kalsnet (KNet) Consulting Group"

NAVY = "#0B1F44"
BLUE = "#1F4E9E"
BRIGHT_BLUE = "#0047FF"
TEAL = "#0F9D8A"
AMBER = "#F2A93B"
CORAL = "#E4572E"
PURPLE = "#6C4AB6"
SLATE = "#5B6B82"
COLORWAY = [BLUE, TEAL, AMBER, CORAL, PURPLE, "#2BB3D9", "#8AA339", "#C2457A"]
TIER_COLORS = {"Low": TEAL, "Medium": AMBER, "High": CORAL}

st.set_page_config(page_title=APP_TITLE, layout="wide", initial_sidebar_state="expanded")

CSS = f"""
<style>
#MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {{visibility: hidden;}}
.block-container {{padding-top: 3.2rem; padding-bottom: 2rem; max-width: 1400px;}}
html, body, [class*="css"] {{font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;}}

.app-banner {{
  background: linear-gradient(110deg, {NAVY} 0%, {BLUE} 55%, {TEAL} 100%);
  border-radius: 14px; padding: 22px 30px; color: #FFFFFF;
  box-shadow: 0 8px 24px rgba(11,31,68,0.25);
}}
.app-title {{font-size: 2.15rem; font-weight: 800; letter-spacing: 0.3px; margin: 0;}}
.app-tagline {{font-size: 1.0rem; opacity: 0.92; margin-top: 4px;}}
.dev-line {{
  color: {BRIGHT_BLUE}; font-weight: 800; font-size: 1.55rem;
  margin: 14px 0 6px 2px; letter-spacing: 0.2px;
}}
.uc-header {{
  background: #FFFFFF; border-left: 8px solid var(--accent); border-radius: 10px;
  padding: 16px 22px; margin: 10px 0 14px 0; box-shadow: 0 2px 10px rgba(11,31,68,0.08);
}}
.uc-header h2 {{margin: 0; color: {NAVY}; font-size: 1.6rem;}}
.uc-header p {{margin: 4px 0 0 0; color: {SLATE}; font-size: 1.0rem;}}
.card {{
  background: #FFFFFF; border-radius: 12px; padding: 16px 18px; height: 100%;
  box-shadow: 0 2px 10px rgba(11,31,68,0.08); border-top: 5px solid var(--accent);
}}
.card h4 {{margin: 0 0 6px 0; color: {NAVY}; font-size: 1.05rem;}}
.card p {{margin: 0; color: #3A4659; font-size: 0.92rem; line-height: 1.45;}}
.kpi {{
  background: #FFFFFF; border-radius: 12px; padding: 14px 16px;
  box-shadow: 0 2px 10px rgba(11,31,68,0.08); border-left: 6px solid var(--accent);
}}
.kpi .label {{color: {SLATE}; font-size: 0.80rem; text-transform: uppercase; letter-spacing: 0.6px;}}
.kpi .value {{color: {NAVY}; font-size: 1.45rem; white-space: nowrap; font-weight: 800; margin-top: 2px;}}
.kpi .help {{color: #7A8699; font-size: 0.76rem; margin-top: 2px;}}
.section-title {{color: {NAVY}; font-weight: 750; font-size: 1.2rem; margin: 18px 0 6px 0;
  border-bottom: 2px solid #E3E9F4; padding-bottom: 4px;}}
.explain {{background: #F2F6FD; border-radius: 10px; padding: 12px 16px; color: #26344D;
  border: 1px solid #DCE6F7; font-size: 0.93rem; line-height: 1.5;}}
.formula-name {{color: {BLUE}; font-weight: 700; font-size: 1.02rem; margin-top: 10px;}}
.insight {{background: #FFFFFF; border-left: 5px solid {TEAL}; border-radius: 8px; padding: 10px 14px;
  margin-bottom: 8px; box-shadow: 0 1px 6px rgba(11,31,68,0.06); color: #24324A;}}

[data-testid="stSidebar"] {{background: linear-gradient(180deg, {NAVY} 0%, #132E63 100%);}}
[data-testid="stSidebar"] * {{color: #E9EEF8 !important;}}
[data-testid="stSidebar"] .stRadio, [data-testid="stSidebar"] [role="radiogroup"] {{width: 100%;}}
[data-testid="stSidebar"] [role="radiogroup"] {{gap: 6px; display: flex; flex-direction: column;}}
[data-testid="stSidebar"] [data-testid="stRadioGroup"] > div {{width: 100%;}}
[data-testid="stSidebar"] [data-testid="stRadioOption"] {{width: 100% !important; margin: 0; box-sizing: border-box;}}
[data-testid="stSidebar"] .stRadio label {{
  background: rgba(255,255,255,0.06); border-radius: 8px; padding: 9px 12px; width: 100%;
  border: 1px solid rgba(255,255,255,0.08);
}}
[data-testid="stSidebar"] .stRadio label:hover {{background: rgba(255,255,255,0.16);}}
.side-brand {{font-weight: 800; font-size: 1.15rem; color: #FFFFFF; margin-bottom: 2px;}}
.side-sub {{font-size: 0.80rem; opacity: 0.8; margin-bottom: 12px;}}

.stTabs [data-baseweb="tab-list"] {{gap: 6px;}}
.stTabs button[role="tab"] {{
  background: #FFFFFF; border-radius: 8px 8px 0 0; padding: 8px 16px; font-weight: 600;
  border: 1px solid #E1E7F2;
}}
.stTabs button[role="tab"][aria-selected="true"] {{background: {BLUE}; border-color: {BLUE};}}
.stTabs button[role="tab"][aria-selected="true"] p {{color: #FFFFFF !important;}}
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] {{display: none;}}
div.stButton > button, div.stDownloadButton > button {{
  border-radius: 8px; font-weight: 650; border: 1px solid {BLUE};
}}
div.stButton > button[kind="primary"] {{background: {BLUE}; color: #FFFFFF;}}
</style>
"""


# ----------------------------------------------------------------------------
# Small helpers
# ----------------------------------------------------------------------------
def usd(x):
    if abs(x) >= 1e9:
        return f"USD {x / 1e9:,.2f} B"
    if abs(x) >= 1e6:
        return f"USD {x / 1e6:,.2f} M"
    return f"USD {x:,.0f}"


def pct(x):
    return f"{100 * x:.1f}%"


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def to_binary(series):
    s = series.copy()
    if not pd.api.types.is_numeric_dtype(s):
        mapping = {"yes": 1, "y": 1, "true": 1, "1": 1, "default": 1, "fraud": 1, "churn": 1, "failure": 1,
                   "no": 0, "n": 0, "false": 0, "0": 0, "": 0}
        s = s.astype(str).str.strip().str.lower().map(mapping)
    s = pd.to_numeric(s, errors="coerce")
    return (s > 0).astype(float).where(s.notna())


def style_fig(fig, height=380):
    fig.update_layout(template="plotly_white", colorway=COLORWAY, height=height,
                      margin=dict(l=20, r=20, t=50, b=20), font=dict(family="Segoe UI, Arial", size=12),
                      title_font=dict(size=15, color=NAVY), legend=dict(orientation="h", y=-0.18))
    return fig


def mpl_png(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue()


def mpl_bar(labels, values, title, xlabel="", color=BLUE, horizontal=True):
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    if horizontal:
        ax.barh(list(labels)[::-1], list(values)[::-1], color=color)
        ax.set_xlabel(xlabel)
    else:
        ax.bar(list(labels), list(values), color=[COLORWAY[i % len(COLORWAY)] for i in range(len(labels))])
        ax.set_ylabel(xlabel)
    ax.set_title(title, color=NAVY, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    return mpl_png(fig)


def mpl_hist(values, title, xlabel, color=BLUE, vline=None):
    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    ax.hist(values, bins=40, color=color, alpha=0.85)
    if vline is not None:
        ax.axvline(vline, color=CORAL, linestyle="--", linewidth=2)
    ax.set_title(title, color=NAVY, fontweight="bold")
    ax.set_xlabel(xlabel)
    ax.spines[["top", "right"]].set_visible(False)
    return mpl_png(fig)


def flow_dot(steps):
    fills = ["#E8F0FE", "#E3F6F3", "#FFF4E0", "#FDE9E4", "#EFEAFA", "#E4F5FB", "#EEF4E2", "#F9E6EF"]
    borders = COLORWAY
    lines = [
        "digraph G {", "rankdir=LR;", 'bgcolor="transparent";', "nodesep=0.35; ranksep=0.45;",
        'node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, penwidth=1.6, '
        'fontcolor="#0B1F44", margin="0.15,0.08"];',
        'edge [color="#5B6B82", penwidth=1.4, arrowsize=0.8];',
    ]
    for i, s in enumerate(steps):
        lines.append(f'n{i} [label="{s}", fillcolor="{fills[i % 8]}", color="{borders[i % 8]}"];')
    for i in range(len(steps) - 1):
        lines.append(f"n{i} -> n{i + 1};")
    lines.append("}")
    return "\n".join(lines)


def decision_dot(start, question, branches):
    lines = [
        "digraph D {", "rankdir=TB;", 'bgcolor="transparent";', "nodesep=0.5; ranksep=0.45;",
        'node [fontname="Helvetica", fontsize=11, fontcolor="#0B1F44", penwidth=1.6];',
        'edge [color="#5B6B82", penwidth=1.4, fontname="Helvetica", fontsize=10, fontcolor="#1F4E9E"];',
        f'start [label="{start}", shape=box, style="rounded,filled", fillcolor="#E8F0FE", color="{BLUE}"];',
        f'q [label="{question}", shape=diamond, style="filled", fillcolor="#FFF4E0", color="{AMBER}"];',
        "start -> q;",
    ]
    fills = {TEAL: "#E3F6F3", AMBER: "#FFF4E0", CORAL: "#FDE9E4", BLUE: "#E8F0FE", PURPLE: "#EFEAFA"}
    for i, (edge, action, color) in enumerate(branches):
        lines.append(f'a{i} [label="{action}", shape=box, style="rounded,filled", '
                     f'fillcolor="{fills.get(color, "#F2F6FD")}", color="{color}"];')
        lines.append(f'q -> a{i} [label="  {edge}  "];')
    lines.append("}")
    return "\n".join(lines)


# ----------------------------------------------------------------------------
# Shared classification engine (used by maintenance, churn and credit risk)
# ----------------------------------------------------------------------------
def encode_features(df, numeric, categorical):
    X = df[numeric].astype(float).copy()
    for c in categorical:
        if c in df.columns:
            d = pd.get_dummies(df[c].astype(str), prefix=c, drop_first=True, dtype=float)
            X = pd.concat([X, d], axis=1)
    return X


def classifier_ui(key, default_model="Random Forest"):
    models = ["Random Forest", "Gradient Boosting", "Logistic Regression"]
    c1, c2, c3 = st.columns(3)
    model = c1.selectbox("ASI learning engine", models, index=models.index(default_model), key=f"{key}_model",
                         help="Random Forest averages many decision trees. Gradient Boosting builds trees "
                              "sequentially to fix earlier errors. Logistic Regression is a transparent linear model.")
    test = c2.slider("Validation share of data", 0.1, 0.5, 0.25, 0.05, key=f"{key}_test",
                     help="Portion of records held back to test the model on data it has never seen.")
    thr = c3.slider("Alert probability threshold", 0.05, 0.95, 0.5, 0.05, key=f"{key}_thr",
                    help="Records with a predicted probability at or above this value are flagged.")
    return {"model": model, "test": test, "thr": thr}


def train_classifier(X, y, model_name, test_size, thr, seed=42):
    y = y.astype(int)
    if y.nunique() < 2:
        raise ValueError("The target field contains only one class. Both outcomes are needed to train the engine.")
    strat = y if y.value_counts().min() >= 2 else None
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=test_size, random_state=seed, stratify=strat)
    if model_name == "Random Forest":
        m = RandomForestClassifier(n_estimators=250, min_samples_leaf=2, random_state=seed,
                                   class_weight="balanced", n_jobs=-1)
    elif model_name == "Gradient Boosting":
        m = GradientBoostingClassifier(random_state=seed)
    else:
        m = Pipeline([("sc", StandardScaler()),
                      ("lr", LogisticRegression(max_iter=2000, class_weight="balanced"))])
    m.fit(Xtr, ytr)
    p_te = m.predict_proba(Xte)[:, 1]
    pred = (p_te >= thr).astype(int)
    if model_name == "Logistic Regression":
        imp = np.abs(m.named_steps["lr"].coef_[0])
    else:
        imp = m.feature_importances_
    imp = pd.Series(imp / (imp.sum() or 1), index=X.columns).sort_values(ascending=False)
    fpr, tpr, _ = roc_curve(yte, p_te)
    out = {
        "model": m, "accuracy": accuracy_score(yte, pred),
        "precision": precision_score(yte, pred, zero_division=0),
        "recall": recall_score(yte, pred, zero_division=0),
        "f1": f1_score(yte, pred, zero_division=0),
        "auc": roc_auc_score(yte, p_te) if yte.nunique() > 1 else float("nan"),
        "cm": confusion_matrix(yte, pred, labels=[0, 1]), "fpr": fpr, "tpr": tpr,
        "importance": imp, "proba_all": m.predict_proba(X)[:, 1], "n_test": len(yte),
    }
    return out


def classifier_figs(r, neg, posl):
    roc = go.Figure()
    roc.add_trace(go.Scatter(x=r["fpr"], y=r["tpr"], mode="lines", name=f"Model AUC {r['auc']:.3f}",
                             line=dict(color=BLUE, width=3), fill="tozeroy", fillcolor="rgba(31,78,158,0.12)"))
    roc.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines", name="Random guess",
                             line=dict(color=SLATE, dash="dash")))
    roc.update_layout(title="ROC Curve on Validation Data", xaxis_title="False Positive Rate",
                      yaxis_title="True Positive Rate")
    cm = px.imshow(r["cm"], text_auto=True, color_continuous_scale="Blues",
                   x=[f"Predicted {neg}", f"Predicted {posl}"], y=[f"Actual {neg}", f"Actual {posl}"],
                   title="Confusion Matrix on Validation Data")
    cm.update_coloraxes(showscale=False)
    imp = r["importance"].head(12)
    fi = px.bar(x=imp.values[::-1], y=imp.index[::-1], orientation="h", title="Driver Importance",
                labels={"x": "Relative importance", "y": ""}, color_discrete_sequence=[TEAL])
    return [
        ("ROC Curve", style_fig(roc), "Shows how well the engine separates the two outcomes at every threshold. "
                                      "The closer the curve hugs the top left corner, the better."),
        ("Confusion Matrix", style_fig(cm), "Counts of correct and incorrect predictions at the chosen threshold."),
        ("Driver Importance", style_fig(fi), "Which input fields drive the prediction most. This is the "
                                              "explainability layer that tells the business why."),
    ]


def classifier_metrics(r):
    return [
        ("Accuracy", pct(r["accuracy"]), "Share of validation records predicted correctly"),
        ("Precision", pct(r["precision"]), "Of the records flagged, share that were truly positive"),
        ("Recall", pct(r["recall"]), "Of the truly positive records, share the engine caught"),
        ("F1 Score", f"{r['f1']:.3f}", "Balance of precision and recall"),
        ("ROC AUC", f"{r['auc']:.3f}", "Ranking quality, 0.5 is random and 1.0 is perfect"),
    ]


def tier(p, low=0.3, high=0.6):
    return np.where(p >= high, "High", np.where(p >= low, "Medium", "Low"))


def tier_fig(df, col="Risk Tier", title="Records by Risk Tier"):
    counts = df[col].value_counts().reindex(["Low", "Medium", "High"]).fillna(0)
    fig = px.pie(values=counts.values, names=counts.index, hole=0.55, title=title,
                 color=counts.index, color_discrete_map=TIER_COLORS)
    return style_fig(fig, 340), counts


# ============================================================================
# USE CASE 1  Predictive Maintenance
# ============================================================================
def synth_maintenance(n, seed):
    rng = np.random.default_rng(seed)
    temp = rng.normal(70, 8, n)
    vib = np.clip(rng.normal(3, 1, n), 0.2, None)
    press = rng.normal(100, 15, n)
    rpm = rng.normal(1500, 200, n)
    hours = rng.uniform(0, 20000, n)
    days = rng.uniform(0, 365, n)
    logit = (-6.2 + 0.09 * (temp - 70) + 1.25 * (vib - 3) + 0.00022 * hours + 0.009 * days
             + 0.025 * np.abs(press - 100))
    fail = rng.binomial(1, sigmoid(logit))
    return pd.DataFrame({
        "machine_id": [f"MCH{i:05d}" for i in range(1, n + 1)],
        "temperature_c": temp.round(1), "vibration_mm_s": vib.round(2), "pressure_psi": press.round(1),
        "rotation_rpm": rpm.round(0), "operating_hours": hours.round(0),
        "days_since_service": days.round(0), "failure_flag": fail,
    })


def params_maintenance(key):
    p = classifier_ui(key)
    c1, c2 = st.columns(2)
    p["cf"] = c1.number_input("Cost of one unplanned failure in USD", 1000, 5_000_000, 50_000, 1000, key=f"{key}_cf")
    p["cp"] = c2.number_input("Cost of one preventive service in USD", 100, 1_000_000, 5_000, 500, key=f"{key}_cp")
    return p


def run_maintenance(df, p):
    num = ["temperature_c", "vibration_mm_s", "pressure_psi", "rotation_rpm", "operating_hours", "days_since_service"]
    X = encode_features(df, num, [])
    r = train_classifier(X, df["failure_flag"], p["model"], p["test"], p["thr"])
    prob = r["proba_all"]
    out = df.copy()
    out["Failure Probability"] = prob.round(4)
    out["Health Index"] = (100 * (1 - prob)).round(1)
    out["Risk Tier"] = tier(prob)
    out["Expected Failure Cost USD"] = (prob * p["cf"]).round(0)
    out["Net Avoided Cost USD"] = (prob * p["cf"] - p["cp"]).round(0)
    out["Recommended Action"] = np.where(prob >= p["thr"], "Schedule preventive service now",
                                         np.where(prob >= 0.3, "Increase monitoring", "Continue normal operation"))
    out = out.sort_values("Failure Probability", ascending=False)
    flagged = out[out["Failure Probability"] >= p["thr"]]
    savings = flagged["Net Avoided Cost USD"].clip(lower=0).sum()
    breakeven = p["cp"] / p["cf"]

    metrics = classifier_metrics(r) + [
        ("Machines Flagged", f"{len(flagged):,}", "Machines at or above the alert threshold"),
        ("Avg Health Index", f"{out['Health Index'].mean():.1f}", "Fleet average, 100 is perfect health"),
        ("Expected Failure Cost", usd(out["Expected Failure Cost USD"].sum()), "Probability weighted fleet exposure"),
        ("Avoidable Cost", usd(savings), "Net value of servicing all flagged machines"),
        ("Break Even Probability", pct(breakeven), "Service is worthwhile above this probability"),
    ]
    tfig, counts = tier_fig(out, title="Fleet by Failure Risk Tier")
    hist = px.histogram(out, x="Health Index", nbins=40, color="Risk Tier", color_discrete_map=TIER_COLORS,
                        title="Fleet Health Index Distribution")
    sc = px.scatter(out, x="vibration_mm_s", y="temperature_c", color="Failure Probability",
                    color_continuous_scale="RdYlGn_r", title="Vibration versus Temperature Colored by Risk",
                    hover_data=["machine_id"], labels={"vibration_mm_s": "Vibration mm per s",
                                                       "temperature_c": "Temperature C"})
    figs = classifier_figs(r, "No Failure", "Failure") + [
        ("Risk Tier", tfig, "Share of the fleet in each risk tier, used to plan maintenance crews."),
        ("Health Index", style_fig(hist), "Distribution of machine health. Left tail machines need attention first."),
        ("Sensor Map", style_fig(sc), "Operating envelope of the fleet. Red points are the most likely to fail."),
    ]
    top = r["importance"].index[0]
    insights = [
        f"The strongest failure driver is {top}, contributing {pct(r['importance'].iloc[0])} of the model signal.",
        f"{int(counts.get('High', 0)):,} machines are in the High tier and {int(counts.get('Medium', 0)):,} "
        f"in the Medium tier.",
        f"Servicing the {len(flagged):,} flagged machines is expected to avoid {usd(savings)} in net cost.",
        f"Preventive service pays for itself whenever failure probability exceeds {pct(breakeven)}.",
        f"The engine catches {pct(r['recall'])} of real failures on unseen validation data.",
    ]
    pdf_imgs = [
        mpl_bar(r["importance"].head(8).index, r["importance"].head(8).values, "Driver Importance",
                "Relative importance", TEAL),
        mpl_bar(counts.index, counts.values, "Machines by Risk Tier", "Machines", horizontal=False),
        mpl_hist(out["Health Index"], "Fleet Health Index Distribution", "Health Index", BLUE),
    ]
    cols = ["machine_id", "Failure Probability", "Health Index", "Risk Tier", "Net Avoided Cost USD",
            "Recommended Action"]
    return dict(metrics=metrics, figs=figs, insights=insights, table=out, pdf_imgs=pdf_imgs, pdf_cols=cols)


UC_MAINTENANCE = dict(
    key="maint", name="Predictive Maintenance", accent=BLUE,
    subtitle="Predict equipment failure before it happens and schedule service at the lowest total cost",
    description=(
        "The ASI engine learns the relationship between sensor readings such as temperature, vibration, "
        "pressure and rotation speed, the age and service history of each asset, and historical failures. "
        "It then scores every machine with a probability of failure, converts it into a Health Index, and "
        "recommends whether to service now, watch closely, or continue normal operation based on the cost "
        "of failure versus the cost of preventive service."),
    importance=[
        "Unplanned downtime is one of the largest hidden costs in manufacturing, energy, transport and utilities.",
        "Calendar based maintenance services healthy machines too early and misses failing machines too late.",
        "Safety incidents and quality defects frequently begin as small sensor deviations that humans overlook.",
    ],
    benefits=[
        "Reduce unplanned downtime by acting on early warning signals.",
        "Lower maintenance spend by servicing only the machines that need it.",
        "Extend asset life and improve safety and product quality.",
        "Give planners a ranked work list with a clear financial justification for every action.",
    ],
    flow=["Sensor and\\nservice data", "Validate and\\nmap fields", "Train ASI\\nfailure engine",
          "Validate on\\nunseen data", "Score failure\\nprobability", "Health Index and\\nrisk tier",
          "Cost based\\nservice plan", "PDF TXT CSV\\nreports"],
    decision=("Machine scored", "Failure probability\\nversus threshold?",
              [("At or above threshold", "Schedule preventive\\nservice now", CORAL),
               ("Between 0.3 and threshold", "Increase monitoring\\nfrequency", AMBER),
               ("Below 0.3", "Continue normal\\noperation", TEAL)]),
    fields=[
        ("machine_id", "Identifier", "Optional", "Unique asset tag", "MCH00017", "Links each score back to a physical asset."),
        ("temperature_c", "Numeric", "Required", "Operating temperature in degrees Celsius", "74.2",
         "Overheating signals friction, lubrication loss or electrical stress."),
        ("vibration_mm_s", "Numeric", "Required", "Vibration velocity in millimetres per second", "3.85",
         "Rising vibration is the classic early sign of bearing wear or imbalance."),
        ("pressure_psi", "Numeric", "Required", "Operating pressure in pounds per square inch", "112.0",
         "Pressure far from normal indicates leaks, blockages or pump problems."),
        ("rotation_rpm", "Numeric", "Required", "Rotation speed in revolutions per minute", "1520",
         "Speed instability reveals drive and load problems."),
        ("operating_hours", "Numeric", "Required", "Total running hours of the asset", "14250",
         "Wear accumulates with usage, older assets fail more often."),
        ("days_since_service", "Numeric", "Required", "Days since the last preventive service", "210",
         "Longer intervals without service raise failure risk."),
        ("failure_flag", "Binary 0 or 1", "Required", "1 if the machine failed in the observation window", "0",
         "The historical outcome the engine learns from."),
    ],
    formulas=[
        ("Ensemble failure probability", r"\hat{p}(x) = \frac{1}{T}\sum_{t=1}^{T} h_t(x)",
         "p = average of T tree votes",
         "Each of T decision trees votes on whether the machine will fail. The average vote is the failure probability."),
        ("Health Index", r"HI = 100 \times \left(1 - \hat{p}\right)", "HI = 100 x (1 minus p)",
         "Converts probability into an intuitive 0 to 100 score where 100 means perfectly healthy."),
        ("Expected failure cost", r"E[C] = \hat{p} \times C_f", "E[C] = p x Cf",
         "Probability weighted cost of letting the machine run, where Cf is the cost of an unplanned failure."),
        ("Net avoided cost", r"S = \hat{p}\,C_f - C_p", "S = p x Cf minus Cp",
         "Value of servicing now, where Cp is the preventive service cost. Positive S means service is worthwhile."),
        ("Break even probability", r"p^{*} = \frac{C_p}{C_f}", "p* = Cp divided by Cf",
         "Service is economically justified whenever the failure probability exceeds this value."),
        ("F1 score", r"F_1 = \frac{2 \cdot Precision \cdot Recall}{Precision + Recall}",
         "F1 = 2PR divided by (P plus R)", "Balances false alarms against missed failures in one number."),
    ],
    synth=synth_maintenance, params=params_maintenance, run=run_maintenance,
)


# ============================================================================
# USE CASE 2  Customer Churn Prediction
# ============================================================================
def synth_churn(n, seed):
    rng = np.random.default_rng(seed + 1)
    tenure = rng.integers(1, 73, n)
    monthly = rng.uniform(20, 120, n)
    calls = rng.poisson(2, n)
    usage = np.clip(rng.normal(40, 15, n), 1, None)
    delay = np.clip(rng.exponential(4, n), 0, 60)
    contract = rng.choice(["Monthly", "Annual", "TwoYear"], n, p=[0.55, 0.28, 0.17])
    ceff = np.select([contract == "Monthly", contract == "Annual"], [0.9, -0.6], -1.6)
    logit = (-0.6 - 0.045 * tenure + 0.018 * (monthly - 70) + 0.42 * calls - 0.02 * (usage - 40)
             + 0.05 * delay + ceff)
    churn = rng.binomial(1, sigmoid(logit))
    return pd.DataFrame({
        "customer_id": [f"CUS{i:05d}" for i in range(1, n + 1)], "tenure_months": tenure,
        "monthly_charges": monthly.round(2), "support_calls": calls, "usage_gb": usage.round(1),
        "payment_delay_days": delay.round(0), "contract_type": contract, "churned": churn,
    })


def params_churn(key):
    p = classifier_ui(key, "Gradient Boosting")
    c1, c2, c3 = st.columns(3)
    p["h"] = c1.slider("Revenue horizon in months", 3, 36, 12, key=f"{key}_h")
    p["s"] = c2.slider("Retention offer success rate", 0.05, 0.9, 0.35, 0.05, key=f"{key}_s")
    p["c"] = c3.number_input("Cost of one retention offer in USD", 0, 5000, 60, 10, key=f"{key}_c")
    return p


def run_churn(df, p):
    num = ["tenure_months", "monthly_charges", "support_calls", "usage_gb", "payment_delay_days"]
    X = encode_features(df, num, ["contract_type"])
    r = train_classifier(X, df["churned"], p["model"], p["test"], p["thr"])
    prob = r["proba_all"]
    out = df.copy()
    out["Churn Probability"] = prob.round(4)
    out["Risk Tier"] = tier(prob)
    out["Revenue At Risk USD"] = (prob * df["monthly_charges"] * p["h"]).round(2)
    out["Retention Net Value USD"] = (prob * p["s"] * df["monthly_charges"] * p["h"] - p["c"]).round(2)
    out["Recommended Action"] = np.where(
        (prob >= p["thr"]) & (out["Retention Net Value USD"] > 0), "Send personalised retention offer",
        np.where(prob >= 0.3, "Proactive service outreach", "Nurture and upsell"))
    out = out.sort_values("Churn Probability", ascending=False)
    target = out[out["Recommended Action"] == "Send personalised retention offer"]
    obs_rate = df["churned"].mean()
    clv = (df["monthly_charges"].mean() / max(obs_rate / 12, 1e-6)) if obs_rate > 0 else float("nan")

    metrics = classifier_metrics(r) + [
        ("Observed Churn Rate", pct(obs_rate), "Share of customers who left in the data"),
        ("Revenue At Risk", usd(out["Revenue At Risk USD"].sum()), f"Probability weighted over {p['h']} months"),
        ("Customers To Target", f"{len(target):,}", "High risk with positive offer value"),
        ("Campaign Net Value", usd(target["Retention Net Value USD"].sum()), "Expected saved revenue less offer cost"),
        ("Indicative CLV", usd(clv), "Average monthly charge divided by monthly churn rate"),
    ]
    tfig, counts = tier_fig(out, title="Customers by Churn Risk Tier")
    box = px.box(out, x="contract_type", y="Churn Probability", color="contract_type",
                 title="Churn Probability by Contract Type", labels={"contract_type": "Contract"})
    box.update_layout(showlegend=False)
    sc = px.scatter(out, x="tenure_months", y="monthly_charges", color="Churn Probability",
                    color_continuous_scale="RdYlGn_r", title="Tenure versus Monthly Charges Colored by Churn Risk",
                    labels={"tenure_months": "Tenure months", "monthly_charges": "Monthly charges USD"})
    figs = classifier_figs(r, "Stay", "Churn") + [
        ("Risk Tier", tfig, "Size of each churn risk group to size retention budgets."),
        ("Contract Effect", style_fig(box), "Contract commitment strongly protects against churn."),
        ("Customer Map", style_fig(sc), "New, high paying customers usually carry the highest churn risk."),
    ]
    by_contract = out.groupby("contract_type")["Churn Probability"].mean().sort_values(ascending=False)
    insights = [
        f"The leading churn driver is {r['importance'].index[0]}.",
        f"Customers on {by_contract.index[0]} contracts show the highest average churn probability at "
        f"{pct(by_contract.iloc[0])}.",
        f"Total revenue at risk over {p['h']} months is {usd(out['Revenue At Risk USD'].sum())}.",
        f"Targeting {len(target):,} customers is expected to yield a net value of "
        f"{usd(target['Retention Net Value USD'].sum())}.",
        f"The engine identifies {pct(r['recall'])} of actual churners before they leave.",
    ]
    pdf_imgs = [
        mpl_bar(r["importance"].head(8).index, r["importance"].head(8).values, "Churn Drivers",
                "Relative importance", TEAL),
        mpl_bar(by_contract.index, by_contract.values, "Average Churn Probability by Contract",
                "Probability", horizontal=False),
        mpl_hist(out["Churn Probability"], "Churn Probability Distribution", "Probability", BLUE, p["thr"]),
    ]
    cols = ["customer_id", "contract_type", "Churn Probability", "Risk Tier", "Revenue At Risk USD",
            "Recommended Action"]
    return dict(metrics=metrics, figs=figs, insights=insights, table=out, pdf_imgs=pdf_imgs, pdf_cols=cols)


UC_CHURN = dict(
    key="churn", name="Customer Churn Prediction", accent=TEAL,
    subtitle="Identify customers likely to leave and invest retention budget where it returns the most",
    description=(
        "The ASI engine studies customer behaviour, billing, service interactions and contract terms to predict "
        "the probability that each customer will cancel. It translates that probability into revenue at risk and "
        "calculates whether a retention offer is financially worthwhile for every individual customer."),
    importance=[
        "Acquiring a new customer typically costs several times more than retaining an existing one.",
        "Churn quietly erodes recurring revenue and customer lifetime value.",
        "Blanket discounts waste money on customers who would have stayed anyway.",
    ],
    benefits=[
        "Protect recurring revenue with early, targeted intervention.",
        "Spend retention budget only where the expected return is positive.",
        "Understand the root causes of churn through explainable drivers.",
        "Improve customer experience by fixing the service issues that drive departures.",
    ],
    flow=["Customer and\\nbilling data", "Validate and\\nencode fields", "Train ASI\\nchurn engine",
          "Validate on\\nunseen data", "Score churn\\nprobability", "Revenue at\\nrisk", "Offer value\\nper customer",
          "PDF TXT CSV\\nreports"],
    decision=("Customer scored", "Churn probability and\\noffer net value?",
              [("High risk and positive value", "Send personalised\\nretention offer", CORAL),
               ("Medium risk", "Proactive service\\noutreach", AMBER),
               ("Low risk", "Nurture and\\nupsell", TEAL)]),
    fields=[
        ("customer_id", "Identifier", "Optional", "Unique customer reference", "CUS00412", "Connects scores to CRM records."),
        ("tenure_months", "Numeric", "Required", "Months the customer has been active", "8",
         "New customers have not yet built loyalty and leave more often."),
        ("monthly_charges", "Numeric", "Required", "Monthly bill in USD", "89.50",
         "Higher bills raise price sensitivity and define the revenue at stake."),
        ("support_calls", "Numeric", "Required", "Support calls in the last period", "4",
         "Repeated calls signal unresolved problems and frustration."),
        ("usage_gb", "Numeric", "Required", "Product usage volume", "35.2",
         "Falling usage is an early disengagement signal."),
        ("payment_delay_days", "Numeric", "Required", "Average days late on payment", "6",
         "Payment friction often precedes cancellation."),
        ("contract_type", "Categorical", "Required", "Monthly, Annual or TwoYear", "Monthly",
         "Commitment length is one of the strongest protectors against churn."),
        ("churned", "Binary 0 or 1", "Required", "1 if the customer left", "1", "The historical outcome the engine learns from."),
    ],
    formulas=[
        ("Churn probability", r"p_i = f_{\theta}(x_i) \in [0,1]", "p = f(x)",
         "The learning engine maps each customer profile x to a probability of leaving."),
        ("Logistic form", r"p_i = \frac{1}{1 + e^{-(\beta_0 + \sum_j \beta_j x_{ij})}}",
         "p = 1 / (1 + exp(minus linear score))",
         "When Logistic Regression is selected each beta shows how a field raises or lowers churn odds."),
        ("Revenue at risk", r"RaR = \sum_i p_i \times M_i \times H", "RaR = sum of p x M x H",
         "Expected revenue lost over a horizon of H months where M is monthly charges."),
        ("Retention net value", r"V_i = p_i \times s \times M_i \times H - c", "V = p x s x M x H minus c",
         "Expected revenue saved by an offer with success rate s, less the offer cost c."),
        ("Customer lifetime value", r"CLV = \frac{\bar{M}}{c_m}", "CLV = average M / monthly churn rate",
         "Indicative value of an average customer over their expected lifetime."),
        ("ROC AUC", r"AUC = P\left(\hat{p}_{churner} > \hat{p}_{stayer}\right)", "AUC = P(churner ranks above stayer)",
         "Probability the engine ranks a random churner above a random loyal customer."),
    ],
    synth=synth_churn, params=params_churn, run=run_churn,
)


# ============================================================================
# USE CASE 3  Credit Risk Scoring
# ============================================================================
def synth_credit(n, seed):
    rng = np.random.default_rng(seed + 2)
    age = rng.integers(21, 70, n)
    income = np.clip(rng.lognormal(11, 0.45, n), 15000, 400000)
    loan = np.clip(income * rng.uniform(0.1, 0.9, n), 1000, None)
    score = np.clip(rng.normal(680, 70, n), 300, 850)
    dti = np.clip(rng.normal(0.32, 0.12, n), 0.01, 0.95)
    emp = np.clip(rng.exponential(6, n), 0, 40)
    delinq = rng.poisson(0.5, n)
    logit = (-2.4 - 0.013 * (score - 680) + 4.0 * (dti - 0.32) + 0.7 * delinq - 0.05 * emp
             + 1.2 * (loan / income - 0.5) - 0.01 * (age - 40))
    default = rng.binomial(1, sigmoid(logit))
    return pd.DataFrame({
        "applicant_id": [f"APP{i:05d}" for i in range(1, n + 1)], "age": age, "annual_income": income.round(0),
        "loan_amount": loan.round(0), "credit_score": score.round(0), "debt_to_income": dti.round(3),
        "employment_years": emp.round(1), "delinquencies": delinq, "default_flag": default,
    })


def params_credit(key):
    p = classifier_ui(key, "Logistic Regression")
    c1, c2, c3 = st.columns(3)
    p["lgd"] = c1.slider("Loss given default", 0.1, 1.0, 0.45, 0.05, key=f"{key}_lgd",
                         help="Share of the exposure that is lost if the borrower defaults.")
    p["pdo"] = c2.number_input("Points to double the odds", 10, 100, 20, 5, key=f"{key}_pdo")
    p["base"] = c3.number_input("Base score at 50 to 1 odds", 300, 900, 600, 10, key=f"{key}_base")
    return p


GRADES = [(750, "A"), (700, "B"), (650, "C"), (600, "D"), (-1e9, "E")]


def run_credit(df, p):
    num = ["age", "annual_income", "loan_amount", "credit_score", "debt_to_income", "employment_years",
           "delinquencies"]
    X = encode_features(df, num, [])
    r = train_classifier(X, df["default_flag"], p["model"], p["test"], p["thr"])
    pd_ = np.clip(r["proba_all"], 1e-4, 1 - 1e-4)
    factor = p["pdo"] / np.log(2)
    offset = p["base"] - factor * np.log(50)
    score = offset + factor * np.log((1 - pd_) / pd_)
    out = df.copy()
    out["Probability of Default"] = pd_.round(4)
    out["ASI Credit Score"] = score.round(0)
    out["Risk Grade"] = [next(g for cut, g in GRADES if s >= cut) for s in score]
    out["Expected Loss USD"] = (pd_ * p["lgd"] * df["loan_amount"]).round(2)
    out["Decision"] = np.where(pd_ >= p["thr"], "Decline", np.where(pd_ >= 0.15, "Refer to underwriter", "Approve"))
    out = out.sort_values("Probability of Default", ascending=False)
    el = out["Expected Loss USD"].sum()
    ead = df["loan_amount"].sum()
    approved = out[out["Decision"] == "Approve"]

    metrics = classifier_metrics(r) + [
        ("Portfolio Exposure", usd(ead), "Total loan amount, the exposure at default"),
        ("Expected Loss", usd(el), "Sum of PD x LGD x EAD"),
        ("Expected Loss Rate", pct(el / ead), "Expected loss divided by exposure"),
        ("Approval Rate", pct(len(approved) / len(out)), "Applications recommended for approval"),
        ("Avg Credit Score", f"{out['ASI Credit Score'].mean():.0f}", "Scaled score, higher is safer"),
    ]
    grade_tbl = out.groupby("Risk Grade").agg(Applicants=("Risk Grade", "size"),
                                               Avg_PD=("Probability of Default", "mean"),
                                               Expected_Loss=("Expected Loss USD", "sum")).reindex(list("ABCDE")).fillna(0)
    gfig = go.Figure()
    gfig.add_bar(x=grade_tbl.index, y=grade_tbl["Applicants"], name="Applicants", marker_color=BLUE)
    gfig.add_scatter(x=grade_tbl.index, y=grade_tbl["Avg_PD"], name="Average PD", yaxis="y2",
                     mode="lines+markers", line=dict(color=CORAL, width=3))
    gfig.update_layout(title="Applicants and Default Probability by Grade", xaxis_title="Risk grade",
                       yaxis_title="Applicants", yaxis2=dict(overlaying="y", side="right", title="Average PD",
                                                            tickformat=".0%"))
    hist = px.histogram(out, x="ASI Credit Score", nbins=45, color="Decision", title="Credit Score Distribution",
                        color_discrete_map={"Approve": TEAL, "Refer to underwriter": AMBER, "Decline": CORAL})
    elfig = px.bar(grade_tbl.reset_index(), x="Risk Grade", y="Expected_Loss", title="Expected Loss by Grade",
                   color="Risk Grade", color_discrete_sequence=COLORWAY, labels={"Expected_Loss": "Expected loss USD"})
    figs = classifier_figs(r, "Repaid", "Default") + [
        ("Grade Profile", style_fig(gfig), "Each grade should show steadily rising default probability."),
        ("Score Distribution", style_fig(hist), "How applicants spread across the score scale and decision bands."),
        ("Expected Loss", style_fig(elfig), "Where the credit losses are concentrated across the portfolio."),
    ]
    insights = [
        f"The most predictive risk driver is {r['importance'].index[0]}.",
        f"Portfolio expected loss is {usd(el)} or {pct(el / ead)} of exposure.",
        f"{pct(len(approved) / len(out))} of applicants qualify for automatic approval.",
        f"Grade E applicants carry an average default probability of {pct(grade_tbl.loc['E', 'Avg_PD'])}.",
        f"Every {p['pdo']} score points doubles the odds of repayment, keeping the score easy to explain.",
    ]
    pdf_imgs = [
        mpl_bar(r["importance"].head(8).index, r["importance"].head(8).values, "Credit Risk Drivers",
                "Relative importance", TEAL),
        mpl_bar(grade_tbl.index, grade_tbl["Applicants"], "Applicants by Risk Grade", "Applicants", horizontal=False),
        mpl_hist(out["ASI Credit Score"], "Credit Score Distribution", "Score", BLUE),
    ]
    cols = ["applicant_id", "Probability of Default", "ASI Credit Score", "Risk Grade", "Expected Loss USD", "Decision"]
    return dict(metrics=metrics, figs=figs, insights=insights, table=out, pdf_imgs=pdf_imgs, pdf_cols=cols)


UC_CREDIT = dict(
    key="credit", name="Credit Risk Scoring", accent=PURPLE,
    subtitle="Estimate default probability, produce an explainable credit score and quantify expected loss",
    description=(
        "The ASI engine estimates the probability that an applicant will default, converts it into a points "
        "based credit score that underwriters can explain, assigns a risk grade from A to E, computes expected "
        "loss using the Basel style formula, and recommends approve, refer or decline."),
    importance=[
        "Credit losses directly reduce profit and regulatory capital.",
        "Regulators require lending decisions that are consistent, fair and explainable.",
        "Manual underwriting is slow and varies between underwriters.",
    ],
    benefits=[
        "Faster, consistent decisions with clear reason codes.",
        "Lower default losses through accurate risk ranking.",
        "Risk based pricing and capital planning from expected loss.",
        "Higher approval rates for good applicants that rules would reject.",
    ],
    flow=["Application\\ndata", "Validate and\\nmap fields", "Train ASI\\ndefault engine", "Probability\\nof default",
          "Scale to\\ncredit score", "Grade A to E", "Expected loss\\nPD x LGD x EAD", "Decision and\\nreports"],
    decision=("Applicant scored", "Probability of\\ndefault?",
              [("At or above threshold", "Decline", CORAL),
               ("0.15 to threshold", "Refer to\\nunderwriter", AMBER),
               ("Below 0.15", "Approve", TEAL)]),
    fields=[
        ("applicant_id", "Identifier", "Optional", "Unique application reference", "APP00091", "Traceability for audit."),
        ("age", "Numeric", "Required", "Applicant age in years", "38", "Proxy for financial stability and history length."),
        ("annual_income", "Numeric", "Required", "Gross yearly income in USD", "72000", "Capacity to repay."),
        ("loan_amount", "Numeric", "Required", "Requested amount in USD, used as EAD", "25000",
         "Larger loans relative to income are harder to repay and define exposure."),
        ("credit_score", "Numeric", "Required", "Bureau score from 300 to 850", "702", "Summarises past repayment behaviour."),
        ("debt_to_income", "Numeric ratio", "Required", "Monthly debt payments divided by monthly income", "0.34",
         "High ratios leave little room to absorb shocks."),
        ("employment_years", "Numeric", "Required", "Years with current employer", "5.5", "Income stability."),
        ("delinquencies", "Numeric", "Required", "Late payments in the last two years", "1", "Recent stress indicator."),
        ("default_flag", "Binary 0 or 1", "Required", "1 if the loan defaulted", "0", "The outcome the engine learns from."),
    ],
    formulas=[
        ("Probability of default", r"PD = \frac{1}{1 + e^{-(\beta_0 + \sum_j \beta_j x_j)}}",
         "PD = 1 / (1 + exp(minus linear score))", "Logistic model output, the standard in credit scorecards."),
        ("Odds of repayment", r"Odds = \frac{1 - PD}{PD}", "Odds = (1 minus PD) / PD", "How many good loans per bad loan."),
        ("Score scaling", r"Factor = \frac{PDO}{\ln 2}, \quad Offset = S_0 - Factor \cdot \ln(50)",
         "Factor = PDO / ln 2 and Offset = S0 minus Factor x ln 50",
         "PDO is the points needed to double the odds and S0 is the score at 50 to 1 odds."),
        ("Credit score", r"Score = Offset + Factor \cdot \ln(Odds)", "Score = Offset + Factor x ln(Odds)",
         "Produces an additive, explainable score on a familiar scale."),
        ("Expected loss", r"EL = PD \times LGD \times EAD", "EL = PD x LGD x EAD",
         "Basel formula, LGD is the loss share if default occurs and EAD is the exposure at default."),
        ("Portfolio loss rate", r"EL\% = \frac{\sum_i EL_i}{\sum_i EAD_i}", "EL rate = sum EL / sum EAD",
         "Benchmark for pricing and provisioning."),
    ],
    synth=synth_credit, params=params_credit, run=run_credit,
)


# ============================================================================
# USE CASE 4  Fraud and Anomaly Detection
# ============================================================================
def synth_fraud(n, seed):
    rng = np.random.default_rng(seed + 3)
    k = max(int(n * 0.025), 5)
    m = n - k
    normal = pd.DataFrame({
        "amount_usd": np.clip(rng.lognormal(3.8, 0.8, m), 1, None), "hour_of_day": rng.choice(range(7, 23), m),
        "distance_from_home_km": np.clip(rng.exponential(12, m), 0, None), "merchant_risk": rng.beta(2, 8, m),
        "txn_last_24h": rng.poisson(3, m), "is_foreign": rng.binomial(1, 0.04, m), "is_fraud": 0,
    })
    fraud = pd.DataFrame({
        "amount_usd": np.clip(rng.lognormal(6.0, 0.7, k), 50, None), "hour_of_day": rng.choice([0, 1, 2, 3, 4, 23], k),
        "distance_from_home_km": rng.uniform(150, 3000, k), "merchant_risk": rng.beta(6, 3, k),
        "txn_last_24h": rng.poisson(11, k), "is_foreign": rng.binomial(1, 0.6, k), "is_fraud": 1,
    })
    d = pd.concat([normal, fraud]).sample(frac=1, random_state=seed).reset_index(drop=True)
    d.insert(0, "transaction_id", [f"TXN{i:06d}" for i in range(1, n + 1)])
    d["amount_usd"] = d["amount_usd"].round(2)
    d["distance_from_home_km"] = d["distance_from_home_km"].round(1)
    d["merchant_risk"] = d["merchant_risk"].round(3)
    return d


def params_fraud(key):
    c1, c2, c3 = st.columns(3)
    alpha = c1.slider("Expected anomaly share", 0.005, 0.15, 0.03, 0.005, key=f"{key}_a",
                      help="Share of transactions the engine should treat as anomalous.")
    trees = c2.slider("Number of isolation trees", 50, 500, 200, 50, key=f"{key}_t")
    review = c3.number_input("Cost to review one alert in USD", 0, 500, 15, 5, key=f"{key}_r")
    return {"alpha": alpha, "trees": trees, "review": review}


def run_fraud(df, p):
    feats = ["amount_usd", "hour_of_day", "distance_from_home_km", "merchant_risk", "txn_last_24h", "is_foreign"]
    X = df[feats].astype(float).copy()
    X["amount_usd"] = np.log1p(X["amount_usd"])
    X["night"] = X["hour_of_day"].isin([0, 1, 2, 3, 4, 5, 23]).astype(float)
    Xs = StandardScaler().fit_transform(X)
    iso = IsolationForest(n_estimators=p["trees"], contamination=p["alpha"], random_state=42)
    iso.fit(Xs)
    raw = -iso.score_samples(Xs)
    score = 100 * (raw - raw.min()) / (raw.max() - raw.min() + 1e-12)
    cut = np.quantile(score, 1 - p["alpha"])
    flag = (score >= cut).astype(int)
    out = df.copy()
    out["Anomaly Score"] = score.round(2)
    out["Flagged"] = flag
    out["Alert Level"] = np.where(score >= cut, "Block and verify",
                                  np.where(score >= np.quantile(score, 0.9), "Step up authentication", "Approve"))
    out = out.sort_values("Anomaly Score", ascending=False)
    flagged = out[out["Flagged"] == 1]
    has_label = "is_fraud" in df.columns and df["is_fraud"].notna().all()
    metrics = [
        ("Transactions", f"{len(out):,}", "Records analysed"),
        ("Alerts Raised", f"{len(flagged):,}", "Transactions above the anomaly cut off"),
        ("Alert Cut Off Score", f"{cut:.1f}", "Score at the chosen anomaly share"),
        ("Value Under Alert", usd(flagged["amount_usd"].sum()), "Money held for verification"),
        ("Review Cost", usd(len(flagged) * p["review"]), "Analyst cost to work all alerts"),
    ]
    figs = []
    insights = []
    if has_label:
        y = df.loc[out.index, "is_fraud"].astype(int)
        tp = int(((out["Flagged"] == 1) & (y == 1)).sum())
        prevented = out.loc[(out["Flagged"] == 1) & (y == 1), "amount_usd"].sum()
        prec = precision_score(y, out["Flagged"], zero_division=0)
        rec = recall_score(y, out["Flagged"], zero_division=0)
        auc = roc_auc_score(y, out["Anomaly Score"]) if y.nunique() > 1 else float("nan")
        metrics += [
            ("Precision", pct(prec), "Share of alerts that were real fraud"),
            ("Recall", pct(rec), "Share of fraud the engine caught"),
            ("ROC AUC", f"{auc:.3f}", "Ranking quality of the anomaly score"),
            ("Fraud Caught", f"{tp:,}", "True positive alerts"),
            ("Loss Prevented", usd(prevented), "Value of fraud stopped, net of review cost "
                                                f"{usd(prevented - len(flagged) * p['review'])}"),
        ]
        fpr, tpr, _ = roc_curve(y, out["Anomaly Score"])
        roc = go.Figure()
        roc.add_scatter(x=fpr, y=tpr, mode="lines", name=f"AUC {auc:.3f}", line=dict(color=BLUE, width=3),
                        fill="tozeroy", fillcolor="rgba(31,78,158,0.12)")
        roc.add_scatter(x=[0, 1], y=[0, 1], mode="lines", name="Random guess", line=dict(color=SLATE, dash="dash"))
        roc.update_layout(title="ROC Curve Against Known Fraud Labels", xaxis_title="False Positive Rate",
                          yaxis_title="True Positive Rate")
        figs.append(("ROC Curve", style_fig(roc), "Labels are used only to evaluate, never to train, so the "
                                                  "engine can find new fraud patterns nobody has labelled yet."))
        insights.append(f"The engine caught {tp:,} fraudulent transactions worth {usd(prevented)} "
                        f"with precision of {pct(prec)}.")
    else:
        insights.append("No fraud labels were supplied, so results show unsupervised alerts only. "
                        "Add an is_fraud column to measure precision and recall.")
    hist = px.histogram(out, x="Anomaly Score", nbins=60, title="Anomaly Score Distribution",
                        color_discrete_sequence=[BLUE])
    hist.add_vline(x=cut, line_dash="dash", line_color=CORAL, annotation_text="Alert cut off")
    sc = px.scatter(out, x="distance_from_home_km", y="amount_usd", color="Anomaly Score", log_y=True,
                    color_continuous_scale="RdYlGn_r", title="Amount versus Distance Colored by Anomaly Score",
                    labels={"distance_from_home_km": "Distance from home km", "amount_usd": "Amount USD"})
    hours = out.groupby("hour_of_day")["Flagged"].sum().reindex(range(24), fill_value=0)
    hb = px.bar(x=hours.index, y=hours.values, title="Alerts by Hour of Day",
                labels={"x": "Hour of day", "y": "Alerts"}, color_discrete_sequence=[CORAL])
    figs += [
        ("Score Distribution", style_fig(hist), "Most transactions score low. The long right tail holds the anomalies."),
        ("Anomaly Map", style_fig(sc), "Large amounts far from home stand out as isolated points."),
        ("Alerts by Hour", style_fig(hb), "Fraud often clusters in overnight hours when customers are asleep."),
    ]
    insights += [
        f"{len(flagged):,} transactions worth {usd(flagged['amount_usd'].sum())} are held for verification.",
        f"Flagged transactions average {usd(flagged['amount_usd'].mean())} versus "
        f"{usd(out.loc[out['Flagged'] == 0, 'amount_usd'].mean())} for normal ones.",
        f"The peak alert hour is {int(hours.idxmax())}.",
        "Isolation Forest isolates unusual records quickly, so it adapts to new attack patterns without labels.",
    ]
    pdf_imgs = [
        mpl_hist(out["Anomaly Score"], "Anomaly Score Distribution", "Score", BLUE, cut),
        mpl_bar([str(h) for h in hours.index], hours.values, "Alerts by Hour of Day", "Alerts", horizontal=False),
    ]
    cols = ["transaction_id", "amount_usd", "hour_of_day", "distance_from_home_km", "Anomaly Score", "Alert Level"]
    return dict(metrics=metrics, figs=figs, insights=insights, table=out, pdf_imgs=pdf_imgs, pdf_cols=cols)


UC_FRAUD = dict(
    key="fraud", name="Fraud and Anomaly Detection", accent=CORAL,
    subtitle="Detect suspicious transactions in real time, including fraud patterns never seen before",
    description=(
        "The ASI engine uses an Isolation Forest, an unsupervised method that isolates records which are few and "
        "different. It does not need labelled fraud to learn, so it can detect new attack patterns. Each "
        "transaction receives an anomaly score from 0 to 100 and an alert level. When fraud labels exist they are "
        "used only to measure accuracy."),
    importance=[
        "Fraud losses and chargebacks grow every year across banking, payments, insurance and retail.",
        "Fraudsters constantly change tactics, so fixed rules quickly become outdated.",
        "Too many false alarms frustrate genuine customers and overload analysts.",
    ],
    benefits=[
        "Stop fraudulent transactions before money leaves the business.",
        "Detect brand new fraud patterns without waiting for labels.",
        "Focus analysts on the highest risk alerts first.",
        "Reduce customer friction by approving normal behaviour automatically.",
    ],
    flow=["Transaction\\nstream", "Validate and\\nmap fields", "Feature\\nengineering", "Standardise\\nfeatures",
          "ASI Isolation\\nForest", "Anomaly score\\n0 to 100", "Alert level\\nrouting", "PDF TXT CSV\\nreports"],
    decision=("Transaction scored", "Anomaly score\\npercentile?",
              [("Above alert cut off", "Block and\\nverify", CORAL),
               ("Top 10 percent", "Step up\\nauthentication", AMBER),
               ("Normal range", "Approve\\ninstantly", TEAL)]),
    fields=[
        ("transaction_id", "Identifier", "Optional", "Unique transaction reference", "TXN004512", "Audit trail."),
        ("amount_usd", "Numeric", "Required", "Transaction value in USD", "1450.00",
         "Fraudsters aim to extract large amounts quickly."),
        ("hour_of_day", "Numeric 0 to 23", "Required", "Local hour the transaction occurred", "2",
         "Overnight activity is unusual for most customers."),
        ("distance_from_home_km", "Numeric", "Required", "Distance between transaction and home location", "820.5",
         "Card use far from home can indicate a stolen card."),
        ("merchant_risk", "Numeric 0 to 1", "Required", "Historical risk rating of the merchant", "0.72",
         "Some merchant categories attract more fraud."),
        ("txn_last_24h", "Numeric", "Required", "Transactions by the same card in 24 hours", "12",
         "Bursts of activity signal card testing or account takeover."),
        ("is_foreign", "Binary 0 or 1", "Required", "1 if the merchant is in another country", "1",
         "Cross border transactions carry higher risk."),
        ("is_fraud", "Binary 0 or 1", "Optional", "Confirmed fraud label", "0",
         "Used only to evaluate the engine, not to train it."),
    ],
    formulas=[
        ("Isolation anomaly score", r"s(x,n) = 2^{-\frac{E[h(x)]}{c(n)}}", "s = 2 to the power of minus E[h(x)] / c(n)",
         "h(x) is the path length needed to isolate a record. Anomalies are isolated in fewer splits, so s is close to 1."),
        ("Normalising constant", r"c(n) = 2H(n-1) - \frac{2(n-1)}{n}", "c(n) = 2H(n minus 1) minus 2(n minus 1)/n",
         "Average path length in a random tree with n records, where H is the harmonic number."),
        ("Risk score 0 to 100", r"R = 100 \times \frac{s - s_{min}}{s_{max} - s_{min}}", "R = 100 x (s minus min) / (max minus min)",
         "Rescales the anomaly score into an easy to read range."),
        ("Alert rule", r"Flag \iff R \ge Q_{1-\alpha}(R)", "Flag when R is at or above the (1 minus alpha) quantile",
         "Alpha is the expected anomaly share selected by the user."),
        ("Loss prevented", r"L = \sum_{i \in TP} amount_i - N_{alerts} \times c_r", "L = sum of caught fraud minus review cost",
         "Net financial benefit of the alerting process."),
    ],
    synth=synth_fraud, params=params_fraud, run=run_fraud,
)


# ============================================================================
# USE CASE 5  Demand Forecasting and Inventory Optimisation
# ============================================================================
def synth_demand(n, seed):
    rng = np.random.default_rng(seed + 4)
    n = max(n, 120)
    dates = pd.date_range(end=pd.Timestamp("2026-09-30"), periods=n, freq="D")
    t = np.arange(n)
    price = np.round(20 + rng.normal(0, 1.2, n) - 2 * (rng.random(n) < 0.1), 2)
    promo = rng.binomial(1, 0.12, n)
    demand = (220 + 0.12 * t + 28 * np.sin(2 * np.pi * dates.dayofweek / 7) + 45 * np.sin(2 * np.pi * dates.dayofyear / 365.25)
              - 6 * (price - 20) + 70 * promo + rng.normal(0, 14, n))
    return pd.DataFrame({"date": dates.strftime("%Y-%m-%d"), "units_sold": np.clip(demand, 0, None).round(0),
                         "unit_price": price, "promotion": promo})


def params_demand(key):
    c1, c2, c3 = st.columns(3)
    model = c1.selectbox("ASI forecasting engine", ["Seasonal Regression", "Gradient Boosting"], key=f"{key}_m")
    hold = c2.slider("Days held back for validation", 14, 120, 42, 7, key=f"{key}_ho")
    hz = c3.slider("Forecast horizon in periods", 7, 180, 60, 7, key=f"{key}_hz")
    c4, c5, c6 = st.columns(3)
    lt = c4.slider("Supplier lead time in periods", 1, 60, 10, key=f"{key}_lt")
    sl = c5.slider("Target service level", 0.80, 0.995, 0.95, 0.005, key=f"{key}_sl")
    promo_share = c6.slider("Planned promotion share in forecast", 0.0, 1.0, 0.1, 0.05, key=f"{key}_ps")
    return {"model": model, "hold": hold, "hz": hz, "lt": lt, "sl": sl, "promo_share": promo_share}


def demand_features(dates, t, price, promo):
    d = pd.DataFrame({"t": t, "price": price, "promotion": promo})
    for k in (1, 2):
        d[f"week_sin{k}"] = np.sin(2 * np.pi * k * dates.dayofweek / 7)
        d[f"week_cos{k}"] = np.cos(2 * np.pi * k * dates.dayofweek / 7)
        d[f"year_sin{k}"] = np.sin(2 * np.pi * k * dates.dayofyear / 365.25)
        d[f"year_cos{k}"] = np.cos(2 * np.pi * k * dates.dayofyear / 365.25)
    return d


def run_demand(df, p):
    d = df.copy()
    d["date"] = pd.to_datetime(d["date"])
    d = d.sort_values("date").groupby("date", as_index=False).agg(
        units_sold=("units_sold", "sum"), unit_price=("unit_price", "mean"), promotion=("promotion", "max"))
    if len(d) < 30:
        raise ValueError("At least 30 dated records are needed for forecasting.")
    hold = min(p["hold"], len(d) // 3)
    dates = pd.DatetimeIndex(d["date"])
    X = demand_features(dates, np.arange(len(d)), d["unit_price"].values, d["promotion"].values)
    y = d["units_sold"].values
    Xtr, Xte, ytr, yte = X.iloc[:-hold], X.iloc[-hold:], y[:-hold], y[-hold:]

    def make():
        return LinearRegression() if p["model"] == "Seasonal Regression" else GradientBoostingRegressor(random_state=42)

    m = make().fit(Xtr, ytr)
    pte = m.predict(Xte)
    mae = mean_absolute_error(yte, pte)
    rmse = float(np.sqrt(mean_squared_error(yte, pte)))
    mape = float(np.mean(np.abs((yte - pte) / np.where(yte == 0, 1, yte))))
    m_full = make().fit(X, y)
    sigma = float(np.std(y - m_full.predict(X), ddof=1))
    step = pd.Series(dates).diff().median()
    fdates = pd.DatetimeIndex([dates[-1] + step * (i + 1) for i in range(p["hz"])])
    rng = np.random.default_rng(7)
    fprice = np.full(p["hz"], d["unit_price"].tail(30).mean())
    fpromo = (rng.random(p["hz"]) < p["promo_share"]).astype(int)
    Xf = demand_features(fdates, np.arange(len(d), len(d) + p["hz"]), fprice, fpromo)
    fc = np.clip(m_full.predict(Xf), 0, None)
    z = NormalDist().inv_cdf(p["sl"])
    ss = z * sigma * np.sqrt(p["lt"])
    rop = fc[: p["lt"]].mean() * p["lt"] + ss
    elast = float("nan")
    if p["model"] == "Seasonal Regression":
        gamma = m_full.coef_[list(X.columns).index("price")]
        elast = gamma * d["unit_price"].mean() / max(d["units_sold"].mean(), 1e-9)
        promo_lift = m_full.coef_[list(X.columns).index("promotion")]
    else:
        base = Xf.copy()
        base["promotion"] = 0
        lift = Xf.copy()
        lift["promotion"] = 1
        promo_lift = float(np.mean(m_full.predict(lift) - m_full.predict(base)))

    out = pd.DataFrame({"date": fdates.strftime("%Y-%m-%d"), "Forecast Units": fc.round(1),
                        "Lower 95": np.clip(fc - 1.96 * sigma, 0, None).round(1),
                        "Upper 95": (fc + 1.96 * sigma).round(1), "Planned Promotion": fpromo,
                        "Planned Price": fprice.round(2)})
    metrics = [
        ("MAE", f"{mae:,.1f}", "Average absolute error in units on validation periods"),
        ("RMSE", f"{rmse:,.1f}", "Root mean squared error, penalises large misses"),
        ("MAPE", pct(mape), "Average percentage error"),
        ("Forecast Accuracy", pct(max(0, 1 - mape)), "One minus MAPE"),
        ("Total Forecast", f"{fc.sum():,.0f} units", f"Over the next {p['hz']} periods"),
        ("Safety Stock", f"{ss:,.0f} units", f"Buffer for a {pct(p['sl'])} service level"),
        ("Reorder Point", f"{rop:,.0f} units", "Order when stock falls to this level"),
        ("Promotion Lift", f"{promo_lift:,.1f} units", "Extra units per period during a promotion"),
        ("Price Elasticity", "n a" if np.isnan(elast) else f"{elast:.2f}", "Percent demand change per percent price change"),
    ]
    fig = go.Figure()
    fig.add_scatter(x=d["date"], y=y, mode="lines", name="Actual", line=dict(color=SLATE, width=1.4))
    fig.add_scatter(x=d["date"].iloc[-hold:], y=pte, mode="lines", name="Validation fit", line=dict(color=AMBER, width=2.5))
    fig.add_scatter(x=fdates, y=out["Upper 95"], mode="lines", line=dict(width=0), showlegend=False)
    fig.add_scatter(x=fdates, y=out["Lower 95"], mode="lines", line=dict(width=0), fill="tonexty",
                    fillcolor="rgba(15,157,138,0.18)", name="95 percent band")
    fig.add_scatter(x=fdates, y=fc, mode="lines", name="Forecast", line=dict(color=TEAL, width=3))
    fig.update_layout(title="Demand History, Validation and Forecast", xaxis_title="Date", yaxis_title="Units")
    dow = d.assign(day=dates.day_name()).groupby("day")["units_sold"].mean().reindex(
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    dfig = px.bar(x=dow.index, y=dow.values, title="Average Demand by Day of Week",
                  labels={"x": "", "y": "Average units"}, color_discrete_sequence=[BLUE])
    pv = px.scatter(d, x="unit_price", y="units_sold", color=d["promotion"].map({0: "No promotion", 1: "Promotion"}),
                    trendline=None, title="Price versus Units Sold", color_discrete_sequence=[BLUE, CORAL],
                    labels={"unit_price": "Unit price USD", "units_sold": "Units sold", "color": ""})
    inv = go.Figure()
    stock = rop + fc[: p["lt"]].sum()
    levels = []
    for v in fc:
        stock -= v
        if stock <= rop:
            stock += fc[: p["lt"]].sum() * 2
        levels.append(stock)
    inv.add_scatter(x=fdates, y=levels, mode="lines", name="Projected stock", line=dict(color=PURPLE, width=2.5, shape="hv"))
    inv.add_hline(y=rop, line_dash="dash", line_color=CORAL, annotation_text="Reorder point")
    inv.add_hline(y=ss, line_dash="dot", line_color=AMBER, annotation_text="Safety stock")
    inv.update_layout(title="Illustrative Inventory Policy Simulation", xaxis_title="Date", yaxis_title="Units on hand")
    figs = [
        ("Forecast", style_fig(fig, 420), "Grey is history, amber is the fit on held back periods and teal is the "
                                          "forward forecast with its 95 percent uncertainty band."),
        ("Weekly Pattern", style_fig(dfig), "Weekly seasonality learned by the engine, used for staffing and replenishment."),
        ("Price and Promotion", style_fig(pv), "Lower prices and promotions lift volume. The engine quantifies both."),
        ("Inventory Policy", style_fig(inv), "Stock is reordered at the reorder point. Safety stock absorbs forecast error."),
    ]
    insights = [
        f"Forecast accuracy on held back periods is {pct(max(0, 1 - mape))} with MAE of {mae:,.1f} units.",
        f"Expected demand over the next {p['hz']} periods is {fc.sum():,.0f} units.",
        f"Holding {ss:,.0f} units of safety stock delivers a {pct(p['sl'])} service level for a "
        f"{p['lt']} period lead time.",
        f"Place a replenishment order whenever stock falls to {rop:,.0f} units.",
        f"Promotions add about {promo_lift:,.1f} units per period. Busiest day is {dow.idxmax()}.",
    ]
    fig_m, ax = plt.subplots(figsize=(7.5, 3.4))
    ax.plot(d["date"], y, color=SLATE, lw=1, label="Actual")
    ax.plot(fdates, fc, color=TEAL, lw=2, label="Forecast")
    ax.fill_between(fdates, out["Lower 95"], out["Upper 95"], color=TEAL, alpha=0.2)
    ax.set_title("Demand History and Forecast", color=NAVY, fontweight="bold")
    ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    pdf_imgs = [mpl_png(fig_m), mpl_bar(dow.index, dow.values, "Average Demand by Day of Week", "Units", horizontal=False)]
    return dict(metrics=metrics, figs=figs, insights=insights, table=out, pdf_imgs=pdf_imgs, pdf_cols=list(out.columns))


UC_DEMAND = dict(
    key="demand", name="Demand Forecasting and Inventory", accent=AMBER,
    subtitle="Forecast future demand and set safety stock and reorder points that protect service at least cost",
    description=(
        "The ASI engine decomposes sales history into trend, weekly and yearly seasonality, price effect and "
        "promotion effect, validates itself on held back periods, and projects demand forward with an uncertainty "
        "band. It then converts forecast error into a safety stock and reorder point for the chosen service level."),
    importance=[
        "Inaccurate forecasts cause both stockouts that lose sales and overstock that ties up cash.",
        "Supply chains have lead times, so decisions must be made before demand is known.",
        "Promotions and pricing change demand and must be planned together with inventory.",
    ],
    benefits=[
        "Higher product availability and customer satisfaction.",
        "Lower inventory holding cost and less waste or obsolescence.",
        "Quantified price elasticity and promotion lift for commercial planning.",
        "Better staffing, production and procurement plans.",
    ],
    flow=["Sales history", "Validate dates\\nand fields", "Trend and\\nseasonality features", "Train ASI\\nforecast engine",
          "Validate on\\nheld back periods", "Forecast with\\nuncertainty band", "Safety stock and\\nreorder point",
          "PDF TXT CSV\\nreports"],
    decision=("Stock level checked", "Stock on hand versus\\nreorder point?",
              [("At or below reorder point", "Place replenishment\\norder now", CORAL),
               ("Near reorder point", "Prepare order and\\nconfirm supplier", AMBER),
               ("Well above", "No action\\nneeded", TEAL)]),
    fields=[
        ("date", "Date", "Required", "Period date, daily or weekly, format YYYY MM DD", "2026 09 30",
         "Anchors trend and seasonality."),
        ("units_sold", "Numeric", "Required", "Units sold in the period", "245", "The demand signal being forecast."),
        ("unit_price", "Numeric", "Required", "Average selling price in USD", "19.80", "Price drives demand through elasticity."),
        ("promotion", "Binary 0 or 1", "Required", "1 if a promotion ran in the period", "0", "Captures promotional uplift."),
    ],
    formulas=[
        ("Seasonal regression", r"\hat{y}_t = \beta_0 + \beta_1 t + \sum_{k=1}^{2}\left[a_k \sin\frac{2\pi k t}{P} + "
                                r"b_k \cos\frac{2\pi k t}{P}\right] + \gamma\, price_t + \delta\, promo_t",
         "y = trend + Fourier seasonality + gamma x price + delta x promo",
         "Fourier terms with P equal to 7 and 365 capture weekly and yearly cycles."),
        ("Mean absolute error", r"MAE = \frac{1}{n}\sum |y_t - \hat{y}_t|", "MAE = average of absolute errors",
         "Average miss in units."),
        ("Root mean squared error", r"RMSE = \sqrt{\frac{1}{n}\sum (y_t - \hat{y}_t)^2}", "RMSE = sqrt of mean squared error",
         "Penalises large misses more heavily."),
        ("Mean absolute percentage error", r"MAPE = \frac{1}{n}\sum \left|\frac{y_t - \hat{y}_t}{y_t}\right|",
         "MAPE = average of absolute percent errors", "Scale free accuracy measure."),
        ("Safety stock", r"SS = z_{\alpha}\, \sigma_e \sqrt{L}", "SS = z x sigma x sqrt(L)",
         "z is the normal quantile of the service level, sigma the forecast error and L the lead time."),
        ("Reorder point", r"ROP = \bar{d}_L \times L + SS", "ROP = average demand during lead time x L + SS",
         "Stock level that triggers a new order."),
        ("Price elasticity", r"\varepsilon = \gamma \times \frac{\bar{P}}{\bar{Q}}", "e = gamma x average price / average units",
         "Percent change in demand for a one percent change in price."),
    ],
    synth=synth_demand, params=params_demand, run=run_demand,
)


# ============================================================================
# USE CASE 6  Customer Segmentation
# ============================================================================
SEG_NAMES = ["Champions", "Loyal Customers", "Potential Loyalists", "Needs Attention", "At Risk",
             "Hibernating", "Price Sensitive", "Lost"]
SEG_ACTIONS = {"Champions": "Reward, early access and referral programs",
               "Loyal Customers": "Upsell premium tiers and loyalty points",
               "Potential Loyalists": "Membership offers and personalised recommendations",
               "Needs Attention": "Limited time offers based on past purchases",
               "At Risk": "Win back campaign with strong incentive",
               "Hibernating": "Low cost reactivation emails",
               "Price Sensitive": "Bundles and value packs",
               "Lost": "Suppress from paid campaigns, survey for feedback"}


def synth_segments(n, seed):
    rng = np.random.default_rng(seed + 5)
    centers = [(12, 30, 4200, 48, 150), (45, 14, 1600, 34, 120), (110, 5, 520, 10, 95), (260, 2, 160, 28, 70)]
    probs = [0.18, 0.30, 0.32, 0.20]
    g = rng.choice(4, n, p=probs)
    rows = []
    for gi in g:
        r_, f_, m_, t_, b_ = centers[gi]
        rows.append([max(1, rng.normal(r_, r_ * 0.18)), max(1, rng.normal(f_, f_ * 0.16)),
                     max(20, rng.normal(m_, m_ * 0.16)), max(1, rng.normal(t_, 5)), max(5, rng.normal(b_, 10))])
    a = np.array(rows)
    return pd.DataFrame({"customer_id": [f"CUS{i:05d}" for i in range(1, n + 1)], "recency_days": a[:, 0].round(0),
                         "frequency": a[:, 1].round(0), "monetary_usd": a[:, 2].round(2), "tenure_months": a[:, 3].round(0),
                         "avg_basket_usd": a[:, 4].round(2)})


def params_segments(key):
    c1, c2 = st.columns(2)
    auto = c1.checkbox("Let the ASI engine choose the best number of segments", True, key=f"{key}_auto")
    k = c2.slider("Number of segments", 2, 8, 4, key=f"{key}_k", disabled=auto)
    return {"auto": auto, "k": k}


def run_segments(df, p):
    feats = ["recency_days", "frequency", "monetary_usd", "tenure_months", "avg_basket_usd"]
    X = df[feats].astype(float)
    Xl = X.copy()
    for c in ["frequency", "monetary_usd"]:
        Xl[c] = np.log1p(Xl[c])
    Z = StandardScaler().fit_transform(Xl)
    sample = Z if len(Z) <= 4000 else Z[np.random.default_rng(0).choice(len(Z), 4000, replace=False)]
    ks = list(range(2, 9))
    inert, sils = [], []
    for k in ks:
        km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(Z)
        inert.append(km.inertia_)
        lab = km.predict(sample)
        sils.append(silhouette_score(sample, lab))
    k = ks[int(np.argmax(sils))] if p["auto"] else p["k"]
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(Z)
    lab = km.labels_
    zdf = pd.DataFrame(Z, columns=feats)
    rfm = zdf["frequency"] + zdf["monetary_usd"] - zdf["recency_days"]
    rank = pd.Series(rfm.values).groupby(lab).mean().sort_values(ascending=False)
    name_map = {c: SEG_NAMES[i] if k > 4 else ["Champions", "Loyal Customers", "Needs Attention", "At Risk"][i]
                for i, c in enumerate(rank.index)}
    out = df.copy()
    out["Segment"] = [name_map[c] for c in lab]
    out["RFM Score"] = rfm.round(3).values
    out["Recommended Action"] = out["Segment"].map(SEG_ACTIONS)
    prof = out.groupby("Segment").agg(Customers=("Segment", "size"), Recency=("recency_days", "mean"),
                                      Frequency=("frequency", "mean"), Monetary=("monetary_usd", "mean"),
                                      Tenure=("tenure_months", "mean"), Basket=("avg_basket_usd", "mean"),
                                      Revenue=("monetary_usd", "sum"))
    prof = prof.loc[[name_map[c] for c in rank.index]]
    prof["Customer Share"] = prof["Customers"] / prof["Customers"].sum()
    prof["Revenue Share"] = prof["Revenue"] / prof["Revenue"].sum()
    sil = silhouette_score(sample, km.predict(sample))
    pcs = PCA(n_components=2, random_state=42).fit_transform(Z)
    out["PC1"], out["PC2"] = pcs[:, 0].round(3), pcs[:, 1].round(3)
    top = prof.index[0]
    metrics = [
        ("Customers", f"{len(out):,}", "Records segmented"),
        ("Segments", f"{k}", "Chosen automatically" if p["auto"] else "Chosen by user"),
        ("Silhouette Score", f"{sil:.3f}", "Separation quality from minus 1 to 1, higher is better"),
        (f"{top} Share", pct(prof.loc[top, "Customer Share"]), "Share of customers in the top segment"),
        (f"{top} Revenue", pct(prof.loc[top, "Revenue Share"]), "Share of revenue from the top segment"),
    ]
    elbow = go.Figure()
    elbow.add_scatter(x=ks, y=inert, mode="lines+markers", name="Inertia", line=dict(color=BLUE, width=3))
    elbow.add_scatter(x=ks, y=sils, mode="lines+markers", name="Silhouette", yaxis="y2", line=dict(color=CORAL, width=3))
    elbow.add_vline(x=k, line_dash="dash", line_color=TEAL, annotation_text="Selected")
    elbow.update_layout(title="Elbow and Silhouette Analysis", xaxis_title="Number of segments", yaxis_title="Inertia",
                        yaxis2=dict(overlaying="y", side="right", title="Silhouette"))
    scat = px.scatter(out, x="PC1", y="PC2", color="Segment", title="Segment Map in Two Principal Components",
                      hover_data=["customer_id", "monetary_usd"], opacity=0.75, color_discrete_sequence=COLORWAY)
    share = prof[["Customer Share", "Revenue Share"]].reset_index().melt(id_vars="Segment", var_name="Measure",
                                                                         value_name="Share")
    sb = px.bar(share, x="Segment", y="Share", color="Measure", barmode="group", title="Customer Share versus Revenue Share",
                color_discrete_sequence=[BLUE, AMBER])
    sb.update_yaxes(tickformat=".0%")
    norm = prof[["Recency", "Frequency", "Monetary", "Tenure", "Basket"]]
    norm = (norm - norm.min()) / (norm.max() - norm.min() + 1e-9)
    radar = go.Figure()
    for i, (seg, row) in enumerate(norm.iterrows()):
        radar.add_scatterpolar(r=list(row.values) + [row.values[0]], theta=list(norm.columns) + [norm.columns[0]],
                               name=seg, fill="toself", opacity=0.55, line=dict(color=COLORWAY[i % 8]))
    radar.update_layout(title="Segment Profiles", polar=dict(radialaxis=dict(visible=True, range=[0, 1])))
    figs = [
        ("Segment Map", style_fig(scat, 420), "Each point is a customer. Clear, separated clouds indicate distinct segments."),
        ("Choosing K", style_fig(elbow), "The engine tests 2 to 8 segments and picks the highest silhouette score."),
        ("Value Concentration", style_fig(sb), "Shows which segments generate revenue out of proportion to their size."),
        ("Profiles", style_fig(radar, 440), "Normalised behaviour of each segment across all five fields."),
    ]
    insights = [f"{k} distinct segments were found with a silhouette score of {sil:.3f}."]
    for seg in prof.index[:3]:
        insights.append(f"{seg} hold {pct(prof.loc[seg, 'Customer Share'])} of customers and generate "
                        f"{pct(prof.loc[seg, 'Revenue Share'])} of revenue. Action: {SEG_ACTIONS[seg]}.")
    insights.append(f"Lowest value segment is {prof.index[-1]}. Action: {SEG_ACTIONS[prof.index[-1]]}.")
    pdf_imgs = [
        mpl_bar(prof.index, prof["Customers"], "Customers by Segment", "Customers", horizontal=False),
        mpl_bar(prof.index, prof["Revenue"], "Revenue by Segment in USD", "USD", horizontal=False),
    ]
    fig_m, ax = plt.subplots(figsize=(7.5, 4))
    for i, seg in enumerate(prof.index):
        s = out[out["Segment"] == seg]
        ax.scatter(s["PC1"], s["PC2"], s=8, alpha=0.6, color=COLORWAY[i % 8], label=seg)
    ax.legend(frameon=False, fontsize=8)
    ax.set_title("Segment Map", color=NAVY, fontweight="bold")
    pdf_imgs.insert(0, mpl_png(fig_m))
    out = out.drop(columns=["PC1", "PC2"]).sort_values("RFM Score", ascending=False)
    cols = ["customer_id", "Segment", "RFM Score", "monetary_usd", "frequency", "Recommended Action"]
    return dict(metrics=metrics, figs=figs, insights=insights, table=out, pdf_imgs=pdf_imgs, pdf_cols=cols,
                extra_table=prof.round(3).reset_index())


UC_SEGMENTS = dict(
    key="seg", name="Customer Segmentation", accent="#2BB3D9",
    subtitle="Discover natural customer groups and tailor marketing, service and pricing to each one",
    description=(
        "The ASI engine groups customers by behaviour using recency, frequency, monetary value, tenure and basket "
        "size. It standardises the fields, tests several segment counts, selects the best one using the silhouette "
        "score, names each segment by value, and recommends the right action for each group."),
    importance=[
        "One size fits all marketing wastes budget and under serves the best customers.",
        "A small share of customers usually generates a large share of revenue.",
        "Segments give every team a shared language for who the customers are.",
    ],
    benefits=[
        "Higher campaign response and conversion through targeted messages.",
        "Protect and grow the most valuable customers.",
        "Re-activate lapsing customers before they are lost.",
        "Smarter product, pricing and service design per segment.",
    ],
    flow=["Customer\\ntransactions", "Validate and\\nmap fields", "Log transform\\nand standardise",
          "Test 2 to 8\\nsegments", "Select K by\\nsilhouette", "ASI K Means\\nclustering", "Name and profile\\nsegments",
          "PDF TXT CSV\\nreports"],
    decision=("Segment assigned", "Segment value\\nlevel?",
              [("Top value", "Reward and\\nretain", TEAL), ("Middle value", "Grow with\\nupsell", BLUE),
               ("Declining", "Win back\\ncampaign", AMBER), ("Lapsed", "Low cost\\nreactivation", CORAL)]),
    fields=[
        ("customer_id", "Identifier", "Optional", "Unique customer reference", "CUS01234", "Links segment to CRM."),
        ("recency_days", "Numeric", "Required", "Days since last purchase", "21", "Recent buyers are more likely to buy again."),
        ("frequency", "Numeric", "Required", "Number of purchases in the period", "14", "Habit and engagement."),
        ("monetary_usd", "Numeric", "Required", "Total spend in USD", "1850.00", "Customer value."),
        ("tenure_months", "Numeric", "Required", "Months since first purchase", "30", "Relationship maturity."),
        ("avg_basket_usd", "Numeric", "Required", "Average order value in USD", "132.10", "Spending style and price tier."),
    ],
    formulas=[
        ("Standardisation", r"z = \frac{x - \mu}{\sigma}", "z = (x minus mean) / standard deviation",
         "Puts every field on the same scale so no single field dominates."),
        ("K Means objective", r"\min_{C_1..C_K} \sum_{k=1}^{K}\sum_{x \in C_k} \lVert x - \mu_k \rVert^2",
         "Minimise total squared distance to segment centres", "Groups customers so members are as similar as possible."),
        ("Silhouette score", r"s(i) = \frac{b(i) - a(i)}{\max\{a(i), b(i)\}}", "s = (b minus a) / max(a, b)",
         "a is the distance to the own segment and b the distance to the nearest other segment."),
        ("RFM value score", r"RFM = z_F + z_M - z_R", "RFM = zF + zM minus zR",
         "Ranks segments from most to least valuable, recency counts negatively."),
        ("Revenue share", r"RS_k = \frac{\sum_{i \in C_k} M_i}{\sum_i M_i}", "Revenue share = segment revenue / total",
         "Shows concentration of value."),
    ],
    synth=synth_segments, params=params_segments, run=run_segments,
)

USE_CASES = [UC_MAINTENANCE, UC_CHURN, UC_CREDIT, UC_FRAUD, UC_DEMAND, UC_SEGMENTS]


# ----------------------------------------------------------------------------
# Data loading and field mapping
# ----------------------------------------------------------------------------
def norm(s):
    return "".join(ch for ch in str(s).lower() if ch.isalnum())


def read_upload(file):
    name = file.name.lower()
    if name.endswith((".xlsx", ".xls")):
        return pd.read_excel(file)
    if name.endswith(".txt") or name.endswith(".tsv"):
        return pd.read_csv(file, sep=None, engine="python")
    return pd.read_csv(file)


def prepare_data(uc, raw, mapping):
    out = pd.DataFrame(index=raw.index)
    id_field = uc["fields"][0][0]
    for fname, ftype, req, *_ in uc["fields"]:
        src = mapping.get(fname)
        if src is None:
            if fname == id_field:
                out[fname] = [f"REC{i:06d}" for i in range(1, len(raw) + 1)]
            continue
        col = raw[src]
        if ftype.startswith("Binary"):
            out[fname] = to_binary(col)
        elif ftype.startswith("Numeric"):
            out[fname] = pd.to_numeric(col, errors="coerce")
        elif ftype == "Date":
            out[fname] = pd.to_datetime(col, errors="coerce")
        else:
            out[fname] = col.astype(str)
    req_cols = [f[0] for f in uc["fields"] if f[0] in out.columns and f[1] != "Identifier"]
    before = len(out)
    out = out.dropna(subset=req_cols).reset_index(drop=True)
    return out, before - len(out)


def data_section(uc):
    key = uc["key"]
    st.markdown('<div class="section-title">Step 1 Choose the data source</div>', unsafe_allow_html=True)
    src = st.radio("Data source", ["Synthetic demonstration data", "Upload real data"], horizontal=True,
                   key=f"{key}_src", label_visibility="collapsed")
    if src.startswith("Synthetic"):
        c1, c2 = st.columns(2)
        n = c1.slider("Number of synthetic records", 200, 20000, 2000, 100, key=f"{key}_n")
        seed = c2.number_input("Random seed for reproducibility", 0, 99999, 42, key=f"{key}_seed")
        df = uc["synth"](n, int(seed))
        st.markdown(f'<div class="explain">Synthetic data is generated with realistic statistical relationships '
                    f'between fields so the engine can demonstrate the full workflow. {len(df):,} records are '
                    f'ready.</div>', unsafe_allow_html=True)
        return df, f"Synthetic data, {len(df):,} records, seed {seed}"

    template = uc["synth"](50, 1)
    c1, c2 = st.columns([3, 1])
    up = c1.file_uploader("Upload a CSV, TXT or Excel file", type=["csv", "txt", "tsv", "xlsx", "xls"], key=f"{key}_up")
    c2.markdown("<br>", unsafe_allow_html=True)
    c2.download_button("Download data template", template.to_csv(index=False).encode(), f"{key}_template.csv",
                       "text/csv", key=f"{key}_tpl", width="stretch")
    if up is None:
        st.info("Upload a file to continue. The template shows the expected layout. Column names do not need to "
                "match because you can map them in the next step.")
        return None, None
    try:
        raw = read_upload(up)
    except Exception as e:  # noqa: BLE001
        st.error(f"The file could not be read. Details: {e}")
        return None, None
    st.success(f"Loaded {len(raw):,} rows and {raw.shape[1]} columns from {up.name}.")
    with st.expander("Preview uploaded data", expanded=False):
        st.dataframe(raw.head(20), width="stretch")
    st.markdown('<div class="section-title">Step 2 Map your columns to the required fields</div>', unsafe_allow_html=True)
    cols = list(raw.columns)
    lookup = {norm(c): c for c in cols}
    mapping = {}
    grid = st.columns(3)
    for i, (fname, ftype, req, desc, *_r) in enumerate(uc["fields"]):
        opts = ["Not available"] + cols
        default = lookup.get(norm(fname))
        idx = opts.index(default) if default in opts else 0
        sel = grid[i % 3].selectbox(f"{fname}  ({req})", opts, index=idx, key=f"{key}_map_{fname}", help=desc)
        mapping[fname] = None if sel == "Not available" else sel
    missing = [f[0] for f in uc["fields"] if f[2] == "Required" and mapping.get(f[0]) is None]
    if missing:
        st.warning("Please map these required fields: " + ", ".join(missing))
        return None, None
    df, dropped = prepare_data(uc, raw, mapping)
    if dropped:
        st.warning(f"{dropped:,} rows had missing or invalid values in required fields and were excluded.")
    if len(df) < 30:
        st.error("Fewer than 30 valid rows remain. Please check the mapping and data quality.")
        return None, None
    return df, f"Uploaded file {up.name}, {len(df):,} valid records"


# ----------------------------------------------------------------------------
# Reports
# ----------------------------------------------------------------------------
def latin(s):
    return str(s).encode("latin-1", "replace").decode("latin-1")


class ReportPDF(FPDF):
    def header(self):
        self.set_fill_color(11, 31, 68)
        self.rect(0, 0, 210, 18, "F")
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 13)
        self.set_xy(10, 5)
        self.cell(0, 8, latin(APP_TITLE))
        self.ln(16)

    def footer(self):
        self.set_y(-13)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(91, 107, 130)
        self.cell(0, 8, latin(f"{DEVELOPER}    Page {self.page_no()} of {{nb}}"), align="C")


def pdf_section(pdf, title):
    pdf.ln(3)
    pdf.set_font("Helvetica", "B", 12.5)
    pdf.set_text_color(31, 78, 158)
    pdf.cell(0, 8, latin(title), new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(31, 78, 158)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(36, 50, 74)


def pdf_text(pdf, text):
    pdf.multi_cell(0, 5.4, latin(text), new_x="LMARGIN", new_y="NEXT")


def pdf_table(pdf, df, widths=None, max_rows=30):
    df = df.head(max_rows)
    n = len(df.columns)
    widths = widths or [190 / n] * n
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_fill_color(31, 78, 158)
    pdf.set_text_color(255, 255, 255)
    for c, w in zip(df.columns, widths):
        pdf.cell(w, 7, latin(str(c))[:32], border=0, fill=True, align="C")
    pdf.ln()
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(36, 50, 74)
    for i, (_, row) in enumerate(df.iterrows()):
        pdf.set_fill_color(242, 246, 253) if i % 2 == 0 else pdf.set_fill_color(255, 255, 255)
        for v, w in zip(row.values, widths):
            if isinstance(v, (float, np.floating)):
                v = f"{v:,.4f}" if abs(v) < 1 else f"{v:,.2f}"
            pdf.cell(w, 6, latin(str(v))[: int(w / 1.6)], border=0, fill=True, align="C")
        pdf.ln()


def build_pdf(uc, res, data_info):
    pdf = ReportPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(True, margin=16)
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 19)
    pdf.set_text_color(11, 31, 68)
    pdf.cell(0, 10, latin(f"{uc['name']} Report"), new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 71, 255)
    pdf.cell(0, 7, latin(DEVELOPER), new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(91, 107, 130)
    pdf.cell(0, 6, latin(f"Generated {dt.datetime.now():%B %d, %Y at %H:%M}    Data source {data_info}"),
             new_x="LMARGIN", new_y="NEXT")

    pdf_section(pdf, "Executive Summary")
    pdf_text(pdf, uc["description"])
    pdf_section(pdf, "Why It Matters")
    for i, t in enumerate(uc["importance"], 1):
        pdf_text(pdf, f"{i}. {t}")
    pdf_section(pdf, "Business Benefits")
    for i, t in enumerate(uc["benefits"], 1):
        pdf_text(pdf, f"{i}. {t}")
    pdf_section(pdf, "Key Results")
    mt = pd.DataFrame(res["metrics"], columns=["Measure", "Value", "Meaning"])
    pdf_table(pdf, mt, [45, 40, 105], 40)
    pdf_section(pdf, "Key Insights")
    for i, t in enumerate(res["insights"], 1):
        pdf_text(pdf, f"{i}. {t}")
    pdf_section(pdf, "Analysis Workflow")
    steps = [s.replace("\\n", " ") for s in uc["flow"]]
    pdf_text(pdf, "  then  ".join(steps))
    pdf_section(pdf, "Formulas Applied")
    for name, _ltx, plain, expl in uc["formulas"]:
        pdf.set_font("Helvetica", "B", 10)
        pdf_text(pdf, f"{name}:  {plain}")
        pdf.set_font("Helvetica", "", 9.5)
        pdf_text(pdf, expl)
    pdf.add_page()
    pdf_section(pdf, "Charts")
    for img in res["pdf_imgs"]:
        if pdf.get_y() > 190:
            pdf.add_page()
        pdf.image(io.BytesIO(img), w=175, x=17)
        pdf.ln(3)
    if "extra_table" in res:
        pdf.add_page()
        pdf_section(pdf, "Segment Profile")
        pdf_table(pdf, res["extra_table"].iloc[:, :8])
    pdf.add_page()
    pdf_section(pdf, "Top Records")
    pdf_table(pdf, res["table"][res["pdf_cols"]], max_rows=35)
    pdf_section(pdf, "Field Dictionary")
    fd = pd.DataFrame([(f[0], f[1], f[2], f[3]) for f in uc["fields"]], columns=["Field", "Type", "Status", "Description"])
    pdf_table(pdf, fd, [40, 28, 22, 100], 20)
    return bytes(pdf.output())


def build_txt(uc, res, data_info):
    lines = [APP_TITLE, DEVELOPER, "", f"{uc['name']} Report", f"Generated {dt.datetime.now():%B %d, %Y %H:%M}",
             f"Data source {data_info}", "", "SUMMARY", uc["description"], "", "KEY RESULTS"]
    lines += [f"  {m[0]:<28}{m[1]:<22}{m[2]}" for m in res["metrics"]]
    lines += ["", "KEY INSIGHTS"] + [f"  {i}. {t}" for i, t in enumerate(res["insights"], 1)]
    lines += ["", "FORMULAS"] + [f"  {f[0]}: {f[2]}" for f in uc["formulas"]]
    lines += ["", "TOP RECORDS", res["table"][res["pdf_cols"]].head(25).to_string(index=False)]
    return "\n".join(lines).encode("utf-8")


# ----------------------------------------------------------------------------
# Page renderers
# ----------------------------------------------------------------------------
def kpi_grid(metrics, accent):
    per_row = 5
    for i in range(0, len(metrics), per_row):
        cols = st.columns(per_row)
        for c, (label, value, help_) in zip(cols, metrics[i:i + per_row]):
            c.markdown(f'<div class="kpi" style="--accent:{accent}"><div class="label">{label}</div>'
                       f'<div class="value">{value}</div><div class="help">{help_}</div></div>',
                       unsafe_allow_html=True)
        st.write("")


def download_row(uc, res, info, suffix):
    key = uc["key"]
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M")
    c1, c2, c3 = st.columns(3)
    c1.download_button("Download PDF report", build_pdf(uc, res, info), f"{key}_report_{stamp}.pdf",
                       "application/pdf", key=f"{key}_pdf_{suffix}", type="primary", width="stretch")
    c2.download_button("Download TXT summary", build_txt(uc, res, info), f"{key}_summary_{stamp}.txt",
                       "text/plain", key=f"{key}_txt_{suffix}", width="stretch")
    c3.download_button("Download CSV results", res["table"].to_csv(index=False).encode(), f"{key}_results_{stamp}.csv",
                       "text/csv", key=f"{key}_csv_{suffix}", width="stretch")


def render_use_case(uc):
    key, accent = uc["key"], uc["accent"]
    st.markdown(f'<div class="uc-header" style="--accent:{accent}"><h2>{uc["name"]}</h2><p>{uc["subtitle"]}</p></div>',
                unsafe_allow_html=True)
    t1, t2, t3, t4, t5, t6 = st.tabs(["Overview", "Workflow and Flow Charts", "Field Guide", "Formulas",
                                      "Data and Analysis", "Reports"])
    with t1:
        st.markdown(f'<div class="explain">{uc["description"]}</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="section-title">Why this use case is important</div>', unsafe_allow_html=True)
            for t in uc["importance"]:
                st.markdown(f'<div class="insight" style="border-left-color:{CORAL}">{t}</div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="section-title">Business benefits</div>', unsafe_allow_html=True)
            for t in uc["benefits"]:
                st.markdown(f'<div class="insight">{t}</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">How to use this module</div>', unsafe_allow_html=True)
        st.markdown('<div class="explain">1. Read the Workflow, Field Guide and Formulas tabs to understand the '
                    'method. 2. Open Data and Analysis, choose synthetic data or upload your own file and map the '
                    'columns. 3. Adjust the engine settings and press Run ASI Analysis. 4. Review the indicators, '
                    'charts and insights. 5. Download the PDF, TXT and CSV outputs from the Reports tab.</div>',
                    unsafe_allow_html=True)
    with t2:
        st.markdown('<div class="section-title">End to end analytical workflow</div>', unsafe_allow_html=True)
        st.graphviz_chart(flow_dot(uc["flow"]), width="stretch")
        st.markdown('<div class="explain">Data enters on the left, is validated and mapped to standard fields, '
                    'processed by the ASI engine, validated on unseen data, converted into business measures and '
                    'finally delivered as dashboards and downloadable reports.</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Decision flow chart</div>', unsafe_allow_html=True)
        c1, c2 = st.columns([3, 2])
        with c1:
            st.graphviz_chart(decision_dot(*uc["decision"]), width="stretch")
        with c2:
            st.markdown('<div class="explain">The decision flow shows how every scored record is routed to a '
                        'concrete business action. Thresholds can be tuned in the Data and Analysis tab to match '
                        'your risk appetite and operating capacity.</div>', unsafe_allow_html=True)
    with t3:
        st.markdown('<div class="section-title">Field dictionary</div>', unsafe_allow_html=True)
        fd = pd.DataFrame(uc["fields"], columns=["Field", "Data Type", "Status", "Description", "Example",
                                                 "Why It Matters"])
        st.dataframe(fd, width="stretch", hide_index=True)
        st.markdown('<div class="explain">Required fields must be present to run the engine. Optional identifier '
                    'fields are generated automatically when missing. Binary fields accept 0 and 1, Yes and No, or '
                    'True and False.</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Engine settings explained</div>', unsafe_allow_html=True)
        st.markdown(SETTINGS_HELP.get(key, ""), unsafe_allow_html=True)
    with t4:
        st.markdown('<div class="section-title">Formulas and their meaning</div>', unsafe_allow_html=True)
        for name, ltx, plain, expl in uc["formulas"]:
            st.markdown(f'<div class="formula-name">{name}</div>', unsafe_allow_html=True)
            st.latex(ltx)
            st.markdown(f'<div class="explain">{expl}</div>', unsafe_allow_html=True)
    with t5:
        df, info = data_section(uc)
        if df is not None:
            with st.expander("Preview analysis ready data", expanded=False):
                st.dataframe(df.head(50), width="stretch")
            st.markdown('<div class="section-title">Step 3 Configure the ASI engine</div>', unsafe_allow_html=True)
            params = uc["params"](key)
            st.markdown('<div class="section-title">Step 4 Run the analysis</div>', unsafe_allow_html=True)
            if st.button("Run ASI Analysis", type="primary", key=f"{key}_run", width="stretch"):
                with st.spinner("The ASI engine is learning from your data"):
                    try:
                        st.session_state[f"res_{key}"] = (uc["run"](df, params), info)
                    except Exception as e:  # noqa: BLE001
                        st.session_state.pop(f"res_{key}", None)
                        st.error(f"The analysis could not complete. Details: {e}")
        stored = st.session_state.get(f"res_{key}")
        if stored:
            res, rinfo = stored
            st.markdown('<div class="section-title">Key performance indicators</div>', unsafe_allow_html=True)
            kpi_grid(res["metrics"], accent)
            st.markdown('<div class="section-title">ASI insights</div>', unsafe_allow_html=True)
            for t in res["insights"]:
                st.markdown(f'<div class="insight" style="border-left-color:{accent}">{t}</div>', unsafe_allow_html=True)
            st.markdown('<div class="section-title">Visual analysis</div>', unsafe_allow_html=True)
            for i in range(0, len(res["figs"]), 2):
                cols = st.columns(2)
                for c, (title, fig, cap) in zip(cols, res["figs"][i:i + 2]):
                    with c:
                        st.plotly_chart(fig, width="stretch", key=f"{key}_fig_{i}_{title}")
                        st.caption(cap)
            if "extra_table" in res:
                st.markdown('<div class="section-title">Segment profile table</div>', unsafe_allow_html=True)
                st.dataframe(res["extra_table"], width="stretch", hide_index=True)
            st.markdown('<div class="section-title">Detailed results</div>', unsafe_allow_html=True)
            st.dataframe(res["table"].head(500), width="stretch", hide_index=True)
            st.markdown('<div class="section-title">Export results</div>', unsafe_allow_html=True)
            download_row(uc, res, rinfo, "a")
    with t6:
        stored = st.session_state.get(f"res_{key}")
        st.markdown('<div class="section-title">Report center</div>', unsafe_allow_html=True)
        if not stored:
            st.info("Run the analysis in the Data and Analysis tab to enable report downloads.")
        else:
            res, rinfo = stored
            st.markdown('<div class="explain">The PDF report contains the executive summary, importance, benefits, '
                        'key results, insights, workflow, formulas, charts, top records and field dictionary. The '
                        'TXT file is a plain summary for email or ticketing systems. The CSV file contains every '
                        'scored record for use in Excel, BI tools or downstream systems.</div>', unsafe_allow_html=True)
            st.write("")
            download_row(uc, res, rinfo, "b")
            st.markdown('<div class="section-title">Summary preview</div>', unsafe_allow_html=True)
            st.code(build_txt(uc, res, rinfo).decode()[:4000], language=None)


SETTINGS_HELP = {
    k: ('<div class="explain"><b>ASI learning engine</b> selects the algorithm. <b>Validation share</b> is the portion '
        'of data held back to test accuracy honestly. <b>Alert probability threshold</b> controls how cautious the '
        'engine is: a lower threshold catches more cases but raises more false alarms.' + extra + '</div>')
    for k, extra in {
        "maint": " <b>Cost of failure</b> and <b>cost of service</b> convert probabilities into money and set the break "
                 "even probability.",
        "churn": " <b>Revenue horizon</b> is the number of months of revenue at stake. <b>Offer success rate</b> is the "
                 "share of at risk customers an offer retains. <b>Offer cost</b> is the cost per customer contacted.",
        "credit": " <b>Loss given default</b> is the share of exposure lost after recovery. <b>Points to double the "
                  "odds</b> and <b>base score</b> scale probability into a familiar credit score.",
    }.items()
}
SETTINGS_HELP["fraud"] = ('<div class="explain"><b>Expected anomaly share</b> sets how many transactions are flagged. '
                          '<b>Number of isolation trees</b> increases stability. <b>Review cost</b> is the analyst '
                          'cost per alert used to compute net loss prevented.</div>')
SETTINGS_HELP["demand"] = ('<div class="explain"><b>Forecasting engine</b> chooses a transparent seasonal regression or '
                           'a flexible gradient boosting model. <b>Validation periods</b> are held back to measure '
                           'accuracy. <b>Horizon</b> is how far ahead to forecast. <b>Lead time</b> and <b>service '
                           'level</b> set safety stock and reorder point. <b>Promotion share</b> is the planned share of '
                           'forecast periods with a promotion.</div>')
SETTINGS_HELP["seg"] = ('<div class="explain"><b>Automatic selection</b> tests 2 to 8 segments and keeps the one with the '
                        'highest silhouette score. Switch it off to set the number of segments manually.</div>')


def render_home():
    st.markdown(f'<div class="uc-header" style="--accent:{BLUE}"><h2>Platform Overview</h2>'
                f'<p>Six production style ASI use cases in one secure, explainable workspace</p></div>',
                unsafe_allow_html=True)
    st.markdown('<div class="explain">Artificial Super Intelligence, or ASI, describes intelligence that learns, '
                'reasons and decides across many domains at once. This platform applies that idea to enterprise '
                'decisions: one shared intelligence layer learns from data, validates itself, explains its reasoning, '
                'quantifies the financial impact of every recommendation and delivers board ready reports. Each '
                'module on the left is a complete use case with explanations, flow charts, synthetic data, real data '
                'upload, interactive charts and PDF, TXT and CSV exports.</div>', unsafe_allow_html=True)
    st.write("")
    for row in (USE_CASES[:3], USE_CASES[3:]):
        cols = st.columns(3)
        for c, uc in zip(cols, row):
            c.markdown(f'<div class="card" style="--accent:{uc["accent"]}"><h4>{uc["name"]}</h4>'
                       f'<p>{uc["subtitle"]}</p></div>', unsafe_allow_html=True)
        st.write("")
    st.markdown('<div class="section-title">Platform architecture</div>', unsafe_allow_html=True)
    arch = f"""
    digraph A {{
      rankdir=LR; bgcolor="transparent"; nodesep=0.3; ranksep=0.55;
      node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, penwidth=1.6, fontcolor="#0B1F44"];
      edge [color="#5B6B82", penwidth=1.4];
      subgraph cluster_in {{ label="Data Layer"; fontname="Helvetica-Bold"; color="{SLATE}"; style="rounded,dashed";
        syn [label="Synthetic data\\ngenerator", fillcolor="#E8F0FE", color="{BLUE}"];
        up [label="Real data upload\\nCSV TXT Excel", fillcolor="#E8F0FE", color="{BLUE}"]; }}
      val [label="Validation and\\nfield mapping", fillcolor="#FFF4E0", color="{AMBER}"];
      subgraph cluster_asi {{ label="ASI Intelligence Layer"; fontname="Helvetica-Bold"; color="{TEAL}"; style="rounded";
        ml [label="Supervised learning\\nForest Boosting Logistic", fillcolor="#E3F6F3", color="{TEAL}"];
        un [label="Unsupervised learning\\nIsolation Forest K Means", fillcolor="#E3F6F3", color="{TEAL}"];
        ts [label="Time series\\nforecasting", fillcolor="#E3F6F3", color="{TEAL}"]; }}
      xai [label="Explainability and\\nfinancial impact", fillcolor="#EFEAFA", color="{PURPLE}"];
      subgraph cluster_out {{ label="Delivery Layer"; fontname="Helvetica-Bold"; color="{SLATE}"; style="rounded,dashed";
        dash [label="Interactive\\ndashboards", fillcolor="#FDE9E4", color="{CORAL}"];
        rep [label="PDF TXT CSV\\nreports", fillcolor="#FDE9E4", color="{CORAL}"]; }}
      syn -> val; up -> val; val -> ml; val -> un; val -> ts; ml -> xai; un -> xai; ts -> xai; xai -> dash; xai -> rep;
    }}"""
    st.graphviz_chart(arch, width="stretch")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="section-title">How every module works</div>', unsafe_allow_html=True)
        for i, t in enumerate(["Learn the use case in Overview, Workflow, Field Guide and Formulas.",
                               "Choose synthetic data or upload your own file and map the columns.",
                               "Tune the engine settings to your business economics.",
                               "Run the analysis and review indicators, charts and insights.",
                               "Download PDF, TXT and CSV outputs for stakeholders."], 1):
            st.markdown(f'<div class="insight" style="border-left-color:{BLUE}"><b>Step {i}</b>  {t}</div>',
                        unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="section-title">Platform capabilities</div>', unsafe_allow_html=True)
        cap = pd.DataFrame({
            "Use Case": [u["name"] for u in USE_CASES],
            "ASI Engine": ["Random Forest", "Gradient Boosting", "Logistic Scorecard", "Isolation Forest",
                           "Seasonal Regression", "K Means"],
            "Primary Output": ["Health Index", "Revenue at risk", "Credit score and EL", "Anomaly score",
                               "Forecast and reorder point", "Named segments"],
        })
        st.dataframe(cap, width="stretch", hide_index=True)


# ----------------------------------------------------------------------------
# Main layout
# ----------------------------------------------------------------------------
def main():
    st.markdown(CSS, unsafe_allow_html=True)
    st.markdown(f'<div class="app-banner"><div class="app-title">{APP_TITLE}</div>'
                f'<div class="app-tagline">{APP_TAGLINE}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="dev-line">{DEVELOPER}</div>', unsafe_allow_html=True)

    with st.sidebar:
        st.markdown('<div class="side-brand">KNet ASI Platform</div>'
                    '<div class="side-sub">Select a use case</div>', unsafe_allow_html=True)
        pages = ["Platform Home"] + [u["name"] for u in USE_CASES]
        choice = st.radio("Navigation", pages, label_visibility="collapsed", key="nav")
        st.markdown("---")
        st.markdown('<div class="side-sub">Kalsnet (KNet) Consulting Group<br>Version 1.0  October 2026</div>',
                    unsafe_allow_html=True)

    if choice == "Platform Home":
        render_home()
    else:
        render_use_case(next(u for u in USE_CASES if u["name"] == choice))


main()

