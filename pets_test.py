from urllib import response
import requests
from endPoints.pet import PetEndPoints

from Utilities.getRandonPet import get_randon_pet

pets = PetEndPoints() 

pet, pet_json = get_randon_pet()

def test_create_pet():
    response = pets.add_new_pet(pet_json)
    assert response.status_code == 200

def test_find_pet_by_id():
    response = pets.get_pet_by_id(pet["id"])
    assert response.status_code == 200



