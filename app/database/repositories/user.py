from sqlalchemy import select
from sqlalchemy.orm import Session


from database.models import UserModel


class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session


    def add(self, model: UserModel) -> None:
        self.db_session.add(model)
        self.db_session.commit()


    def get(self, id: str) -> UserModel:
        return self.db_session.scalar(
            select(UserModel).where(id=id)
        )
    

    def update(self, model: UserModel) -> UserModel:
        self.db_session.commit()
        self.db_session.refresh(model)
        return model
    

    def delete(self, model: UserModel) -> None:
        self.db_session.delete(model)
        self.db_session.commit()
