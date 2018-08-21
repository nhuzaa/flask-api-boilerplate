from flask import Flask
from flask_migrate import Migrate
from app.db import db


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile('config.py')

    db.init_app(app)

    from .users import users_bp
    app.register_blueprint(users_bp)

    Migrate(app, db)

    return app
