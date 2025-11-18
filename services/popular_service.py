import httpx
from bs4 import BeautifulSoup
from requests.popular_request import PopularRequest
from helpers.global_helper import extract_title, extract_thumbnail, extract_chapters, extract_slug
from helpers.selector_helper import get_selector

class PopularService:
    async def get_popular_items(self, request: PopularRequest):
        selector = get_selector(request.source)
        selectors = selector._selector("popular.json")
        url = selectors["based_url"]

        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(url, headers={"User-Agent": "MyScraperBot/1.0"})
            response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        popular_items = soup.select(selectors["item_selector"])
        results = []

        for item in popular_items:
            title = extract_title(item, selectors["title_selector"])
            thumbnail = extract_thumbnail(item, selectors["thumbnail_selector"])
            chapters = extract_chapters(item, selectors["chapter_selector"], selectors["chapter_link_selector"])
            manga_url = title.get("url")
            slug = extract_slug(manga_url)

            results.append({
                "title": title.get("text"),
                "url": manga_url,
                "slug": slug,
                "thumbnail": thumbnail,
                "chapters": chapters
            })

        return results
