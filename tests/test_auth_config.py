import requests

from config import API_TOKEN, BASE_URL

def test_get_users():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }

    response = requests.get(
        f"{BASE_URL}/headers",
        headers=headers
    )

    assert response.status_code == 200
    data = response.json()
    print(data)