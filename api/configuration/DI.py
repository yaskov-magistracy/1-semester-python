from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator, Annotated
from fastapi import Depends
from DAL.Database import async_session_factory
from DAL.AccountsRepository import AccountsRepository
from core.Accounts.AccountsService import AccountsService
from DAL.NotificationsRepository import NotificationsRepository
from core.Notifications.NotificationsService import NotificationsService
from core.Notifications.EmailSender import EmailSender

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

async def getEmailSender() -> EmailSender:
    return EmailSender()
EmailSenderDep = Annotated[EmailSender, Depends(getEmailSender)]

async def getNotificationsRepository(session: DbSessionDep) -> NotificationsRepository:
    return NotificationsRepository(session)
NotificationsRepositoryDep = Annotated[NotificationsRepository, Depends(getNotificationsRepository)]

async def getNotificationsService(notificationsRepo: NotificationsRepositoryDep) -> NotificationsService:
    return NotificationsService(notificationsRepo)
NotificationsServiceDep = Annotated[NotificationsService, Depends(getNotificationsService)]