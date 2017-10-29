# coding: utf-8
import pytest
from decouple import config

from banking.app import create_app, db as _db

_app = create_app()


@pytest.fixture(scope="session")
def app(request):
    # Sobrescreve a string de conexão com o banco de dados da aplicação para usar o banco de testes
    _app.config["SQLALCHEMY_DATABASE_URI"] = config("SQLALCHEMY_DATABASE_URI_TEST", "sqlite:///:memory:")
    ctx = _app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return _app


@pytest.fixture(scope="session", autouse=True)
def db(app, request):
    def teardown():
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture
def api_test_client(app):
    return app.test_client()
