import httpx
from bs4 import BeautifulSoup
from requests.popular_request import PopularRequest
from helpers.global_helper import extract_title, extract_thumbnail, extract_chapters

class PopularService:
    async def get_popular_items(self, request: PopularRequest):
        url = str(request.url)

        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(url, headers={"User-Agent": "MyScraperBot/1.0"})
            response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        popular_items = soup.select(request.item_selector)
        results = []

        for item in popular_items:
            title = extract_title(item, request.title_selector)
            thumbnail = extract_thumbnail(item, request.thumbnail_selector)
            chapters = extract_chapters(item, request.chapter_selector, request.chapter_link_selector)

            results.append({
                "title": title.get("text"),
                "url": title.get("url"),
                "thumbnail": thumbnail,
                "chapters": chapters
            })

        return results
