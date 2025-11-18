from pydantic import BaseModel, HttpUrl

class MangaDetailRequest(BaseModel):
    source: str
    manga: str