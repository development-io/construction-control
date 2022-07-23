from typing import List
from models.сonstruction_objects import Object
from repositories.сonstruction_objects import ObjectRepository
from fastapi import APIRouter, Depends, HTTPException, status, Response
from .depends import get_object_repository
from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=List[Object])
async def get_all(
        limit: int = 50,
        offset: int = 0,
        objects: ObjectRepository = Depends(get_object_repository),):
    return await objects.get_all(limit=limit, offset=offset)