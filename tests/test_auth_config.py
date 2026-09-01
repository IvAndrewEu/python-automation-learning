import requests

from config import API_TOKEN, BASE_URL

def test_get_headers():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }

    response = requests.get(
        f"{BASE_URL}/bearer",
        headers=headers
    )

    assert response.status_code == 200
    data = response.json()
    print(response.status_code)
    print(response.json())

def test_get_headers_without_token():
    response = requests.get(f"{BASE_URL}/bearer")

    assert response.status_code == 401