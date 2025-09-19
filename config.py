from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    def DATABASE_CONNECTION_STRING(self) -> str:
        return "postgresql+asyncpg://postgres:password@localhost:5432/python2"

    def EMAIL_LOGIN(self) -> str:
        return "chernorusy@mail.ru"

    def EMAIL_PASSWORD(self) -> str:
        return ""
    
settings = Settings()