from model.BookShop import BookShop
from model.Book import Book

class Application:
    def __init__(self):
        self.__users = []
        self.__bookshop = BookShop('', [])

    #FIXME save in json with pickle
    def save(self):
        b = BookShop('bookshop', [Book('', '', '', True, 0, 0)])
        b.save_in_json()

    def reload(self):
        pass

Application().save()
