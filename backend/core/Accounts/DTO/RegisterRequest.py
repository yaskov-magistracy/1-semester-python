from pydantic import BaseModel, EmailStr

from DAL.Models import AccountRoleModel

class RegisterRequest(BaseModel):
    login: str
    email: EmailStr
    password: str
    role: AccountRoleModel