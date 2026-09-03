import requests
import pytest

from config import BASE_URL

@pytest.mark.parametrize(
    "payload",
    [
        ({"name": "Andrew", "age": 27}),
        ({"age": 27}),
        ({"name": "Andrew", "age": "twenty seven"})
    ],
    ids=[
        "valid_test",
        "without_name",
        "wrong_age_type"
    ]
)
def test_post_body(payload):


    response = requests.post(
        f"{BASE_URL}/anything",
        json=payload
    )

    data = response.json()
    assert response.status_code == 200
    assert data["json"] == payload