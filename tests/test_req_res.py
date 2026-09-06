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
        ),
        (
                {
                  "email": "test@test.test",
                    "password": 123
                },
                400,
                "user not found"
        ),
        (
                {
                    "email": None,
                    "password": "Test1"
                },
            400,
            "Missing email or username"
        ),
        (
                {
                    "email": "test@test.test",
                    "password": None
                },
            400,
            "Missing password"
        ),
        (
                {
                    "email": "    ",
                    "password": "Test1"
                },
            400,
            "user not found"
        ),
        (
                {
                    "email": "test@test.test",
                    "password": "    "
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
        "wrong_email_type",
        "wrong_password_type",
        "email_none",
        "password_none",
        "email_with_spaces",
        "password_with_spaces"
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

    assert response.status_code == expected_status
    assert data["error"] == message_error

def test_wrong_password_type():
    headers = {
        "x-api-key": REQRES_API_KEY
    }

    payload = {
            "email": "test@test.test",
            "password": "    "
    }

    response = requests.post(
        "https://reqres.in/api/login",
        json=payload,
        headers=headers
    )

    print(response.status_code)
    print(response.json())