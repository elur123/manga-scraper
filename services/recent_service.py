import httpx
from bs4 import BeautifulSoup
from requests.recent_request import RecentRequest
from helpers.global_helper import extract_title, extract_thumbnail, extract_chapters

class RecentService:
    async def get_recent_items(self, request: RecentRequest):
        url = str(request.url)

        if(request.page > 1):
            url += 'page/' + str(request.page) + '/'

        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(url, headers={"User-Agent": "MyScraperBot/1.0"})
            response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        recent_items = soup.select(request.item_selector)
        results = []

        for item in recent_items:
            ratings = self.extract_ratings(item, request.rating_selector)
            title = extract_title(item, request.title_selector)
            thumbnail = extract_thumbnail(item, request.thumbnail_selector)
            chapters = extract_chapters(item, request.chapter_selector, request.chapter_link_selector)

            results.append({
                "title": title.get("text"),
                "url": title.get("url"),
                "ratings": float(ratings.get("text")),
                "thumbnail": thumbnail,
                "new_chapters": chapters
            })

        return results
    
    def extract_ratings(self, item, selector):
        tag = item.select_one(selector)
        if tag:
            return {"text": tag.text}
        return {"text": None}
