from tortoise import fields, models

class User(models.Model):
    user_id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100)

    # Bookmark와 관계 (1:N)
    bookmarks: fields.ReverseRelation["Bookmark"]

    class Meta:
        table = "users"

    def __str__(self):
        return self.username


# app/models/user.py
from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
