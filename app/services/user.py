from sqlalchemy.ext.asyncio import AsyncSession

from app.core.constants.enums.user import UserRoles
from app.core.constants.messages import ERROR_DATABASE_USER_NOT_FOUND
from app.core.errors import NotFoundError
from app.db.models import UserModel
from app.db.repositories.user import UserRepository
from app.schemas.user import (
    UserRequest,
    UserResponse
)


class UserService:
    """
    A service class to handle user operations.
    
    - Args:
        - db_session: AsyncSession : A database session object.
        
    - Attributes:
        - repository: UserRepository : A repository object to handle database operations for the user.
    
    
    """
    def __init__(self, db_session: AsyncSession):
        self.repository = UserRepository(db_session)


    async def add(self, request: UserRequest) -> UserResponse:
        """
        A method to add a user to the database.
        
        - Args:
            - request: UserRequest : A user request object.
            
        - Returns:
            - response: UserResponse : A user response object
        """
        
        model = self.map_request_to_model(request)
        
        model = await self.repository.add(model)
        
        response = self.map_model_to_response(model)
        
        return response
        

    async def get_by_id(self, user_id: str) -> UserResponse:
        """
        A method to get a user by id.
        
        - Args:
            - user_id: str : A user id.
        - Returns:
            - response: UserResponse : A user response object with the user data.
        """
        
        model = await self.repository.get(id=user_id)
        
        if not model:
            
            raise NotFoundError(ERROR_DATABASE_USER_NOT_FOUND)
        
        response = self.map_model_to_response(model)
        
        return response
        
    
    async def get_all(self):
        pass

    async def update(self, id: str, request: UserRequest):
        pass

    async def delete(self, id: str):
        pass
    
    
    def map_request_to_model(self, request: UserRequest) -> UserModel:
        """
        A method to map a user request to a user model.
        
        - Args:
            - request: UserRequest : A user request object.
            
        - Returns:
            - model: UserModel : A user model object.
        """
        model = UserModel(
            **request.to_dict(
                include={
                    "role": UserRoles.USER.value
                }
            )
        )
        
        return model
    
    
    def map_model_to_response(self, model: UserModel) -> UserResponse:
        """
        A method to map a user model to a user response.
        
        - Args:
            - model: UserModel : A user model object.
            
        - Returns:
            - response: UserResponse : A user response object.
        """
        response = UserResponse(
            **model.to_dict(
                exclude=[
                    "password"
                ]
            )
        )
        
        return response