import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("BOT_TOKEN")

app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Men ChatGPT uslubidagi botman 🤖")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Siz yozdingiz: " + update.message.text)

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Bot ishga tushdi...")
app.run_polling()
