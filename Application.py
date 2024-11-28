from model.BookShop import BookShop

class Application:
    def __init__(self):
        self.__users = []
        self.__bookshop = BookShop()

    #FIXME save in json with pickle
    def save(self):
        pass

    def reload(self):
        pass

    
