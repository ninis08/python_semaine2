from model.BookShop import BookShop
from model.User import User
from model.Book import Book
import os

import jsonpickle

class Application:

    __json_file = "application-bib.json"

    def __init__(self):
        self.__user = User('admin')
        self.__bookshop = BookShop()

    def save_in_json(self):
        with open(self.__json_file, "w") as f:
            f.write(jsonpickle.encode(self))

    def reload(self):
        if not os.path.exists(self.__json_file):
            print(f'Fichier {self.__json_file} introuvable.')
            return False
        with open(self.__json_file, "r") as f:
            application = jsonpickle.decode(f.read(),  classes = [Book, BookShop])
            self.__bookshop = application._Application__bookshop
            self.__user = application._Application__user
        return True


    def display_books(self):
        print("\n=== Liste des Livres Disponibles ===")
        for index, book in enumerate(self.__bookshop.books):
            print(f"[{index + 1}] Titre: {book.title}, Auteur: {book.author}, "
                f"Prix: {book.price}€, Quantité: {book.quantity}, Tags: {book.tags}")
        print("====================================\n")

    def main(self):
        self.reload()
        while True:
            print("\n=== Menu Principal ===")
            print("1. Afficher les livres")
            print("2. Acheter un livre")
            print("3. Enregistrer la librairie")
            print("4. Recharger la librairie")
            print("5. Quitter")
            print("=======================")
            choix = input("Entrez votre choix : ")

            # reference fonction
            # dictionnaire

            if choix == "1":
                self.display_books()

            elif choix == "2":
                self.display_books()
                book_index = int(input("Entrez le numéro du livre à acheter : ")) - 1
                if 0 <= book_index < len(self.__bookshop.books):
                    book = self.__bookshop.books[book_index]
                    if self.__user.buy_book(self.__bookshop.books, book):
                        print(f"Vous avez acheté '{book.title}'.")
            elif choix == "3":
                self.save_in_json()
                print(f"Librairie enregistrée dans '{self.__json_file}'.")

            elif choix == "4":
                self.reload()
                print(f"Librairie rechargée depuis '{self.__json_file}'.")

            elif choix == "5":
                print("À bientôt !")
                break

            else:
                print("Veuillez sélectionner une option entre 1 et 5.")

if __name__ == "__main__":
    Application().main()