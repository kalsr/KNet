

# Unified Single-File Fraud/Scam Detector



# ============================================================

# FRAUD / SCAM DETECTOR - Unified ML-Only & LLM+ML Mode

# Designed & Developed by Randy Singh - KNet Consulting

# ============================================================



# ---------------------------

# REQUIRED LIBRARIES

# ---------------------------

# pip install ttkbootstrap scikit-learn matplotlib pandas fpdf2 openai anthropic google-generativeai gpt4all

# ---------------------------



import os, re, random, json, tkinter as tk

from tkinter import filedialog, messagebox

import ttkbootstrap as ttk

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from fpdf import FPDF

from datetime import datetime

from sklearn.ensemble import IsolationForest



# LLM libraries (optional, only if LLM+ML mode)

try:

    import openai

    from openai import OpenAI

    OPENAI_AVAILABLE = True

except: OPENAI_AVAILABLE = False



try:

    import anthropic

    CLAUDE_AVAILABLE = True

except: CLAUDE_AVAILABLE = False



try:

    import google.generativeai as genai

    GEMINI_AVAILABLE = True

except: GEMINI_AVAILABLE = False



try:

    from gpt4all import GPT4All

    GPT4ALL_AVAILABLE = True

except: GPT4ALL_AVAILABLE = False



# ============================================================

# THEME SETUP

# ============================================================



def apply_theme(root):

    style = ttk.Style()

    style.theme_use("superhero")

    style.configure("TButton", font=("Calibri",12,"bold"), padding=10)

    style.configure("TLabel", font=("Calibri",12))

    style.configure("TEntry", font=("Consolas",11))



# ============================================================

# MACHINE LEARNING MODEL (IsolationForest)

# ============================================================



def extract_features(line):

    line_low = line.lower()

    keywords = ["failed","error","invalid","unauthorized","denied","403","blocked","brute","suspicious"]

    keyword_vec = [1 if k in line_low else 0 for k in keywords]

    digit_count = sum(c.isdigit() for c in line_low)

    uppercase_count = sum(c.isupper() for c in line)

    length = len(line)

    return np.array(keyword_vec + [digit_count, uppercase_count, length])



def train_ml_model():

    benign = ["User login OK","GET /home 200 OK","Regular system check","Read operation successful",

              "File opened normally","Heartbeat OK"]

    suspicious = ["Failed login attempt from 192.168.1.22","Multiple failed password attempts",

                  "Unauthorized access detected","Apache error 403 /admin",

                  "Invalid user root Linux auth","Windows EventLog access denied",

                  "Brute-force attack detected","Suspicious POST request 10.0.0.5"]

    all_logs = benign + suspicious

    X = np.array([extract_features(l) for l in all_logs])

    model = IsolationForest(n_estimators=200, contamination=0.35, random_state=42)

    model.fit(X)

    return model



ML_MODEL = train_ml_model()



def ml_analyze(logs):

    X = np.array([extract_features(l) for l in logs])

    preds = ML_MODEL.predict(X)

    score = np.sum(preds==-1)*10

    anomalies = [logs[i] for i in range(len(logs)) if preds[i]==-1]

    return score, anomalies



# ============================================================

# HEURISTIC ANALYSIS

# ============================================================



def heuristic_analysis(logs):

    score, flags = 0, []

    for l in logs:

        l_low = l.lower()

        if "failed" in l_low: score+=5; flags.append(l)

        if "unauthorized" in l_low: score+=7; flags.append(l)

        if "invalid user" in l_low: score+=6; flags.append(l)

        if "403" in l_low: score+=4; flags.append(l)

        if "brute" in l_low: score+=10; flags.append(l)

        if "suspicious" in l_low: score+=10; flags.append(l)

    return score, list(set(flags))



# ============================================================

# LLM ANALYSIS (Optional, only if mode = LLM+ML)

# ============================================================



def run_llm_analysis(logs):

    prompt = ("You are a cybersecurity log analyst. Analyze these logs and identify:\n"

              "- Potential fraud or scam behavior\n"

              "- Indicators of compromise\n"

              "- Risk summary (0–100)\n"

              "- Key suspicious events\n\n"

              f"LOGS:\n{chr(10).join(logs)}\n\n")

    if OPENAI_AVAILABLE and os.getenv("OPENAI_API_KEY"):

        try:

            client = OpenAI()

            response = client.chat.completions.create(

                model="gpt-4o-mini",

                messages=[{"role":"user","content":prompt}]

            )

            return "OpenAI GPT Response:\n" + response.choices[0].message["content"]

        except: pass

    if CLAUDE_AVAILABLE and os.getenv("ANTHROPIC_API_KEY"):

        try:

            client = anthropic.Anthropic()

            resp = client.messages.create(

                model="claude-3-haiku-20240307",

                messages=[{"role":"user","content":prompt}],

                max_tokens=400

            )

            return "Claude Response:\n" + resp.content[0].text

        except: pass

    if GEMINI_AVAILABLE and os.getenv("GOOGLE_API_KEY"):

        try:

            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

            model = genai.GenerativeModel("gemini-1.5-flash")

            resp = model.generate_content(prompt)

            return "Gemini Response:\n" + resp.text

        except: pass

    if GPT4ALL_AVAILABLE:

        try:

            model = GPT4All("ggml-gpt4all-j-v1.3-groovy")

            response = model.generate(prompt)

            return "GPT4All Response:\n" + response

        except: pass

    return "No LLM API keys configured or not available."



