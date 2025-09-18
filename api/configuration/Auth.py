from fastapi import Depends, HTTPException, Request, Response
from core.Accounts.DTO.LoginResponse import LoginResponse
from api.configuration.DI import AccountsRepositoryDep
from core.Accounts.AccountRole import AccountRole
from typing import Annotated
import uuid
from uuid import uuid4

authSessions = {}

AUTH_TOKEN_KEY = "fastApiCookie"

def SetCookie(response: Response, loginResponse: LoginResponse):
    token = uuid4()
    authSessions[token] = loginResponse
    response.set_cookie(
        key=AUTH_TOKEN_KEY,
        value=token,
        httponly=True,
        max_age=360000,
        secure=True,   
        samesite="lax"   
    )

async def GetAuthInfo(request: Request, accountsRepo: AccountsRepositoryDep) -> LoginResponse:
    token = request.cookies.get(AUTH_TOKEN_KEY)
    if not token:
        raise HTTPException(401)
    
    session = authSessions.get(uuid.UUID(token), None)
    if not session:
        raise HTTPException(401, "Token is dead")
    
    account = await accountsRepo.GetById(session.id)
    if account.blockReason:
        raise HTTPException(403, f"Account is blocked. Reason: {account.blockReason}")
    return session
AuthInfo = Annotated[LoginResponse, Depends(GetAuthInfo)]

async def GetAdminAuthInfo(authInfo: AuthInfo) -> LoginResponse:
    if authInfo.role != AccountRole.Admin:
        raise HTTPException(403, f"You have not permissions")
    
    return authInfo
AdminAuthInfo = Annotated[LoginResponse, Depends(GetAdminAuthInfo)]