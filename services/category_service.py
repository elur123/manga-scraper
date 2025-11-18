import httpx
from bs4 import BeautifulSoup
from requests.category_request import CategoryRequest
from helpers.global_helper import extract_title, extract_thumbnail, extract_chapters
from helpers.selector_helper import get_selector

class CategoryService:
    async def get_category_items(self, request: CategoryRequest):
        selector = get_selector(request.source)
        selectors = selector._selector("category.json")
        url = selectors["based_url"]

        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(url, headers={"User-Agent": "MyScraperBot/1.0"})
            response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        recent_items = soup.select(selectors["item_selector"])
        results = []

        for item in recent_items:
            title = extract_title(item, selectors["title_selector"])

            results.append({
                "title": title.get("text"),
                "url": title.get("url"),
            })

        return results
