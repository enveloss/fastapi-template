from .base import Base
from sqlalchemy import Column, TIMESTAMP, Text, Integer

from datetime import datetime

from src.schemas.user import UserSchema

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    token = Column(Text)
    balance = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP(True), nullable=False, index=True, default=datetime.now)
   
    def to_user_schema(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            balance=self.balance,
            created_at=self.created_at,
        )