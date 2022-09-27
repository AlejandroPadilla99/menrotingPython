#locals
from api.user import usersEndPoint
from utilities.user_utilities import UserUtilities
from utilities.schemas import Schemas

#Global objects
users = usersEndPoint()
schema = Schemas()


def test_create_user():
    
    #Preconditions
    user = UserUtilities()

    #test
    response = users.create_user(user.user_as_json)
    assert response.status_code == 200
    assert schema.validate_user_schema(response_dict=response.as_dict) == True

    del user

def test_login_user():

    #Preconditions
    user = UserUtilities

    #test

