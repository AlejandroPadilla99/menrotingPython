from dataclasses import dataclass

import requests

@dataclass
class Response:
    status_code : int
    text : str
    as_dict : object
    headers : dict
    

class CoreApi:
    def get(self, url):
        response = requests.get(url)
        return self.__get__responses(response)

    def post(self, url, playload, headers):
        response = requests.post(url, data=playload, headers=headers)
        return self.__get__responses(response)
    
    def put(self, url, playload, headers):
        response = requests.post(url, data=playload, headers=headers)
        return self.__get__responses(response)

    def delete(self, url):
        response = requests.get(url)
        return self.__get__responses(response)

    def __get__responses(self,response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}
        
        headers = response.headers
        
        return Response(status_code, text, as_dict, headers)
        
    

