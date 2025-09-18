from fastapi import APIRouter
from api.configuration.DI import NotificationsServiceDep
from core.Notifications.DTO.AddNotificationRequest import AddNotificationRequest
from core.Notifications.DTO.RepeatNotificationRequest import RepeatNotificationRequest
from DAL.Models import NotificationModel
from api.configuration.Auth import AuthInfo, AdminAuthInfo
from core.Notifications.Notification import Notification

notificationsApiRouter = APIRouter(
    prefix="/notifications",
    tags=["Notifications"],
)

@notificationsApiRouter.post("/")
async def Add(
    notificationsService: NotificationsServiceDep,
    authInfo: AuthInfo,
    request: AddNotificationRequest
    ) -> Notification:
    return await notificationsService.Add(authInfo.id, request)

@notificationsApiRouter.post("/repeat")
async def Repeat(
    notificationsService: NotificationsServiceDep,
    authInfo: AuthInfo,
    request: RepeatNotificationRequest
    ) -> Notification:    
    return await notificationsService.Repeat(request)

@notificationsApiRouter.get("/")
async def GetAll(
    notificationsService: NotificationsServiceDep,
    authInfo: AdminAuthInfo
    ) -> list[Notification]:
    return await notificationsService.GetAll()


@notificationsApiRouter.get("/my")
async def GetMy(
    notificationsService: NotificationsServiceDep,
    authInfo: AuthInfo
    ) -> list[Notification]:
    return await notificationsService.GetMy(authInfo.id) 