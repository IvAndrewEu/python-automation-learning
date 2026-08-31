import os

BASE_URL = os.getenv("BASE-URL")
API_TOKEN = os.getenv("API-TOKEN")

if BASE_URL is None:
    raise ValueError("BASE_URL is not set")

if API_TOKEN is None:
    raise ValueError("API_TOKEN is not set")