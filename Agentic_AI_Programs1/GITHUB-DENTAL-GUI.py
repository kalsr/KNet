# GITHUB-DENTAL-GUI


import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
from twilio.rest import Client

# Twilio credentials
TWILIO_SID = "your_account_sid"
TWILIO_TOKEN = "your_auth_token"
TWILIO_FROM = "+1234567890"
TWILIO_TO = "+1987654321"

twilio_client = Client(TWILIO_SID, TWILIO_TOKEN)

# Database setup
conn = sqlite3.connect("dental_office.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS activities (
    id INTEGER PRIMARY KEY,
    description TEXT,
    timestamp TEXT
)
""")
conn.commit()

# GUI setup
root = tk.Tk()
root.title("Dental Office AI Dashboard")
root.geometry("1000x600")
root.configure(bg="#f0f8ff")

# Functions
def log_call(call_type):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO calls (type, timestamp) VALUES (?, ?)", (call_type, time))
    conn.commit()
    messagebox.showinfo("Call Logged", f"{call_type} call logged at {time}")
    if call_type == "Missed":
        send_sms_alert(f"Missed call at {time}")

def send_sms_alert(message):
    try:
        twilio_client.messages.create(
            body=message,
            from_=TWILIO_FROM,
            to=TWILIO_TO
        )
        messagebox.showinfo("SMS Sent", f"Alert sent: {message}")
    except Exception as e:
        messagebox.showerror("SMS Error", f"Failed to send SMS: {e}")

def log_activity():
    activity = activity_entry.get()
    if activity:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO activities (description, timestamp) VALUES (?, ?)", (activity, time))
        conn.commit()
        messagebox.showinfo("Activity Logged", f"{activity} logged at {time}")
        activity_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter an activity.")

def show_logs():
    cursor.execute("SELECT * FROM calls")
    calls = cursor.fetchall()
    cursor.execute("SELECT * FROM activities")
    activities = cursor.fetchall()
    logs = "\n".join(
        [f"📞 {c[1]} at {c[2]}" + (f" | Transcript: {c[3]}" if c[3] else "") for c in calls] +
        [f"🦷 {a[1]} at {a[2]}" for a in activities]
    )
    messagebox.showinfo("Logs", logs if logs else "No logs yet.")

# Layout
title = tk.Label(root, text="Dental Office AI Dashboard", font=("Helvetica", 24), bg="#f0f8ff")
title.pack(pady=20)

button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

tk.Button(button_frame, text="📞 Log Incoming Call", bg="#90ee90", font=("Helvetica", 14), width=20,
          command=lambda: log_call("Incoming")).grid(row=0, column=0, padx=10, pady=10)

tk.Button(button_frame, text="❌ Log Missed Call", bg="#ffcccb", font=("Helvetica", 14), width=20,
          command=lambda: log_call("Missed")).grid(row=0, column=1, padx=10, pady=10)

tk.Button(button_frame, text="📋 Show Logs", bg="#add8e6", font=("Helvetica", 14), width=20,
          command=show_logs).grid(row=0, column=2, padx=10, pady=10)

activity_label = tk.Label(root, text="Log Dental Activity:", font=("Helvetica", 16), bg="#f0f8ff")
activity_label.pack(pady=10)

activity_entry = tk.Entry(root, font=("Helvetica", 14), width=50)
activity_entry.pack(pady=5)

tk.Button(root, text="✅ Log Activity", bg="#d3d3d3", font=("Helvetica", 14), command=log_activity).pack(pady=10)

root.mainloop()
