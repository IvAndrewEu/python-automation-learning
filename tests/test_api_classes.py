import pytest


@pytest.mark.parametrize(
    "user_id",
    [1, 2]
)
@pytest.mark.api
class TestUsers:

    def test_get_user_status(self, base_url, session, user_id):
        response = session.get(f"{base_url}/users/{user_id}")

        assert response.status_code == 200, (f"{response.status_code} != 200")

    def test_get_user_id(self, base_url, session, user_id):
        response = session.get(f"{base_url}/users/{user_id}")
        data = response.json()

        assert data["id"] == user_id, (f"{data['id']} != {user_id}")


@pytest.fixture(scope = "class")
def resource_name():
    print("CREATE POSTS RESOURCE")
    yield "posts"
    print("DELETE POSTS RESOURCE")
@pytest.mark.regression #указывается прям перед классом, а не перд фикстурой
class TestPosts:

    def test_get_posts(self, base_url, session, resource_name):
        response = session.get(f"{base_url}/{resource_name}")
        data = response.json()

        assert response.status_code == 200, (f"{response.status_code} != 200, да, что-то не так")
        assert isinstance(data, list), (f"{type(data)} != list")

    def test_get_post(self, base_url, session, resource_name):
        response = session.get(f"{base_url}/{resource_name}/1")
        data = response.json()

        assert response.status_code == 200, (f"{response.status_code} != 200")
        assert data["id"] == 1, (f"{data['id']} != 1")
