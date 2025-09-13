from pydantic import BaseModel

class RegisterRequest(BaseModel):
    login: str
    email: str
    password: str