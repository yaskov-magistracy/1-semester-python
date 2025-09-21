from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    def DATABASE_CONNECTION_STRING(self) -> str:
        return "postgresql+asyncpg://postgres:password@localhost:5432/python2"

    def EMAIL_LOGIN(self) -> str:
        return "chernorusy@mail.ru"

    def EMAIL_PASSWORD(self) -> str:
        return ""
    
    def REDIS_HOST(self) -> str:
        return "127.0.0.1"
    
    def REDIS_PORT(self) -> str:
        return "6380"
    
    def REDIS_PASSWORD(self) -> str:
        return "password"

settings = Settings()