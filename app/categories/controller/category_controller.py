from sqlalchemy.orm import Session
from app.categories.model.category_model import CategoryModel


class CategoryController:
    def get_categories(self, db: Session):
        return db.query(CategoryModel).all()

    def get_category_by_id(self, db: Session, category_id: int):
        return db.query(CategoryModel).filter_by(id=category_id).first()
