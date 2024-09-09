from flask import Blueprint, request
from app.bot.handlers import handle_start
import json

bot_webhook = Blueprint('bot_webhook', __name__)


@bot_webhook.route(rule='/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text == '/start':
            handle_start(chat_id)
        return {
            'status': 'ok',
            'chat_id': chat_id,
            'text': text
        }, 200