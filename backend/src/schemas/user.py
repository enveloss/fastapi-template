from pydantic import BaseModel

from datetime import datetime

class UserSchema(BaseModel):
    id: str
    balance: int
    created_at: datetime