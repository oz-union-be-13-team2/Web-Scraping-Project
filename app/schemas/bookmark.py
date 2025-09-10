from pydantic import BaseModel

class BookmarkCreate(BaseModel):
    """북마크 생성 요청"""
    quote_id: int

class BookmarkResponse(BaseModel):
    """북마크 응답"""
    bookmark_id: int
    user_id: int
    quote_id: int

    class Config:
        from_attributes = True
