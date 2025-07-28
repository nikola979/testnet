import subprocess

def check_packet_loss(host="8.8.8.8"):
    result = subprocess.run(["ping", "-c", "4", host], stdout=subprocess.PIPE, text=True)
    output = result.stdout
    if "100% packet loss" in output:
        return "100% packet loss"
    elif "0% packet loss" in output:
        return "No packet loss"
    else:
        return "Partial packet loss"
        
        import json
from datetime import datetime

def log_result(name, value):
    with open("log.json", "a") as f:
        f.write(json.dumps({
            "timestamp": datetime.now().isoformat(),
            name: value
        }) + "\n")