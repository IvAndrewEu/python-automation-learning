import requests

from config import BASE_URL

def test_post_body():
    payload = {
        "name": "Andrew",
        "age": 27
    }

    response = requests.post(
        f"{BASE_URL}/anything",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()
    print(data)