from typing import List

from ..database import chat_db
from ..helpers import util
from ..models.entity import Chat


def set_mail(chat_: Chat):
    if not chat_db.chat_exists(chat_):
        chat = util.fill_data(chat_)
        chat_db.create(chat)
    else:
        chat = search(chat_)
        chat = util.format_chat(chat_, chat)
        chat_db.update(chat)


def set_data(chat: Chat) -> bool:
    if not chat_db.chat_exists(chat):
        return False

    chat_ = search(chat)
    chat = util.format_chat(chat, chat_)
    chat_db.update(chat)
    return True


def search(chat: Chat) -> List[Chat]:
    return chat_db.search(chat)


def reset():
    util.reset_database()
    chat_db.reset_table()
