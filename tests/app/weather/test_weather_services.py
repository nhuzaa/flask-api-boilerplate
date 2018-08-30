from tests.test_base import BaseTestCase

from app.weather.services import WeatherService

weather_service = WeatherService()


class WeatherServicesTestCase(BaseTestCase):
    def test_all(self):
        weather = weather_service.all(query={"q": "London,uk"})

        self.assertIsNotNone(weather)
