from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class DiaryBase(BaseModel):
    title : str = Field(...,max_length=100)
    content : str = Field(...,max_length=100)

class DiaryCreateRequest(DiaryBase):
    pass

class DiaryUpdateRequest(BaseModel):
    title : Optional[str] = Field(None, max_length=100)
    content : Optional[str] = Field(None, max_length=1000)

class DiaryResponse(DiaryBase):
    diary_id : int
    user_id : int
    created_at : datetime

class Config:
    orm_mode = True