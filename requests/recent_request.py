from pydantic import BaseModel, HttpUrl

class RecentRequest(BaseModel):
    url: HttpUrl
    page: int
    item_selector: str
    rating_selector: str
    title_selector: str
    thumbnail_selector: str
    chapter_selector: str
    chapter_link_selector: str