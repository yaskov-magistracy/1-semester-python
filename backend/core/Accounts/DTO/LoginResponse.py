from ..AccountRole import AccountRole
from pydantic import BaseModel, UUID4

class LoginResponse(BaseModel):
    id: UUID4
    role: AccountRole