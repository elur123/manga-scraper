from pydantic import BaseModel, HttpUrl

class MangaReadRequest(BaseModel):
    source: str
    manga: str
    chapter: str