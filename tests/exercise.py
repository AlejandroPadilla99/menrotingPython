import requests

URL = "https://jsonplaceholder.typicode.com/"

# check that the response status code is equal to 200
def test_get_user_with_id_1_check_status_code_equals_200():
    response = requests.get(URL+"users/1")
    assert response.status_code == 200

# Check that the response header 'Content-Type' is equal to 'application/json; charset=utf-8'
def test_get_user_with_id_1_check_content_type_equals_json():
    response = requests.get(URL+"users/1")
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

# Check that the reponse body field 'name' exists
def test_get_user_with_id_1_check_name_field_exists():
    response = requests.get(URL+"users/1")
    response_body = response.json()
    assert "name" in response_body
    
# Check that the reponse bodu field 'name' has a value equal to 'Leanne Graham'
def test_get_user_with_id_1_check_name_equals_leanne_graham():
    response = requests.get(URL+"users/1")
    response_body = response.json()
    assert response_body["name"] == "Leanne Graham"

# Check that the reponse body field 'company.name' has a value equals to 'Romaguera-Crona'
def test_get_user_with_id_1_check_company_name_equals_romaguera_crona():
    response = requests.get(URL+"users/1")
    response_body = response.json()
    assert response_body["company"]["name"] == "Romaguera-Crona"

# Check that the response body is a list (an array) containing 1- elements
def test_get_all_users_check_number_of_users_equals_10():
    response = requests.get(URL+"users")
    response_body = response.json()
    assert len(response_body) == 10
 
