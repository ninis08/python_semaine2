from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from typing import List
from .Base import Base

class BookShop(Base):
    __tablename__ = 'book_bookshop'

    id: Mapped[int] = mapped_column(primary_key=True)
    shop_name: Mapped[str] = mapped_column(String())

    # Relation avec Book
    books: Mapped["Book"] = relationship("Book", back_populates="bookshop")
