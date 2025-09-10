from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.db.database import TORTOISE_ORM
from app.api.v1 import diary, token
from app.api.v1 import user

app = FastAPI()

app.include_router(diary.router)
app.include_router(user.router)
app.include_router(token.router)

# Tortoise와 FastAPI 연결
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,  # 마이그레이션은 aerich가 관리하므로 False
    add_exception_handlers=True,
)



@app.get("/")
async def root():
    return {"message": "Hello, FastAPI + TortoiseORM!"}