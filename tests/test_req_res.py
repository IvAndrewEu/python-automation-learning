import requests
import pytest

from config import REQRES_API_KEY


@pytest.mark.parametrize(
    "payload, expected_status, message_error",
    [
        (
                {
                    "email": "",
                    "password": ""
                },
            400,
            "Missing email or username"
        ),
        (
                {
                    "email": "",
                    "password": "Test1"
                 },
            400,
            "Missing email or username"
        ),
        (
                {
                    "email": "test@test.test",
                    "password": ""
                },
            400,
            "Missing password"

        )
    ],
    ids=[
        "without_email_password",
        "without_email",
        "without_password"
    ]
)
def test_post_body(payload, expected_status, message_error):
    headers = {
        "x-api-key": REQRES_API_KEY
    }

    response = requests.post(
        "https://reqres.in/api/login",
        json=payload,
        headers=headers
    )


    data = response.json()
    print(data)

    assert response.status_code == expected_status
    assert data["error"] == message_error