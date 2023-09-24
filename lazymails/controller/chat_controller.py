from typing import List

from ..database import chat_db
from ..helpers import mail, util
from ..models.entity import Chat


def set_mail(chat_: Chat) -> bool:
    if not util.mail_is_valid(chat_.mail):
        return False

    if not chat_db.chat_exists(chat_):
        chat = util.fill_data(chat_)
        chat_db.create(chat)
    else:
        chat = search(chat_)
        chat = util.format_chat(chat_, chat)
        chat_db.update(chat)

    return True


def set_data(chat: Chat) -> bool:
    if not chat_db.chat_exists(chat):
        return False

    chat_ = search(chat)
    chat = util.format_chat(chat, chat_)
    chat_db.update(chat)
    return True


def search(chat: Chat) -> List[Chat]:
    return chat_db.search(chat)


def send(chat: Chat, group: str):
    chat_ = search(chat)
    mail.sendMessage(chat_[0].mail, group)
    print('Mail sent!')


def reset():
    util.reset_database()
    chat_db.reset_table()
