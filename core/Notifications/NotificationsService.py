from DAL.NotificationsRepository import NotificationsRepository
from core.Notifications.DTO.AddNotificationRequest import AddNotificationRequest
from core.Notifications.DTO.RepeatNotificationRequest import RepeatNotificationRequest
from DAL.Models import NotificationModel
import uuid
from typing import List
from fastapi import HTTPException
from .Notification import Notification

class NotificationsService():
    notificationsRepo: NotificationsRepository

    def __init__(self, notificationsRepo: NotificationsRepository):
        self.notificationsRepo = notificationsRepo
    
    async def Add(
        self,
        accountdId: uuid,
        request: AddNotificationRequest
        ) -> Notification:
        notification = await self.notificationsRepo.Add(NotificationModel(accountId=accountdId, time=request.time, text=request.text))
        return self.ToApiModel(notification)

    async def Repeat(
        self,
        request: RepeatNotificationRequest
        ) -> Notification:
        notification = await self.notificationsRepo.GetById(request.targetId)
        newNotification = NotificationModel(accountId=notification.accountId, text=notification.text, time=request.newTime)
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