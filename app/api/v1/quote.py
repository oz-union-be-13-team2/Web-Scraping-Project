from fastapi import APIRouter, HTTPException, status
from app.models.quote import Quote
from app.schemas.quote import QuoteCreate, QuoteResponse

router = APIRouter(prefix="/quotes", tags=["quotes"])

@router.post("/", response_model=QuoteResponse, status_code=status.HTTP_201_CREATED)
async def create_quote(request: QuoteCreate):
    """명언 추가"""
    quote = await Quote.create(**request.dict())
    return QuoteResponse.model_validate(quote)

@router.get("/{quote_id}", response_model=QuoteResponse)
async def get_quote(quote_id: int):
    """명언 조회"""
    quote = await Quote.get_or_none(quote_id=quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="명언을 찾을 수 없습니다.")
    return QuoteResponse.model_validate(quote)

@router.delete("/{quote_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_quote(quote_id: int):
    """명언 삭제"""
    deleted_count = await Quote.filter(quote_id=quote_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="존재하지 않는 명언입니다.")
    return None
