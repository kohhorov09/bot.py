from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DB_FILE = "db.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

@app.route("/save", methods=["POST"])
def save():
    content = request.json
    chat_id = str(content["chat_id"])
    data = load_data()
    data[chat_id] = content["game_data"]
    save_data(data)
    return jsonify({"status": "saved"})

@app.route("/load/<chat_id>", methods=["GET"])
def load(chat_id):
    data = load_data()
    return jsonify(data.get(str(chat_id), None))

if __name__ == "__main__":
    app.run(debug=True)
