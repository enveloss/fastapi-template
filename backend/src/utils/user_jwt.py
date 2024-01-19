from pydantic import BaseModel

import jwt
from src.config import config

class UserJWTPayload(BaseModel):
    user_id: int

def create_jwt(payload: UserJWTPayload) -> str:
    return jwt.encode(
        payload=payload.model_dump(), 
        key=config.base.jwt_key
    )

def validate_jwt(token: str) -> UserJWTPayload:
    payload = jwt.decode(
        jwt=token.encode(),
        key=config.base.jwt_key,
        algorithms=['HS256']
    )

    return UserJWTPayload(**payload)

