from core.library import Library
from core.book import Book

if __name__ == "__main__":
    b = Book("The 6:20 Man", "David Bladachi", "21-990")
    l = Library()
    l.add_book(b)
    print(l.books)
    