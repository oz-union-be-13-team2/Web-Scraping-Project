from tortoise import models, fields

class Diary(models.Model):
    diary_id = fields.IntField(pk=True)
    user_id = fields.ForeignKeyField(
        "models.User",
        related_name="diaries",
        on_delete=fields.CASCADE,
    )
    title = fields.CharField(max_length=100)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
