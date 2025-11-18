from pydantic import BaseModel, HttpUrl

class PopularRequest(BaseModel):
    source: str