from DAL.NotificationsRepository import NotificationsRepository
from core.Notifications.DTO.AddNotificationRequest import AddNotificationRequest
from core.Notifications.DTO.RepeatNotificationRequest import RepeatNotificationRequest
from DAL.Models import NotificationModel
import uuid
from typing import List
from fastapi import HTTPException
from .Notification import Notification
from core.Notifications.EmailSender import EmailSender
from DAL.AccountsRepository import AccountsRepository

class NotificationsService():
    notificationsRepo: NotificationsRepository
    emailSender: EmailSender
    accountsRepo: AccountsRepository

    def __init__(self, notificationsRepo: NotificationsRepository, emailSender: EmailSender, accountsRepo: AccountsRepository):
        self.notificationsRepo = notificationsRepo
        self.emailSender = emailSender
        self.accountsRepo = accountsRepo
    
    async def Add(
        self,
        accountId: uuid,
        request: AddNotificationRequest
        ) -> Notification:
        print(request)
        notification = await self.notificationsRepo.Add(NotificationModel(accountId=accountId, time=request.time, text=request.text))
        account = await self.accountsRepo.GetById(accountId)
        await self.emailSender.SendEmail(account.email, request.text, request.time)
        return self.ToApiModel(notification)

    async def Repeat(
        self,
        request: RepeatNotificationRequest
        ) -> Notification:
        notification = await self.notificationsRepo.GetById(request.targetId)
        account = await self.accountsRepo.GetById(notification.accountId)
        newNotification = NotificationModel(accountId=notification.accountId, text=notification.text, time=request.newTime)
        await self.emailSender.SendEmail(account.email, newNotification.text, newNotification.time)
        newNotification = await self.notificationsRepo.Add(newNotification)
        return self.ToApiModel(newNotification)

    async def GetAll(
            self
        ) -> list[Notification]:
        notifications = await self.notificationsRepo.SearchAll()
        return map(self.ToApiModel, notifications)


    async def GetMy(
        self,
        accountId: uuid
        ) -> list[Notification]:
        notifications = await self.notificationsRepo.SearchAll(accountId=accountId)
        return map(self.ToApiModel, notifications)
    
    def ToApiModel(self, notificationModel: NotificationModel) -> Notification:
        return Notification(id=notificationModel.id, time=notificationModel.time, text=notificationModel.text)