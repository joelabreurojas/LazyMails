from .bot import (
    start,
    help,
    mail,
    settings,
    wait,
    now,
    handle_message,
    error
)
from decouple import config
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)


def create_bot():
    print('Startting bot...')
    app = Application.builder().token(config('BOT_TOKEN')).build()

    # Commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('mail', mail))
    app.add_handler(CommandHandler('settings', settings))
    app.add_handler(CommandHandler('wait', wait))
    app.add_handler(CommandHandler('now', now))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling()
