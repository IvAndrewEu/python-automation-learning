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

        ),
        (
                {

                },
                400,
                "Missing email or username"
        ),
        (
                {
                    "email": 123,
                    "password": "Test1"
                },
                400,
                "user not found"
        )
    ],
    ids=[
        "without_email_password",
        "without_email",
        "without_password",
        "empty_body",
        "wrong_email_type"
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
    print(response.status_code)
    print(data)

    assert response.status_code == expected_status
    assert data["error"] == message_error