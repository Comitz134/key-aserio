import os
from flask import Flask, jsonify, render_template
from datetime import datetime
import hashlib

app = Flask(__name__, template_folder="templates")

def get_daily_key():
    hoje = datetime.utcnow().strftime("%Y-%m-%d")
    return hashlib.md5(hoje.encode()).hexdigest()[:10]

@app.route("/dailykey")
def dailykey():
    return jsonify({"key": get_daily_key()})

@app.route("/")
def index():
    key = get_daily_key()
    return render_template("index.html", key=key)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
