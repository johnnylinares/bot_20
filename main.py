# Libreries
import asyncio
from binance.client import Client
from telegram import Bot

# Conections
from bot.price_tracker import price_tracker
from logs import log_message
from config.settings import (
    API_KEY, API_SECRET,
    BOT_TOKEN, CHANNEL_ID,
)

# Main Function
async def main():
    client = Client(API_KEY, API_SECRET)
    bot = Bot(token=BOT_TOKEN)

    await log_message(message="🤖 BOT ACTIVATED")
    await price_tracker(client, bot, CHANNEL_ID)

# Run
if __name__ == "__main__":
    asyncio.run(main())
