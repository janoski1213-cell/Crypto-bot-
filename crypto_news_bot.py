import requests
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

try:
    URL = "https://min-api.cryptocompare.com/data/v2/news/?lang=ES"
    r = requests.get(URL, timeout=15).json()
    news = r.get("Data", [])

    if news:
        n = news[0]
        title = n.get("title", "Noticia Cripto")
        url = n.get("url", "")
        body = n.get("body", "")[:400]
        text = f"NOTICIA CRIPTO\n\n{title}\n\n{body}...\n\n{url}"
    else:
        text = "Bitcoin se mantiene activo. Revisa el mercado."

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"},
        timeout=15
    )
    print("Enviado en español")

except Exception as e:
    print(f"Error: {e}")
