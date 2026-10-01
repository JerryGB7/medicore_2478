import os 
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from .config import Settings

DATABASE_URL = Settings.database_url

engine = create_async_engine(DATABASE_URL, echo=True)

LocalSession = async_sessionmaker(engine, expire_on_commit=False)