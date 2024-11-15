from pytest import fixture

from database.connection import Session

@fixture
def db_session():
    try:
        session = Session()
        yield session

    finally:
        session.close()