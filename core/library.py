from core.user import User
from core.book import Book
from core.json_meneger import Data



class Library:
    def __init__(self):
        self.books = Data.load_from_json_books("data/books.json")
        self.users = Data.load_from_json_users("data/users.json")
        self.availeble_books = []
        for book in self.books:
            if book["is_availeble"]:
                 self.availeble_books.append(book)

    def add_book(self, book:Book):
        book_dict = vars(book)
        Data.add_data_to_json_books(book_dict)

    def add_user(self, user:User):
        users_dict = vars(user)
        Data.add_data_to_json_books(users_dict)

    def borrow_book(self, user_id, book_isbn):
        if book_isbn in self.availeble_books:
            book_isbn.is_availble = False
            user_id.self.borrowed_books.append(book_isbn)

    def search_book_by_title(self, title:str):
        for book in self.books:
            if book["title"] == title:
                return book  
            
    def search_book_by_outher(self, outher:str):
        for book in self.books:
            if book["outher"] == outher:
                return book