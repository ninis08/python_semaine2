from model.BookShop import BookShop
from model.User import User
from model.Book import Book
import os
import jsonpickle

class Application:

    __json_file = "application-bib.json"

    def __init__(self):
        self.reload()
        self.__actions = {
            "1": self.display_books,
            "2": self.buy_book,
            "2a": self.add_book_in_bookshop,
            "3": self.save_library,
            "4": self.reload_library,
            "5": self.exit_program,
        }

    def add_book_in_bookshop(self, book):
        self.__bookshop.add_book(jsonpickle.decode(book))
        self.save_in_json()
        return ('Livre bien ajouté')

    def save_in_json(self):
        with open(self.__json_file, "w") as f:
            f.write(jsonpickle.encode(self))

    def reload(self):
        if not os.path.exists(self.__json_file):
            print(f'Fichier {self.__json_file} introuvable.')
            return False
        with open(self.__json_file, "r") as f:
            application = jsonpickle.decode(f.read(), classes=[Book, BookShop])
            self.__bookshop = application._Application__bookshop
            self.__user = application._Application__user
        return True

    def display_books(self, *args):
        return self.__bookshop.books

    def buy_book(self, book_index):
        book_index = int(book_index)
        try:
            if 0 <= book_index < len(self.__bookshop.books):
                book = self.__bookshop.books[book_index]
                print(book)
                if self.__user.buy_book(self.__bookshop, book):
                    return (f"Vous avez acheté '{book.title}'.")
            else:
                return ("Numéro invalide. Veuillez réessayer.")
        except ValueError:
            return ("Entrée invalide. Veuillez entrer un numéro.")

    def save_library(self):
        self.save_in_json()
        print(f"Librairie enregistrée dans '{self.__json_file}'.")

    def reload_library(self):
        if self.reload():
            print(f"Librairie rechargée depuis '{self.__json_file}'.")

    def exit_program(self):
        print("À bientôt !")
        exit()

    def main(self):
        self.reload()

        

        while True:
            print("\n=== Menu Principal ===")
            print("1. Afficher les livres")
            print("2. Acheter un livre")
            print("2a. Créer un livre")
            print("3. Enregistrer la librairie")
            print("4. Recharger la librairie")
            print("5. Quitter")
            print("=======================")
            choix = input("Entrez votre choix : ")

            action = self.__actions.get(choix)
            if action:
                action()  # Appel de la fonction associée
            else:
                print("Veuillez sélectionner une option entre 1 et 5.")

if __name__ == "__main__":
    Application().main()
