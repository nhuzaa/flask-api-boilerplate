from flask import Flask
from flask_migrate import Migrate
from app.db import db
from .routes import register_routes
from .initializers import errorhandler, loghandler


def create_app(is_test=False):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("app.settings")

    if is_test:
        app.config.from_pyfile("test_config.py")
        app.config["TESTING"] = True
    else:
        app.config.from_pyfile("config.py")

    db.init_app(app)
    register_routes(app)
    errorhandler.init_errorhandler(app)

    Migrate(app, db)

    loghandler.init_logging(app)

    app.logger.info("Server started")

    return app
