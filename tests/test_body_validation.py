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
    assert data["json"]["age"] == 27, f"data['json']['age'] != 27)"
    assert data["json"]["name"] == "Andrew", f"data['json']['name'] != Andrew"