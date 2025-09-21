

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import io, datetime, base64

# ---------- Page setup ----------
st.set_page_config(page_title="Coke vs Pepsi — Advanced Investment Analyzer", layout="wide")

# ---------- Custom CSS for GUI colors ----------
st.markdown("""
    <style>
        body {background-color: #f7f9fc;}
        .stApp {background-color: #f7f9fc;}
        h1, h2, h3 {color: #0b6fb0;}
        .css-1d391kg, .css-18e3th9 {background-color: #e8f1fa;}
        .stButton>button {
            background-color: #0b6fb0;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #084c77;
            color: #fff;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Helper functions ----------
def fetch_company_data(ticker):
    tk = yf.Ticker(ticker)
    info = tk.info
    hist = tk.history(period='5y', interval='1d', auto_adjust=False)
    try:
        cashflow = tk.cashflow
        bs = tk.balance_sheet
        fin = tk.financials
    except Exception:
        cashflow, bs, fin = None, None, None
    return {'info': info, 'history': hist, 'cashflow': cashflow, 'bs': bs, 'fin': fin}

def compute_simple_metrics(data):
    info = data['info']
    price = info.get('regularMarketPrice') or info.get('previousClose')
    div_yield = info.get('dividendYield')
    div_yield = div_yield * 100.0 if div_yield else None
    pe = info.get('trailingPE', None)
    de_ratio = info.get('debtToEquity', None)
    revenue = info.get('totalRevenue', None)
    net_income = info.get('netIncomeToCommon', None) or info.get('netIncome', None)
    rev_bil = revenue / 1e9 if revenue else None
    ni_bil = net_income / 1e9 if net_income else None
    return {'price': price, 'dividend_yield_pct': div_yield, 'pe': pe,
            'de_ratio': de_ratio, 'revenue_bil': rev_bil, 'net_income_bil': ni_bil}

def extract_historical_fcf(cashflow_df):
    if cashflow_df is None or cashflow_df.empty:
        return None
    idx = [i.lower() for i in cashflow_df.index.astype(str)]
    for candidate in ['free cash flow', 'freecashflow', 'freecashflows']:
        for i, name in enumerate(idx):
            if candidate in name:
                return cashflow_df.iloc[i].fillna(0).astype(float).values[:5]
    ocf, capex = None, None
    for i, name in enumerate(idx):
        if 'operat' in name and 'cash' in name:
            ocf = cashflow_df.iloc[i].astype(float)
        if 'capital' in name and 'expend' in name:
            capex = cashflow_df.iloc[i].astype(float)
    if ocf is not None and capex is not None:
        return (ocf - capex).fillna(0).values[:5]
    return None

def dcf_5yr(fcf_hist, revenue, growth_rate, terminal_growth, discount_rate, shares_outstanding):
    if fcf_hist is None or len(fcf_hist) == 0:
        base = None
    else:
        base = np.mean(fcf_hist[:3])
    if base is None and revenue is not None:
        base = revenue * 1e9 * 0.10
    if base is None:
        return None
    years = np.arange(1, 6)
    projected = [base * ((1 + growth_rate) ** y) for y in years]
    terminal_fcf = projected[-1] * (1 + terminal_growth)
    terminal_value = terminal_fcf / (discount_rate - terminal_growth) if discount_rate > terminal_growth else np.nan
    discounted = [projected[i] / ((1 + discount_rate) ** (i+1)) for i in range(5)]
    discounted_terminal = terminal_value / ((1 + discount_rate) ** 5)
    pv_total = np.nansum(discounted) + discounted_terminal
    intrinsic_per_share = pv_total / shares_outstanding if shares_outstanding and shares_outstanding > 0 else pv_total
    return {'pv_total': pv_total, 'intrinsic_per_share': intrinsic_per_share,
            'projected': projected, 'terminal_value': terminal_value,
            'discounted': discounted, 'discounted_terminal': discounted_terminal}

def one_year_return(hist):
    if hist is None or hist.empty:
        return None
    closes = hist['Close'].dropna()
    if len(closes) < 2:
        return None
    start, end = closes.iloc[0], closes.iloc[-1]
    return (end - start) / start * 100.0 if start else None

def minmax_norm(series, invert=False):
    s = series.dropna()
    if s.empty:
        return pd.Series([0.5] * len(series), index=series.index)
    mn, mx = s.min(), s.max()
    if mx == mn:
        return pd.Series([0.5] * len(series), index=series.index)
    norm = (series - mn) / (mx - mn)
    return 1.0 - norm if invert else norm

# ---------- Sidebar with logos ----------
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/0/09/Coca-Cola_logo.svg", use_column_width=True)
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/a/a6/Pepsi_logo_2014.svg", use_column_width=True)

# ---------- Main title ----------
st.markdown("<h1>🍾 Coke vs Pepsi — Advanced Investment Analyzer</h1>", unsafe_allow_html=True)
st.markdown("Compare The Coca-Cola Company (KO) and PepsiCo (PEP) with **DCF 5-year models, sensitivity analysis, PDF reports, and composite scoring.**<br><br><b style='color:red;'>Educational only — not financial advice.</b>", unsafe_allow_html=True)

# ---------- Fetch data ----------
tickers = {"Coke": "KO", "Pepsi": "PEP"}
data = {name: fetch_company_data(tk) for name, tk in tickers.items()}
metrics = {name: compute_simple_metrics(d) for name, d in data.items()}

# ---------- DCF ----------
assumptions = {
    "growth_rate": 0.05,
    "terminal_growth": 0.025,
    "discount_rate": 0.08,
    "shares": {"KO": 4.32e9, "PEP": 1.38e9}
}
dcf_results = {}
for name, tk in tickers.items():
    fcf_hist = extract_historical_fcf(data[name]['cashflow'])
    dcf_results[name] = dcf_5yr(fcf_hist,
                                metrics[name]['revenue_bil'],
                                assumptions['growth_rate'],
                                assumptions['terminal_growth'],
                                assumptions['discount_rate'],
                                assumptions['shares'][tk])

# ---------- Display Metrics ----------
st.subheader("📊 Key Metrics")
df_metrics = pd.DataFrame(metrics).T
st.dataframe(df_metrics)

# ---------- Display DCF ----------
st.subheader("💰 DCF Valuation (5-Year)")
df_dcf = pd.DataFrame({name: {"Intrinsic Value": r['intrinsic_per_share'] if r else None}
                      for name, r in dcf_results.items()}).T
st.dataframe(df_dcf)

# ---------- Composite Score ----------
st.subheader("⚖️ Composite Scoring")
df_scores = pd.DataFrame({
    "Price": [metrics['Coke']['price'], metrics['Pepsi']['price']],
    "PE": [metrics['Coke']['pe'], metrics['Pepsi']['pe']],
    "DivYield": [metrics['Coke']['dividend_yield_pct'], metrics['Pepsi']['dividend_yield_pct']],
    "DCF": [df_dcf.loc['Coke', 'Intrinsic Value'], df_dcf.loc['Pepsi', 'Intrinsic Value']]
}, index=['Coke', 'Pepsi'])
df_scores["Score"] = minmax_norm(df_scores["PE"], invert=True) + \
                     minmax_norm(df_scores["DivYield"]) + \
                     minmax_norm(df_scores["DCF"]) 
st.dataframe(df_scores)

# ---------- PDF Export ----------
st.subheader("📑 Export Report")
if st.button("Generate PDF Report"):
    buf = io.BytesIO()
    with PdfPages(buf) as pdf:
        plt.figure()
        df_metrics.T.plot(kind="bar")
        plt.title("Key Metrics Comparison")
        pdf.savefig(); plt.close()
        
        plt.figure()
        df_dcf["Intrinsic Value"].plot(kind="bar")
        plt.title("DCF Intrinsic Value")
        pdf.savefig(); plt.close()
        
    pdf_bytes = buf.getvalue()
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="Coke_vs_Pepsi_Report.pdf">📥 Download Report</a>'
    st.markdown(href, unsafe_allow_html=True)
