# Crypto Price Alert Bot

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.9+-blueviolet.svg)](https://www.python.org/downloads/)
![Maintenance](https://img.shields.io/badge/Maintained-yes-green)

A Python-based bot that monitors cryptocurrency prices on Binance Futures and sends real-time alerts to a Telegram channel when significant price changes occur.

## Table of Contents

1.  [Features](#features)
2.  [Getting Started](#getting-started)
    1.  [Prerequisites](#prerequisites)
    2.  [Installation](#installation)
    3.  [Configuration](#configuration)
3.  [Usage](#usage)
4.  [Contributing](#contributing)
5.  [License](#license)
6.  [Author](#author)
7.  [Acknowledgments](#acknowledgments)

## Features

* **Real-time Price Monitoring:** Tracks cryptocurrency prices on Binance Futures.
* **Customizable Alerts:** Sends alerts to a Telegram channel based on a configurable percentage change threshold.
* **24-Hour Volume Display:** Includes the 24-hour trading volume in alerts.
* **Emoji Indicators:** Uses emojis to visually represent price trends (🟢📈 for upward, 🔴📉 for downward).
* **Robust Logging:** Logs bot activity and errors for easy debugging and monitoring.
* **Asynchronous Operations:** Built with `asyncio` for efficient performance.

## Getting Started

### Prerequisites

* Python 3.9 or higher
* A Telegram bot token
* Binance API keys (for Futures trading)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/tu-usuario/tu-proyecto.git](https://github.com/tu-usuario/tu-proyecto.git)
    cd tu-proyecto
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  **Create a `.env` file in the root directory of the project.**

2.  **Add the following environment variables to the `.env` file:**

    ```
    API_KEY="YOUR_BINANCE_API_KEY"
    API_SECRET="YOUR_BINANCE_API_SECRET"
    BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
    CHANNEL_ID="YOUR_TELEGRAM_CHANNEL_ID"
    CHANNEL_LOG_ID="YOUR_TELEGRAM_LOG_CHANNEL_ID" # (Optional, for separate log channel)
    BOT_LOG_TOKEN="YOUR_TELEGRAM_LOG_BOT_TOKEN"    # (Optional, for separate log channel)
    LOG_LEVEL="INFO"  # (Optional, default: INFO, options: DEBUG, INFO, WARNING, ERROR, CRITICAL)
    LOG_FILE_PATH="/path/to/your/logfile.log" # (Optional, path to save logs in a file)
    ```

    * Replace the placeholder values with your actual API keys and tokens.
    * Obtain your Telegram Bot token from BotFather.
    * Obtain your Telegram Channel ID by adding the bot to your channel and forwarding a message to [@username_to_id_bot](https://t.me/username_to_id_bot).
    * `LOG_LEVEL` and `LOG_FILE_PATH` are optional. If `LOG_FILE_PATH` is provided, logs will be saved to the specified file.

## Usage

1.  **Run the bot:**

    ```bash
    python main.py
    ```

    The bot will start monitoring prices and send alerts to your specified Telegram channel.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

[Tu Nombre](https://github.com/tu-usuario)

## Acknowledgments

* Thanks to the [python-binance](https://github.com/sammchardy/python-binance) library for simplifying the Binance API interactions.
* Thanks to the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library for easy Telegram bot development.
