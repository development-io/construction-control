import datetime
from pydantic import BaseModel


class BaseObject(BaseModel):
    author: str
    performer: str
    status: str
    bot_tg_enabled: bool = None
    closed: bool = None
    term_in_fact: datetime.datetime
    term_to_plan: datetime.datetime

class Object(BaseObject):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

class ObjectIn(BaseObject):
    pass
