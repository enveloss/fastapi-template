from src.config import config

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine(config.base.db_conn_string)
Session = async_sessionmaker(engine, expire_on_commit=False)