'''
Entry point for app tests
'''

import os
import pytest

from flask import Request

from app import create_app
from app.models import db as _db


#TODO: Figure out how to test things


@pytest.fixture(scope='session')
def app(request):
    '''Session-wide test Flask application.'''
    app = create_app(__name__, 'app/test_config.py')

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""

    def teardown():
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


def get_resource(app, path):
    testClient = app.test_client()
    rv = testClient.get(path)
    assert(rv.status_code == 200)


def test_get_index(app):
    get_resource(app, '/')


def test_get_humanstxt(app):
    # get_resource(app, '/humans.txt')
