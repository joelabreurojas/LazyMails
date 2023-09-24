import re
from pathlib import Path
from typing import List

from ..models.entity import Chat

DATABASE = Path.cwd() / 'mrmeets' / 'database' / 'chat.db'


def fill_data(chat: Chat) -> Chat:
    chat_dict = chat._asdict()
    chat_dict['frequency'] = 0
    chat_dict['date'] = ''

    return Chat(**chat_dict)


def format_chat(chat: Chat, chat_: List[Chat]) -> Chat:
    chat_dict = chat_[0]._asdict()
    print(chat)

    if isinstance(chat.mail, str):
        chat_dict['mail'] = chat.mail

    if isinstance(chat.frequency, int):
        chat_dict['frequency'] = chat.frequency

    if isinstance(chat.date, str):
        chat_dict['date'] = chat.date

    return Chat(
        id=chat_dict['id'],
        mail=chat_dict['mail'],
        frequency=chat_dict['frequency'],
        date=chat_dict['date']
    )


def mail_is_valid(mail: str) -> bool:
    if not isinstance(mail, str):
        return False

    regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    return bool(re.search(regex, mail))


def reset_database():
    if DATABASE.exists():
        DATABASE.unlink()

    DATABASE.touch()
