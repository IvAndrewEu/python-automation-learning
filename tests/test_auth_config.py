import requests
import pytest

from config import API_TOKEN, BASE_URL



@pytest.mark.parametrize(
    "headers, expected_status",
    [({"Authorization": f"Bearer {API_TOKEN}"}, 200),
    ({"Authorization": f"Bearer wrong token"}, 401),
     ({}, 401)]
)
def test_get_headers(headers, expected_status):
    response = requests.get(
        f"{BASE_URL}/bearer",
        headers=headers
    )

    assert response.status_code == expected_status

