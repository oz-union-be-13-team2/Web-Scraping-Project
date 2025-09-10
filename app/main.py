from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.data import get_random_question
from app.db.database import TORTOISE_ORM
from app.api.v1 import diary
from app.api.v1 import user
from app.api.v1 import quote
from app.scraping.quote_scraper import scrape_and_save_quotes

app = FastAPI()

app.include_router(diary.router)
app.include_router(user.router)
app.include_router(quote.router)

# Tortoise와 FastAPI 연결
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,  # 마이그레이션은 aerich가 관리하므로 False
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