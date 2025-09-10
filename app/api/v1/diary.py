# 일기 API
from datetime import datetime
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app.models.diary import Diary

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
async def create_diary(request: DiaryRequest):
    diary = await Diary.create(
        title=request.title,
        content=request.content,
    )
    return DiaryResponse(
        id = diary.diary_id,
        title = diary.title,
        content = diary.content,
        created_at = diary.created_at,
    )

@router.get("/", response_model=List[DiaryResponse])
async def list_diaries():
    diaries = await Diary.all()
    return [
        DiaryResponse(
            id = d.diary_id,
            title = d.title,
            content = d.content,
            created_at = d.created_at,
        )
        for d in diaries
    ]