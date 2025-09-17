from abc import ABC, abstractmethod
from .Models import BaseModel
from sqlalchemy import and_, not_, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Generic, TypeVar
from uuid import UUID

T = TypeVar("T", bound=BaseModel)

class BaseRepository(ABC, Generic[T]):
    def __init__(self, session: AsyncSession):
        self.session = session

    @property
    @abstractmethod
    def model(self) -> type[T]:
        raise NotImplementedError

    async def Add(self, data: T) -> T:
        instance = data#self.model(data)
        self.session.add(instance)
        await self.session.flush()
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def GetById(self, id: UUID) -> T | None:
        result = await self.session.execute(
            select(self.model)
            .where(self.model.id == id))
        
        return result.scalars().one_or_none()

    async def SearchAll(self, skip: int = 0, limit: int = 100, **filters) -> list[T]:
        result = await self.session.execute(
            select(self.model)
            .filter_by(**filters)
            .offset(skip)
            .limit(limit))
        
        return result.scalars().all()

    async def SearchOne(self, **filters) -> T | None:
        result = await self.session.execute(
            select(self.model)
            .filter_by(**filters))

        return result.scalars().one_or_none()

    async def Update(self, id: UUID, data: dict) -> T | None:
        await self.session.execute(
            update(self.model)
            .where(self.model.id == id)
            .values(**data))
        updated = await self.GetById(id)
        if (updated == None):
            raise Exception("Where is no entity with same Id")
        
        await self.session.commit()
        return updated

    async def UpdateField(self, id: UUID, column: str, value: Any) -> T:
        await self.session.execute(
            update(self.model)
            .where(self.model.id == id)
            .values(**{column: value})
        )

        await self.session.commit()
        return await self.GetById(id)

    async def Delete(self, id: UUID) -> None:
        await self.session.execute(
            delete(self.model).where(self.model.id == id))
