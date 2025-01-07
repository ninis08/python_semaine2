import socket
import jsonpickle
from model.Book import Book

def handle_request(request_data):
    host = 'localhost'
    port = 9999

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request_data.encode())  # Envoi de la requête au serveur
        
        # Réception de la réponse et décodage
        response = s.recv(1024).decode()
        return jsonpickle.decode(response)

def display_books():
    print("\n=== Liste des Livres Disponibles ===")
    response = handle_request('display_books//')  # Demande des livres au serveur
    
    # Affichage des livres
    for index, book_data in enumerate(response):
        book = Book.from_dict(book_data)  # Utilisation de from_dict pour convertir en objet Book
        print(f"[{index + 1}] Titre: {book.title}, Auteur: {book.author}, "
              f"Prix: {book.price}€, Quantité: {book.quantity}, Tags: {book.tags}")
    print("====================================\n")

def main():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Afficher les livres")
        print("3. Quitter")
        print("=======================")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            display_books()
        elif choix == "3":
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
