import pytest
from app.users.services import UsersService

users_service = UsersService()


def test_create_with_valid_parameters(dummy_user_data):
    user = users_service.create(**dummy_user_data)
    user = users_service.get(user.id)
    assert user.first_name == "Sudhir"


def test_create_with_missing_parameters(dummy_user_data):
    from sqlalchemy.exc import IntegrityError

    dummy_user_data["first_name"] = None

    with pytest.raises(IntegrityError):
        users_service.create(**dummy_user_data)


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
