from flask import Flask, request, jsonify
import time
import os

app = Flask(__name__)
devices = {}

@app.route("/ping", methods=["POST"])
def ping():
    data = request.json
    device = data.get("id")

    if device:
        devices[device] = time.time()

    return jsonify({"status": "ok"})

@app.route("/count", methods=["GET"])
def count():
    now = time.time()

    active = {
        k: v for k, v in devices.items()
        if now - v < 120
    }

    return jsonify({
        "active_devices": len(active),
        "devices": list(active.keys())
    })

@app.route("/")
def home():
    return "Device Tracker Running 🚀"

# Render uses PORT env
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
