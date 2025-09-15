from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from config import settings

databaseUrl = settings.DATABASE_CONNECTION_STRING()

engine = create_async_engine(
    databaseUrl,
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

class BaseModel(Base):
    __abstract__ = True
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)