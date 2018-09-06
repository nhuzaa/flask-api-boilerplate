from flask import Flask
from flask_migrate import Migrate
import os

from app.db import db
from .routes import register_routes
from .initializers import errorhandler, loghandler


def create_app(is_test=False):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("app.settings")

    try:
        if is_test:
            app.config["TESTING"] = True
            app.config.from_pyfile("test_config.py")
        else:
            app.config.from_pyfile("config.py")
    except FileNotFoundError:
        configs = ["SQLALCHEMY_DATABASE_URI"]
        for config in configs:
            app.config[config] = os.environ[config]

    db.init_app(app)
    register_routes(app)
    errorhandler.init_errorhandler(app)

    Migrate(app, db)

    if not is_test:
        loghandler.init_logging(app)

    app.logger.info("Server started")

    return app
