import requests

from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def create():
    return {"result": [{"created": true, "created_at": datetime}]}


@router.get("/")
async def get_all():
    return {"result": [{"created": true, "created_at": datetime}]}