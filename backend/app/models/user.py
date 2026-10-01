from __future__ import annotations
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column  
from sqlalchemy import Enum as sqlenum

from .base import Base
from .enum import RBAC


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[RBAC] = mapped_column(sqlenum(RBAC, name="user_role", callable_values=lambda enum_cls: [member.value for member in enum_cls]), default=RBAC.FIELD_TECHNICIAN)
    is_active: Mapped[bool] = mapped_column(Boolean,default=True)
