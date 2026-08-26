def test(session, base_url):
    response = session.get(base_url)

    assert response.status_code == 200
