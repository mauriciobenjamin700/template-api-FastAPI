from pytest import fixture

from app.db.configs.connection import Session

@fixture
def db_session():
    try:
        session = Session()
        yield session

    finally:
        session.close()