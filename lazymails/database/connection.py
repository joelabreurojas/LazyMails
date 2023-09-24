import sqlite3
from contextlib import contextmanager
from typing import Any, Dict, Iterator, List, Optional

from ..helpers import util


def fetch_all(query: str, parameters: Optional[Any] = None) -> List[Any]:
    with __get_cursor() as cursor:
        if parameters is None:
            cursor.execute(query)
        else:
            cursor.execute(query, [parameters])
        return cursor.fetchall()


def fetch_one(query: str, parameters: str) -> Any:
    with __get_cursor() as cursor:
        cursor.execute(query, [parameters])
        return cursor.fetchone()


def fetch_none(query: str, parameters: Optional[Dict[str, Any]] = None):
    with __get_cursor() as cursor:
        if parameters is None:
            cursor.execute(query)
        else:
            cursor.execute(query, parameters)


@contextmanager
def __get_cursor() -> Iterator[sqlite3.Cursor]:
    connection: sqlite3.Connection = sqlite3.connect(util.DATABASE)
    cursor: sqlite3.Cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    finally:
        cursor.close()
        connection.close()
