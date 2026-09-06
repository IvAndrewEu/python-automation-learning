import requests
from config import REQRES_API_KEY


def test_success_login():
    headers = {
        "x-api-key": REQRES_API_KEY
    }

    payload = {
        "project_id": "49353",
        "email": "qa@example.com"
    }

    response = requests.post(
        "https://reqres.in/api/app-users/login",
        headers=headers,
        json=payload
    )

    data = response.json()
    print(response.status_code)
    print(data)


