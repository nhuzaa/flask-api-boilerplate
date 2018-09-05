# EXAMPLES:
# def test_add_and_lookup_entry(phonebook):
#     phonebook.add("Bob", "123")
#     assert "123" == phonebook.lookup("Bob")
#
#
# def test_phonebook_gives_access_to_names_and_numbers(phonebook):
#     phonebook.add("Alice", "234")
#     phonebook.add("Bob", "123")
#     assert set(phonebook.names()) == {"Alice", "Bob"}
#     assert "234" in phonebook.numbers()
#     # assert "Ali" in phonebook.names()
#
#
# def test_missing_entry_raises_KeyError(phonebook):
#     with pytest.raises(KeyError):
#         phonebook.lookup("missing")
#
#
# def test_skip_this():
#     pytest.skip("WIP")
#     pass

import pytest
from app.users.services import UsersService

users_service = UsersService()


def test_setup(app):
    assert app.config["TESTING"] == True


def test_create_with_invalid_parameters():
    data = {
        "first_name": "Sudhir",
        "last_name": "Shrestha",
        "username": "sudhirt4",
        "password": "password",
    }
    with pytest.raises(TypeError):
        users_service.create(**data)
