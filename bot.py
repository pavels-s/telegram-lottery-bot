# ---------------------------------------
# ⚠️ FIRST TIME SETUP INSTRUCTIONS ⚠️
# ---------------------------------------
# 1. Open your terminal / command prompt.
# 2. Run this command to install the required library:
#    pip install pyTelegramBotAPI
#
#    (Note: Do NOT run 'pip install telebot', that is the wrong package!)
# ---------------------------------------

import telebot
import random
import os
from threading import Thread
from flask import Flask

# CONFIGURATION
# Token is now taken from environment variable (secure!)
API_TOKEN = os.environ.get('BOT_TOKEN', '')

bot = telebot.TeleBot(API_TOKEN)

# Flask web server for Render (keeps service alive)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/health')
def health():
    return "OK"

def run_flask():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

bot = telebot.TeleBot(API_TOKEN)

# Global storage
games = {}

# --- TEXTS ---
RULES_TEXT = (
    "👋 **Welcome to the Lottery Bot!**\n\n"
    "📜 *Rules:*\n"
    "1. Send me a list of player names.\n"
    "2. Each name must be on a new line.\n"
    "3. There must be more than 2 names.\n\n"
    "👇 *Please type the names now:*"
)


# --- KEYBOARDS ---

def get_start_keyboard():
    """Button to restart if the user gets lost"""
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = telebot.types.KeyboardButton('🔄 New Game')
    markup.add(btn)
    return markup


def get_game_keyboard():
    """Buttons for the active game"""
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_next = telebot.types.KeyboardButton('🎲 Next Winner')
    btn_finish = telebot.types.KeyboardButton('🏁 Finish & Stats')
    btn_reset = telebot.types.KeyboardButton('🔄 New Game')
    markup.add(btn_next, btn_finish, btn_reset)
    return markup


# --- HANDLERS ---

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    chat_id = message.chat.id
    # Reset game data
    games[chat_id] = {'names': [], 'winners': []}

    # Show rules and the 'New Game' button just in case
    bot.send_message(chat_id, RULES_TEXT, parse_mode='Markdown', reply_markup=get_start_keyboard())


@bot.message_handler(func=lambda m: m.text == '🔄 New Game')
def restart_game(message):
    # Behaves exactly like /start
    send_welcome(message)


@bot.message_handler(func=lambda m: m.text == '🎲 Next Winner')
def next_winner(message):
    chat_id = message.chat.id
    game = games.get(chat_id)

    if not game or not game['names']:
        bot.reply_to(message, "Please send the list of names first.", reply_markup=get_start_keyboard())
        return

    winner = random.choice(game['names'])
    game['winners'].append(winner)

    bot.send_message(chat_id, f"🎉 And the winner is...\n🏆 *{winner}* ", parse_mode='Markdown')


@bot.message_handler(func=lambda m: m.text == '🏁 Finish & Stats')
def finish_game(message):
    chat_id = message.chat.id
    game = games.get(chat_id)

    if not game or not game['winners']:
        bot.send_message(chat_id, "No stats yet. Play first!", reply_markup=get_start_keyboard())
        return

    # Count stats
    stats = {}
    for w in game['winners']:
        stats[w] = stats.get(w, 0) + 1

    stats_msg = "📊 *Lottery Statistics*\n\n"
    for name, count in stats.items():
        stats_msg += f"👤 {name}: {count} win(s)\n"

    # Show stats and button to restart
    bot.send_message(chat_id, stats_msg, parse_mode='Markdown', reply_markup=get_start_keyboard())


# --- MAIN TEXT HANDLER ---
# This captures the names
@bot.message_handler(func=lambda m: True)
def handle_names(message):
    chat_id = message.chat.id
    raw_text = message.text

    # Split names by new line
    if '\n' in raw_text:
        names = [n.strip() for n in raw_text.split('\n') if n.strip()]
    else:
        names = [raw_text.strip()]

    # Validation: If less than 2 names
    if len(names) < 2:
        error_text = "⚠️ **Oops!** I need at least 2 names to start.\n\nPlease type the list again."
        bot.reply_to(message, error_text, parse_mode='Markdown', reply_markup=get_start_keyboard())
        return

    # Success! Start game
    games[chat_id] = {'names': names, 'winners': []}

    bot.send_message(
        chat_id,
        f"✅ Awesome! I found {len(names)} players.\n ⭐️ Let's gooo!",
        reply_markup=get_game_keyboard()
    )


if __name__ == "__main__":
    print("🤖 Bot is running...")
    
    # Start Flask in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Start the bot
    bot.infinity_polling()
