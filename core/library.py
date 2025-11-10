from book import Book
import json

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.availeble_books = []
        for book in self.books:
            if book.is_availeble:
                self.availeble_books.append(b)

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
    def load_book():
        with open("data/book.json", "r") as books:
             json.load(books)


