from tortoise import models, fields

class Question(models.Model):
    question_id = fields.IntField(pk=True)
    question_text = fields.TextField()
