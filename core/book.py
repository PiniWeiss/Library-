class Book:
    def __init__(self,title:str, outher:str, ISBN:str ,is_availeble:bool=True):
        self.title = title
        self.outher = outher
        self.ISBN = ISBN
        self.is_availeble = is_availeble
        
    def __str__(self):
        return f"Book name: {self.title}. Outher: {self.outher}. Book id: {self.ISBN}"
    