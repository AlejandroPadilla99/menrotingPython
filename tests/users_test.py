import requests
from endPoints.user import usersEndPoint

users = usersEndPoint()


def test_create_new_user():
    response = users.create_user()
    assert response.status_code == 200
