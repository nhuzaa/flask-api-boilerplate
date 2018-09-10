import pytest
from app.common.services import Service
from app.users.models import User

Service.__model__ = User

users_service = Service()


def test_get_existing_user(dummy_user):
    user = users_service.get(dummy_user.id)

    assert user.first_name == dummy_user.first_name


def test_get_non_existent_user():
    user = users_service.get(100)
    assert user is None


def test_get_or_404(dummy_user):
    user = users_service.get_or_404(dummy_user.id)
    assert user.first_name == dummy_user.first_name


def test_get_or_404_non_existent_user():
    from werkzeug.exceptions import NotFound

    with pytest.raises(NotFound):
        users_service.get_or_404(100)


def test_first(dummy_user):
    first_user = users_service.first()
    assert first_user.id == dummy_user.id


def test_new():
    data = {
        # "email": "sudhirshresthaktm@gmail.com",
        "first_name": "Sudhir",
        "last_name": "Shrestha",
        "username": "sudhirt4",
        "password": "password",
    }
    user = users_service.new(**data)
    assert user.first_name == data["first_name"]


def test_update_with_instance_object():
    data = {"first_name": "Sudir"}
    with pytest.raises(ValueError):
        users_service.update("string", **data)


def test_all(dummy_user):
    users = users_service.all()
    assert len(users) == 1


def test_get_all(dummy_user):
    ids = [dummy_user.id]
    users = users_service.get_all(*ids)
    assert len(users) == 1
