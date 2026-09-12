import requests
import feedparser
from datetime import datetime

TELEGRAM_BOT_TOKEN = "8356310433:AAECrFAusJHD_nmngEjfy3z9doOafN9e3Tw"
TELEGRAM_CHAT_ID = "7408748137"

RSS_FEEDS = [
    "https://cointelegraph.com/rss",
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "https://cryptopanic.com/news/rss/"
]

def get_crypto_news(limit=3):
    noticias = []
    for feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:5]:
                titulo = entry.title
                if titulo not in [n['title'] for n in noticias]:
                    noticias.append({
                        'title': titulo,
                        'link': entry.link,
                        'published': entry.get('published', ''),
                        'source': feed.feed.get('title', 'Crypto News')
                    })
        except Exception as e:
            continue
    return noticias[:limit]

def format_message(noticias):
    hora = datetime.now().strftime("%d/%m %H:%M Chile")
    msg = f"🚀 *CRYPTO BREAKING - {hora}* 🚀\n\n"
    for i, n in enumerate(noticias, 1):
        msg += f"*{i}. {n['title']}*\n🔗 {n['link']}\n\n"
    return msg

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload, timeout=15)

if __name__ == "__main__":
    news = get_crypto_news(limit=3)
    if news:
        send_to_telegram(format_message(news))
