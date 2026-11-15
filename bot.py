import requests

# ======================
# FILL THESE IN LATER
# ======================
TELEGRAM_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"
CHAT_ID = "PASTE_YOUR_CHAT_ID_HERE"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.json()

# Test message
test_message = "✅ *AI Daily Summary Bot is working!*\n\nThis is a test message."
result = send_telegram_message(test_message)

print(result)
