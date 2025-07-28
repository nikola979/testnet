import socket

def check_open_port(host="google.com", port=443):
    try:
        socket.create_connection((host, port), timeout=5)
        return f"Port {port} is open on {host}"
    except:
        return f"Port {port} is closed or unreachable"
        
        import json
from datetime import datetime

def log_result(name, value):
    with open("log.json", "a") as f:
        f.write(json.dumps({
            "timestamp": datetime.now().isoformat(),
            name: value
        }) + "\n")