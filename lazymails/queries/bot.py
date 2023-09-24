from decouple import config
from telegram import Update
from telegram.ext import ContextTypes

from ..controller import chat_controller
from ..helpers.mail import sendMessage
from ..models.entity import Chat


# Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Hello! Use /mail <EMAIL> to set a receiver'
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        In process...
        """
    )


async def mail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text.replace('/mail', '').strip()

    if update.message.chat.type in ['group', 'supergroup']:
        chat_controller.set_mail(
            Chat(id=1, mail=text)
        )
        print(chat_controller.search(Chat(id=1)))


async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text.replace('/settings', '').strip()
    number: int = int(text)

    if update.message.chat.type in ['group', 'supergroup']:
        chat_controller.set_data(
            Chat(id=1, frequency=number)
        )
        print(chat_controller.search(Chat(id=1)))


async def wait(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text.replace('/wait', '').strip()

    if update.message.chat.type in ['group', 'supergroup']:
        chat_controller.set_data(
            Chat(id=1, date=text)
        )
        print(chat_controller.search(Chat(id=1)))


async def now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text.replace('/now', '').strip()

    if update.message.chat.type in ['group', 'supergroup']:
        sendMessage(text)


# Responses
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User {update.message.chat.id} in {message_type}: "{text}"')

    if config('BOT_USERNAME') in text:
        text: str = text.replace(config('BOT_USERNAME'), '').strip()

    response: str = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello! Are you ready for a new meet?'

    if 'how are you' in processed:
        return 'I am good!'

    return r'¯\_(ツ)_/¯'


# Errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
