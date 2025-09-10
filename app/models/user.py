from tortoise import fields, models

class User(models.Model):
    user_id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)

    # Bookmark와 관계 (1:N)
    bookmarks: fields.ReverseRelation["Bookmark"]

    class Meta:
        table = "users"

    def __str__(self):
        return self.username
