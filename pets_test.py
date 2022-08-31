from urllib import response
from wsgiref import validate
import requests
from endPoints.pet import PetEndPoints
from Utilities.schemas import Schemas

from Utilities.getRandonPet import get_randon_pet

pets = PetEndPoints() 
schemas = Schemas()

pet, pet_json = get_randon_pet()

def test_create_pet():
    response = pets.add_new_pet(pet_json)
    #validate_resunlt = schemas.validate_pet_schema(response_text=response.text)
    assert response.status_code == 200
    #assert validate_resunlt == True
    assert response.as_dict["id"] == pet["id"]
    assert response.as_dict["category"]["id"] == pet["category"]["id"]
    assert response.as_dict["name"] == pet["name"]
    #preguntar por como validar listas
    assert response.as_dict["status"] == pet["status"]

def test_find_pet_by_id():
    response = pets.get_pet_by_id(pet["id"])
    assert response.status_code == 200

def test_update_pet():
    response = pets.update_pet(pet_json)
    assert response.status_code == 200

def test_delete_pet_by_id():
    response = pets.delete_pet_by_id(pet["id"])
    assert response.status_code == 200



