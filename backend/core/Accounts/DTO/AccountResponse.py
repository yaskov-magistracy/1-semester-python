from pydantic import BaseModel, UUID4
from ..AccountRole import AccountRole

class AccountResponse(BaseModel):
    id: UUID4
    login: str
    email: str
    role: AccountRole
    blockReason: str | None