from typing import Any, Dict
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.inspection import inspect


class Base(DeclarativeBase):
    """
    Classe que permite conectar objetos a tabelas no banco de dados, além de mapealas para que a classe vire uma tabela no banco de dados
    
    Caso seja printada, a classe irá exibir todos os seus atributos e valores (caso tenha)
    """
    def __repr__(self) -> str:
        cls = self.__class__
        column_attrs = inspect(cls).mapper.column_attrs
        columns = {attr.key: getattr(self, attr.key) for attr in column_attrs}
        columns_str = ", ".join(f"{key}={value!r}" for key, value in columns.items())
        return f"{cls.__name__}({columns_str})"
    
    def dict(self, *args, **kwargs) -> Dict[str, Any]:
        """
        Converte o objeto para um dicionário, removendo chaves com valores None.
        
        Args:
            *args: Argumentos adicionais para a conversão.
            **kwargs: Argumentos adicionais para a conversão.
            
        Returns:
            Dict[str, Any]: O objeto convertido em dicionário.
        """
        column_attrs = inspect(self.__class__).mapper.column_attrs
        columns = {attr.key: getattr(self, attr.key) for attr in column_attrs}
        columns = {k: v for k, v in columns.items() if v is not None}
        return columns