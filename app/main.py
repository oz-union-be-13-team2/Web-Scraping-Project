from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.api.v1 import user_question, diary, notification, quote, bookmark, user, question

from app.data import get_random_question
from app.db.database import TORTOISE_ORM
from app.api.v1 import diary, token
from app.api.v1 import user
from app.api.v1 import quote
from app.scraping.quote_scraper import scrape_and_save_quotes

app = FastAPI()

# 라우터 등록
app.include_router(user_question.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/auth")

# # 기존 라우터 포함 (주석 해제 필요)
# app.include_router(diary.router, prefix="/api/v1")
app.include_router(quote.router, prefix="/api/v1")
app.include_router(bookmark.router, prefix="/api/v1")
app.include_router(question.router, prefix="/api/v1")

# DB 연결 (예시: SQLite → PostgreSQL/MySQL 가능)
app.include_router(diary.router)
app.include_router(user.router)
app.include_router(quote.router)
app.include_router(token.router)

# Tortoise와 FastAPI 연결
register_tortoise(
    app,
    db_url="asyncpg://postgres:1234@localhost:5432/fastapi_mini_project",
    modules={
        "models": [
            "app.models.user",
            "app.models.user_question",
            "app.models.quote",
            "app.models.bookmark",
            "app.models.question",
            "app.models.diary",
        ]
    },
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.on_event("startup")
async def startup_event():
    await scrape_and_save_quotes()
@app.get("/")
async def root():
    return {"message": "Hello, FastAPI + TortoiseORM!"}

@app.get("/random_question")
def random_question():
    question = get_random_question()
    return {"question" : question}