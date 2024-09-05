from app import app
from flask import request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot, None, use_context=True)


def start_bot(update, context):
    update.message.reply_text('Welcome to Mailbox Bot')


dispatcher.add_handler(CommandHandler('start', start))


@app.route('/webhook', method=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot=bot)
    dispatcher.process_update(update)

    return 'ok'