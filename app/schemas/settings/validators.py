from pydantic import field_validator
from re import match

from app.core.errors import ValidationError
from app.core.constants.messages import (
    ERROR_EMAIL_INVALID_FORMAT_TYPE,
    ERROR_EMAIL_INVALID_FORMAT_MASK,
    ERROR_NAME_INVALID_FORMAT_MIN_LENGTH,
    ERROR_PASSWORD_INVALID_FORMAT_DIGIT,
    ERROR_PASSWORD_INVALID_FORMAT_LOWERCASE,
    ERROR_PASSWORD_INVALID_FORMAT_MAX_LENGTH,
    ERROR_PASSWORD_INVALID_FORMAT_MIN_LENGTH,
    ERROR_PASSWORD_INVALID_FORMAT_SPECIAL_CHARACTER,
    ERROR_PASSWORD_INVALID_FORMAT_UPPERCASE,
    ERROR_PHONE_INVALID_FORMAT_LENGTH,
)


@field_validator("email", mode="before")
def validate_email(cls, value: str) -> str:
    """
    A function that validates the email field.

    - Args:
        - cls: The class instance.
        - value: The email value.
    - Returns:
        - str: The email value.
    """
    if not isinstance(value, str):
        raise ValidationError(field="email", detail=ERROR_EMAIL_INVALID_FORMAT_TYPE)
    
    value = value.strip()
    
    if not match(r"[^@]+@[^@]+\.[^@]+", value):
        raise ValidationError(field="email", detail=ERROR_EMAIL_INVALID_FORMAT_MASK)
    
    return value

@field_validator("name", mode="before")
def validate_name(cls, value: str) -> str:
    """
    A function that validates the name field.

    - Args:
        - cls: The class instance.
        - value: The name value.
    - Returns:
        - str: The name value.
    """
    if not isinstance(value, str):
        raise ValidationError(field="name", detail=ERROR_NAME_INVALID_FORMAT_TYPE)
    
    value = value.strip()
    
    if len(value) <= 1:
        raise ValidationError(field="name", detail=ERROR_NAME_INVALID_FORMAT_MIN_LENGTH)
    
    value = value.upper()
    
    return value

@field_validator("password", mode="before")
def validate_password(cls, value: str) -> str:
    """
    A function that validates the password field.

    - Args:
        - cls: The class instance.
        - value: The password value.
    - Returns:
        - str: The password value.
    """
    if not isinstance(value, str):
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_TYPE)
    
    value = value.strip()
    
    if len(value) < 8:
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_MIN_LENGTH)
    
    if len(value) > 255:
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_MAX_LENGTH)
    
    if not any(char.isdigit() for char in value):
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_DIGIT)
    
    if not any(char.islower() for char in value):
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_LOWERCASE)
    
    if not any(char.isupper() for char in value):
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_UPPERCASE)
    
    if not any(char in "!@#$%&*()_+-=[]{};:,.<>?/" for char in value):
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_SPECIAL_CHARACTER)
    
    return value

@field_validator("phone", mode="before")
def validate_phone(cls, value: str) -> str:
    """
    A function that validates the phone field.

    - Args:
        - cls: The class instance.
        - value: The phone value.
    - Returns:
        - str: The phone value.
    """
    if not isinstance(value, str):
        raise ValidationError(field="phone", detail=ERROR_PHONE_INVALID_FORMAT_TYPE)
    
    value = value.strip()
    
    value = "".join([char for char in value if char.isdigit()])
    
    if len(value) < 11:
        raise ValidationError(field="phone", detail=ERROR_PHONE_INVALID_FORMAT_LENGTH)
    
    return value