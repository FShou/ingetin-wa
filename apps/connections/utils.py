import requests
from core.settings import WAHA_BASE_URL


def check_status():
    response = requests.get(url=f"{WAHA_BASE_URL}/api/sessions/default")
    print(response)
    if response.status_code == 200:
        status = response.json().get("status") # STOPPED, SCAN_QR, CONNECTED
        return status
    return "NOT_READY" 

def disconnect():
    requests.post(url=f"{WAHA_BASE_URL}/api/sessions/default/logout")

def get_qr_code():
    response = requests.get(url=f"{WAHA_BASE_URL}/api/default/auth/qr?format=raw")
    base64_string = response.json().get("value")
    return base64_string

