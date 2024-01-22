from datetime import datetime
from pydantic import BaseModel, ConfigDict


class CourseBase(BaseModel):
    course_name: str
    course_price_dollar: float


class CourseCreate(CourseBase):
    category_id: int


class Course(CourseBase):
    id: int
    created_at: datetime
    published: bool

    model_config = ConfigDict(from_attributes=True)
