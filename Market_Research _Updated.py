# This Market_Research application is developed by Randy Singh from KNet CONSUTING Group

# python
import streamlit as st
import pandas as pd
import random
import re
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from urllib.parse import quote_plus
import plotly.express as px
import plotly.graph_objects as go

APP_TITLE = "Agentic Research & Analysis Workbench"
APP_VERSION = "v3.0 (Charts + Summary + Gauge)"

# --------------------------- Utilities ---------------------------

def rand_float(a=0.0, b=1.0, ndigits=2):
    return round(random.uniform(a, b), ndigits)

def rand_choice(seq):
    return random.choice(seq)

def utc_now_iso():
    return datetime.now(timezone.utc).isoformat()

# --------------------------- Domain Knowledge ---------------------------

SECTORS = ["Technology", "Healthcare", "Energy", "Financials", "Consumer Discretionary",
           "Industrials", "Consumer Staples", "Utilities", "Real Estate", "Materials",
           "Telecommunication Services"]

TICKERS = ["AAPL","MSFT","GOOGL","AMZN","NVDA","TSLA","META","JPM","V","WMT",
           "XOM","JNJ","PG","BAC","HD","PFE","KO","PEP","DIS","CSCO"]

SAMPLE_HEADLINES = [
    "Company beats earnings expectations; guidance raised for next quarter.",
    "Regulatory changes projected to benefit sector over the next 12 months.",
    "Analysts report growing demand driven by AI and automation adoption.",
]

SECTOR_KEYWORDS = {
    "Technology":["AI","chip","cloud","software"],
    "Healthcare":["drug","vaccine","biotech"],
    "Energy":["oil","gas","renewable"],
    "Financials":["bank","loan","fintech"]
}

POSITIVE_WORDS = set("beat beats growth bullish surge strong profit".split())
NEGATIVE_WORDS = set("miss misses cut slowdown bearish slump decline loss weak".split())
TICKER_REGEX = re.compile(r"\b[A-Z]{1,5}\b")

# --------------------------- Core Logic ---------------------------

def simple_sentiment(text: str) -> float:
    tokens = re.findall(r"[A-Za-z']+", text.lower())
    pos = sum(1 for t in tokens if t in POSITIVE_WORDS)
    neg = sum(1 for t in tokens if t in NEGATIVE_WORDS)
    if pos == 0 and neg == 0:
        return 0.0
    return round((pos - neg) / max(1, (pos + neg)), 2)

def guess_sector(text: str) -> str:
    t = text.lower()
    for sector, keys in SECTOR_KEYWORDS.items():
        for k in keys:
            if k.lower() in t:
                return sector
    return rand_choice(SECTORS)

def extract_ticker(text: str) -> str:
    caps = TICKER_REGEX.findall(text.upper())
    for c in caps:
        if c in TICKERS:
            return c
    return rand_choice(TICKERS)

def synthesize_insight(query: str) -> dict:
    return {
        "timestamp": utc_now_iso(),
        "query": query,
        "ticker": extract_ticker(query),
        "sector": guess_sector(query),
        "trend_score": rand_float(0, 100),
        "volatility": rand_float(0.5, 5.0),
        "news_sentiment": rand_float(-1.0, 1.0),
        "headline": rand_choice(SAMPLE_HEADLINES),
        "source_type": "Synthetic",
        "source_url": "",
        "confidence": rand_float(0.5, 0.99),
    }

def generate_sample_dataset(n=50, query="market trends"):
    return [synthesize_insight(query) for _ in range(n)]

def fetch_google_news_rss(query: str, max_items=20):
    url = f"https://news.google.com/rss/search?q={quote_plus(query)}+when:7d&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    items = []
    for e in feed.entries[:max_items]:
        items.append({
            "title": e.get("title", ""),
            "link": e.get("link", ""),
            "published": e.get("published", ""),
            "summary": BeautifulSoup(e.get("summary", ""), "html.parser").get_text(" ", strip=True) if e.get("summary") else ""
        })
    return items

