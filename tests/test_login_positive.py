import requests
from config import REQRES_API_KEY


def test_success_login():
    headers = {
        "x-api-key": REQRES_API_KEY
    }

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(
        "https://reqres.in/api/login",
        headers=headers,
        json=payload
    )

    data = response.json()
    print(data)

    assert response.status_code == 200
    assert data["token"]


    token = data["token"]
    auth_header = {
        "Authorization": f"Bearer {token}"
    }


