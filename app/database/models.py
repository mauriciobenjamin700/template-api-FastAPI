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
import sys


sys.path.append(abspath(dirname(__file__)))


from configs.base import Base
from configs.connection import engine


class UserModel(Base):
    """
    
    - Attributes: 
        - id: str PK,
        - google_id: str UNIQUE,
        - name: str NOT NULL,
        - phone: str UNIQUE NOT NULL,
        - email: str UNIQUE NOT NULL,
        - password: str NOT NULL
        - level: str NOT NULL # ["user", "admin"]
        - cpf_cnpj: str,
        - pixkey_type: str 
        - pixkey

    """
    __tablename__ = 'client'  
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    google_id: Mapped[str] = mapped_column(String, unique=True, nullable=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String, unique=True,nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    level: Mapped[str] = mapped_column(String, nullable=False)
    cpf_cnpj: Mapped[str] = mapped_column(String, nullable=True)
    pixkey_type: Mapped[str] = mapped_column(String, nullable=True)
    pixkey: Mapped[str] = mapped_column(String, nullable=True)


def create_tables():
    try:
        global engine
        Base.metadata.create_all(bind=engine)
        print("Tabelas criadas com sucesso!")

    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")