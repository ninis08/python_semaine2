from sqlalchemy import create_engine
from model.Base import Base
from model.Book import Book  # Assurez-vous que Book inclut les colonnes supplémentaires

# Configurer l'URL de la base de données
DATABASE_URL = "postgresql://user:password@localhost:6543/books_db"
engine = create_engine(DATABASE_URL)

def create_tables():
    """
    Crée la table 'book' définie dans le modèle SQLAlchemy.
    """
    print("Création des tables dans la base de données...")
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables créées avec succès !")
    except Exception as e:
        print(f"Erreur lors de la création des tables : {e}")

def drop_tables():
    """
    Supprime toutes les tables dans la base de données.
    """
    print("Suppression des tables...")
    try:
        Base.metadata.drop_all(bind=engine)
        print("Tables supprimées avec succès !")
    except Exception as e:
        print(f"Erreur lors de la suppression des tables : {e}")

if __name__ == "__main__":
    drop_tables()  # Supprime les anciennes tables pour éviter les conflits
    create_tables()  # Recrée les tables
