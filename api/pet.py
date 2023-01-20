#local
from config import URL
from api.core import CoreApi, Response
from api.base_header import baseHeader

class PetEndPoints(baseHeader):

    def __init__(self):
        super().__init__()
        self.base_url = URL
        self.request = CoreApi()

    def add_new_pet(self, body: str) -> Response:
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

        response = self.request.post(url=self.base_url+"/pet", playload=body, headers=self.headers)
        return response
    
    def update_pet(self, body: str) -> Response:
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

        response = self.request.put(url=self.base_url+"/pet", payload=body, headers=self.headers)
        return response
   
    def get_pet_by_id(self, pet_id: str) -> Response:
        '''
        Parameters
        ----------
        ped_id: str
            The ped id

        Return
        ------
        Response: Object
            A object that contain the response from the request
        '''

        response = self.request.get(url=self.base_url+f'/pet/{pet_id}')
        return response
   
    def delete_pet_by_id(self, pet_id: str) -> Response:
        '''
        Parameters
        ----------
        ped_id: str
            The ped id
        
        Return
        ------
        Response: Object
            A object that contain the response from the request
        '''
        response = self.request.delete(url=self.base_url+f'/pet/{pet_id}')
        return response