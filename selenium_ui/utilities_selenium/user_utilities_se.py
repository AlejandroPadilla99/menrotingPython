#lib
from faker import Faker

faker = Faker()

class User:
    '''
        A class to represent a user and provide some utilities functions 
    '''
    
    def __init__(self) -> None:
        self.id = faker.name()
        self.user_credentials = None
        self.account_data = None
        self.profile_data = None

        self.create_user_credentials()
        self.create_account_data()
        self.create_profile_data(
            language_preference='english',
            favorite_category='FISH',
            my_list=False,
            my_banner=False
        )

    def create_user_credentials(self) -> None:
        self.user_credentials = {
            'id' : self.id,
            'password': faker.password(),
        }
        
    def create_account_data(self) -> None:
        self.account_data ={
            'first_name': faker.first_name(),
            'second_name': faker.last_name(),
            'email': faker.email(),
            'phone': faker.phone_number(),
            'address1': faker.street_address(),
            'address2': faker.street_address(),
            'city': faker.city(),
            'state': faker.city(),
            'zip': faker.postcode(),
            'country': faker.country()
        } 
    
    def create_profile_data(self, language_preference: str, favorite_category: str, my_list: bool, my_banner: bool ) -> None:
        self.profile_data = {
            'language_preference': language_preference,
            'favorite_category': favorite_category,
            'my_list': my_list,
            'my_banner': my_banner
        }
