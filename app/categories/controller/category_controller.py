from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.categories.model.category_model import CategoryModel
from app.schemas.category_schema import CategoryCreate


class CategoryController:
    def get_categories(self, db: Session):
        return db.query(CategoryModel).all()

    def get_category_by_id(self, db: Session, category_id: int):
        category = db.query(CategoryModel).filter_by(id=category_id).first()

        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")

        return category

    def get_courses_in_category_by_id(self, db: Session, category_id: int):
        category = self.get_category_by_id(db, category_id)

        return category.courses

    def create_category(self, db: Session, category_data: CategoryCreate):
        category = CategoryModel(**category_data.model_dump())

        try:
            db.add(category)
            db.commit()
            db.refresh(category)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Category already registered")

        return category

    def delete_category(self, db: Session, category_id: int):
        category = self.get_category_by_id(db, category_id)

        db.delete(category)
        db.commit()

        return
