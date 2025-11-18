from pydantic import BaseModel, HttpUrl

class CategoryRequest(BaseModel):
    source: str