from pydantic import BaseModel, HttpUrl

class CategoryRequest(BaseModel):
    url: HttpUrl
    item_selector: str
    title_selector: str