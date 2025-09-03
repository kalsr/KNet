import streamlit as st
import pandas as pd
import json
import os
import random
import re
import threading
import time
from datetime import datetime, timezone
from urllib.parse import quote_plus

# External libraries (install via: pip install requests feedparser beautifulsoup4)
import requests
import feedparser
from bs4 import BeautifulSoup

from tkinter import Tk, Text, StringVar, BooleanVar, END, N, S, E, W, messagebox, filedialog
from tkinter import ttk

APP_TITLE = "Agentic Research & Analysis Workbench"
APP_VERSION = "v2.0 (Live Fetch Enabled)"

# --------------------------- Utilities ---------------------------

def rand_float(a=0.0, b=1.0, ndigits=2):
    return round(random.uniform(a, b), ndigits)

def rand_choice(seq):
    return random.choice(seq)

def secure_seed():
    try:
        seed_bytes = os.urandom(16)
        seed_int = int.from_bytes(seed_bytes, "big")
        random.seed(seed_int)
    except Exception:
        random.seed()

def utc_now_iso():
    return datetime.now(timezone.utc).isoformat()

# --------------------------- Domain Knowledge ---------------------------

SECTORS = [
    "Technology", "Healthcare", "Energy", "Financials", "Consumer Discretionary",
    "Industrials", "Consumer Staples", "Utilities", "Real Estate", "Materials",
    "Telecommunication Services"
]

TICKERS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META", "JPM", "V", "WMT",
    "XOM", "JNJ", "PG", "BAC", "HD", "PFE", "KO", "PEP", "DIS", "CSCO",
    "INTC", "MRK", "ADBE", "CRM", "NKE", "ORCL", "ABNB", "AMD", "NFLX", "T"
]

SAMPLE_HEADLINES = [
    "Company beats earnings expectations; guidance raised for next quarter.",
    "Regulatory changes projected to benefit sector over the next 12 months.",
    "Analysts report growing demand driven by AI and automation adoption.",
    "Commodity prices remain volatile; hedging strategies recommended.",
    "Consumer sentiment improves; discretionary spending ticking up.",
    "Supply chain pressures easing; margins expected to expand.",
    "Short interest declines; technical indicators suggest bullish momentum.",
    "New product launch announced; preorders surpass initial estimates.",
    "M&A rumors swirl; potential synergies discussed by market watchers.",
    "Dividend increase announced; buyback authorization extended."
]

SOURCE_CONFIDENCE = {
    "bloomberg": 0.9,
    "reuters": 0.92,
    "wsj": 0.9,
    "marketwatch": 0.85,
    "cnbc": 0.88,
    "yahoo": 0.8,
    "seekingalpha": 0.75,
    "investing": 0.75,
    "forbes": 0.8,
    "ft": 0.9,
    "theguardian": 0.78,
    "apnews": 0.88,
    "techcrunch": 0.8,
    "businessinsider": 0.78,
    "fool": 0.76
}

SECTOR_KEYWORDS = {
    "Technology": ["AI", "chip", "semiconductor", "cloud", "software", "SaaS", "GPU", "data center", "5G", "cybersecurity"],
    "Healthcare": ["drug", "vaccine", "clinical", "FDA", "biotech", "pharma", "treatment", "hospital"],
    "Energy": ["oil", "gas", "OPEC", "WTI", "Brent", "renewable", "solar", "wind", "battery"],
    "Financials": ["bank", "credit", "loan", "Fed", "interest rate", "fintech", "insurance", "brokerage"],
    "Consumer Discretionary": ["retail", "e-commerce", "luxury", "auto", "EV", "travel", "airline", "hotel"],
    "Industrials": ["manufacturing", "logistics", "supply chain", "factory", "defense", "aerospace"],
    "Consumer Staples": ["beverage", "food", "staples", "grocery", "household"],
    "Utilities": ["utility", "grid", "electric", "water", "power"],
    "Real Estate": ["REIT", "real estate", "housing", "mortgage", "office"],
    "Materials": ["mining", "commodity", "steel", "copper", "chemical"],
    "Telecommunication Services": ["telecom", "carrier", "broadband", "wireless"]
}

POSITIVE_WORDS = set("""
beat beats beating raises raised growth bullish surge record strong upgrade upside rally expansion profitable profit
""".split())
NEGATIVE_WORDS = set("""
miss misses missed cut cuts cutting slowdown bearish slump decline warning downgrade downside loss losses weak weakens
""".split())

