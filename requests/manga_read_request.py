from pydantic import BaseModel, HttpUrl

class MangaReadRequest(BaseModel):
    url: HttpUrl
    image_selector: str