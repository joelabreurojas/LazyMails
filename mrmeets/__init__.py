from .bot import start_command, help_command, custom_command, handle_message, error
from decouple import config
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from typing import Final

BOT_TOKEN: Final = config('TOKEN')


def create_bot():
    print('Startting bot...')
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
