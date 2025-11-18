from pydantic import BaseModel, HttpUrl

class RecentRequest(BaseModel):
    source: str
    page: int