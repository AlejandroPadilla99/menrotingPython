from requests import request
from config import URL
from config import userSchema
from API.coreApi import coreApi
from endPoints.baseHeader import baseHeader


class usersEndPoint(baseHeader):
    def __init__(self):
        super().__init__()
        self.base_url = URL
        self.request = coreApi
    
    def create_array_users(self, body=None):
        return
    
    def create_list_users(self, body=None):
        return
    
    def get_user_by_username(self, name=None):
        return
    
    def update_user_by_username(self, username=None, body=None):
        return
    
    def delete_user_by_username(self, username=None, body=None):
        return
    
    def login_user(self, username=None, password=None ):
        return
    
    def logout_user(self):
        return
    
    def create_user(self, body=None):
        response = self.request.post(self.base_url, userSchema, self.headers)
        return response
    
    