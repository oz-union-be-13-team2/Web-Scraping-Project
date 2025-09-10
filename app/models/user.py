from tortoise import models, fields


class User(models.Model):
    user_id = fields.IntField(pk=True)
    user_name = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100)