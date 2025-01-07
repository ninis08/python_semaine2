from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import validates
from .base import Base  # Base doit être défini dans le fichier Base.py

class Book(Base):
    __tablename__ = 'books'  # Nom de la table dans la base de données

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    tags = Column(Text)  # Stocke les tags sous forme de chaîne de caractères
    numeric = Column(Boolean, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

    def __init__(self, title, author, tags, numeric, price, quantity):
        self.title = title
        self.author = author
        self.tags = tags
        self.numeric = numeric
        self.price = price
        self.quantity = quantity

    # Méthode to_dict pour transformer un objet Book en dictionnaire
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "tags": self.tags,
            "numeric": self.numeric,
            "price": self.price,
            "quantity": self.quantity,
        }

    @classmethod
    def from_dict(cls, data):
        # Créer une instance de Book à partir d'un dictionnaire
        return cls(
            title=data["title"],
            author=data["author"],
            tags=data["tags"],
            numeric=data["numeric"],
            price=data["price"],
            quantity=data["quantity"],
        )

if __name__ == "__main__":
    books = [
        Book("Book 1", "Author 1", "tag1,tag2", False, 12, 5),
        Book("Book 2", "Author 2", "tag2,tag3", True, 5, 5),
        Book("Book 3", "Author 3", "tag1,tag3", False, 8, 5)
    ]
