import socket
import jsonpickle
from model.Book import Book

def handle_request(request_data):
    # Vous devez spécifier l'adresse et le port du serveur
    host = 'localhost'
    port = 9999  # Remplacez par le port que vous utilisez

    # Créer un socket pour communiquer avec le serveur
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))  # Se connecter au serveur
        s.sendall(request_data.encode())  # Envoyer la requête au serveur
        
        # Recevoir la réponse du serveur
        response = s.recv(1024).decode()  # Vous pouvez ajuster la taille du buffer
        return jsonpickle.decode(response)  # Décoder la réponse avec jsonpickle

def add_book_in_bookshop():
    title = input("Titre: ")
    author = input("Auteur: ")
    tags = input("Liste des tags [tag1,tag2,...]: ")
    is_numeric = input("Livre numérique ? (True/False) ")
    price = input("Prix unitaire: ")
    quantity = input("Quantité: ")

    # Créer l'objet Book
    book = Book(title, author, tags.split(','), is_numeric.lower() == 'true', float(price), int(quantity))
    
    # Envoyer la requête pour ajouter le livre dans la librairie
    response = handle_request("add_book_in_bookshop//" + jsonpickle.encode(book))
    print(response)  # Afficher la réponse du serveur

def display_books():
    print("\n=== Liste des Livres Disponibles ===")
    response = handle_request('display_books//')
    books = [Book.from_dict(book_data) for book_data in response]
    for index, book in enumerate(books):
        print(f"[{index + 1}] Titre: {book.title}, Auteur: {book.author}, "
              f"Prix: {book.price}€, Quantité: {book.quantity}, Tags: {book.tags}")
    print("====================================\n")

def buy_book():
    book_index = int(input("Entrez le numéro du livre à acheter : ")) - 1
    response = handle_request('buy_book//' + str(book_index))
    print(response)
    return

def exit_program():
    exit(1)

def main():
    actions = {
        "1": display_books,
        "2": buy_book,
        "2a": add_book_in_bookshop,
        "3": exit_program,
    }
    
    while True:
        print("\n=== Menu Principal ===")
        print("1. Afficher les livres")
        print("2. Acheter un livre")
        print("2a. Créer un livre")
        print("3. Quitter")
        print("=======================")
        choix = input("Entrez votre choix : ")

        action = actions.get(choix)
        if action:
            action()  # Appel de la fonction associée
        else:
            print(f"Veuillez sélectionner une option entre 1 et {len(actions.keys())}.")

main()
