from fastapi import Depends, HTTPException, Request, Response
from core.Accounts.DTO.LoginResponse import LoginResponse
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

def GetAuthInfo(request: Request) -> LoginResponse:
    token = request.cookies.get(AUTH_TOKEN_KEY)
    if not token:
        raise HTTPException(401)
    
    session = authSessions.get(uuid.UUID(token), None)
    if not session:
        raise HTTPException(401, "Token is dead")
    return session
AuthInfo = Annotated[LoginResponse, Depends(GetAuthInfo)]