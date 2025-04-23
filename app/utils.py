import requests

def check_status(url):
    try:
        response = requests.get(url, timeout=5)
        return "🟢 Online" if response.status_code == 200 else "🔴 Error"
    except Exception:
        return "🔴 Unreachable"
