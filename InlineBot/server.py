from flask import Flask
import threading

app = Flask(__name__)

@app.route('/health')
def health_check():
    return "OK", 200

def run():
    app.run(host="0.0.0.0", port=8080)

def start_web():
    t = threading.Thread(target=run)
    t.start()
