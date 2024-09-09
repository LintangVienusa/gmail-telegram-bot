from flask import Flask
from app.bot.webhook import bot_webhook


def create_app():
    app = Flask(__name__)

    app.register_blueprint(bot_webhook, url_prefix='/bot')

    return app