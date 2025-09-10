# app/models/token_blacklist.py
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class TokenBlacklist(Base):
    __tablename__ = "token_blacklist"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    token = Column(String(512), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
