from fastapi import FastAPI
from db.base import database
from endpoints import parser_yaw, task_manager, filters, bot_tg_notification
import uvicorn

app = FastAPI(
    title="Hackathon INDEV API",
    description="Техническая документация платформы",
    contact={
        "name": "Алиев Сулейман Алиевич",
        "url": "https://t.me/GoDevelopment",
        "email": "godevup@mail.ru",
    },
    docs_url="/docs",
    openapi_url='/api/openapi.json'
)

app.include_router(parser_yaw.router, prefix="/api/pogoda", tags=["Погода"])
app.include_router(task_manager.router, prefix="/api/task/list", tags=["Менеджер тасков"])
app.include_router(filters.router, prefix="/api/filters", tags=["Фильтрация"])
app.include_router(bot_tg_notification.router, prefix="/api/tg", tags=["Нотификация в телеграм бот"])

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", port=80, host="0.0.0.0", reload=True)