from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime
from uuid import uuid4
from enum import Enum
from datetime import datetime, timezone
from .Database import Base


class BaseModel(Base):
    __abstract__ = True
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)

class AccountRoleModel(str, Enum):
    Admin = "Admin"
    User = "User"

class AccountModel(BaseModel):
    __tablename__ = "accounts"
    login: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    passwordHash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[AccountRoleModel] = mapped_column(default=AccountRoleModel.User)
    blockReason: Mapped[str] = mapped_column(String(1000))

    notifications: Mapped[list["NotificationModel"]] = relationship(
        "NotificationModel",
        back_populates="account",
        cascade= "all, delete-orphan"
    )



class NotificationModel(BaseModel):
    __tablename__ = "notifications"
    time: Mapped[datetime] = mapped_column(DateTime(timezone=False))
    text: Mapped[str] = mapped_column(String(1000), nullable=False)

    account: Mapped["AccountModel"] = relationship(
        "AccountModel",
        back_populates="notifications"
    )