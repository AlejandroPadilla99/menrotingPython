from endPoints.pet import PetEndPoints
from Utilities.schemas import Schemas
from Utilities.pet_utilities import PetUtilities

pets = PetEndPoints() 
schemas = Schemas()


def test_create_pet():
    
    #preconditons
    pet = PetUtilities()

    #test
    response = pets.add_new_pet(pet.pet_as_json)

    assert response.status_code == 200
    #assert response.as_dict.keys() == pet.pet_as_dic.keys()
    #assert response.as_dict == pet.pet_as_dic

    del pet

def test_find_pet_by_id():
    
    #preconditions
    pet = PetUtilities()
    pets.add_new_pet(pet.pet_as_json)

    #test
    response = pets.get_pet_by_id(pet.id)

    assert response.status_code == 200

    del pet

def test_update_pet():

    #preconditons
    pet = PetUtilities()
    pets.add_new_pet(pet.pet_as_json)
    pet.make_randon_pet()

    #test
    response = pets.update_pet(pet.pet_as_json)

    assert response.status_code == 200

    del pet

def test_delete_pet_by_id():

    #preconditions
    pet = PetUtilities()
    pets.add_new_pet(pet.pet_as_json)

    #test
    response = pets.delete_pet_by_id(pet.id)
    assert response.status_code == 200

    del pet
