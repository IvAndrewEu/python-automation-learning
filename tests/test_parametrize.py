import pytest

@pytest.mark.parametrize(
    "user_id, post_id",
    [
        (1, 1),
        (2, 15),
        (3, 25)
    ],
    ids=[
        "test_userId_1_posts",
        "test_userId_2_posts",
        "test_userId_3_posts"
    ]
)

def test_filter_posts(session, base_url, user_id, post_id):
    response = session.get(
        f'{base_url}/posts',
        params={
            'userId': user_id,
            'id': post_id
        }
    )

    data = response.json()

    assert response.status_code == 200, (f"ожиемый результат: status_code = 200, фактический результат: status_code = {response.status_code}")
    assert isinstance(data, list), (f"ожидаемый результат: тип тела отвтеа = list, фактический результат: {type(data)}")
    assert len(data) == 1, (f"ожидаеиый реузльтат: в теле отвте 1 элемент, фактический результат: в теле ответа {len(data)} элементов")
    assert data[0]["userId"] == user_id, (f"передаваймый user_id не созпадает с userId в ответе")
    assert data[0]["id"] == post_id, (f"передаваймый id не созпадает с id в ответе")

