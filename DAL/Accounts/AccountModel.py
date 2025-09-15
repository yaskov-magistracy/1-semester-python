from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from ..Database import BaseModel
from .AccountRoleModel import AccountRoleModel

class AccountModel(BaseModel):
    __tablename__ = "accounts"
    login: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    passwordHash: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    role: Mapped[AccountRoleModel] = mapped_column(default=AccountRoleModel.User)