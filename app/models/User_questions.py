from tortoise import models, fields


class User_questions(models.Model):
    user_question_id = fields.IntField(pk=True)
    user_id = fields.ForeignKeyField(
        "models.User",
        related_name="User_questions",
        on_delete=fields.CASCADE,
    )
    question_id = fields.ForeignKeyField(
        "models.Question",
        related_name="User_questions",
        on_delete=fields.CASCADE,
    )
    answered_at = fields.DatetimeField(auto_now_add=True)
    answer_text = fields.TextField()
