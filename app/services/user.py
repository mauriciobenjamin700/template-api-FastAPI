from sqlalchemy.orm import Session


from db.repositories.user import UserRepository
from schemas.user import UserRequest


class UserUseCases:
    def __init__(self, db_session: Session):
        self.repository = UserRepository(db_session)


    def add(self, request: UserRequest):
        pass

    def get(self, id: str):
        pass
    
    def get_all(self):
        pass

    def update(self, id: str, request: UserRequest):
        pass

    def delete(self, id: str):
        pass