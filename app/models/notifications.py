from tortoise import fields, models

class Notifications(models.Model):
    notification_id = fields.IntField(pk=True)
    user_id = fields.ForeignKeyField(
        "models.User",
        related_name="User_notifications",
        on_delete=fields.CASCADE,
    )
    title = fields.CharField(max_length=50)
    message = fields.TextField()
    is_read = fields.BooleanField(default=False)
    noti_time = fields.DatetimeField(auto_now_add=True)
