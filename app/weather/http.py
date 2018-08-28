from flask import current_app
from requests import Session


class WeatherSession(Session):
    def __init__(self, *args, **kwargs):
        super(WeatherSession, self).__init__(*args, **kwargs)
        self.params = {"appid": current_app.config["WEATHER_APP_ID"]}

    def request(self, method, url, *args, **kwargs):
        prefix_url = current_app.config["WEATHER_APP_BASE_URL"]
        url = prefix_url + url

        return super(WeatherSession, self).request(method, url, *args, **kwargs)
