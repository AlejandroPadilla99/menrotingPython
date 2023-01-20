from config import URL
from api.core import CoreApi, Response
from api.base_header import baseHeader


class UsersEndPoint(baseHeader):

    def __init__(self):
        super().__init__()
        self.base_url = URL
        self.request = CoreApi() 

    def login_user(self, username: str, password: str )-> Response:
        '''
        Parameters
        ----------
        username: str
            the user name of the user
        password: str
            the password of the user 
        
        Return
        ------
        Response: Object
            A object that contain the response from the request 
        '''

        response = self.request.get(url=self.base_url+"/user/login")
        return response
    
    def logout_user(self) -> Response:
        '''
        Return
        ------
        Response: Object
            A object that contain the response from the request
        '''

        response = self.request.get(url=self.base_url+"/user/logout")
        return response
    
    def create_user(self, body: str) -> Response:
        ''' 
        Parameters
        ----------
        body: str
            A string with the payload in json format 

        Return
        ------
        Response: Object
            A object that contain the response from the request
        '''
       
        response  = self.request.post(url=self.base_url+"/user", playload=body, headers=self.headers)
        return response 