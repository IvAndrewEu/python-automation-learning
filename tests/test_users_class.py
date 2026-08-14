import pytest


@pytest.fixture(scope="class")
def class_data():
    print("CREATE CLASS DATA")

    yield "users"

    print("DELETE CLASS DATA")

@pytest.mark.api
class TestUsers:

    @pytest.fixture
    def user_id(self):
        return 1

    def test_get_users(self, session, base_url, class_data):
        response = session.get(f"{base_url}/{class_data}")
        data = response.json()

        assert response.status_code == 200, (f"получили {response.status_code} вместо 200")
        assert isinstance(data, list), (f"data {type(data)}, а не list")
        assert len(data) == 10, (f"количество элементов списка {len(data)} вместо 10")
        assert class_data == "users"


    def test_get_user(self, session, base_url, user_id, class_data):
        response = session.get(f"{base_url}/{class_data}/{user_id}")
        data = response.json()

        assert response.status_code == 200, (f"получили {response.status_code} вместо 200")
        assert isinstance(data, dict), (f"data {type(data)}, а не dict")
        assert data["id"] == user_id, (f"id = {data["id"]} вместо {user_id}")
        assert class_data == "users"

    @pytest.mark.parametrize(
        "post_id",
        [1, 2, 3],
        ids = ["post_1", "post_2", "post_3"]
    )
    def test_get_post(self, session, base_url, post_id):
        response = session.get(f"{base_url}/posts/{post_id}")
        data = response.json()

        assert response.status_code == 200, (f"получили {response.status_code} вместо 200")
        assert isinstance(data, dict), (f"data {type(data)}, а не dict")
        assert data["id"] == post_id, (f"id = {data["id"]} вместо {post_id}")


@pytest.mark.parametrize(
    "post_id",
    [1, 2, 3],
    ids = ["post_1", "post_2", "post_3"]
)
class TestPosts:

    def test_post_status(self, session, base_url, post_id):
        response = session.get(f"{base_url}/posts/{post_id}")
        data = response.json()

        assert response.status_code == 200

    def test_post_id(self, session, base_url, post_id):
        response = session.get(f"{base_url}/posts/{post_id}")
        data = response.json()

        assert data["id"] == post_id