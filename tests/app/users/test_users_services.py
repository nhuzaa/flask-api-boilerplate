import pytest
from app.users.services import UsersService

users_service = UsersService()


def test_create_with_valid_parameters():
    data = {
        # "email": "sudhirshresthaktm@gmail.com",
        "first_name": "Sudhir",
        "last_name": "Shrestha",
        "username": "sudhirt4",
        "password": "password",
    }
    user = users_service.create(**data)
    user = users_service.get(user.id)
    assert user.first_name == "Sudhir"


def test_create_with_missing_parameters():
    data = {"last_name": "Shrestha", "username": "sudhirt4", "password": "password"}
    with pytest.raises(TypeError):
        users_service.create(**data)


def test_update_with_valid_parameters(dummy_user):
    user = users_service.get(dummy_user.id)
    data = {"first_name": "Sudir"}

    users_service.update(user, **data)

    user = users_service.get(user.id)
    assert user.first_name == "Sudir"


def test_delete(dummy_user):
    user = users_service.get(dummy_user.id)
    users_service.delete(user)
    user = users_service.get(dummy_user.id)
    assert user is None
