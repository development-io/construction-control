from typing import List, Optional
import datetime
from models.сonstruction_objects import Object, ObjectIn
from db.сonstruction_objects import objects
from .base import BaseRepository


class ObjectRepository(BaseRepository):
    async def get_all(self, limit: int = 50, offset: int = 0) -> List[Object]:
        query = objects.select().limit(limit).offset(offset)
        return await self.database.fetch_all(query=query)