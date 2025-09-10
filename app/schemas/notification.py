from pydantic import BaseModel
from datetime import datetime

class NotificationResponse(BaseModel):
    """알림 목록 조회 및 응답에 사용되는 Pydantic 모델입니다."""
    notification_id: int
    user_id: int
    title: str
    message: str
    is_read: bool
    noti_time: datetime

    class Config:
        from_attributes = True