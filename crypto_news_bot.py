import requests
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

try:
    # Pide noticias directo en español
    urimport requests
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

try:
    URL = "https://min-api.cryptocompare.com/data/v2/news/?lang=ES"
    r = requests.get(URL, timeout=15).json()

    if r['Data']:
        noticia = r['Data'][0]
        titulo = noticia['title']
        enlace = noticia['url']
        cuerpo = noticia['body'][:400]
        mensaje = f"🚀 *NOTICIA CRIPTO* 🚀\n\n{titulo}\n\n{cuerpo}...\n\n{enlace}"
    else:
        mensaje = "🚀 Bitcoin se mantiene activo. Revisa el mercado."

    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
        "chat_id": CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }, timeout=15)

    print("Enviado en español")

except Exception as e:
    print(f"Error:{e}")
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
        "chat_id": CHAT_ID,
        "text": "🤖 Bot activo - Revisando mercado cripto..."
    }, timeout=15)
    # Aunque fal
    })
