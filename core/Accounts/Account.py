import uuid
from .AccountRole import AccountRole

class Account():
    id: uuid
    login: str
    email: str
    passwordHash: str
    role: AccountRole

    def __init__(self, id, login, email, passwordHash, role):
        self.id = id
        self.login = login
        self.email = email
        self.passwordHash = passwordHash
        self.role = role