TICKER_REGEX = re.compile(r"\\b[A-Z]{1,5}\\b")

def simple_sentiment(text: str) -> float:
    if not text:
        return 0.0
    tokens = re.findall(r"[A-Za-z']+", text.lower())
    pos = sum(1 for t in tokens if t in POSITIVE_WORDS)
    neg = sum(1 for t in tokens if t in NEGATIVE_WORDS)
    if pos == 0 and neg == 0:
        return 0.0
    score = (pos - neg) / max(1, (pos + neg))
    return round(score, 2)

def guess_sector(text: str) -> str:
    t = (text or "").lower()
    for sector, keys in SECTOR_KEYWORDS.items():
        for k in keys:
            if k.lower() in t:
                return sector
    return rand_choice(SECTORS)

def extract_ticker(text: str) -> str:
    # Heuristic: match short ALLCAPS tokens; prefer known TICKERS list
    if not text:
        return rand_choice(TICKERS)
    caps = TICKER_REGEX.findall(text.upper())
    for c in caps:
        if c in TICKERS:
            return c
    return rand_choice(TICKERS)

# --------------------------- Synthetic Insight (kept for demo) ---------------------------

def synthesize_insight(query: str) -> dict:
    ticker = extract_ticker(query) or rand_choice(TICKERS)
    sector = guess_sector(query)
    trend_score = rand_float(0, 100, 2)
    volatility = rand_float(0.5, 5.0, 2)
    sentiment = rand_float(-1.0, 1.0, 2)
    headline = rand_choice(SAMPLE_HEADLINES)
    confidence = rand_float(0.5, 0.99, 2)
    now = utc_now_iso()
    return {
        "timestamp": now,
        "query": query,
        "ticker": ticker,
        "sector": sector,
        "trend_score": trend_score,
        "volatility": volatility,
        "news_sentiment": sentiment,
        "headline": headline,
        "source_type": "Synthetic",
        "source_url": "",
        "confidence": confidence,
    }

def generate_sample_dataset(min_n=50, max_n=100, query="market trends"):
    n = random.randint(min_n, max_n)
    return [synthesize_insight(query) for _ in range(n)]

# --------------------------- Live Fetcher ---------------------------

def fetch_google_news_rss(query: str, max_items: int = 80):
    url = f"https://news.google.com/rss/search?q={quote_plus(query)}+when:7d&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    items = []
    for e in feed.entries[:max_items]:
        title = e.get("title", "")
        link = e.get("link", "")
        published = e.get("published", "") or e.get("updated", "")
        summary = BeautifulSoup(e.get("summary", ""), "html.parser").get_text(" ", strip=True) if e.get("summary") else ""
        items.append({
            "title": title,
            "link": link,
            "published": published,
            "summary": summary
        })
    return items

def fetch_article_snippet(url: str, max_len: int = 280) -> str:
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code != 200:
            return ""
        soup = BeautifulSoup(resp.text, "html.parser")
        # Try common selectors
        candidates = []
        for sel in ["article", "main", "div[itemprop='articleBody']"]:
            node = soup.select_one(sel)
            if node:
                candidates.append(node.get_text(" ", strip=True))
        if not candidates:
            # fallback: first few paragraphs
            paras = [p.get_text(" ", strip=True) for p in soup.find_all("p")]
            text = " ".join(paras[:6])
        else:
            text = max(candidates, key=len)
        return text[:max_len]
    except Exception:
        return ""

def build_record_from_news(query: str, title: str, link: str, published: str, summary: str) -> dict:
    sentiment = simple_sentiment(f"{title} {summary}")
    sector = guess_sector(f"{title} {summary}")
    ticker = extract_ticker(title)
    base_trend = 50 + (sentiment * 30)  # map -1..+1 to ~20..80
    trend_score = max(0, min(100, base_trend + rand_float(-5, 5)))
    volatility = rand_float(0.5, 5.0, 2)

    hostname = ""
    try:
        hostname = re.sub(r"^https?://", "", link).split("/")[0]
    except Exception:
        pass
    conf = 0.7
    for key, val in SOURCE_CONFIDENCE.items():
        if key in hostname.lower():
            conf = val
            break

    snippet = fetch_article_snippet(link) if link else ""

    return {
        "timestamp": utc_now_iso(),
        "query": query,
        "ticker": ticker,
        "sector": sector,
        "trend_score": round(trend_score, 2),
        "volatility": volatility,
        "news_sentiment": sentiment,
        "headline": title,
        "source_type": hostname or "Web",
        "source_url": link,
        "published": published,
        "summary": summary if summary else snippet,
        "confidence": round(conf, 2),
    }

