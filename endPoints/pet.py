from urllib import response
from config import URL
from API.coreApi import CoreApi
from endPoints.baseHeader import baseHeader
from Utilities.makeUrl import get_url_for_pet_by_id
#from Utilities.getRandonPet import get_randon_pet


class PetEndPoints(baseHeader):
    def __init__(self):
        super().__init__()
        self.base_url = URL
        self.request = CoreApi()

    def uploads_image(self, body=None):
        pass
    
    def add_new_pet(self, body=None):
        response = self.request.post(self.base_url+"/pet", body, self.headers)
        return response
    
    def update_pet(self, body=None):
        response = self.request.put(self.base_url+"/pet", body, self.headers)
        return response
    
    def get_pet_by_status(self, status_list=None):
        #params = f"findByStatus?status="
        pass
    
    def get_pet_by_id(self, petId=None):
        end_point = get_url_for_pet_by_id("/pet/",petId) 
        response = self.request.get(self.base_url+end_point)
        return response

    def update_pet_with_form_data(self, petId=None, name=None, status=None):
        pass
    
    def delete_pet_by_id(self, petId):
        pass