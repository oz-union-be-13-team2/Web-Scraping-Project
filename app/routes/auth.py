# app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models.user import User
from app.models.token_blacklist import TokenBlacklist
from app.auth import create_access_token, oauth2_scheme, get_db, verify_token

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
def register(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    if db.query(User).filter_by(username=form.username).first():
        raise HTTPException(status_code=400, detail="이미 존재하는 사용자입니다.")
    new_user = User(username=form.username, password=pwd_context.hash(form.password))
    db.add(new_user)
    db.commit()
    return {"message": "회원가입 완료"}

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=form.username).first()
    if not user or not pwd_context.verify(form.password, user.password):
        raise HTTPException(status_code=401, detail="로그인 실패")
    token = create_access_token(data={"sub": str(user.user_id)})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = verify_token(token, db)
    blacklist = TokenBlacklist(user_id=user_id, token=token)
    db.add(blacklist)
    db.commit()
    return {"message": "로그아웃 완료"}
