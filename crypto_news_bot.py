import requests
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

try:
    # Pide noticias directo en español
    url = "https://min-api.cryptocompare.com/data/v2/news/?lang=ES"
    r = requests.get(url, timeout=15).json()

    if r['Data']:
        noticia = r['Data'][0]
        titulo = noticia['title']
        link = noticia['url']
        cuerpo = noticia['body'][:400]

        mensaje = f"🚀 *NOTICIA CRIPTO* 🚀\n\n📰 {titulo}\n\n💬 {cuerpo}...\n\n🔗 {link}\n\n⏰ Bot 24/7"
    else:
        mensaje = "🚀 Bitcoin se mantiene activo. Revisa el mercado en CoinMarketCap 🚀"

    # Enviar
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={
        "chat_id": CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }, timeout=15)

    print("Enviado en español")

except Exception as e:
    print(f"Error: {e}")
    # Aunque falle la noticia, igual avisa que el bot está vivo
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={
        "chat_id": CHAT_ID,
        "text": "🤖 Bot activo - Revisando mercado cripto..."
    })
