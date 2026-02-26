from telegram.ext import Application, CommandHandler

TOKEN = "8498085251:AAGIFVWOYjVQ9PCOxR6po086yNMueI9kI3M"

async def start(update, context):
    await update.message.reply_text("Bot live hai 😎🔥")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
