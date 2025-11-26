# 🎲 Telegram Name Randomizer Bot

> **Hello!** This is my first telegram bot. I'm learning Python and wanted to create something practical that could be useful in real life. 
> This bot helps randomly select names from a list - perfect for giveaways or making fair decisions. So, it's always lottery :)
> 
> This bot is hosted for free on https://www.render.com (dashboard: https://telegram-lottery-bot-kfwz.onrender.com/)
> To keep this bot "alive" I am using UptimeRobot (dashboard: https://stats.uptimerobot.com/JPnnkOWUZi)

# 🎰 Simple Lottery Telegram Bot

A lightweight and easy-to-use Telegram bot written in Python. Code is documented and beginner-friendly for understanding.
It allows users to input a list of names and randomly select winners for raffles, lotteries, or giveaways.

## ✨ Features

* **Simple Input:** Just paste a list of names (each on a new line).
* **Random Selection:** Fairly picks a winner from the provided list.
* **Statistics:** Tracks how many times each person won during the current session.
* **Input Validation:** Ensures there are at least 2 players before starting.
* **User Friendly:** Interactive buttons (Next Winner, Finish & Stats, New Game).

## 🛠 Prerequisites

* Python 3.x installed on your system.
* A Telegram Bot Token (from [@BotFather](https://t.me/BotFather)).

## 📦 Installation

1.  **Clone the repository** (or download the files):
    ```bash
    git clone [https://github.com/your-username/lottery-bot.git](https://github.com/your-username/lottery-bot.git)
    cd lottery-bot
    ```

2.  **Install the required library:**
    This bot uses `pyTelegramBotAPI`.
    ```bash
    pip install pyTelegramBotAPI
    ```

3.  **Configuration:**
    * Open the `bot.py` (or `main.py`) file in your code editor.
    * Find the line: `API_TOKEN = 'YOUR_TOKEN_HERE'`
    * Replace `'YOUR_TOKEN_HERE'` with your actual Telegram Bot Token.

    > **⚠️ Security Note:** Never publish your bot token publicly on GitHub or other websites.

### 🚀 How to Run the Bot

1.  **Open your Terminal** (or Command Prompt/CMD on Windows).
2.  **Navigate** to the folder where you saved your `bot.py` file.
    *Example:*
    ```bash
    cd /path/to/your/lottery-bot-folder
    ```
3.  **Execute the script** using Python:
    ```bash
    python bot.py
    ```
    The bot will now start listening for messages, and you should see the message: `Bot is running...`


### 🛑 How to Stop the Bot (CLI)

If you run the bot using `python bot.py`, it will run indefinitely in your console (using `bot.infinity_polling()`).

To stop the running process:

1.  Make sure the **Command Prompt** or **Terminal** window where the bot is running is active.
2.  Press the key combination: **Ctrl + C**.

The bot process will be immediately terminated, and you will return to the command line prompt.


And good luck at your lottery! 

  
