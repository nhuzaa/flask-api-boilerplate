from flask import Flask
from flask_migrate import Migrate
from app.db import db
from .routes import register_routes
from .errorhandler import init_errorhandler


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    db.init_app(app)
    register_routes(app)
    init_errorhandler(app)

    Migrate(app, db)

    return app
