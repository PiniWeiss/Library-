from user import User
from book import Book
import json

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.availeble_books = []
        for book in self.books:
            if book.is_availeble:
                self.availeble_books.append(book)

    def add_book(self, book:Book):
        self.books.append(book)
        print(f"{book} added to the library.")

    def add_user(self, user):
        self.users.append(user)
        print(f"{user} add to your libary")

    def borrow_book(self, user_id, book_isbn):
        if book_isbn in self.availeble_books:
            book_isbn.is_availble = False
            user_id.self.borrowed_books.append(book_isbn)

    def search_book_by_title(self, title:str):
        for book in self.books:
            if book.title == title:
                return book  
            
    def search_book_by_outher(self, outher:str):
        for book in self.books:
            if book.outher == outher:
                return book
            
    
    @staticmethod
    def add_user_to_json(user:User):
        user_dict = {}
        user_dict["name"] = user.name
        user_dict["id"] = user.id
        user_dict["borroed_books"] = []
        with open("data/users_ss.json", "r") as d:
            users = json.load(d)
            users["users"].append(user_dict) 
                
        with open("data/users_ss.json", "w") as users_data:
            json.dump(users, users_data, indent=4)

# Library.add_user_to_json(User("pini","999-9",[]))