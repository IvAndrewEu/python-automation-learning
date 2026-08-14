import pytest
import requests

@pytest.fixture
def session():
    return requests.Session()

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"