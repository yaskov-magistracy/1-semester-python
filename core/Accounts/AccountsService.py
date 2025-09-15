from .DTO import RegisterRequest, LoginRequest, LoginResponse
from DAL.AccountsRepository import AccountsRepository
from DAL.Models import AccountModel

class AccountsService():
    accountsRepo: AccountsRepository

    def __init__(self, accountsRepo: AccountsRepository):
        self.accountsRepo = accountsRepo

    async def Register(self, request: RegisterRequest):
        pass