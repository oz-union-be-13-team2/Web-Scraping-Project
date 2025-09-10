from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# --- User Signup ---
router = APIRouter(prefix="/users", tags=["users"])

class UserRequest(BaseModel):
    user_name: str
    password: str
class UserResponse(BaseModel):
    id: int
    user_name: str


@router.post("/", response_model= UserResponse)
async def create_user(response: UserResponse):





# 예시 API 엔드포인트 스펙 설명
"""
POST /api/users/signup
Request Body: UserSignupRequest
Response Body: UserSignupResponse
Status Code: 201 Created
"""