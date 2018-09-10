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


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


from sqlalchemy import event


@pytest.yield_fixture(scope="function", autouse=True)
def session(db):
    """
    Referred from : https://github.com/pytest-dev/pytest-flask/issues/70#issuecomment-361005780

    :param db:
    :return:
    """
    with db.app.app_context():
        conn = _db.engine.connect()
        txn = conn.begin()

        options = dict(bind=conn, binds={})
        sess = _db.create_scoped_session(options=options)

        sess.begin_nested()

        @event.listens_for(sess(), "after_transaction_end")
        def restart_savepoint(sess2, trans):
            if trans.nested and not trans._parent.nested:
                sess2.expire_all()
                sess.begin_nested()

        _db.session = sess
        yield sess

        sess.remove()
        txn.rollback()
        conn.close()


@pytest.fixture(scope="function")
def dummy_user():
    from app.users.services import UsersService

    users_service = UsersService()

    data = {
        "first_name": "Sudhir",
        "last_name": "Shrestha",
        "username": "sudhirt4",
        "password": "password",
    }
    user = users_service.create(**data)
    return user


@pytest.fixture(scope="function")
def dummy_user_data():
    return {
        "first_name": "Sudhir",
        "last_name": "Shrestha",
        "username": "sudhirt4",
        "password": "password",
    }
