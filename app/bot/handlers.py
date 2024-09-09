from app.bot.services import send_message


def handle_start(chat_id):
    start_text = "Selamat datang di Bot Kotaksuratku!"

    send_message(chat_id, start_text)