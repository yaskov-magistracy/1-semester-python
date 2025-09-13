from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator, Annotated
from fastapi import Depends
from infra.database import async_session_factory
from DAL.Accounts.AccountsRepository import AccountsRepository
from core.Accounts.AccountsService import AccountsService

async def getDbSession() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session
DbSessionDep = Annotated[AsyncSession, Depends(getDbSession)]

async def getAccountsRepo(session: DbSessionDep) -> AccountsRepository:
    return AccountsRepository(session)
UserRepositoryDep = Annotated[AccountsRepository, Depends(getAccountsRepo)]

async def getAccountsService(accountsRepo: AccountsRepository) -> AccountsService:
    return AccountsService(accountsRepo)
AccountsServiceDep = Annotated[AccountsService, Depends(getAccountsService)]