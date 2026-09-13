import pytest
import requests

@pytest.fixture
def session():
    session = requests.Session()

    session.headers.update({
        "X-Test-Client": "python-aqa"
    })

    return session

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"