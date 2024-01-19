from fastapi import Header, HTTPException

from logging import getLogger
from src.utils.user_jwt import validate_jwt, UserJWTPayload

logger = getLogger(__name__)

def user_jwt(user_jwt=Header(None)) -> UserJWTPayload:
    try: 
        return validate_jwt(user_jwt)
    except Exception as e: 
        logger.error(f'User JWT Error - {e}')
        raise HTTPException(401, detail='JWT_IS_INVALID')