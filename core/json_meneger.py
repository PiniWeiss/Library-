import json

class Data:
    @staticmethod
    def load_from_json(data_json:json):
        with open(data_json) as data:
            data_json_dict = json.load(data)
            return data_json_dict
        
    @staticmethod  
    def load_from_json_books(data_json):
        return Data.load_from_json(data_json)["books"]
    
    @staticmethod
    def add_data_to_json_books(data, data_json="data/books.json"):    
        books_list = Data.load_from_json(data_json)["books"]
        books_list.append(data)
        books_dict = {}
        books_dict["books"] = books_list
        with open(data_json, "w") as books:         
            json.dump(books_dict, books, indent=4)

    @staticmethod
    def load_from_json_users(data_json):
        return Data.load_from_json(data_json)["users"]
        
    @staticmethod
    def add_data_to_json_users(data, data_json="data/users.json"):
        users_list = Data.load_from_json(data_json)["users"]
        users_list.append(data)
        users_dict = {}
        users_dict["books"] = users_list
        with open(data_json, "w") as users:         
            json.dump(users_dict, users, indent=4)