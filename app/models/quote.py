from tortoise import fields, models

class Quote(models.Model):
    quote_id = fields.IntField(pk=True)
    content = fields.TextField()
    author = fields.CharField(max_length=100, null=True)
    language = fields.CharField(max_length=50, null=True)
    source = fields.CharField(max_length=100, null=True)

    # Bookmark와 관계 (1:N)
    bookmarks: fields.ReverseRelation["Bookmark"]

    class Meta:
        table = "quotes"

    def __str__(self):
        return f"{self.content[:40]} - {self.author or 'Unknown'}"
