import httpx
from bs4 import BeautifulSoup
from requests.manga_detail_request import MangaDetailRequest
from requests.manga_read_request import MangaReadRequest
from requests.search_request import SearchRequest
from helpers.global_helper import extract_title, extract_thumbnail, extract_url_scheme, extract_slug
from helpers.selector_helper import get_selector
class MangaService:
    async def search(self, request: SearchRequest):
        selector = get_selector(request.source)
        selectors = selector._selector("search.json")
        base_url = selectors["based_url"]
        url = f"{base_url}/?s={request.search}&post_type=wp-manga"

        if(request.page > 1):
            url_scheme = extract_url_scheme(url)
            url = f"{url_scheme["scheme"]}://{url_scheme["netloc"]}/page/{request.page}/?{url_scheme["query"]}"

        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(url, headers={"User-Agent": "MyScraperBot/1.0"})
            response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        search_items = soup.select(selectors["item_selector"])
        data = []

        for item in search_items:
            title = extract_title(item, selectors["title_selector"])
            based_url = title.get("url")
            thumbnail = extract_thumbnail(item, selectors["thumbnail_selector"])
            status = item.select_one(selectors["status_selector"])
            latest_chapter = item.select_one(selectors["latest_chapter"])

            data.append({
                "title": title.get("text"),
                "url": based_url,
                "slug": extract_slug(based_url),
                "thumbnail": thumbnail,
                "status": status.text.strip(),
                "latest_chapter": {
                    "text": latest_chapter.text.strip(),
                    "link": latest_chapter['href'],
                    "chapter": extract_slug(latest_chapter['href'])
                }
            })

        return data

    async def get_manga_details(self, request: MangaDetailRequest):
        selector = get_selector(request.source)
        selectors = selector._selector("details.json")
        url = f"{selectors["based_url"]}/{request.manga}/"

        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(url, headers={"User-Agent": "MyScraperBot/1.0"})
            response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        title = soup.select_one(selectors["title_selector"])
        description = soup.select_one(selectors["description_selector"])
        thumbnail = extract_thumbnail(soup, selectors["thumbnail_selector"])
        status = soup.select_one(selectors["status_selector"])

        if description:
            paragraphs = description.find_all("p")
            description_text = " ".join(p.get_text(strip=True) for p in paragraphs)
        else:
            description_text = None

        chapter_items = soup.select(selectors["chapters_selector"])
        chapters = []

        for item in chapter_items:
            if item:
                chapter_title = item.text.strip()
                chapter_url = item["href"]
                chapter_slug = extract_slug(chapter_url, -1)
                if chapter_title:
                    chapters.append({
                        "title": chapter_title,
                        "url": chapter_url,
                        "slug": chapter_slug
                    })

        return {
            "thumbnail": thumbnail,
            "title": title.get_text(strip=True),
            "slug": request.manga,
            "description": description_text,
            "status": status.get_text(strip=True),
            "chapters": chapters
        }
    
    async def read_manga(self, request: MangaReadRequest):
        selector = get_selector(request.source)
        selectors = selector._selector("read.json")
        url = f"{selectors["based_url"]}/{request.manga}/{request.chapter}/"

        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(url, headers={"User-Agent": "MyScraperBot/1.0"})
            response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        images = soup.select(selectors["image_selector"])
        data = []

        for image in images:
            img_src = image["src"]
            if img_src:
                data.append(img_src.strip())

        return data
