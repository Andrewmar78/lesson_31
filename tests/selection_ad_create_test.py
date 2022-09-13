import pytest


@pytest.mark.django_db
def test_selection_create_ad(client, user_token, user, ad):
    expected_response = {
        "id": 1,
        "user": user.id,
        "name": "Test",
        "ads": [ad.id]
    }

    data = {
        "user": user.id,
        "name": "Test",
        "ads": [ad.id]
    }

    response = client.post(
        "/selection/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION='Token ' + user_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
