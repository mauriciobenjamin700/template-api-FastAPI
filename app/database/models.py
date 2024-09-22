from datetime import datetime
from sqlalchemy import Boolean, DateTime, Float, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from api.app.database.base import Base
from api.app.database.connection import engine


class Client(Base):
    """
    
    - Attributes: 
        - id: str PK,
        - google_id: str UNIQUE,
        - name: str NOT NULL,
        - phone: str UNIQUE NOT NULL,
        - email: str UNIQUE NOT NULL,
        - password: str NOT NULL
        - level: str NOT NULL # ["CLIENT", "INTERLOCUTOR", "PRODUCER"]
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
