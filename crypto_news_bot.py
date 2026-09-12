import requests
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

r = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN", timeout=15).json()
news = r.get("Data", [])[0]

text = f"{news['title']}\n\n{news['body'][:400]}...\n\n{news['url']}"

requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
    "chat_id": CHAT_ID,
    "text": text
}, timeout=15)

print("Sent")
