from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.api.v1 import user_question, diary, notification, quote, bookmark, user, question
app = FastAPI()

# 라우터 등록
app.include_router(user_question.router, prefix="/api/v1")
app.include_router(notification.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")

# # 기존 라우터 포함 (주석 해제 필요)
# app.include_router(diary.router, prefix="/api/v1")
app.include_router(quote.router, prefix="/api/v1")
app.include_router(bookmark.router, prefix="/api/v1")
app.include_router(question.router, prefix="/api/v1")

# DB 연결 (예시: SQLite → PostgreSQL/MySQL 가능)
app.include_router(diary.router)
app.include_router(user.router)

# Tortoise와 FastAPI 연결
register_tortoise(
    app,
    db_url="asyncpg://a:0000@localhost:5432/postgres",
    modules={
        "models": [
            "app.models.user",
            "app.models.user_question",
            "app.models.notification",
            "app.models.quote",
            "app.models.bookmark",
            "app.models.question",
            "app.models.diary",
        ]
    },
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}
