from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URL: str = Field(
        title="URL do banco de dados",
        description="URL do banco de dados",
        default="postgresql://user:password@localhost:5432/database"
    ) 
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)  


config = Settings()