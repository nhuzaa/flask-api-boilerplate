import json

from tests.test_base import BaseTestCase


class WeatherAPITestCase(BaseTestCase):
    def test_get_users(self):
        response = self.app_test_client.get("/weather/")

        assert response.status_code == 200
