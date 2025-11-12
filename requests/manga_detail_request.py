from pydantic import BaseModel, HttpUrl

class MangaDetailRequest(BaseModel):
    url: HttpUrl
    title_selector: str
    thumbnail_selector: str
    description_selector: str
    chapters_selector: str
    status_selector: str