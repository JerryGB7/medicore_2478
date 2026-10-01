from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING: 
    from .equipment import Equipment
    from .work_order import Work_Order
    from .worker import Worker

class Hospital(Base):
    __tablename__ = "hospitals"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    location_region: Mapped[str] = mapped_column(String(50))
    capacity: Mapped[int] = mapped_column(Integer)
    supervisor_id: Mapped[int] = mapped_column(Integer)

    equipments: Mapped[list["Equipment"]] = relationship(back_populates="hospital")
    work_orders: Mapped[list["Work_Order"]] = relationship(back_populates="hospital")
    workers: Mapped[list["Worker"]] = relationship(back_populates="hospital")