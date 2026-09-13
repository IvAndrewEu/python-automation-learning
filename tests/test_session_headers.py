

def test_session_headers(session):
    response = session.get("https://httpbin.org/headers")
    data = response.json()
    print(data)

    assert data["X-Test-Client"]
    assert data["X-Test-Client"] == "python-aqa"