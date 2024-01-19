from fastapi import FastAPI

from app.routers.category import router as category_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.title = "Simple Academy REST API"
    app.version = "v1"

    app.include_router(category_router, prefix="/api/v1")

    return app
