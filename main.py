from fastapi import FastAPI
from requests.category_request import CategoryRequest
from requests.popular_request import PopularRequest
from requests.recent_request import RecentRequest
from requests.manga_detail_request import MangaDetailRequest

from controllers.category_controller import CategoryController
from controllers.popular_controller import PopularController
from controllers.recent_controller import RecentController
from controllers.manga_controller import MangaController

app = FastAPI(title="Simple Scraper API")

category_controller = CategoryController()
recent_controller = RecentController()
popular_controller = PopularController()
manga_controller = MangaController()

@app.post("/categories")
async def categories(request: CategoryRequest):
    return await category_controller.list(request)

@app.post("/recent")
async def recent(request: RecentRequest):
    return await recent_controller.list(request)

@app.post("/popular")
async def popular(request: PopularRequest):
    return await popular_controller.list(request)

@app.post("/manga-details")
async def manga_details(request: MangaDetailRequest):
    return await manga_controller.details(request)

@app.get("/")
async def root():
    return {"message": "Welcome to the Simple Scraper API"}
