#lib
import requests
import logging
from dataclasses import dataclass

#logging
logging.basicConfig(filename="newfiloe.log", format='%(asctime)s %(message)s', filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@dataclass
class Response:
    status_code : int
    text : str
    as_dict : object
    headers : dict
    
class CoreApi:
    def get(self, url: str) -> Response:
        response = requests.get(url)
        self.__print_logs(method='GET', url=url, playload="", headers="", response=response)
        return self.__get__responses(response)

    def post(self, url: str, playload: str, headers: dict) -> Response:
        response = requests.post(url, data=playload, headers=headers)
        self.__print_logs(method='POST', url=url, playload=playload, headers=headers, response=response)
        return self.__get__responses(response)
    
    def put(self, url: str, playload: str, headers: dict) -> Response:
        response = requests.post(url, data=playload, headers=headers)
        self.__print_logs(method='PUT', url=url, playload=playload, headers=headers, response=response)
        return self.__get__responses(response)

    def delete(self, url: str) -> Response:
        response = requests.get(url)
        self.__print_logs(method='DELETE', url=url, playload="", headers="", response=response)
        return self.__get__responses(response)

    @staticmethod
    def __print_logs(method: str, url: str, playload: str, headers: str, response: str) -> None:
        logger.debug("---------- Request -------------")
        logger.info("mehtod = " + method)
        logger.info("url = " + url)
        logger.info("body = " + playload)
        logger.info("headers = " + str(headers))
        logger.debug("---------- Response ------------")
        logger.info("status code = " + str(response.status_code))
        logger.info("body = " + response.text)

    @staticmethod
    def __get__responses(response: str) -> Response:
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}
        
        headers = response.headers
        
        return Response(status_code, text, as_dict, headers)