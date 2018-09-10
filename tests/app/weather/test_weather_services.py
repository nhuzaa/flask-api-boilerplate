from app.weather.services import WeatherService

weather_service = WeatherService()


def test_all():
    weather = weather_service.all(query={"q": "London,uk"})

    assert weather
