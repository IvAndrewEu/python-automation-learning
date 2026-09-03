import requests
import pytest

from config import REQRES_API_KEY


@pytest.mark.parametrize(
    "payload, expected_status",
    [
        (
                {
                    "email": "",
                    "password": ""
                },
            400
        ),
        (
                {
                    "email": "",
                    "password": "Test1"
                 },
            400
        ),
        (
                {
                    "email": "test@test.test",
                    "password": ""
                },
            400
        )
    ],
    ids=[
        "without_email_password",
        "without_email",
        "without_password"
    ]
)
def test_post_body(payload, expected_status):
    headers = {
        "x-api-key": REQRES_API_KEY
    }

    response = requests.post(
        "https://reqres.in/api/login",
        json=payload,
        headers=headers
    )

    assert response.status_code == expected_status