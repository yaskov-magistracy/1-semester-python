from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    def DATABASE_CONNECTION_STRING(self) -> str:
        envVar = os.getenv('DATABASE_CONNECTION_STRING')
        if envVar:
            return envVar
        return "postgresql+asyncpg://postgres:password@localhost:5432/python2"

    def EMAIL_LOGIN(self) -> str:
        envVar = os.getenv('EMAIL_LOGIN')
        if envVar:
            return envVar
        return "chernorusy@mail.ru"

    def EMAIL_PASSWORD(self) -> str:
        envVar = os.getenv('EMAIL_PASSWORD')
        if envVar:
            return envVar
        return ""
    
    def REDIS_HOST(self) -> str:
        envVar = os.getenv('REDIS_HOST')
        if envVar:
            return envVar
        return "127.0.0.1"
    
    def REDIS_PORT(self) -> str:
        envVar = os.getenv('REDIS_PORT')
        if envVar:
            return envVar
        return "6379"
    
    def REDIS_PASSWORD(self) -> str:
        envVar = os.getenv('REDIS_PASSWORD')
        if envVar:
            return envVar
        return "password"

settings = Settings()