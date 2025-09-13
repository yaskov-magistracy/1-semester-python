from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    "postgresql+asyncpg://postgres:password@localhost:5432/python-magistracy",
    pool_size=30,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,
)

async_session_factory = async_sessionmaker(
    engine,     
    expire_on_commit=False,
    class_=AsyncSession)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True