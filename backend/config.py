from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

class Settings(BaseSettings):
    def DATABASE_CONNECTION_STRING(self) -> str:
        return os.getenv('DATABASE_CONNECTION_STRING')

    def EMAIL_LOGIN(self) -> str:
        return os.getenv('EMAIL_LOGIN')

    def EMAIL_PASSWORD(self) -> str:
        return os.getenv('EMAIL_PASSWORD')
    
    def REDIS_HOST(self) -> str:
        return os.getenv('REDIS_HOST')
    
    def REDIS_PORT(self) -> str:
        return os.getenv('REDIS_PORT')
    
    def REDIS_PASSWORD(self) -> str:
        return os.getenv('REDIS_PASSWORD')


load_dotenv()
settings = Settings()