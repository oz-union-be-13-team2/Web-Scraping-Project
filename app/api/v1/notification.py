from datetime import datetime
from zoneinfo import ZoneInfo
from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel

from app.models.diary import Diary
from app.models.user import User
from app.schemas.diary import DiaryUpdateRequest
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/diaries", tags=["diaries"])

class DiaryRequest(BaseModel):
    title : str
    content : str

class DiaryResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

@router.post("/", response_model=DiaryResponse)
async def create_diary(request: DiaryRequest, current_user: User = Depends(get_current_user)):
    diary = await Diary.create(
        user_id = current_user,
        title=request.title,
        content=request.content,
    )
    return DiaryResponse(
        id = diary.diary_id,
        title = diary.title,
        content = diary.content,
        created_at = diary.created_at.astimezone(ZoneInfo("Asia/Seoul")),
    )

@router.get("/my", response_model=List[DiaryResponse])
async def list_my_diaries(current_user: User = Depends(get_current_user)):
    diaries = await Diary.filter(user_id=current_user.id)
    if not diaries:
        raise HTTPException(status_code=404, detail="Diary not found")
    return [
        DiaryResponse(
            id = d.diary_id,
            title= d.title,
            content= d.content,
            created_at = d.created_at.astimezone(ZoneInfo("Asia/Seoul")),
        )
        for d in diaries
    ]

@router.get("/", response_model=List[DiaryResponse])
async def all_list_diaries():
    diaries = await Diary.all()
    if not diaries:
        raise HTTPException(status_code=404, detail="Diary not found")
    return [
        DiaryResponse(
            id = di.diary_id,
            title= di.title,
            content= di.content,
            created_at = di.created_at.astimezone(ZoneInfo("Asia/Seoul")),
        )
        for di in diaries
    ]

@router.delete("/{diary_id}", status_code=204)
async def delete_diary(
        diary_id : int,
        current_user: User = Depends(get_current_user)
):
    diary = await Diary.get_or_none(diary_id=diary_id)
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")

    if diary.user_id.id != current_user.id:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "Not authorized to delete this diary"
        )
    await diary.delete()
    return None

@router.put("/{diary_id}", response_model=DiaryResponse)
async def update_diary(
        diary_id : int,
        request: DiaryUpdateRequest,
        current_user: User = Depends(get_current_user)
):
    diary = await Diary.get_or_none(diary_id = diary_id)
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")

    diary.title = request.title
    diary.content = request.content
    await diary.save()

    return DiaryResponse(
        id = diary.diary_id,
        title = diary.title,
        content = diary.content,
        created_at = diary.created_at.astimezone(ZoneInfo("Asia/Seoul")),
    )