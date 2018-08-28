from .users import users_bp
from .weather import weather_bp


def register_routes(app):
    app.register_blueprint(weather_bp, url_prefix="/weather")
    app.register_blueprint(users_bp, url_prefix="/users")
