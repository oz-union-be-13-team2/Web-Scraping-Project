from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models import User

router = APIRouter(prefix="/users", tags=["users"])

class UserRequest(BaseModel):
    user_name : str
    password : str

class UserResponse(BaseModel):
    user_id : int
    user_name: str
    password : str

@router.post("/", response_model=UserResponse)
async def create_user(request: UserRequest):
    user = await User.create(
        user_name=request.user_name,
        password=request.password,
    )
    return UserResponse(
        user_id = user.user_id,
        user_name = user.user_name,
        password = user.password,
    )

@router.get("/{user_id}", response_model=UserResponse)
async def list_users(user_id:int):
    user = await User.get_or_none(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(
        user_id = user.user_id,
        user_name = user.user_name,
        password = user.password,
    )
