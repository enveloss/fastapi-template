from src.env import DB_CONN_STRING

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine(DB_CONN_STRING)
Session = async_sessionmaker(engine, expire_on_commit=False)