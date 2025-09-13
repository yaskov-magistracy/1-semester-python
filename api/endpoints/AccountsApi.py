from fastapi import APIRouter, HTTPException, Response, Path, Query, Body
from api.configuration.DI import AccountsServiceDep
from core.Accounts.DTO.RegisterRequest import RegisterRequest
from core.Accounts.DTO.LoginRequest import LoginRequest
from core.Accounts.DTO.LoginResponse import LoginResponse
from typing import Annotated

accountsApiRouter = APIRouter(
    prefix="/acccounts",
    tags=["Accounts"],
)


@accountsApiRouter.post("/register", response_model=LoginResponse)
async def Register(
    accountsService: AccountsServiceDep,
    registerRequest: Annotated[RegisterRequest, Body()]
    ) -> LoginResponse:
    response = await accountsService.Register(registerRequest)
    return response