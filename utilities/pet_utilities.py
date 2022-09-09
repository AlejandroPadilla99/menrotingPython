import random
import json
from dbm import dumb
from faker import Faker
from faker.providers import DynamicProvider


fake = Faker() 

class PetUtilities():
    
    def __init__(self) -> None:
        self.id = random.randint(0,9223372036854053000) 
        self.__create_provides_faker()
        self.make_randon_pet()
    
    
    def make_pet_to_json(self) -> None: 
        self.pet_as_json = json.dumps(self.pet_as_dic,indent = 4)


    def make_randon_pet(self) -> None:
        self.pet_as_dic = {
            "id": self.id,
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

        self.make_pet_to_json()
        
    def clean_pet(self) -> None:
        self.pet_as_dic = {}

    @staticmethod
    def __create_provides_faker() -> None:
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



    