from config import URL
from API.coreApi import coreApi


class storeEndPoints():
    def __init__(self):
        self.base_url = URL
        self.request = coreApi

    def place_order_for_pet(self, body=None):
        return
    
    def get_purchase_order_by_id(self, body=None):
        return
    
    def delete_purchase_order_by_id(self, body=None):
        return
    
    def get_pet_inentories_status(self):
        return
