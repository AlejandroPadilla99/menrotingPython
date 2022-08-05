import requests
from endPoints.user import usersEndPoint

users = usersEndPoint()


def test_login_user():
    response = users.login_user()
    assert response.status_code == 200

def test_logout_user():
    response = users.logout_user()
    assert response.status_code == 200
