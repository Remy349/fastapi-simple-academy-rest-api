from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from app.categories.controller.category_controller import CategoryController
from app.db.engine import get_db
from app.schemas.category_schema import Category, CategoryCreate

router = APIRouter()

category_controller = CategoryController()


@router.get(
    "/categories",
    status_code=HTTP_200_OK,
    response_model=list[Category],
)
def get_categories(db: Session = Depends(get_db)):
    return category_controller.get_categories(db)


@router.post(
    "/categories",
    status_code=HTTP_201_CREATED,
    response_model=Category,
)
def create_category(category_data: CategoryCreate, db: Session = Depends(get_db)):
    return category_controller.create_category(db, category_data)


@router.get(
    "/categories/{category_id}",
    status_code=HTTP_200_OK,
    response_model=Category,
)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    return category_controller.get_category_by_id(db, category_id)


@router.delete(
    "/categories/{category_id}",
    status_code=HTTP_204_NO_CONTENT,
    response_model=None,
)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return category_controller.delete_category(db, category_id)
