from aiogram import Bot, Dispatcher, executor, types
# from models.сonstruction_objects import Object
from fastapi import APIRouter

import logging
import requests
import os

logging.basicConfig(level=logging.INFO)

router = APIRouter()

bot = Bot(token=os.getenv('BOT_TOKEN_API', default=None))
dp = Dispatcher(bot)

# @router.get("/", response_model=List[Object])
@dp.message_handler()
async def echo_message(msg: types.Message):
    tmpl = 'Test'
    await bot.send_message(msg.from_user.id, tmpl)


# @dp.message_handler(commands=['master'])
# async def send_welcome(message: types.Message):
#     await message.answer("Мастер уже в пути!")


# @dp.message_handler(commands=['cleaning'])
# async def send_welcome(message: types.Message):
#     await message.answer("Клининг вызван!")


# @dp.message_handler(commands=['car_wash'])
# async def send_welcome(message: types.Message):
#     await message.answer("Автомойка оплачена!")


# @dp.message_handler(commands=['concierge'])
# async def send_welcome(message: types.Message):
#     await message.answer("НУЖНО РЕАЛИЗОВАТЬ!!!")


# @dp.message_handler(commands=['food'])
# async def send_welcome(message: types.Message):
#     await message.answer("НУЖНО РЕАЛИЗОВАТЬ!!!")


# @dp.message_handler()
# async def send_welcome(message: types.Message):
#     await message.answer("Неверная команда.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
