import requests
import os
from deep_translator import GoogleTranslator

# Configuración
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Noticias
url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
resp = requests.get(url).json()
noticia = resp['Data'][0]
titulo_en = noticia['title']
cuerpo_en = noticia['body'][:300]

# Traducir al español
traductor = GoogleTranslator(source='en', target='es')
titulo_es = traductor.translate(titulo_en)
cuerpo_es = traductor.translate(cuerpo_en)

mensaje = f"🚀 *NOTICIA CRIPTO* 🚀\n\n📰 {titulo_es}\n\n💬 {cuerpo_es}...\n\n🔗 {noticia['url']}"

# Enviar a Telegram
requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={
    "chat_id": CHAT_ID,
    "text": mensaje,
    "parse_mode": "Markdown"
})
print("Noticia enviada en español")
