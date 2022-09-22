from config import URL
from api.core import CoreApi, Response
from api.base_header import baseHeader


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
    
    def logout_user(self) -> Response :
        response = self.request.get(self.base_url+"/user/logout")
        return response
    
    def create_user(self, body: str) -> Response:
        response  = self.request.post(self.base_url+"/user", body, self.headers)
        return response
    
    