# ============================================================

# LOG PARSERS

# ============================================================



APACHE_REGEX = re.compile(r'(\d+\.\d+\.\d+\.\d+).*"(GET|POST|PUT|DELETE).*" (\d{3})')

LINUX_REGEX = re.compile(r'(invalid user|failed password|authentication failure)', re.IGNORECASE)

WINDOWS_REGEX = re.compile(r'(Access denied|Failed login|Audit failure|EventID:\s*\d+)', re.IGNORECASE)



def parse_apache(lines):

    parsed=[]

    for l in lines:

        m = APACHE_REGEX.search(l)

        if m: ip,method,code = m.groups(); parsed.append(f"ApacheLog | IP:{ip} | METHOD:{method} | STATUS:{code}")

        else: parsed.append(l.strip())

    return parsed



def parse_linux_log(lines):

    parsed=[]

    for l in lines:

        if LINUX_REGEX.search(l): parsed.append("LinuxAuth | SUSPICIOUS: "+l.strip())

        else: parsed.append("LinuxLog | "+l.strip())

    return parsed



def parse_windows_log(lines):

    parsed=[]

    for l in lines:

        if WINDOWS_REGEX.search(l): parsed.append("WinEvent | ALERT: "+l.strip())

        else: parsed.append("WinEvent | "+l.strip())

    return parsed



def load_file_auto(path):

    ext = os.path.splitext(path)[1].lower()

    if ext==".json":

        with open(path,"r",errors="ignore") as f: data=json.load(f)

        return [str(x) for x in data]

    elif ext==".csv":

        df=pd.read_csv(path)

        return df.astype(str).agg(" | ".join,axis=1).tolist()

    elif ext in [".log",".txt"]:

        with open(path,"r",errors="ignore") as f: lines=f.readlines()

        if any("GET" in l or "POST" in l for l in lines): return parse_apache(lines)

        if any("invalid user" in l.lower() or "auth" in path.lower() for l in lines): return parse_linux_log(lines)

        if any("Event" in l or "Windows" in l for l in lines): return parse_windows_log(lines)

        return [l.strip() for l in lines]

    else: messagebox.showerror("Error","Unsupported file type."); return []



# ============================================================

# SAMPLE DATA

# ============================================================



SAMPLE_EVENTS = ["Failed login from IP 192.168.1.55","User admin attempted unauthorized access",

                 "Multiple login attempts detected","Access granted for normal user",

                 "Apache error 403 for /admin","Suspicious POST request from 10.0.0.22",

                 "Brute-force pattern detected","Linux auth.log: invalid user root",

                 "Windows EventLog: access denied","Firewall blocked outgoing connection"]



def generate_sample_data(n=40): return [f"[Event {i+1}] {random.choice(SAMPLE_EVENTS)}" for i in range(n)]



# ============================================================

# CHARTS

# ============================================================



def plot_scores(ml_score,heuristic_score,combined_score):

    labels=["ML Score","Heuristic Score","Combined Score"]

    scores=[ml_score,heuristic_score,combined_score]

    plt.figure(figsize=(6,4))

    bars=plt.bar(labels,scores,color=["#FF5733","#33FF57","#3357FF"])

    plt.ylim(0,max(scores)+20)

    plt.title("Fraud/Scam Score Visualization")

    plt.grid(axis="y",linestyle="--",alpha=0.7)

    for bar,score in zip(bars,scores): plt.text(bar.get_x()+bar.get_width()/2,bar.get_height()+1,str(score),ha="center",fontweight="bold")

    plt.show()



# ============================================================

# PDF REPORT

# ============================================================



