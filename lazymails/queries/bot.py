from decouple import config
from telegram import Update
from telegram.ext import ContextTypes

from ..controller import chat_controller
from ..models.entity import Chat


# Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Hello! Use /mail <EMAIL> to set a receiver'
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        I can assist you in emailing your lazy instructor...

        To remind them of your group's presence!
        
        Works in private, group and supergroup
        /start - Start the bot
        /help - Show a user manual

        Only for group and supergroup
        /mail <EMAIL> - Set the mail receiver
        /now - Send a mail... NOW

        In develop:
        /settings <1-7> - Set the mail frequency in days
        /wait <year/month/day> - Do not send mail until a date has been reached
        """
    )


async def mail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text.replace('/mail', '').strip()
    chat_id = update.message.chat.id

    if update.message.chat.type in ['group', 'supergroup']:
        response = chat_controller.set_mail(
            Chat(id=chat_id, mail=text)
        )
        chat = Chat(id=chat_id)
        chat_data = chat_controller.search(chat)
        print(chat_data)
        if response:
            message = 'All ok.'
        else:
            message = 'Houston, we have a sleeper.'
        await update.message.reply_text(message)


async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text.replace('/settings', '').strip()
    chat_id = int(update.message.chat.id)

    if update.message.chat.type in ['group', 'supergroup']:
        number: int = int(text)
        chat_controller.set_data(
            Chat(id=chat_id, frequency=number)
        )
        chat = Chat(id=chat_id)
        print(chat_controller.search(chat))
        await update.message.reply_text(chat_controller.search(chat))


async def wait(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text.replace('/wait', '').strip()
    chat_id = int(update.message.chat.id)

    if update.message.chat.type in ['group', 'supergroup']:
        chat_controller.set_data(
            Chat(id=chat_id, date=text)
        )
        chat = Chat(id=chat_id)
        print(chat_controller.search(chat))
        await update.message.reply_text(chat_controller.search(chat))


async def now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type in ['group', 'supergroup']:
        chat_controller.send(Chat(id=1), update.message.chat.title)


# Responses
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User {update.message.chat.id} in {message_type}: "{text}"')

    if message_type == 'group':
        if config('BOT_USERNAME') in text:
            new_text: str = text.replace(config('BOT_USERNAME'), '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello! Are you ready for a new mail?'

    if 'how are you' in processed:
        return 'I am not busy or free, just... Zzz.'

    return r'¯\_(ツ)_/¯'


# Errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
