from pydantic import BaseModel

from DAL.Models import AccountRoleModel

class RegisterRequest(BaseModel):
    login: str
    email: str
    password: str
    role: AccountRoleModel