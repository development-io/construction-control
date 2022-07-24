from fastapi import APIRouter

import logging
import requests
import os

router = APIRouter()

token = os.getenv('BOT_TOKEN_API', default=None)

@router.get("/act")
async def echo_bot():
    response = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()
    if response.get('result') is not None:
        send_msg = """
Новое уведомление:
ЖК "Мечта"
Отделочные работы - 2 этап
Акт приемки подписан заказчиком"""
        chat_id = 371519970
        msg = requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={send_msg}").json()
        return msg

@router.get("/new_task")
async def echo_bot():
    response = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()
    if response.get('result') is not None:
        send_msg = """
Новая задача
ЖК "Мечта"
Этаж 2 Подъезд 2
Установка унитазов
Начало 31.12.2022
Готовность 01.01.2023"""
        chat_id = 371519970
        msg = requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={send_msg}").json()
        return msg
    
@router.get("/new_incident")
async def echo_bot():
    response = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()
    if response.get('result') is not None:
        send_msg = """
Новая задача
ЖК "Мечта"
Этаж 2 Подъезд 2
Установка унитазов
Начало 31.12.2022
Готовность 01.01.2023"""
        chat_id = 371519970
        msg = requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={send_msg}").json()
        return msg

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
    
