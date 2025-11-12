from fastapi import HTTPException
import httpx
from requests.popular_request import PopularRequest
from services.popular_service import PopularService

class PopularController:
    def __init__(self):
        self.popular_service = PopularService()

    async def list(self, request: PopularRequest):
        try:
            data = await self.popular_service.get_popular_items(request)

            return {
                "status": "success",
                "data": data,
                "status_code": 200
            }

        except httpx.RequestError as e:
            raise HTTPException(status_code=400, detail=f"Request error: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")