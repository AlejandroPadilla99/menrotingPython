from dbm import dumb
from faker import Faker
import json

fake = faker() 


def get_randon_pet():
    data = { }
    pet = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ], 
        "status": "available"
    }

    petJson = json.dumb(pet)
    return data , pet