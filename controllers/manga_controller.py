from fastapi import HTTPException
import httpx
from requests.manga_detail_request import MangaDetailRequest
from services.manga_service import MangaService

class MangaController:
    def __init__(self):
        self.manga_service = MangaService()

    async def details(self, request: MangaDetailRequest):
        try:
            data = await self.manga_service.get_manga_details(request)
            return {
                "status": "success",
                "data": data,
                "status_code": 200
            }

        except httpx.RequestError as e:
            raise HTTPException(status_code=400, detail=f"Request error: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")