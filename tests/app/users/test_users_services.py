import pytest
from app.users.services import UsersService

users_service = UsersService()


def test_get():
    data = {
        "first_name": "Sudhir",
        "last_name": "Shrestha",
        "username": "sudhirt4",
        "password": "password",
    }
    user = users_service.create(**data)

    user = users_service.get(user.id)

    assert user.first_name == "Sudhir"


def test_create_with_invalid_parameters():
    data = {"last_name": "Shrestha", "username": "sudhirt4", "password": "password"}
    with pytest.raises(TypeError):
        users_service.create(**data)
