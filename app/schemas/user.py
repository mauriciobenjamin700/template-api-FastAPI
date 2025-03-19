from pydantic import Field


from app.core.constants.messages.user import *
from app.schemas.base import BaseSchema


class UserRequest(BaseSchema):
    name: str = Field(
        title="Nome",
        description="Nome do usuário",
        examples=["User Example"],
        default=None,
        validate_default=True
    )
    phone: str = Field(
        title="Telefone",
        description="Telefone do usuário",
        examples=["+5511999999999"],
        default=None,
        validate_default=True
    )
    email: str = Field(
        title="Email",
        description="Email do usuário",
        examples=["user@example.com"],
        default=None,
        validate_default=True
    )
    password: str = Field(
        title="Senha",
        description="Senha do usuário",
        examples=["123456"],
        default=None,
        validate_default=True
    )
    level: str = Field(
        title="Nível",
        description="Nível do usuário",
        examples=["user", "admin"],
        default=None,
        validate_default=True
    )
    cpf_cnpj: str = Field(
        title="CPF/CNPJ",
        description="CPF ou CNPJ do usuário",
        examples=["12345678901"],
        default=None,
        validate_default=True
    )
    pixkey_type: str = Field(
        title="Tipo de Pix Key",
        description="Tipo de Pix Key do usuário",
        examples=["RANDOM", "CPF", "CNPJ", "EMAIL", "PHONE"],
        default=None,
        validate_default=True
    )
    pixkey: str = Field(
        title="Pix Key",
        description="Pix Key do usuário",
        examples=["ADADADADASDAAFA"],
        default=None,
        validate_default=True
    )