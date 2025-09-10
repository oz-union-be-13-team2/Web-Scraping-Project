from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from app.models.notification import Notification
from app.schemas.notification import NotificationResponse

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.get("/", response_model=List[NotificationResponse])
async def get_user_notifications(is_read: Optional[bool] = None):
    # 실제 user_id는 JWT 토큰에서 가져와야 함
    user_id = 1

    query = Notification.filter(user_id=user_id)

    if is_read is not None:
        query = query.filter(is_read=is_read)

    notifications = await query.order_by("-noti_time")

    # 알림이 없을 경우 빈 리스트 반환
    if not notifications:
        # 혹은 404 에러를 발생시켜 클라이언트에게 알릴 수 있음
        # raise HTTPException(status_code=404, detail="알림을 찾을 수 없습니다.")
        return []

    return notifications

@router.put("/{notification_id}/read", response_model=NotificationResponse)
async def update_notification_read_status(notification_id: int):
    """특정 알림을 읽음 처리합니다."""
    notification = await Notification.filter(
        notification_id=notification_id,
        user_id=USER_ID
    ).first()

    if not notification:
        raise HTTPException(status_code=404, detail="알림을 찾을 수 없습니다.")

    notification.is_read = True
    await notification.save()

    return notification

@router.delete("/{notification_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_notification(notification_id: int):
    """특정 알림을 삭제합니다."""
    notification = await Notification.filter(
        notification_id=notification_id,
        user_id=USER_ID
    ).first()

    if not notification:
        raise HTTPException(status_code=404, detail="알림을 찾을 수 없습니다.")

    await notification.delete()
    return {"message": "알림이 성공적으로 삭제되었습니다."}