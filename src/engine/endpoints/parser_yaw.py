import requests

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_weather():
    headers = {"Content-Type": "application/json; charset=utf-8", "X-Yandex-API-Key": "fb36aa7c-cc86-4e4b-a4cd-3587e57a5f02"}

    lat_value = '45.035470'
    lon_value = '38.975313'
    lang = 'ru_RU'

    url_api = 'https://api.weather.yandex.ru/v2/informers?lat={lat_value}&lon={lon_value}&lang={lang}'
    url_pogoda = 'https://yandex.ru/pogoda/35?page=main&day=&ta_features=favorites%3Bsgn&turboapp=1'

    response = requests.get(url_api, headers=headers)
    city = "Краснодар +27"
    description = "Вероятность осадков: 6%, Влажность: 52%, Ветер: 2 м/с"

    return {"result": [{ 'city': city, 'details_info': description}]}