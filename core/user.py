class User:
    UID = 2000
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = User.UID
        User.UID += 1
        self.borrowed_books = []
