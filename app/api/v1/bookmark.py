from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.bookmark import Bookmark
from app.models.quote import Quote
from app.schemas.bookmark import BookmarkCreate, BookmarkResponse
from app.schemas.quote import QuoteResponse

router = APIRouter(prefix="/bookmarks", tags=["bookmarks"])

# ⚠️ 임시 user_id (실제 환경에서는 JWT 인증으로 대체)
USER_ID = 1

@router.post("/", response_model=BookmarkResponse, status_code=status.HTTP_201_CREATED)
async def add_bookmark(request: BookmarkCreate):
    """명언을 북마크에 추가 (중복 방지)"""

    # 1. 중복 방지
    existing = await Bookmark.filter(user_id=USER_ID, quote_id=request.quote_id).first()
    if existing:
        raise HTTPException(status_code=409, detail="이미 북마크된 명언입니다.")

    # 2. 명언 존재 여부 확인
    quote = await Quote.get_or_none(quote_id=request.quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="존재하지 않는 명언입니다.")

    # 3. 북마크 생성
    bookmark = await Bookmark.create(user_id=USER_ID, quote_id=request.quote_id)
    return BookmarkResponse.model_validate(bookmark)


@router.get("/", response_model=List[QuoteResponse])
async def get_bookmarks():
    """사용자의 모든 북마크 조회"""
    bookmarks = await Bookmark.filter(user_id=USER_ID).prefetch_related("quote")
    return [QuoteResponse.model_validate(b.quote) for b in bookmarks]


@router.delete("/{bookmark_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bookmark(bookmark_id: int):
    """북마크 삭제"""
    deleted = await Bookmark.filter(bookmark_id=bookmark_id, user_id=USER_ID).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail="존재하지 않는 북마크입니다.")
    return None
