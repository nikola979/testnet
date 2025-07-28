import requests

def check_connection():
    try:
        requests.get("https://www.google.com", timeout=3)
        return "Connected"
    except requests.ConnectionError:
        return "No Connection"
        
        import json
from datetime import datetime

def log_result(name, value):
    with open("log.json", "a") as f:
        f.write(json.dumps({
            "timestamp": datetime.now().isoformat(),
            name: value
        }) + "\n")