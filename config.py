from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    def DATABASE_CONNECTION_STRING(self) -> str:
        return "postgresql+asyncpg://postgres:password@localhost:5432/python"
    
settings = Settings()