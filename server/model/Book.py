from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, Text, ForeignKey

from .BookShop import BookShop
from .BookCase import BookCase
from .Base import Base

class Book(Base):
    __tablename__ = 'book_book'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    tags: Mapped[str] = mapped_column(Text)  # Stocke les tags comme une chaîne séparée par des virgules
    numeric: Mapped[bool] = mapped_column(Boolean, default=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=0)

    # Clé étrangère et relation avec BookCase
    bookcase_id: Mapped[int] = mapped_column(ForeignKey("book_bookcase.id"), nullable=True)
    bookcase: Mapped["BookCase"] = relationship("BookCase", back_populates="books")

    # Clé étrangère et relation avec BookShop
    bookshop_id: Mapped[int] = mapped_column(ForeignKey("book_bookshop.id"), nullable=True)
    bookshop: Mapped["BookShop"] = relationship("BookShop", back_populates="books")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "tags": self.tags.split(",") if self.tags else [],
            "numeric": self.numeric,
            "price": self.price,
            "quantity": self.quantity,
        }
