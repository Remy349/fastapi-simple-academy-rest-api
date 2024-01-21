from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.courses.model.course_model import CourseModel


class CourseController:
    def get_courses(self, db: Session):
        return db.query(CourseModel).all()

    def get_course_by_id(self, db: Session, course_id: int):
        course = db.query(CourseModel).filter_by(id=course_id).first()

        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")

        return course

    def delete_course(self, db: Session, course_id: int):
        course = self.get_course_by_id(db, course_id)

        db.delete(course)
        db.commit()

        return
