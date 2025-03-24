from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)


from app.core.settings import config
from app.db.configs.base import Base
from app.db.models import *


class AsyncDatabaseManager:
    """
    A class to represent an async database manager. It is used to manage the database connection and session.

    - Methods:
        - connect: Connect to the database.
        - disconnect: Disconnect from the database.
        - open_session: Open a new session.
        - close_session: Close the current session.
        - create_tables: Create the tables in the database.
        - drop_tables: Drop the tables in the database.
    """
    def __init__(self, db_url: str = config.DB_URL) -> None:
        self.db_url = db_url
        self.__engine = None
        self.__session_maker = None
        self.__session = None


    def connect(self):
        if self.__engine is None and self.__session_maker is None:
            self.__engine = create_async_engine(
                self.db_url,
                # future=True,
                #echo=True,
                echo=False
            )
            self.__session_maker = async_sessionmaker(
                self.__engine,
                expire_on_commit=False,
                class_=AsyncSession
            )
            self.__session = self.__session_maker()


    async def disconnect(self):
        if self.__engine is not None and self.__session_maker is not None:
            await self.__engine.dispose()
            self.__engine = None
            self.__session_maker = None
            self.__session = None

    async def open_session(self):
        if self.__session is None:
            self.__session = self.__session_maker()

    async def close_session(self):
        if self.__session is not None:
            await self.__session.close()
            self.__session = None

    async def create_tables(self):
        async with self.__engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def drop_tables(self):
        async with self.__engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)


    async def __aenter__(self):
        await self.open_session()
        return self.__session

    async def __aexit__(self, exc_type, exc, tb):
        #await self.close_session()
        pass


db=AsyncDatabaseManager(config.DB_URL)
db.connect()
