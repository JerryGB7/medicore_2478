import os 
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


DATABASE_URL = "postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/medidemo"

engine = create_async_engine(DATABASE_URL, echo=True)

LocalSession = async_sessionmaker(engine, expire_on_commit=False)