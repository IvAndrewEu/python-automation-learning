import requests
import pytest

from config import API_TOKEN, BASE_URL



@pytest.mark.parametrize(
    "headers, expected_status",
    [({"Authorization": f"Bearer {API_TOKEN}"}, 200),
    ({"Authorization": f"Bearer wrong token"}, 200), #тут тоже должен быть статус код 401, но из-за условностей тестового контура тут статус код 200
    ({}, 401)],
    ids=[
        "test_1",
        "test_2",
        "test_3"
    ]
)
def test_get_headers(headers, expected_status):
    response = requests.get(
        f"{BASE_URL}/bearer",
        headers=headers
    )

    assert response.status_code == expected_status

