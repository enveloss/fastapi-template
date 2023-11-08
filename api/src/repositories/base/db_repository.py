from typing import Optional

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

class DBRepository[_T]:
    model: _T = None

    def __init__(self, conn: AsyncSession):
        self.conn = conn

    async def add_one(self, data: dict = {}) -> _T:
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.conn.execute(stmt)
        return res.scalar_one()

    async def edit_one(self, id: int, **data) -> Optional[_T]:
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model)
        res = await self.conn.execute(stmt)
        return res.scalar_one()
    
    async def get_one(self, **filter_by) -> Optional[_T]:
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.conn.execute(stmt)
        return res.scalar()
    
    async def get_many(self, order_by: list=[], **filter_by) -> list[_T]:
        stmt = select(self.model).filter_by(**filter_by).order_by(*order_by)
        res = await self.conn.execute(stmt)
        return res.scalars().all()
    
    async def delete(self, **filter_by) -> _T:
        stmt = delete(self.model).filter_by(**filter_by).returning(self.model)
        res = await self.conn.execute(stmt)
        return res.scalar()