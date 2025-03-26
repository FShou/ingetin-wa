import requests

def send_wa(sender, recepiant, message):
    url = "http://localhost:3001/api/sendText"
    data = {
        "session": "default",
        "chatId": "6285161006215@c.us",
        "text": "Hi From Django"
    }
    response = requests.post(url, json=data)
    # response.raise_for_status()
    print(f"Sender: {sender}\nRecepiant: {recepiant}\nMessage: {message}")
    print(response)
