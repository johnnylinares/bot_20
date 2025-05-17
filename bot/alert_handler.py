# Libreries
import telegram
from binance.client import Client
import os

# Conections
from dotenv import load_dotenv
load_dotenv()

client = Client(api_key=os.getenv("API_KEY"), api_secret=os.getenv("BINANCE_API_SECRET"))
bot = telegram.Bot(token=os.getenv("BOT_TOKEN"))
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Asignar el canal de Telegram donde enviarás los mensajes

async def send_alert(symbol, percentage_change):
    await bot.send_message(chat_id=CHANNEL_ID, text=f'#{symbol} ({percentage_change:+.2f}%)')