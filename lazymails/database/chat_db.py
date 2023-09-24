from typing import Any, List

from ..models.entity import Chat
from .connection import fetch_all, fetch_none, fetch_one


def create(chat: Chat):
    query = """
        INSERT INTO chats
        VALUES (:id, :mail, :frequency, :date)
    """

    parameters = chat._asdict()
    fetch_none(query, parameters)


def update(chat: Chat):
    query = """
        UPDATE chats
        SET mail = :mail, frequency = :frequency, date = :date
        WHERE id = :id
    """

    parameters = chat._asdict()
    fetch_none(query, parameters)


def search(chat: Chat) -> List[Chat]:
    query = 'SELECT * FROM chats WHERE id LIKE ?'
    parameters = f'%{chat.id}%'

    records = fetch_all(query, parameters)

    return __package_data(records)


def reset_table():
    query = 'DROP TABLE IF EXISTS chats'
    fetch_none(query)

    fields = '(id int, mail text, frequency int, date text)'

    query = f'CREATE TABLE IF NOT EXISTS chats {fields}'
    fetch_none(query)


def chat_exists(chat: Chat) -> bool:
    query = 'SELECT id FROM chats WHERE id LIKE ?'
    parameters = chat.id

    record = fetch_one(query, parameters)

    return bool(record)


def __package_data(records: List[Any]) -> List[Chat]:
    chats: List[Chat] = list()

    for record in records:
        chat = Chat(
            id=record[0],
            mail=record[1],
            frequency=record[2],
            date=record[3],
        )
        chats.append(chat)

    return chats
