from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from app.courses.controller.course_controller import CourseController
from app.db.engine import get_db
from app.schemas.course_schema import Course, CreateCourse

router = APIRouter()

course_controller = CourseController()


@router.get(
    "/courses",
    status_code=HTTP_200_OK,
    response_model=list[Course],
)
def get_courses(db: Session = Depends(get_db)):
    return course_controller.get_courses(db)


@router.post(
    "/courses",
    status_code=HTTP_201_CREATED,
    response_model=Course,
)
def create_course(course_data: CreateCourse):
    return


@router.get(
    "/courses/{course_id}",
    status_code=HTTP_200_OK,
    response_model=Course,
)
def get_course_by_id(course_id: int, db: Session = Depends(get_db)):
    return course_controller.get_course_by_id(db, course_id)


@router.delete(
    "/courses/{course_id}",
    status_code=HTTP_204_NO_CONTENT,
    response_model=None,
)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    return course_controller.delete_course(db, course_id)
