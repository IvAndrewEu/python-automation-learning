

def test_session_headers(session):
    response = session.get("https://httpbin.org/headers")
    data = response.json()
    print(data)

    assert response.headers["X-Test-Client"]
    assert response.headers["X-Test-Client"] == "python-aqa"