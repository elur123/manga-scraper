from pydantic import BaseModel, HttpUrl

class SearchRequest(BaseModel):
    source: str
    search: str
    page: int