def test_get_users(session, base_url):
    response = session.get(f"{base_url}/users")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 10

