from flask import Flask
from flask_migrate import Migrate

from app.db import db
from .routes import register_routes
from .initializers import setup_initializers


def create_app(is_test=False):
    app = Flask(__name__, instance_relative_config=True)

    setup_initializers(app, is_test)

    db.init_app(app)
    register_routes(app)
    Migrate(app, db)

    app.logger.info("Server started")
    return app
