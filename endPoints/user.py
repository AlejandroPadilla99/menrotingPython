from urllib import response
from config import URL
from API.coreApi import CoreApi
from endPoints.baseHeader import baseHeader


class usersEndPoint(baseHeader):
    def __init__(self):
        super().__init__()
        self.base_url = URL
        self.request = CoreApi()
    
    def create_array_users(self, body=None):
        pass
    
    def create_list_users(self, body=None):
        pass
    
    def get_user_by_username(self, name=None):
        pass
    
    def update_user_by_username(self, username=None, body=None):
        pass
    
    def delete_user_by_username(self, username=None, body=None):
        pass
    
    def login_user(self, username=None, password=None ):
        response = self.request.get(self.base_url+"/user/login")
        return response
    
    def logout_user(self):
        response = self.request.get(self.base_url+"/user/logout")
        return response
    
    def create_user(self, body=None):
        response  = self.request.post(self.base_url+"/user", body, self.headers)
        return response
    
    