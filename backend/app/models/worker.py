from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .work_order import Work_Order
    from .hospital import Hospital  
    from .equipment import Equipment

class Worker(Base):
    __tablename__ = "workers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    hospital_id: Mapped[int] = mapped_column(Integer, ForeignKey("hospitals.id"))
    equipment_id: Mapped[int] = mapped_column(Integer, ForeignKey("equipments.id"))

    hospital: Mapped["Hospital"] = relationship(back_populates="workers")
    equipment: Mapped["Equipment"] = relationship(back_populates="workers")
    work_orders: Mapped["Work_Order"] = relationship(back_populates="workers")