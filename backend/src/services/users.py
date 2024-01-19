from src.repositories.base.unit_of_work import UnitOfWork

class UsersService:
    @staticmethod
    async def create_user():
        async with UnitOfWork() as uow:
            pass