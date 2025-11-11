class User:
    UID = 2000
    def __init__(self, name: str, id: str, borrowed_books: list):
        self.name = name
        self.id = User.UID
        User.UID += 1
        self.borrowed_books = borrowed_books
