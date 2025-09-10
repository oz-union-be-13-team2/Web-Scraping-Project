from tortoise import fields, models

class Bookmark(models.Model):
    bookmark_id = fields.IntField(pk=True)

    # 외래키 (Quote, User)
    quote = fields.ForeignKeyField(
        "models.Quote",
        related_name="bookmarks",
        on_delete=fields.CASCADE,
    )
    user = fields.ForeignKeyField(
        "models.User",
        related_name="bookmarks",
        on_delete=fields.CASCADE,
    )

    class Meta:
        table = "bookmarks"

    def __str__(self):
        return f"Bookmark(user={self.user_id}, quote={self.quote_id})"
