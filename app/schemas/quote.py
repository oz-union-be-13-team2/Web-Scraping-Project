from pydantic import BaseModel
from typing import Optional

class QuoteCreate(BaseModel):
    content: str
    author: str
    language: Optional[str] = None
    source: Optional[str] = None

class QuoteResponse(BaseModel):
    quote_id: int
    content: str
    author: str
    language: Optional[str] = None
    source: Optional[str] = None

    class Config:
        from_attributes = True   # ORM 객체를 Pydantic 모델로 변환 허용
