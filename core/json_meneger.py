import json

class Data:
    @staticmethod
    def load_from_json(data_json):
        with open(data_json) as data:
            data_json_dict = json.load(data)
            return data_json_dict
        
    @staticmethod  
    def load_from_json_books(data_json):
        return Data.load_from_json(data_json)["books"]
    


