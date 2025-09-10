from tortoise import models, fields


class Quote(models.Model):
    quote_id = fields.IntField(pk=True)
    content = fields.TextField()
    author = fields.CharField(max_length=100)
    language = fields.CharField(max_length=50)
    source = fields.CharField(max_length=100)
