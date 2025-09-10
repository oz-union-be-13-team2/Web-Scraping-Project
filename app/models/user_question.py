from tortoise import fields, models


class UserQuestion(models.Model):
    user_question_id = fields.IntField(pk=True)  # 기본키 이름 명확화
    user = fields.ForeignKeyField(
        "models.User",
        related_name="user_questions",
        on_delete=fields.CASCADE,
    )
    question = fields.ForeignKeyField(
        "models.Question",
        related_name="user_questions",
        on_delete=fields.CASCADE,
    )
    answer_text = fields.TextField(null=True)
    answered_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_questions"

    def __str__(self):
        return f"UserQuestion(id={self.user_question_id})"