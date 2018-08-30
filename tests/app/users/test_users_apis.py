import json

from tests.test_base import BaseTestCase


class UsersAPITestCase(BaseTestCase):
    def test_get_users(self):
        response = self.app_test_client.get("/users/")

        assert response.status_code == 200
        assert json.loads(response.data) == []
