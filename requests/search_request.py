from pydantic import BaseModel, HttpUrl

class SearchRequest(BaseModel):
    url: HttpUrl
    page: int
    item_selector: str
    rating_selector: str
    title_selector: str
    thumbnail_selector: str
    status_selector: str
    latest_chapter: str