def fetch_live_insights(query: str, max_items: int = 80):
    news = fetch_google_news_rss(query, max_items=max_items)
    records = [build_record_from_news(query, n["title"], n["link"], n["published"], n["summary"]) for n in news]
    return records

# --------------------------- Summary ---------------------------

def summarize(records):
    if not records:
        return "No data to summarize."
    by_sector = {}
    for r in records:
        by_sector.setdefault(r["sector"], []).append(r)

    lines = []
    lines.append(f"Report generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Total insights: {len(records)}")
    lines.append("")

    # Sector highlights
    lines.append("Sector highlights (avg trend / sentiment):")
    rankings = []
    for sector, recs in by_sector.items():
        avg_trend = sum(x["trend_score"] for x in recs) / len(recs)
        avg_sent = sum(x.get("news_sentiment", 0) for x in recs) / len(recs)
        rankings.append((sector, avg_trend, avg_sent, len(recs)))
    rankings.sort(key=lambda x: x[1], reverse=True)
    for sector, avg_trend, avg_sent, count in rankings[:5]:
        lines.append(f"  â¢ {sector}: avg trend={avg_trend:.2f}, avg sentiment={avg_sent:.2f}, samples={count}")
    lines.append("")

    # Top tickers
    top_tickers = sorted(records, key=lambda r: (r["trend_score"], r.get("news_sentiment", 0)), reverse=True)[:10]
    lines.append("Top 10 bullish tickers:")
    for r in top_tickers:
        lines.append(f"  â¢ {r['ticker']} ({r['sector']}) â trend={r['trend_score']}, sent={r.get('news_sentiment', 0)}, src={r.get('source_type','')}")

    lines.append("")
    lines.append("Notes:")
    lines.append("  Live insights are derived from public news feeds and simple heuristics; validate before trading decisions.")
    return "\n".join(lines)

# --------------------------- GUI Application ---------------------------

