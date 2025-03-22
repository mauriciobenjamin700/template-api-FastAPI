from pydantic import Field


def email_field(title: str = "E-mail", description: str = "E-mail", example: str = "email@gmail.com") -> Field:
    
    return Field(
        title=title,
        description=description,
        examples=[example],
        default=None,
        validate_default=True
    )

def message_field(title: str = "Mensagem", description: str = "Mensagem", example: str = "Mensagem") -> Field:
    
    return Field(
        title=title,
        description=description,
        examples=[example],
        default=None,
        validate_default=True
    )

def name_field(title: str = "Nome", description: str = "Nome", example: str = "Jose") -> Field:

    return Field(
        title=title,
        description=description,
        examples=[example],
        default=None,
        validate_default=True
    )    

def password_field(title: str = "Senha", description: str = "Senha", example: str = "password1234") -> Field:
    
    return Field(
        title=title,
        description=description,
        examples=[example],
        default=None,
        validate_default=True
    )

def phone_field(title: str = "Telefone", description: str = "Telefone", example: str = "(11) 99999-9999") -> Field:
    
    return Field(
        title=title,
        description=description,
        examples=[example],
        default=None,
        validate_default=True
    )

def value_field(title: str = "Valor", description: str = "Valor", example: float = 100.00) -> Field:
    
    return Field(
        title=title,
        description=description,
        examples=[example],
        default=None,
        validate_default=True
    )