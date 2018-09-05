# https://github.com/sunscrapers/flask-boilerplate/blob/master/tests/conftest.py

import pytest
from app import create_app, db as _db


@pytest.yield_fixture(scope="session")
def app():
    _app = create_app(is_test=True)

    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()

    return _app


@pytest.yield_fixture(scope="session")
def db(app):
    _db.app = app
    _db.create_all()

    yield _db

    _db.drop_all()

    return _db


@pytest.fixture(scope="session", autouse=True)
def client(app):
    return app.test_client()


@pytest.yield_fixture(scope="function", autouse=True)
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection)
    session = db.create_scoped_session(options=options)

    db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()
