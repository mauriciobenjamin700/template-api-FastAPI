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
    name: str = name_field()
    phone: str = phone_field()
    email: str = email_field()
    password: str = password_field()