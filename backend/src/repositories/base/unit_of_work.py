from src.database import Session

from src.repositories.cities import CitiesRepository
from src.repositories.complaints import ComplaintsRepository
from src.repositories.contacts import ContactsRepository
from src.repositories.deposit_orders import DepositOrdersRepository
from src.repositories.likes import LikesRepository
from src.repositories.profile_logs import ProfileLogsRepository
from src.repositories.profiles import ProfilesRepository
from src.repositories.transactions import TransactionsRepository
from src.repositories.users import UsersRepository
from src.repositories.profile_update_requests import ProfileUpdateRequestsRepository

class UnitOfWork:
    async def __aenter__(self):
        self.conn = Session()

        self.cities = CitiesRepository(self.conn)
        self.complaints = ComplaintsRepository(self.conn)
        self.contacts = ContactsRepository(self.conn)
        self.deposit_orders = DepositOrdersRepository(self.conn)
        self.likes = LikesRepository(self.conn)
        self.profile_logs = ProfileLogsRepository(self.conn)
        self.profiles = ProfilesRepository(self.conn)
        self.transactions = TransactionsRepository(self.conn)
        self.users = UsersRepository(self.conn)
        self.profile_update_requests = ProfileUpdateRequestsRepository(self.conn)

        return self

    async def __aexit__(self, *args):
        await self.conn.commit()

    