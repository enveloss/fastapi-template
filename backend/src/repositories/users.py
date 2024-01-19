from .base.db_repository import DBRepository
from sqlalchemy import insert, update

from src.models import User

from src.utils.user_jwt import create_jwt, UserJWTPayload

class UsersRepository(DBRepository[User]):
    model = User

    async def create_user(self, **data) -> User:
        stmt = insert(User).values(**data).returning(User)
        res = await self.conn.execute(stmt)
        user = res.scalar()

        stmt = update(User)\
            .where(User.uuid == user.uuid)\
            .values(token=create_jwt(UserJWTPayload(user_uuid=user.uuid)))\
        
        await self.conn.execute(stmt)
        
        return user