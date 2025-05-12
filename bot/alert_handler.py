import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import io
import telegram
from binance.client import Client
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Crear el cliente de Binance con las credenciales de tu .env
client = Client(api_key=os.getenv("API_KEY"), api_secret=os.getenv("BINANCE_API_SECRET"))

# Crear la instancia del bot de Telegram con el token
bot = telegram.Bot(token=os.getenv("BOT_TOKEN"))
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Asignar el canal de Telegram donde enviarás los mensajes

async def send_alert(symbol, percentage_change):
    """
    Sends an alert via Telegram with a chart showing the price action of a symbol.
    """
    # Retrieve historical candlestick data from Binance API
    klines = client.futures_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE, limit=140)

    # Convert data into DataFrame
    df = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        '_1', '_2', '_3', '_4', '_5', '_6'
    ])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df = df.astype(float)  # Convert all columns to float

    # Set colors for candlestick chart
    market_colors = mpf.make_marketcolors(
        up='#089981',  # Green for bullish
        down='#000000',  # Black for bearish
        edge={'up': '#000000', 'down': '#000000'},
        wick={'up': '#000000', 'down': '#000000'}
    )

    # Set style for the chart with background color #dbdbdb
    chart_style = mpf.make_mpf_style(
        marketcolors=market_colors,
        gridcolor='gray',
        gridstyle='--',
        facecolor='#dbdbdb'
    )

    # Create figure and axis with adjusted size and background color
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor('#dbdbdb')
    ax.set_facecolor('#dbdbdb')

    # Plot candlestick chart
    mpf.plot(df, type='candle', style=chart_style, ax=ax, volume=False)

    # Draw a line for the current price
    current_price = df['close'].iloc[-1]
    ax.axhline(current_price, color='blue', linestyle='--', linewidth=2)

    # Set title with percentage change and color depending on price movement
    title_color = '#089981' if percentage_change >= 0 else 'red'
    ax.set_title(f'{symbol} ({percentage_change:+.2f}%)', color=title_color, fontsize=40, fontweight="bold", family="Arial")

    # Add subtle gridlines
    ax.grid(True, which='both', axis='both', color='black', linestyle='-', linewidth=0.3, alpha=0.3)

    # Ensure that the x-axis labels (timestamps) are horizontal
    for label in ax.get_xticklabels():
        label.set_rotation(0)

    # Adjust margins to remove extra space
    fig.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.05)

    # Save the chart image to a buffer with high resolution
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300)  # <-- Aumenta la calidad
    buf.seek(0)
    plt.close(fig)

    # Send the chart to Telegram
    await bot.send_photo(chat_id=CHANNEL_ID, photo=buf, caption=f'#{symbol} ({percentage_change:+.2f}%)')
