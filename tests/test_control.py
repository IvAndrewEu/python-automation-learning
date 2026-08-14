import pytest

@pytest.mark.parametrize(
    "user_id",
    [1, 2, 3],
    ids=[
        "user_id_1",
        "user_id_2",
        "user_id_3"
    ]
)
@pytest.mark.api
class TestUsers:

    def test_get_user(self,base_url, session, user_id):
        response = session.get(f"{base_url}/users/{user_id}")
        data = response.json()

        assert response.status_code == 200, (f"{response.status_code} != 200")
        assert isinstance(data, dict), (f"{type(data)} != dict")
        assert data["id"] == user_id, (f"{data['id']} != {user_id}")



@pytest.fixture(scope = "class")
def resource_name():
    print("CREATE POSTS")
    yield "posts"
    print("DELETE POSTS")

@pytest.mark.regression
class TestPosts:
    def test_get_posts(self, base_url, session, resource_name):
        response = session.get(f"{base_url}/{resource_name}")
        data = response.json()

        assert response.status_code == 200, (f"{response.status_code} != 200")
        assert isinstance(data, list), (f"{type(data)} != list")

    def test_get_post(self, base_url, session, resource_name):
        response = session.get(f"{base_url}/{resource_name}/1")
        data = response.json()

        assert response.status_code == 200, (f"{response.status_code} != 200")
        assert data["id"] == 1, (f"{data['id']} != 1")