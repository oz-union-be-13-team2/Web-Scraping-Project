from tortoise import fields, models

class Notification(models.Model):
    notification_id = fields.IntField(pk=True)
    user = fields.ForeignKeyField(
        "models.User",
        related_name="notifications",
        on_delete=fields.CASCADE,
    )
    title = fields.CharField(max_length=50)
    message = fields.TextField()
    is_read = fields.BooleanField(default=False)
    noti_time = fields.DatetimeField(auto_now_add=True)