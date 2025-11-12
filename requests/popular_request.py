from pydantic import BaseModel, HttpUrl

class PopularRequest(BaseModel):
    url: HttpUrl
    item_selector: str
    title_selector: str
    thumbnail_selector: str
    chapter_selector: str
    chapter_link_selector: str