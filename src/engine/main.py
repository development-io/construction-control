from fastapi import FastAPI
from db.base import database
from domain import parser_yaw
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
# app.include_router(banks.router, prefix="/api/banks", tags=["banks"])
#fb36aa7c-cc86-4e4b-a4cd-3587e57a5f02

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", port=80, host="0.0.0.0", reload=True)