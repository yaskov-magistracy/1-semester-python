from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator, Annotated
from fastapi import Depends
from DAL.Database import async_session_factory
from DAL.Accounts.AccountsRepository import AccountsRepository
from core.Accounts.AccountsService import AccountsService

async def getDbSession() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session
DbSessionDep = Annotated[AsyncSession, Depends(getDbSession)]

async def getAccountsRepository(session: DbSessionDep) -> AccountsRepository:
    return AccountsRepository(session)
AccountsRepositoryDep = Annotated[AccountsRepository, Depends(getAccountsRepository)]

async def getAccountsService(accountsRepo: AccountsRepositoryDep) -> AccountsService:
    return AccountsService(accountsRepo)
AccountsServiceDep = Annotated[AccountsService, Depends(getAccountsService)]