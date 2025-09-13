from fastapi import APIRouter
from .AccountsApi import accountsApiRouter

apiRouters = APIRouter(
    prefix="/api/v1"
)
apiRouters.include_router(accountsApiRouter)