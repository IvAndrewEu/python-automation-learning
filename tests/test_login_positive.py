import requests
from config import REQRES_API_KEY


def test_success_login():
    headers = {
        "x-api-key": REQRES_API_KEY
    }

    payload = {
        "email": "test@test.test",
        "password": "Test1"
    }

    response = requests.post(
        "https://reqres.in/api/login",
        headers=headers,
        json=payload
    )

    data = response.json()
    print(data)

    assert response.status_code == 200