class ResearchGUI:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title(f"{APP_TITLE} â {APP_VERSION}")
        self.records = []
        self.status_var = StringVar(value="Ready")
        self.query_var = StringVar(value="AI stock market trends")
        self.autosave_var = BooleanVar(value=False)

        self._style()
        self._make_layout()
        secure_seed()
        self._set_status("Ready. Generate data, run research, or fetch live news.")

    def _style(self):
        style = ttk.Style()
        try:
            if "clam" in style.theme_names():
                style.theme_use("clam")
        except Exception:
            pass

        style.configure("Run.TButton", font=("Segoe UI", 11, "bold"), padding=10, foreground="#ffffff", background="#0066cc")
        style.map("Run.TButton", foreground=[("active","#ffffff")], background=[("active","#0052a3")])

        style.configure("Gen.TButton", font=("Segoe UI", 11, "bold"), padding=10, foreground="#ffffff", background="#14833b")
        style.map("Gen.TButton", foreground=[("active","#ffffff")], background=[("active","#0f6a30")])

        style.configure("Fetch.TButton", font=("Segoe UI", 11, "bold"), padding=10, foreground="#ffffff", background="#0a7c86")
        style.map("Fetch.TButton", foreground=[("active","#ffffff")], background=[("active","#08626a")])

        style.configure("Save.TButton", font=("Segoe UI", 11, "bold"), padding=10, foreground="#ffffff", background="#7a3e9d")
        style.map("Save.TButton", foreground=[("active","#ffffff")], background=[("active","#61317c")])

        style.configure("Load.TButton", font=("Segoe UI", 11, "bold"), padding=10, foreground="#ffffff", background="#b35c00")
        style.map("Load.TButton", foreground=[("active","#ffffff")], background=[("active","#8f4a00")])

        style.configure("Clear.TButton", font=("Segoe UI", 11, "bold"), padding=10, foreground="#ffffff", background="#b00020")
        style.map("Clear.TButton", foreground=[("active","#ffffff")], background=[("active","#8c001a")])

        style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"))
        style.configure("Body.TLabel", font=("Segoe UI", 11))
        style.configure("Status.TLabel", font=("Segoe UI", 10), anchor="w")

    def _make_layout(self):
        top = ttk.Frame(self.root, padding=12)
        top.grid(row=0, column=0, sticky=(N,S,E,W))
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=0)
        self.root.grid_columnconfigure(0, weight=1)

        ttk.Label(top, text="Research Query:", style="Body.TLabel").grid(row=0, column=0, padx=(0,8), pady=4, sticky=W)
        self.query_entry = ttk.Entry(top, textvariable=self.query_var, width=60)
        self.query_entry.grid(row=0, column=1, padx=(0,12), pady=4, sticky=(W,E))
        top.grid_columnconfigure(1, weight=1)

        self.run_btn = ttk.Button(top, text="Run Research", style="Run.TButton", command=self.on_run_research)
        self.run_btn.grid(row=0, column=2, padx=6, pady=4, sticky=E)

        self.gen_btn = ttk.Button(top, text="Generate Sample Data", style="Gen.TButton", command=self.on_generate_sample)
        self.gen_btn.grid(row=0, column=3, padx=6, pady=4, sticky=E)

        self.fetch_btn = ttk.Button(top, text="Fetch Live News", style="Fetch.TButton", command=self.on_fetch_live)
        self.fetch_btn.grid(row=0, column=4, padx=6, pady=4, sticky=E)

        self.save_btn = ttk.Button(top, text="Save as JSON/JDON", style="Save.TButton", command=self.on_save_json)
        self.save_btn.grid(row=0, column=5, padx=6, pady=4, sticky=E)

        self.load_btn = ttk.Button(top, text="Upload Log (JSON/JDON)", style="Load.TButton", command=self.on_load_json)
        self.load_btn.grid(row=0, column=6, padx=6, pady=4, sticky=E)

        self.clear_btn = ttk.Button(top, text="Clear Data", style="Clear.TButton", command=self.on_clear)
        self.clear_btn.grid(row=0, column=7, padx=6, pady=4, sticky=E)

        panes = ttk.PanedWindow(self.root, orient="horizontal")
        panes.grid(row=1, column=0, sticky=(N,S,E,W), padx=12, pady=(0,12))
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        left = ttk.Frame(panes, padding=(0,0,6,0))
        self.tree = ttk.Treeview(left, columns=(
            "timestamp","query","ticker","sector","trend_score","volatility","news_sentiment","source_type","confidence","headline","published","source_url"
        ), show="headings", height=18)
        col_specs = {
            "timestamp":120, "query":160, "ticker":80, "sector":150, "trend_score":110, "volatility":100,
            "news_sentiment":120, "source_type":150, "confidence":100, "headline":400, "published":160, "source_url":280
        }
        for col, width in col_specs.items():
            self.tree.heading(col, text=col.replace("_"," ").title())
            self.tree.column(col, width=width, anchor="w")
        yscroll = ttk.Scrollbar(left, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=yscroll.set)
        self.tree.grid(row=0, column=0, sticky=(N,S,E,W))
        yscroll.grid(row=0, column=1, sticky=(N,S))
        left.grid_rowconfigure(0, weight=1)
        left.grid_columnconfigure(0, weight=1)

        right = ttk.Frame(panes, padding=(6,0,0,0))
        ttk.Label(right, text="Actionable Summary", style="Header.TLabel").grid(row=0, column=0, sticky=W, pady=(0,6))
        self.summary = Text(right, wrap="word", height=20)
        self.summary.grid(row=1, column=0, sticky=(N,S,E,W))
        yscroll2 = ttk.Scrollbar(right, orient="vertical", command=self.summary.yview)
        self.summary.configure(yscrollcommand=yscroll2.set)
        yscroll2.grid(row=1, column=1, sticky=(N,S))
        right.grid_rowconfigure(1, weight=1)
        right.grid_columnconfigure(0, weight=1)

        panes.add(left, weight=3)
        panes.add(right, weight=2)

        status = ttk.Frame(self.root, padding=(12,6))
        status.grid(row=2, column=0, sticky=(E,W))
        self.status_lbl = ttk.Label(status, textvariable=self.status_var, style="Status.TLabel")
        self.status_lbl.grid(row=0, column=0, sticky=W)
        status.grid_columnconfigure(0, weight=1)

        try:
            self.root.state("zoomed")
        except Exception:
            try:
                self.root.attributes("-zoomed", True)
            except Exception:
                self.root.geometry("1500x900+60+40")

    # ------- Helpers -------
    def _set_status(self, msg):
        self.status_var.set(msg)
        self.status_lbl.update_idletasks()

    def _refresh_table(self):
        self.tree.delete(*self.tree.get_children())
        for r in self.records:
            values = (
                r.get("timestamp",""), r.get("query",""), r.get("ticker",""), r.get("sector",""), r.get("trend_score",""),
                r.get("volatility",""), r.get("news_sentiment",""), r.get("source_type",""), r.get("confidence",""),
                r.get("headline",""), r.get("published",""), r.get("source_url","")
            )
            self.tree.insert("", END, values=values)

    def _refresh_summary(self):
        report = summarize(self.records)
        self.summary.delete("1.0", END)
        self.summary.insert("1.0", report)

    # ------- Button Actions -------
    def on_generate_sample(self):
        self._set_status("Generating synthetic dataset...")
        self.root.after(50, self._generate_sample_impl)

    def _generate_sample_impl(self):
        query = self.query_var.get().strip() or "market trends"
        self.records = generate_sample_dataset(50, 100, query=query)
        self._refresh_table()
        self._refresh_summary()
        self._set_status(f"Generated {len(self.records)} records.")

    def on_clear(self):
        self.records = []
        self._refresh_table()
        self._refresh_summary()
        self._set_status("Cleared all data.")

    def on_save_json(self):
        if not self.records:
            messagebox.showinfo("Nothing to save", "No records to save. Generate, fetch, or run research first.")
            return
        default_name = f"agentic_research_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json *.jdon"), ("All files", "*.*")],
            initialfile=default_name
        )
        if not file_path:
            return
        payload = {
            "app": APP_TITLE,
            "version": APP_VERSION,
            "saved_at": datetime.now().isoformat(),
            "records": self.records,
            "summary": summarize(self.records)
        }
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)
            self._set_status(f"Saved {len(self.records)} records to: {file_path}")
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save file:\\n{e}")

    def on_load_json(self):
        file_path = filedialog.askopenfilename(
            title="Upload Log File",
            filetypes=[("JSON files", "*.json *.jdon"), ("All files", "*.*")]
        )
        if not file_path:
            return
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            loaded_records = data.get("records", [])
            if not isinstance(loaded_records, list):
                raise ValueError("Invalid log format: 'records' is not a list.")
            self.records = loaded_records
            self._refresh_table()
            self._refresh_summary()
            self._set_status(f"Loaded {len(self.records)} records from: {os.path.basename(file_path)}")
        except Exception as e:
            messagebox.showerror("Load Error", f"Failed to load log:\\n{e}")

    def on_run_research(self):
        query = self.query_var.get().strip()
        if not query:
            messagebox.showinfo("Provide a query", "Please enter a research query to run.")
            return
        self._set_status("Running autonomous research (simulated batches)...")
        self.run_btn.config(state="disabled")
        t = threading.Thread(target=self._research_thread, args=(query,), daemon=True)
        t.start()

    def _research_thread(self, query):
        try:
            batch_total = random.randint(3, 6)
            for i in range(batch_total):
                time.sleep(rand_float(0.4, 1.2))
                batch = [synthesize_insight(query) for _ in range(random.randint(10, 20))]
                self.records.extend(batch)
                self.root.after(0, self._refresh_table)
                self.root.after(0, self._refresh_summary)
                self.root.after(0, lambda i=i, bt=batch_total: self._set_status(f"Collected batch {i+1}/{bt} â total records: {len(self.records)}"))
            self.root.after(0, lambda: self._set_status(f"Research complete. Total records: {len(self.records)}"))
        finally:
            self.root.after(0, lambda: self.run_btn.config(state="normal"))

    def on_fetch_live(self):
        query = self.query_var.get().strip()
        if not query:
            messagebox.showinfo("Provide a query", "Please enter a news query (e.g., 'AI in financial markets').")
            return
        self.fetch_btn.config(state="disabled")
        self._set_status("Fetching live news...")
        t = threading.Thread(target=self._fetch_live_thread, args=(query,), daemon=True)
        t.start()

    def _fetch_live_thread(self, query):
        try:
            news_records = fetch_live_insights(query, max_items=80)
            if not news_records:
                self.root.after(0, lambda: messagebox.showinfo("No Results", "No live news found for this query."))
                return
            # Replace current dataset with live results
            self.records = news_records
            self.root.after(0, self._refresh_table)
            self.root.after(0, self._refresh_summary)
            self.root.after(0, lambda: self._set_status(f"Fetched {len(news_records)} live news insights."))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Fetch Error", f"Failed to fetch live news:\\n{e}"))
        finally:
            self.root.after(0, lambda: self.fetch_btn.config(state="normal"))

def main():
    root = Tk()
    app = ResearchGUI(root)
    root.mainloop()

if __name__ == "__main__":

    main()
