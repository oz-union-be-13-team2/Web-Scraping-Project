from pydantic import BaseModel

class QuestionCreate(BaseModel):
    """
    새로운 질문을 생성할 때 사용되는 스키마입니다.
    """
    question_text: str

class QuestionResponse(BaseModel):
    """
    질문 조회 및 응답에 사용되는 스키마입니다.
    """
    question_id: int
    question_text: str

    class Config:
        from_attributes = True