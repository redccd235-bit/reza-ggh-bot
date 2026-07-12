import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات فعال شد ✔️")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("دستورهای موجود:\n/start\n/help")

def main():
    import os
    token = os.getenv("TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))

    app.run_polling()

if __name__ == "__main__":
    main()
