import pytest
from app import create_app


@pytest.fixture
def app():
    app = create_app(True)

    yield app


@pytest.fixture
def client():
    return "COOM"


@pytest.fixture
def auth():
    return "auth"
