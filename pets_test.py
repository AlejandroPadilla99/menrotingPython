from endPoints.pet import PetEndPoints
from Utilities.schemas import Schemas
from Utilities.pet_utilities import PetUtilities

pets = PetEndPoints() 
schemas = Schemas()
pet = PetUtilities()

def test_create_pet():

    response = pets.add_new_pet(pet.pet_as_json)
    #validate_result = schemas.validate_pet_schema(response_text=response.text)
    assert response.status_code == 200
    #assert validate_result == True
    assert response.as_dict["id"] == pet.pet_as_dic["id"]
    assert response.as_dict["category"]["id"] == pet.pet_as_dic["category"]["id"]
    assert response.as_dict["name"] == pet.pet_as_dic["name"]
    for item in range(0,len(response.as_dict['tags'])):
        assert response.as_dict['tags'][item] == pet.pet_as_dic['tags'][item]
    assert response.as_dict["status"] == pet.pet_as_dic["status"]

def test_find_pet_by_id():
    response = pets.get_pet_by_id(pet.id)
    assert response.status_code == 200

def test_update_pet():
    pet.make_randon_pet()
    response = pets.update_pet(pet.id)
    assert response.status_code == 200

def test_delete_pet_by_id():
    response = pets.delete_pet_by_id(pet.id)
    assert response.status_code == 200
    response2 = pets.get_pet_by_id(pet.id)
    assert response2.status_code == 404