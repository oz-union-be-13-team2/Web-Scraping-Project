# 질문 API

from fastapi import APIRouter, HTTPException, status
from typing import List

from app.models.question import Question
from app.schemas.question import QuestionResponse, QuestionCreate

router = APIRouter(prefix="/questions", tags=["questions"])

@router.post("/", response_model=QuestionResponse, status_code=status.HTTP_201_CREATED)
async def create_question(request: QuestionCreate):
    """
    새로운 자기성찰 질문을 데이터베이스에 추가합니다.
    """
    # 데이터베이스에 새로운 질문을 생성합니다.
    # request.question_text를 사용해 Pydantic 모델에서 받은 데이터를 저장합니다.
    question = await Question.create(question_text=request.question_text)

    # 생성된 질문 객체를 Pydantic 모델로 변환하여 반환합니다.
    return question
@router.get("/", response_model=List[QuestionResponse])
async def list_all_questions():
    """
    모든 자기성찰 질문 목록을 조회합니다.
    """
    questions = await Question.all()
    if not questions:
        raise HTTPException(status_code=404, detail="질문을 찾을 수 없습니다.")
    return questions

@router.get("/{question_id}", response_model=QuestionResponse)
async def get_question_by_id(question_id: int):
    """
    특정 ID의 질문을 조회합니다.
    """
    question = await Question.get_or_none(question_id=question_id)
    if not question:
        raise HTTPException(status_code=404, detail="해당 ID의 질문을 찾을 수 없습니다.")
    return question