def build_record_from_news(query, title, link, published, summary):
    sentiment = simple_sentiment(f"{title} {summary}")
    return {
        "timestamp": utc_now_iso(),
        "query": query,
        "ticker": extract_ticker(title),
        "sector": guess_sector(title),
        "trend_score": rand_float(20, 80),
        "volatility": rand_float(0.5, 5.0),
        "news_sentiment": sentiment,
        "headline": title,
        "source_type": link.split('/')[2] if link else "Web",
        "source_url": link,
        "published": published,
        "summary": summary,
        "confidence": 0.8,
    }

def fetch_live_insights(query, max_items=20):
    news = fetch_google_news_rss(query, max_items)
    return [build_record_from_news(query, n["title"], n["link"], n["published"], n["summary"]) for n in news]

# --------------------------- Streamlit App ---------------------------

st.set_page_config(page_title=APP_TITLE, layout="wide")
st.title(f"{APP_TITLE} — {APP_VERSION}")

query = st.text_input("Enter research query:", "AI stock market trends")

col1, col2, col3 = st.columns(3)

if col1.button("Generate Sample Data"):
    records = generate_sample_dataset(80, query)
    df = pd.DataFrame(records)
    st.session_state["records"] = df

if col2.button("Fetch Live News"):
    records = fetch_live_insights(query, max_items=50)
    df = pd.DataFrame(records)
    st.session_state["records"] = df

if col3.button("Clear Data"):
    st.session_state["records"] = pd.DataFrame()

# Show data if available
if "records" in st.session_state and not st.session_state["records"].empty:
    df = st.session_state["records"]

    st.subheader("Research Results")
    st.dataframe(df, use_container_width=True)

    # 📊 Charts
    st.subheader("Charts & Insights")

    # 1. Average trend score by sector
    sector_avg = df.groupby("sector")["trend_score"].mean().reset_index()
    fig1 = px.bar(sector_avg, x="sector", y="trend_score",
                  title="Average Trend Score by Sector",
                  labels={"trend_score":"Avg Trend Score"})
    st.plotly_chart(fig1, use_container_width=True)

    # 2. Scatter plot (trend vs sentiment)
    fig2 = px.scatter(df, x="trend_score", y="news_sentiment",
                      color="sector", hover_data=["ticker","headline"],
                      title="Trend Score vs Sentiment by Sector")
    st.plotly_chart(fig2, use_container_width=True)

    # 3. Top 10 tickers
    top10 = df.groupby("ticker")["trend_score"].mean().reset_index().sort_values("trend_score", ascending=False).head(10)
    fig3 = px.bar(top10, x="ticker", y="trend_score", title="Top 10 Bullish Tickers")
    st.plotly_chart(fig3, use_container_width=True)

    # 📝 Text Insights
    st.subheader("Key Insights Summary")
    top_sector = sector_avg.sort_values("trend_score", ascending=False).iloc[0]
    top_ticker = top10.iloc[0]
    avg_sentiment = df["news_sentiment"].mean()

    st.markdown(f"""
    - 🏆 **Top Sector**: `{top_sector['sector']}` with an average trend score of **{top_sector['trend_score']:.2f}**
    - 📈 **Most Bullish Ticker**: `{top_ticker['ticker']}` with a trend score of **{top_ticker['trend_score']:.2f}**
    - 📰 **Overall Market Sentiment**: **{avg_sentiment:.2f}**
    """)

    # 📈 Sentiment Gauge
    st.subheader("Market Sentiment Gauge")
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_sentiment,
        title={'text': "Overall Sentiment (-1 = Bearish, +1 = Bullish)"},
        gauge={
            'axis': {'range': [-1, 1]},
            'bar': {'color': "blue"},
            'steps': [
                {'range': [-1, -0.3], 'color': "red"},
                {'range': [-0.3, 0.3], 'color': "lightgray"},
                {'range': [0.3, 1], 'color': "green"}
            ],
        }
    ))
    st.plotly_chart(fig_gauge, use_container_width=True)

    # 📥 Download button
    st.subheader("Download Data")
    json_data = df.to_json(orient="records", indent=2)
    st.download_button("Download JSON", json_data, file_name="research_log.json")
