import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import TELEGRAM_TOKEN
from sheets_handler import save_user_data
from gpt_module import generate_profile

logging.basicConfig(level=logging.INFO)
user_states = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ברוך הבא לשידוך AI! כדי להתחיל, כתוב /new")

async def new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_states[user_id] = {"step": "age"}
    await update.message.reply_text("בן כמה אתה?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text
    state = user_states.get(user_id, {})

    if not state:
        await update.message.reply_text("התחל עם /new")
        return

    if state["step"] == "age":
        state["age"] = text
        state["step"] = "city"
        await update.message.reply_text("מאיזו עיר אתה?")
    elif state["step"] == "city":
        state["city"] = text
        state["step"] = "summary"
        profile = generate_profile(state)
        save_user_data(user_id, state)
        await update.message.reply_text(f"כרטיס מוכן:

{profile}

להצעות נוספות – המשך מעקב כאן.")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("new", new))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
