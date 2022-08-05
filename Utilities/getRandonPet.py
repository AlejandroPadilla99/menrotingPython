import random
import json
from dbm import dumb
from xml.etree.ElementTree import Element
from faker import Faker
from faker.providers import DynamicProvider

fake = Faker() 

#Providers
pet_category_provider = DynamicProvider(
    provider_name = "pet_category",
    elements = ["Fish", "Dog", "Cat", "Reptile", "Bird"]
)
pet_status_provider = DynamicProvider(
    provider_name = "pet_status",
    elements = ["availeble", "pending", "sold"]
)

fake.add_provider(pet_category_provider)
fake.add_provider(pet_status_provider)


def get_randon_pet():

    pet = {
        "id": random.randint(0,9223372036854053000),
        "category": {
            "id": random.randint(0,9223372036854053000),
            "name": fake.pet_category()
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": random.randint(0,9223372036854053000),
                "name": "string"
            }
        ], 
        "status": fake.pet_status()
    }

    petJson = json.dumps(pet,indent = 4)

    return pet, petJson