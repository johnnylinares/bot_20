import time
import asyncio
from binance.client import Client
from bot.alert_handler import send_alert

async def price_tracker(client: Client, bot, channel_id, threshold=0.01):
    price_history = {}

    while True:
        try:
            tickers = client.futures_ticker()
            now = time.time()

            for ticker in tickers:
                symbol = ticker['symbol']
                price = float(ticker['lastPrice'])

                if not symbol.endswith("USDT"):
                    continue

                if symbol not in price_history:
                    price_history[symbol] = []

                price_history[symbol].append((now, price))
                price_history[symbol] = [p for p in price_history[symbol] if now - p[0] <= 3600]  # Última hora

                if len(price_history[symbol]) >= 2:
                    old_price = price_history[symbol][0][1]
                    percentage_change = ((price - old_price) / old_price) * 100

                    if abs(percentage_change) >= threshold:
                        await send_alert(symbol, percentage_change)
                        price_history[symbol] = []  # Reset para evitar spam

            await asyncio.sleep(10)

        except Exception as e:
            print(f"[ERROR] {e}")
            await asyncio.sleep(10)
