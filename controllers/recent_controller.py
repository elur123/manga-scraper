from fastapi import HTTPException
import httpx
from requests.recent_request import RecentRequest
from services.recent_service import RecentService

class RecentController:
    def __init__(self):
        self.recent_service = RecentService()

    async def list(self, request: RecentRequest):
        try:
            data = await self.recent_service.get_recent_items(request)
            return {
                "status": "success",
                "data": data,
                "status_code": 200
            }

        except httpx.RequestError as e:
            raise HTTPException(status_code=400, detail=f"Request error: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")