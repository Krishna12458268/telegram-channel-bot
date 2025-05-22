import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Directly hardcode your bot token here
TOKEN = "7718821913:AAEgDmZmevfua0NWLf1HEPM-4oOfNM8bVeo"
CHANNEL_LINK = "https://t.me/tradewithshuklaofficial"  # Replace with your channel link

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("👉 Join Our Channel", url=CHANNEL_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome! Click the button below to join our official Telegram channel 👇",
        reply_markup=reply_markup
    )

# Create the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Register the /start command handler
app.add_handler(CommandHandler("start", start))

# Run the bot
if __name__ == "__main__":
    print("🤖 Bot is running...")
    app.run_polling()
