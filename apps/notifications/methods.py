import requests

from core.settings import WAHA_BASE_URL

def send_wa(notification):
    url = f"{WAHA_BASE_URL}/api/sendText"
    data = {
        "session": "default",
        "chatId": f"{notification.recepiant}@c.us",
        "text": notification.message
    }
    response = requests.post(url, json=data)
    # response.raise_for_status()
    print(response)


