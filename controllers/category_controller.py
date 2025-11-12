from fastapi import HTTPException
import httpx
from requests.category_request import CategoryRequest
from services.category_service import CategoryService

class CategoryController:
    def __init__(self):
        self.category_service = CategoryService()

    async def list(self, request: CategoryRequest):
        try:
            data = await self.category_service.get_category_items(request)
            return {
                "status": "success",
                "data": data,
                "status_code": 200
            }

        except httpx.RequestError as e:
            raise HTTPException(status_code=400, detail=f"Request error: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")