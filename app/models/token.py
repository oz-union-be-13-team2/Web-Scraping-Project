from tortoise import models, fields

class Token(models.Model):
    token_id = fields.IntField(pk=True)
    user_id = fields.ForeignKeyField(
        "models.User",
        related_name="tokens",
        on_delete=fields.CASCADE,
    )
    token = fields.TextField()
    expired_at = fields.DatetimeField(auto_now_add=True)
