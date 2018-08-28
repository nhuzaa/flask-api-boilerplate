from flask import Blueprint, jsonify

from .services import WeatherService

weather_service = WeatherService()

weather_bp = Blueprint('weather', __name__)


@weather_bp.route('/', methods=['GET'])
def get_weather():
    weather = weather_service.all(query={"q": "London,uk"})

    return jsonify(weather), 200
