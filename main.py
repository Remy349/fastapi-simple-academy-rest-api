from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

app = FastAPI()

app.title = "Simple Academy REST API"
app.version = "v1"


class Category(BaseModel):
    id: int
    category_name: str
    created_at: datetime = datetime.utcnow()


categories: list[Category] = []


@app.get(
    "/v1/categories",
    status_code=HTTP_200_OK,
    response_model=list[Category],
)
async def get_categories():
    return categories


@app.post(
    "/v1/categories",
    status_code=HTTP_201_CREATED,
    response_model=Category,
)
async def create_category(category_data: Category):
    category = Category(
        id=category_data.id,
        category_name=category_data.category_name,
    )

    categories.append(category)

    return category


@app.get(
    "/v1/categories/{category_id}",
    status_code=HTTP_200_OK,
    response_model=Category,
)
async def get_category_by_id(category_id: int):
    for category in categories:
        if category.id == category_id:
            return category

    raise HTTPException(status_code=404, detail="Category not found")


@app.delete(
    "/v1/categories/{category_id}",
    status_code=HTTP_204_NO_CONTENT,
    response_model=None,
)
async def delete_category_by_id(category_id: int):
    for index, category in enumerate(categories):
        if category.id == category_id:
            categories.pop(index)

            return

    raise HTTPException(status_code=404, detail="Category not found")
