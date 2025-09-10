from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 👉 API 요청에 사용되는 모델
class UserQuestionCreate(BaseModel):
    """
    사용자가 답변을 생성할 때 보내는 요청 데이터의 스키마.
    user_id는 서버에서 처리하므로 포함하지 않음.
    """
    question_id: int
    answer_text: str

# 👉 API 응답에 사용되는 모델
class UserQuestionResponse(BaseModel):
    """
    서버가 클라이언트에게 보내는 답변 데이터의 스키마.
    """
    user_question_id: int
    user_id: int
    question_id: int
    answer_text: Optional[str] = None
    answered_at: datetime

    class Config:
        # Pydantic V2에서 ORM 모드를 활성화하는 방법
        from_attributes = True