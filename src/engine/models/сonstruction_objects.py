import datetime
from pydantic import BaseModel


class BaseObject(BaseModel):
    author_id: int
    performer_id: int
    status: str
    term_in_fact: datetime.datetime
    term_to_plan: datetime.datetime

class Object(BaseObject):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

class ObjectIn(BaseObject):
    pass