def generate_pdf_report(results,llm_output=None):

    pdf=FPDF(); pdf.add_page(); pdf.set_font("Arial","B",16)

    pdf.cell(0,10,"Fraud/Scam Detection Report",0,1,"C")

    pdf.set_font("Arial","",12)

    pdf.cell(0,10,f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",0,1); pdf.ln(5)

    pdf.cell(0,10,f"ML Score: {results.get('ml_score',0)}",0,1)

    pdf.cell(0,10,f"Heuristic Score: {results.get('heuristic_score',0)}",0,1)

    pdf.cell(0,10,f"Combined Score: {results.get('combined_score',0)}",0,1); pdf.ln(5)

    pdf.set_font("Arial","B",12); pdf.cell(0,10,"ML Flagged Logs:",0,1); pdf.set_font("Arial","",11)

    for l in results.get("ml_flags",[]): pdf.multi_cell(0,8,"- "+l)

    pdf.set_font("Arial","B",12); pdf.cell(0,10,"Heuristic Flags:",0,1); pdf.set_font("Arial","",11)

    for l in results.get("heuristic_flags",[]): pdf.multi_cell(0,8,"- "+l)

    if llm_output:

        pdf.set_font("Arial","B",12); pdf.cell(0,10,"LLM Analysis:",0,1); pdf.set_font("Arial","",11)

        pdf.multi_cell(0,8,llm_output)

    report_name=f"Fraud_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    pdf.output(report_name)

    return report_name



# ============================================================

# MAIN GUI APPLICATION

# ============================================================



class FraudDetectorUnifiedApp:

    def __init__(self,root):

        self.root=root; self.root.title("Fraud/Scam Detector - Unified ML & LLM")

        self.root.geometry("1250x820"); apply_theme(self.root)

        self.current_logs=[]; self.analysis_results={}

        self.mode=tk.StringVar(value="ML-only")

        self.build_gui()



    def build_gui(self):

        ttk.Label(self.root,text="Fraud / Scam Detector\nDesigned by Randy Singh - KNet Consulting",

                  font=("Calibri",22,"bold"),bootstyle="primary").pack(pady=15)

        mode_frame=ttk.Frame(self.root); mode_frame.pack(pady=5)

        ttk.Label(mode_frame,text="Select Mode:").grid(row=0,column=0,padx=5)

        ttk.Radiobutton(mode_frame,text="ML-only Offline",variable=self.mode,value="ML-only").grid(row=0,column=1,padx=5)

        ttk.Radiobutton(mode_frame,text="LLM + ML Online",variable=self.mode,value="LLM+ML").grid(row=0,column=2,padx=5)

        controls=ttk.Frame(self.root); controls.pack(pady=10)

        ttk.Button(controls,text="Generate Sample Data",bootstyle="success",command=self.generate_sample).grid(row=0,column=0,padx=10)

        ttk.Button(controls,text="Reset Data",bootstyle="danger",command=self.reset_data).grid(row=0,column=1,padx=10)

        ttk.Button(controls,text="Upload Log File",bootstyle="info",command=self.upload_file).grid(row=0,column=2,padx=10)

        ttk.Button(controls,text="Run Analysis",bootstyle="primary",command=self.run_analysis).grid(row=0,column=3,padx=10)

        ttk.Button(controls,text="Export PDF Report",bootstyle="secondary",command=self.export_pdf).grid(row=0,column=4,padx=10)

        self.sample_slider=ttk.Scale(controls,from_=10,to=100,bootstyle="info"); self.sample_slider.set(40)

        self.sample_slider.grid(row=1,column=0,columnspan=2,pady=10)

        self.output=tk.Text(self.root,height=30,width=150,font=("Courier",11)); self.output.pack(pady=15)



    def generate_sample(self):

        n=int(self.sample_slider.get())

        self.current_logs=generate_sample_data(n)

        self.display("Generated Sample Logs:\n\n"+"\n".join(self.current_logs))



    def reset_data(self):

        self.current_logs=[]; self.analysis_results={}

        self.output.delete("1.0",tk.END); self.display("Data reset.\n")



    def upload_file(self):

        path=filedialog.askopenfilename(title="Select Log File",filetypes=[("Log Files","*.log *.txt *.json *.csv"),("All Files","*.*")])

        if path:

            logs=load_file_auto(path)

            if logs: self.current_logs=logs; self.display(f"Loaded file: {os.path.basename(path)}\n\n"+"\n".join(logs))



    def run_analysis(self):

        if not self.current_logs: messagebox.showwarning("No Data","Please load or generate data first."); return

        ml_score,ml_flags=ml_analyze(self.current_logs)

        heuristic_score,heuristic_flags=heuristic_analysis(self.current_logs)

        combined_score=ml_score+heuristic_score

        self.analysis_results={"ml_score":ml_score,"heuristic_score":heuristic_score,"combined_score":combined_score,"ml_flags":ml_flags,"heuristic_flags":heuristic_flags}

        llm_output=None

        if self.mode.get()=="LLM+ML": llm_output=run_llm_analysis(self.current_logs)

        out="======== FRAUD ANALYSIS RESULTS ========\n"

        out+=f"ML Score: {ml_score}\nHeuristic Score: {heuristic_score}\nCombined Score: {combined_score}\n\n"

        out+="=== ML Flagged Entries ===\n"+"\n".join(ml_flags)+"\n\n"

        out+="=== Heuristic Flags ===\n"+"\n".join(heuristic_flags)+"\n\n"

        if llm_output: out+="=== LLM Analysis ===\n"+llm_output+"\n"

        self.display(out)

        plot_scores(ml_score,heuristic_score,combined_score)



    def export_pdf(self):

        if not self.analysis_results: messagebox.showwarning("No Analysis","Run analysis before exporting PDF."); return

        llm_output=None

        if self.mode.get()=="LLM+ML": llm_output=run_llm_analysis(self.current_logs)

        report_name=generate_pdf_report(self.analysis_results,llm_output)

        messagebox.showinfo("PDF Exported",f"PDF report saved as {report_name}")



    def display(self,text):

        self.output.delete("1.0",tk.END); self.output.insert(tk.END,text)



# ============================================================

# MAIN ENTRY

# ============================================================



if __name__=="__main__":

    root=ttk.Window(themename="superhero")

    app=FraudDetectorUnifiedApp(root)

    root.mainloop()

