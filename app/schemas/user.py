from pydantic import Field


from app.schemas.settings.base import BaseSchema
from app.schemas.settings.fields import(
    name_field,
    phone_field,
    email_field,
    password_field,
)
from app.schemas.settings.validators import (
    validate_email,
    validate_name,
    validate_password,
    validate_phone,
)


class UserRequest(BaseSchema):
    """
    Class to validate the request body of the user register endpoint.
    
    - Args:
        - name: str,
        - phone: str,
        - email: str,
        - password: str
        
    - Attributes:
        - name: str,
        - phone: str,
        - email: str,
        - password: str
        
    - Raises:
        - ValidationError: If any field is invalid.
    """
    name: str = name_field()
    phone: str = phone_field()
    email: str = email_field()
    password: str = password_field()
    
    __name_validator = validate_name
    __phone_validator = validate_phone
    __email_validator = validate_email
    __password_validator = validate_password
    