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
        book_dict = vars(book)
        Data.add_data_to_json_books(book_dict)



    def search_by_type(self,value,list_items, type):
        for item in list_items:
            if item[type] == value:
                return item  
            

    def search_book_by_title(self,value):
        list_books = self.books
        return self.search_by_type(value,list_books,type="title")

            
    def search_book_by_outher(self):
        list_books = self.books
        return self.search_by_type(list_books,type="outher")

            
    
    
            