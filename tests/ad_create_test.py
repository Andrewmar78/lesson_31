import pytest


@pytest.mark.django_db
def test_create_ad(client, user_token, category, user):
    expected_response = {
        "id": user.id,
        "name": "Test ad more than 10 letters",
        "author": user.username,
        "price": 1000,
        "description": "Any description less than 2000 letters",
        "is_published": False,
        "image": None,
        "category": category.name,
        }

    data = {
        "author_id": user.id,
        "name": "Test ad more than 10 letters",
        "price": 1000,
        "description": "Any description less than 2000 letters",
        "is_published": False,
        "category_id": category.id
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION='Token ' + user_token,
    )

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_ad_create_small_name(client, user_token, category, user):
    expected_response = {
        "name": [
            "The field must contain at least 10 characters."
        ]
    }

    data = {
        "author_id": user.id,
        "name": "Small",
        "price": 1000,
        "description": "Any description",
        "is_published": False,
        "category_id": category.id
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION='Token ' + user_token,
    )

    assert response.status_code == 400
    assert response.data == expected_response
