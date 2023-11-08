from .base.db_repository import DBRepository
from src.models import User

class UsersRepository(DBRepository[User]):
    model = User