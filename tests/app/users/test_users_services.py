from tests.test_base import BaseTestCase

from app.users.services import UsersService

users_service = UsersService()


class UsersServicesTestCase(BaseTestCase):
    def test_get(self):
        data = {
            "first_name": "Sudhir",
            "last_name": "Shrestha",
            "username": "sudhirt4",
            "password": "password",
        }
        user = users_service.create(**data)

        user = users_service.get(user.id)

        self.assertEqual(user.first_name, "Sudhir")

    def test_create_with_invalid_parameters(self):
        data = {"last_name": "Shrestha", "username": "sudhirt4", "password": "password"}
        with self.assertRaises(TypeError):
            users_service.create(**data)
