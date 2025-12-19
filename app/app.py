from flask import Flask, jsonify, request
import os
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "message": "Hello from the Flask app behind Traefik!",
        "host": socket.gethostname(),
        "path": request.path
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})
