from typing import NamedTuple, Optional


class Chat(NamedTuple):
    id: Optional[int] = None
    mail: Optional[str] = None
    frequency: Optional[int] = None
    date: Optional[str] = None
