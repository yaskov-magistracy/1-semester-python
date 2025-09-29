from core.Accounts.DTO.BlockRequest import BlockRequest
from .DTO.RegisterRequest import *
from .DTO.LoginRequest import *
from .DTO.LoginResponse import *
from .DTO.AccountResponse import *
from DAL.AccountsRepository import AccountsRepository
from DAL.Models import AccountModel
from uuid import uuid4
from fastapi import HTTPException
import uuid

class AccountsService():
    accountsRepo: AccountsRepository

    def __init__(self, accountsRepo: AccountsRepository):
        self.accountsRepo = accountsRepo

    async def GetAll(self, iniciatorId: uuid) -> list[AccountResponse]:
        accounts = await self.accountsRepo.SearchAll()
        return map(self.ToApiModel, accounts)

    async def Register(self, request: RegisterRequest) -> LoginResponse:
        existed = await self.accountsRepo.SearchOne(login = request.login) 
        if (existed != None):
            raise HTTPException(400, "Login is occuped")
        existed = await self.accountsRepo.SearchOne(email = request.email) 
        if (existed != None):
            raise HTTPException(400, "Email is occuped")

        created = await self.accountsRepo.Add(AccountModel(
            login=request.login,
            email=request.email, 
            passwordHash=await self.CalculatePasswordHash(request.password),
            role=request.role))
        return LoginResponse(id=created.id, role=created.role, email=created.email)
    
    async def Login(self, request: LoginRequest) -> LoginResponse:
        existed = await self.accountsRepo.SearchOne(login=request.login)
        if (existed == None):
            raise HTTPException(400, "Login or password is incorrect")
        isPasswordCorrect = (await self.CalculatePasswordHash(request.password)) == existed.passwordHash
        if (isPasswordCorrect == False):
            raise HTTPException(400, "Login or password is incorrect")
        if (existed.blockReason != None):
            raise HTTPException(400, f"Account is blocked. reason: {existed.blockReason}")
        
        if existed.blockReason:
            raise HTTPException(400, f"Your account was blocked. Reason: {existed.blockReason}")
        
        return LoginResponse(id=existed.id, role=existed.role, email=existed.email)
    
    async def CalculatePasswordHash(self, password: str) -> str:
        return password # Типо хеширую пароль
    
    async def Block(self, iniciatorId: uuid, request: BlockRequest) -> None:
        iniciator = await self.accountsRepo.GetById(iniciatorId)
        if not iniciator:
            raise HTTPException(403)
        if iniciator.role != AccountRoleModel.Admin:
            raise HTTPException(401)
        
        target = await self.accountsRepo.SearchOne(login=request.targetLogin)
        if not target:
            raise HTTPException(404, f"Account with id: ${request.targetLogin} does not exists")
        
        await self.accountsRepo.UpdateField(target.id, "blockReason", request.blockReason)

    def ToApiModel(self, account: AccountModel) -> AccountResponse:
        return AccountResponse(id=account.id, login=account.login, email=account.email, role=account.role, blockReason=account.blockReason)