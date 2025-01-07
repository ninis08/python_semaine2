from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from .Base import Base

class BookCase(Base):
    __tablename__ = 'book_bookcase'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    location: Mapped[str] = mapped_column(String, nullable=False)

    # Relation inverse
    books: Mapped["Book"] = relationship("Book", back_populates="bookcase")
