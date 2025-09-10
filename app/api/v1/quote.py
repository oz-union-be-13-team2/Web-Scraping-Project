import random
from fastapi import APIRouter, HTTPException

from app.models.quote import Quote
from app.scraping.quote_scraper import scrape_and_save_quotes

router = APIRouter(prefix="/quotes", tags=["quotes"])

@router.post("/scrape")
async def scrape_quote():
    await scrape_and_save_quotes()
    return {"message" : "스크래핑 완료!"}

@router.get("/random_quote")
async def get_random_quote():
    count = await Quote.all().count()
    if count == 0:
        raise HTTPException(status_code=404, detail="명언이 없습니다.")

    offset = random.randint(0, count - 1)
    quote = await Quote.all().offset(offset).first()
    return {"id": quote.quote_id, "text": quote.content, "author": quote.author}
