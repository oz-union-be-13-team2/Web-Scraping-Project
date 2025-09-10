import re

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from tortoise.transactions import in_transaction

from app.models.quote import Quote

URL = "https://blog.naver.com/handa1489/223815369987"

async def scrape_and_save_quotes():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(URL)

        frame = page.frame(name="mainFrame")
        if not frame:
            print("iframe not found")
            return

        content = await frame.content()
        soup = BeautifulSoup(content, "html.parser")

        pattern = re.compile(r"“.*?”")
        raw_quotes = [q.get_text(strip=True) for q in soup.select("span[id^='SE-']")]
        quotes = [q for q in raw_quotes if pattern.match(q)]

        async with in_transaction() as connection:
            for text in quotes:
                if not await Quote.exists(content=text):
                    await Quote.create(
                        content=text,
                        author="알 수 없음",
                        language="ko",
                        source="네이버 블로그"
                    )
        print(f"{len(quotes)}개의 명언을 저장했습니다.")

