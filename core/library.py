from core.book import Book
import json
from core.json_meneger import Data


class Library:
    def __init__(self):
        self.books = Data.load_from_json_books("data/books.json")
        self.users = []
        self.availeble_books = []
        for book in self.books:
            if book["is_availeble"]:
                self.availeble_books.append(book)

    def add_book(self, book:Book):
        self.books.append(book)
        print(f"{book} added to the library.")


    def search_book_by_title(self, title:str):
        for book in self.books:
            if book.title == title:
                return book  
            
    def search_book_by_outher(self, outher:str):
        for book in self.books:
            if book.outher == outher:
                return book
            
    @staticmethod
    def load_books_from_json(self):
        with open("data/books.json", "r") as books:
           books_j = json.load(books)
        for book in books_j["books"]:
            self.books.append(book)
    
    @staticmethod
    def add_book_to_json(book:Book):
        book_dict = {}
        book_dict["title"] = book.title
        book_dict["outher"] = book.outher
        book_dict["ISBN"] = book.ISBN
        with open("data/books.json", "r") as books:
                books_j = json.load(books)              
                books_j["books"].append(book_dict)
        with open("data/books.json", "w") as books:
            
            json.dump(books_j, books, indent=4)
            



