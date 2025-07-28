from flask import Flask, jsonify, render_template
from utils.connection import check_connection
from utils.packet_loss import check_packet_loss
from utils.web_service import check_web_service
from utils.port_scan import check_open_port

app = Flask(__name__)  # ← ovo mora biti pre svih @app.route dekoratora

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/connection")
def connection():
    return jsonify(result=check_connection())

@app.route("/packet-loss")
def packet_loss():
    return jsonify(result=check_packet_loss())

@app.route("/web-service")
def web_service():
    return jsonify(result=check_web_service())

@app.route("/port-check")
def port_check():
    return jsonify(result=check_open_port())

if __name__ == "__main__":
    app.run(debug=True)