from sqlalchemy.orm import Session
from model.Book import Book
from model.Base import SessionLocal, engine

# Assurez-vous que toutes les tables sont créées
def create_tables():
    from model.Base import Base
    Base.metadata.create_all(bind=engine)
    print("Tables créées.")

# Insérer des livres dans la base de données
def insert_books():
    with SessionLocal() as session:
        books = [
            Book(
                title="Le Petit Prince",
                author="Antoine de Saint-Exupéry",
                tags="philosophie,enfants",
                numeric=False,
                price=10,
                quantity=5,
                bookcase_id=1,  # Ces IDs doivent exister dans les tables liées
                bookshop_id=1
            ),
            Book(
                title="1984",
                author="George Orwell",
                tags="dystopie,politique",
                numeric=True,
                price=15,
                quantity=3,
                bookcase_id=1,
                bookshop_id=1
            ),
        ]
        session.add_all(books)
        session.commit()
        print("Livres insérés avec succès.")

# Vérifier les données insérées
def fetch_books():
    with SessionLocal() as session:
        books = session.query(Book).all()
        for book in books:
            print(book.to_dict())

if __name__ == "__main__":
    create_tables()
    insert_books()
    print("\n=== Livres dans la base ===")
    fetch_books()
