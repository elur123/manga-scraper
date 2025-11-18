import httpx
from bs4 import BeautifulSoup
from requests.recent_request import RecentRequest
from helpers.global_helper import extract_title, extract_thumbnail, extract_chapters, extract_slug
from helpers.selector_helper import get_selector

class RecentService:
    async def get_recent_items(self, request: RecentRequest):
        selector = get_selector(request.source)
        selectors = selector._selector("recent.json")
        url = selectors["based_url"]

        if(request.page > 1):
            url += f"/page/{request.page}/"

        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(url, headers={"User-Agent": "MyScraperBot/1.0"})
            response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        recent_items = soup.select(selectors["item_selector"])
        results = []

        for item in recent_items:
            ratings = self.extract_ratings(item, selectors["rating_selector"])
            title = extract_title(item, selectors["title_selector"])
            thumbnail = extract_thumbnail(item, selectors["thumbnail_selector"])
            chapters = extract_chapters(item, selectors["chapter_selector"], selectors["chapter_link_selector"])
            manga_url = title.get("url")
            slug = extract_slug(manga_url)

            results.append({
                "title": title.get("text"),
                "url": manga_url,
                "slug": slug,
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
