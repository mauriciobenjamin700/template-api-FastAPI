from pytest import fixture
import sys


sys.path.append('app')


from app.db.configs.connection import Session


@fixture
def db_session():
    try:
        session = Session()
        yield session

    finally:
        session.close()