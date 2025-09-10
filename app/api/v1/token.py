
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from datetime import timedelta

from app.core import security
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])

class TokenRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RefreshRequest(BaseModel):
    refresh_token: str

class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/token", response_model=TokenResponse)
async def login_for_tokens(request: TokenRequest):

    user = await User.get_or_none(user_name=request.username)
    if not user or not security.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=30)
    access_token = security.create_access_token(
        data={"sub": str(user.user_id)}, expires_delta=access_token_expires
    )
    refresh_token = security.create_refresh_token(data={"sub": str(user.user_id)})

    return TokenResponse(access_token=access_token, refresh_token=refresh_token)

@router.post("/refresh", response_model=AccessTokenResponse)
async def refresh_access_token(request: RefreshRequest):

    payload = security.decode_token(request.refresh_token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    user_id = payload.get("sub")
    new_access_token = security.create_access_token(data={"sub": user_id})

    return AccessTokenResponse(access_token=new_access_token)
