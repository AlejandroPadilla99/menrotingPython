from urllib import response
from config import URL
from api.core import CoreApi, Response
from api.base_header import baseHeader
from utilities.makeUrl import get_url_for_pet_by_id


class PetEndPoints(baseHeader):
    def __init__(self):
        super().__init__()
        self.base_url = URL
        self.request = CoreApi()

    def add_new_pet(self, body: str) -> Response:
        response = self.request.post(self.base_url+"/pet", body, self.headers)
        return response
    
    def update_pet(self, body: str) -> Response:
        response = self.request.put(self.base_url+"/pet", body, self.headers)
        return response
   
    def get_pet_by_id(self, pet_id: str) -> Response:
        end_point = get_url_for_pet_by_id("/pet/",pet_id) 
        response = self.request.get(self.base_url+end_point)
        return response
   
    def delete_pet_by_id(self, pet_id: str) -> Response:
        end_point = get_url_for_pet_by_id("/pet/",pet_id) 
        response = self.request.delete(self.base_url+end_point)
        return response
