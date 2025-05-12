import asyncio
from binance.client import Client
from telegram import Bot
from config.settings import (
    API_KEY, API_SECRET,
    BOT_TOKEN, CHANNEL_ID
)
from bot.price_tracker import price_tracker

async def main():
    client = Client(API_KEY, API_SECRET)
    bot = Bot(token=BOT_TOKEN)

    await price_tracker(client, bot, CHANNEL_ID)

if __name__ == "__main__":
    asyncio.run(main())
