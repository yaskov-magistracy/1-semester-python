from fastapi import APIRouter, Depends, HTTPException, Response, Request, Body
from api.configuration.DI import AccountsServiceDep
from core.Accounts.AccountRole import AccountRole
from core.Accounts.DTO.BlockRequest import BlockRequest
from core.Accounts.DTO.RegisterRequest import RegisterRequest
from core.Accounts.DTO.LoginRequest import LoginRequest
from core.Accounts.DTO.LoginResponse import LoginResponse
from typing import Annotated
from uuid import uuid4
from api.configuration.Auth import AUTH_TOKEN_KEY, SetCookie, AuthInfo
import uuid

notificationsApiRouter = APIRouter(
    prefix="/notifications",
    tags=["Notifications"],
)

