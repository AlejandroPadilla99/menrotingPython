#lib
from assertpy import assert_that

#locals
from api.user import UsersEndPoint
from utilities.user_utilities import UserUtilities
from utilities.schemas import Schemas

#Global objects
users = UsersEndPoint()
schema = Schemas()


def test_create_user():
    
    #Preconditions
    user = UserUtilities()

    #test
    response = users.create_user(user.user_as_json)
    assert_that(response.status_code).is_equal_to(200)
    assert schema.validate_user_schema(response_dict=response.as_dict) == True

    del user

def test_create_user_with_wrong_body():

    #test
    response = users.create_user("'{username: 'juan'")
    assert_that(response.status_code).is_equal_to(400)
    assert_that(response.as_dict.get('message')).is_equal_to('bad input')

def test_create_user_with_empy_body():

    #test
    response = users.create_user('')
    assert_that(response.status_code).is_equal_to(405)
    assert_that(response.as_dict.get('message')).is_equal_to('no data')