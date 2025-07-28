import requests

def check_web_service(url="https://github.com"):
    try:
        response = requests.head(url, timeout=5)
        return f"Status: {response.status_code}"
    except requests.RequestException:
        return "Unreachable"
        
        import json
from datetime import datetime

def log_result(name, value):
    with open("log.json", "a") as f:
        f.write(json.dumps({
            "timestamp": datetime.now().isoformat(),
            name: value
        }) + "\n")