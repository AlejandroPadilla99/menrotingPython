from config import URL
from API.coreApi import coreApi


class petEndPoint():
    def __init__(self):
        self.base_url = URL
        self.request = coreApi

    def uploads_image(self, body=None):
        return
    
    def add_new_pet(self, body=None):
        return
    
    def update_pet(self, body=None):
        return
    
    def get_pet_by_status(self, list=None):
        return
    
    def get_pet_by_id(self, petId=None):
        return

    def update_pet_with_form_data(self, petId=None, name=None, status=None):
        return
    
    def delete_pet_by_id(self, petId):
        return
