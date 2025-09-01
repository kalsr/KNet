# GITHUB-DENTAL-VOICE.

from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
import sqlite3
from datetime import datetime

app = Flask(__name__)

# SQLite setup
conn = sqlite3.connect("dental_office.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS calls (id INTEGER PRIMARY KEY, type TEXT, timestamp TEXT, transcript TEXT)")
conn.commit()

@app.route("/incoming_call", methods=["POST"])
def incoming_call():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO calls (type, timestamp) VALUES (?, ?)", ("Incoming", time))
    conn.commit()

    response = VoiceResponse()
    response.say("Thank you for calling. Please leave a message after the beep.")
    response.record(transcribe=True, max_length=30, action="/handle_recording")
    return str(response)

@app.route("/handle_recording", methods=["POST"])
def handle_recording():
    transcript = request.form.get("TranscriptionText", "No transcription available")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO calls (type, timestamp, transcript) VALUES (?, ?, ?)", ("Voicemail", time, transcript))
    conn.commit()
    return "Voicemail saved."

if __name__ == "__main__":
    app.run(port=5000)