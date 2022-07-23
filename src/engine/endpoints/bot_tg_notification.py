from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from fastapi import APIRouter

import requests
import os

router = APIRouter()

# @router.get("/")
# async def notificate(message: str):
#     """
#     Нотификация в телеграм
#     """
#     return {"result": [{"created": true, "created_at": datetime}]}
 

# bot = Bot(token=os.getenv(key, default=None))
# dp = Dispatcher(bot)

# @dp.message_handler()
# async def echo_send(message: types.Message):
#     await message

# executor.start_polling(dp, skip_updates=True)

# print('sds')