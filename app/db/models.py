from os.path import(
    abspath,
    dirname
)
from sqlalchemy import (
    String,
)
from sqlalchemy.orm import (
    Mapped, 
    mapped_column
)

from app.db.configs.base import Base


class UserModel(Base):
    """
    
    - Attributes: 
        - id: str PK,
        - name: str NOT NULL,
        - phone: str UNIQUE NOT NULL,
        - email: str UNIQUE NOT NULL,
        - password: str NOT NULL
        - role: str NOT NULL # ["user", "admin"]

    """
    __tablename__ = 'client'  
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String, unique=True,nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    level: Mapped[str] = mapped_column(String, nullable=False)
    cpf_cnpj: Mapped[str] = mapped_column(String, nullable=True)
    pixkey_type: Mapped[str] = mapped_column(String, nullable=True)
    pixkey: Mapped[str] = mapped_column(String, nullable=True)