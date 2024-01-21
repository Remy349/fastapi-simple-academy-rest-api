from fastapi import FastAPI
from app.core.config import settings

from app.categories.api.category_api import router as category_api
from app.courses.api.course_api import router as course_api

app = FastAPI()

app.title = settings.API_TITLE
app.version = settings.API_VERSION

app.include_router(category_api, prefix="/api/v1", tags=["categories"])
app.include_router(course_api, prefix="/api/v1", tags=["courses"])
