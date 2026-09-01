import requests
import pytest
from config import API_TOKEN, BASE_URL



@pytest.mark.parametrize(
    "token, expected_status",
    [({API_TOKEN}, "wrong token"),
    (200, 401)]
)
def test_get_headers(token, expected_status)
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BASE_URL}/bearer",
        headers=headers
    )

    assert response.status_code == {expected_status}
    data = response.json()

