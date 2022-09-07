import random
import json
from faker import Faker

faker = Faker()

class UserUtilities():
    def __init__(self) -> None:
        self.id  = random.randint(1,100000000000)
        self.user_as_dic = None
        self.user_as_json = None
        self.create_randon_user()
    

    def create_randon_user(self) -> None:
        self.user_as_dic = {
            'id': self.id,
            'name': faker.name(),
            'firsName': faker.first_name(),
            'lastName': faker.last_name(),
            'mail': faker.email(),
            'password': faker.password(),
            'phone': faker.phone_number(),
            "userStatus": random.randint(1,5)
        }
        self.user_as_json = json.dumps(self.user_as_dic,indent = 4)
