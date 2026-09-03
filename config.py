import os

BASE_URL = os.getenv("BASE_URL")
API_TOKEN = os.getenv("API_TOKEN")
REQRES_API_KEY = os.getenv("REQRES_API_KEY")

if BASE_URL is None:
    raise ValueError("BASE_URL is not set")

if API_TOKEN is None:
    raise ValueError("API_TOKEN is not set")

if REQRES_API_KEY is None:
    raise ValueError("REQRES_API_KEY is not set")