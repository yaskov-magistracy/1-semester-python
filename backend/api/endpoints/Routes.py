from fastapi import APIRouter
from .AccountsApi import accountsApiRouter
from .NotificationsApi import notificationsApiRouter

apiRouters = APIRouter(
    prefix="/api/v1"
)
apiRouters.include_router(accountsApiRouter)
apiRouters.include_router(notificationsApiRouter)