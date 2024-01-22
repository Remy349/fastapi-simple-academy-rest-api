from datetime import datetime
from pydantic import BaseModel, ConfigDict

from app.schemas.course_schema import Course


class CategoryBase(BaseModel):
    category_name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    created_at: datetime
    courses: list[Course]

    model_config = ConfigDict(from_attributes=True)
