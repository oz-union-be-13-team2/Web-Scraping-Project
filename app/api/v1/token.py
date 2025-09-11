from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import jwt, JWTError
from tortoise import fields, models
import uuid

from app.core import security
from app.models.user import User

SECRET_KEY = "your-secret-key"   # 나중에 .env로 빼기
ALGORITHM = "HS256"

router = APIRouter(prefix="/token", tags=["token"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token/token")


class RevokedToken(models.Model):
    id = fields.IntField(pk=True)
    jti = fields.CharField(max_length=255, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "revoked_tokens"


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
    jti = str(uuid.uuid4())
    to_encode.update({"exp": expire, "jti": jti})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        jti = payload.get("jti")
        if jti and await RevokedToken.get_or_none(jti=jti):
            return None
        return payload
    except JWTError:
        return None


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
    access_token = create_access_token(
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
    new_access_token = create_access_token(data={"sub": user_id})

    return AccessTokenResponse(access_token=new_access_token)


# logout
@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    payload = await decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    jti = payload.get("jti")
    if jti:
        await RevokedToken.create(jti=jti)

    return {"msg": "Logged out successfully"}


'''# app/auth.py
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.token_blacklist import TokenBlacklist
from app.database import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str, db: Session):
    # 블랙리스트 확인
    blacklisted = db.query(TokenBlacklist).filter(TokenBlacklist.token == token).first()
    if blacklisted:
        raise HTTPException(status_code=401, detail="블랙리스트된 토큰입니다.")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return int(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰입니다.")
'''