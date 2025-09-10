class Bookmark(models.Model):
    bookmark_id = fields.IntField(pk=True)
    quote_id = fields.ForeignKeyField(
        "models.Quote",
        related_name="bookmarks",
        on_delete=fields.CASCADE,
    )
    user_id = fields.ForeignKeyField(
        "models.User",
        related_name="bookmarks",
        on_delete=fields.CASCADE,
    )