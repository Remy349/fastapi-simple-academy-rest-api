from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.engine import Base


class CourseModel(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    course_name: Mapped[str] = mapped_column(String(300), nullable=False)
    course_price_dollar: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    published: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))

    category = relationship("CategoryModel", back_populates="courses")
