from .http import WeatherSession
from . import endpoints


class WeatherService(object):
    def all(self, query):
        endpoint = endpoints.get_all
        params = {
            'q': query
        }

        weather_session = WeatherSession()
        response = weather_session.get(endpoint, params=params)

        return response.json()
