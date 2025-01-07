import socket
import jsonpickle
from model.Book import Book
from model.BookShop import BookShop
from model.BookCase import BookCase

def handle_request(request_data):
    # Analyser la requête
    try:
        # Par exemple, on pourrait exécuter des actions en fonction de la requête
        if "display_books" in request_data:
            books = BookShop.get_books()  
            return jsonpickle.encode(books)
        elif "add_book_in_bookshop" in request_data:
            book = jsonpickle.decode(request_data.split("//")[1])
            BookShop.add_book(book)  # Ajoutez un livre dans la librairie
            return jsonpickle.encode({"status": "Book added successfully!"})
        elif "buy_book" in request_data:
            book_index = int(request_data.split("//")[1])
            BookShop.buy_book(book_index)  # Achetez le livre
            return jsonpickle.encode({"status": "Book bought successfully!"})
    except Exception as e:
        return jsonpickle.encode({"error": str(e)})

def start_server():
    host = 'localhost'
    port = 9999

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Serveur en attente de connexion sur {host}:{port}...")
        
        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connexion établie avec {client_address}")
                data = client_socket.recv(1024).decode()
                if data:
                    response = handle_request(data)
                    client_socket.sendall(response.encode())

if __name__ == "__main__":
    start_server()
