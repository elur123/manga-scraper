import httpx
from bs4 import BeautifulSoup
from requests.manga_detail_request import MangaDetailRequest
from helpers.global_helper import extract_title, extract_thumbnail

class MangaService:
    async def get_manga_details(self, request: MangaDetailRequest):
        url = str(request.url)

        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(url, headers={"User-Agent": "MyScraperBot/1.0"})
            response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        title = soup.select_one(request.title_selector)
        description = soup.select_one(request.description_selector)
        thumbnail = extract_thumbnail(soup, request.thumbnail_selector)
        status = soup.select_one(request.status_selector)

        if description:
            paragraphs = description.find_all("p")
            description_text = " ".join(p.get_text(strip=True) for p in paragraphs)
        else:
            description_text = None

        chapter_items = soup.select(request.chapters_selector)
        chapters = []

        for item in chapter_items:
            if item:
                chapter_title = item.text.strip()
                chapter_url = item["href"]
                if chapter_title:
                    chapters.append({
                        "title": chapter_title,
                        "url": chapter_url
                    })

        return {
            "thumbnail": thumbnail,
            "title": title.get_text(strip=True),
            "description": description_text,
            "status": status.get_text(strip=True),
            "chapters": chapters
        }
