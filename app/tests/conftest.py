from pytest import fixture

from db.connection import Session

@fixture
def db_session():
    try:
        session = Session()
        yield session

    finally:
        session.close()