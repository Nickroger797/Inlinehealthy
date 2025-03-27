from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def start_web():
    port = int(os.environ.get("PORT", 8080))  # Koyeb का default port use करो
    app.run(host="0.0.0.0", port=port)
