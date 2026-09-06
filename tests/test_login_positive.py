import requests
from config import REQRES_API_KEY


def test_success_login():
    headers = {
        "x-api-key": REQRES_API_KEY
    }

    payload = {
        "email": "qa@example.com"
    }

    response = requests.post(
        "https://reqres.in/api/app-users/login",
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


