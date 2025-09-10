from fastapi import APIRouter, HTTPException, status
from typing import List

from app.models.user_question import UserQuestion
from app.schemas.user_question import UserQuestionCreate, UserQuestionResponse
# from app.dependencies import get_current_user # 실제 JWT 인증 함수

router = APIRouter(prefix="/user_questions", tags=["user_questions"])

# 임시로 user_id를 1로 설정. 실제로는 JWT 토큰에서 추출
USER_ID = 1


# 👉 특정 질문에 대한 답변 등록 (보안 강화)
@router.post("/", response_model=UserQuestionResponse, status_code=status.HTTP_201_CREATED)
async def create_user_question(request: UserQuestionCreate):
    # 클라이언트로부터 user_id를 받지 않고, 서버가 인증된 사용자 ID를 사용
    # 현재는 임시로 USER_ID 변수를 사용
    user_question = await UserQuestion.create(
        user_id=USER_ID,
        question_id=request.question_id,
        answer_text=request.answer_text,
    )
    return user_question


# 👉 로그인한 사용자의 답변 리스트 조회
@router.get("/", response_model=List[UserQuestionResponse])
async def list_user_questions():
    # 전체가 아닌, 로그인한 사용자 본인의 답변만 조회
    user_questions = await UserQuestion.filter(user_id=USER_ID).order_by("-answered_at")

    if not user_questions:
        raise HTTPException(status_code=404, detail="답변을 찾을 수 없습니다.")

    return user_questions

@router.delete("/{question_id}", status_code=204)
async def delete_user_question(question_id: int):
    user_question = await UserQuestion.filter(user_id=USER_ID, question_id=question_id).first()
    if not user_question:
        raise HTTPException(status_code=404, detail="존재하지 않는 답변입니다.")
    await user_question.delete()
    return None
