#libs
from assertpy import assert_that

#locals
from api.pet import PetEndPoints
from utilities.schemas import Schemas
from utilities.pet_utilities import PetUtilities
from utilities.custom_asserts import assert_validate_dic

#global objects
pets = PetEndPoints() 
schemas = Schemas()


def test_create_pet():
    
    #preconditons
    pet = PetUtilities()

    #test
    response = pets.add_new_pet(body=pet.pet_as_json)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(schemas.validate_pet_schema(response_text=response.as_dict)).is_true()
    assert_validate_dic(dic_correct=response.as_dict, dic_response=pet.pet_as_dic)

    del pet

def test_find_pet_by_id():
    
    #preconditions
    pet = PetUtilities()
    pets.add_new_pet(body=pet.pet_as_json)

    #test
    response = pets.get_pet_by_id(pet_id=pet.id)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(schemas.validate_pet_schema(response_text=response.as_dict)).is_true()
    assert_validate_dic(dic_correct=response.as_dict, dic_response=pet.pet_as_dic)

    del pet

def test_update_pet():

    #preconditons
    pet = PetUtilities()
    pets.add_new_pet(body=pet.pet_as_json)
    pet.make_randon_pet()

    #test
    response = pets.update_pet(body=pet.pet_as_json)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(schemas.validate_pet_schema(response_text=response.as_dict)).is_true()
    assert_validate_dic(dic_correct=response.as_dict, dic_response=pet.pet_as_dic)

    del pet

def test_delete_pet_by_id():

    #preconditions
    pet = PetUtilities()
    pets.add_new_pet(body=pet.pet_as_json)

    #test
    response = pets.delete_pet_by_id(pet_id=pet.id)

    assert_that(response.status_code).is_equal_to(200)

    del pet
