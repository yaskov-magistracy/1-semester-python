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

accountsApiRouter = APIRouter(
    prefix="/acccounts",
    tags=["Accounts"],
)


@accountsApiRouter.post("/register")
async def Register(
    accountsService: AccountsServiceDep,
    request: RegisterRequest,
    response: Response
    ) -> LoginResponse:
    loginResponse = await accountsService.Register(request)
    SetCookie(response, loginResponse)
    return loginResponse

@accountsApiRouter.post("/login")
async def Login(
    accountsService: AccountsServiceDep,
    request: LoginRequest,
    response: Response
    ) -> LoginResponse:
    loginResponse = await accountsService.Login(request)
    SetCookie(response, loginResponse)
    return loginResponse

@accountsApiRouter.post("/my", summary="Get info about authorized account")
async def My(authInfo: AuthInfo) -> LoginResponse:
    return authInfo

@accountsApiRouter.post("/logout")
async def Logout(request: Request) -> None:
    request.cookies.pop(AUTH_TOKEN_KEY, "")    
    return Response(status_code=204)

@accountsApiRouter.post("/block")
async def Block(
    accountsService: AccountsServiceDep,
    authInfo: AuthInfo,
    blockRequest: BlockRequest
    ):
    if authInfo.role != AccountRole.Admin:
        raise HTTPException(401)
    
    await accountsService.Block(authInfo.id, blockRequest)
    return Response(status_code=204)
