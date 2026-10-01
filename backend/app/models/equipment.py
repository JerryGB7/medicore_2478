from __future__ import annotations
from typing import TYPE_CHECKING


from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy import Enum as sqlenum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .enum import equipment_status

if TYPE_CHECKING:
    from .hospital import Hospital
    from .work_order import Work_Order
    from .worker import Worker

class Equipment(Base):
    __tablename__ = "equipments"

    id: Mapped[int] = mapped_column(primary_key=True)
    serial_number: Mapped[int] = mapped_column(Integer)
    model: Mapped[str] = mapped_column(String(50))
    status: Mapped[equipment_status] = mapped_column(sqlenum(equipment_status, name="equipment_status",
                                                             values_callable=lambda enum_cls: [member.value for member in enum_cls]),
                                                             default=equipment_status.AVAILABLE)
    charge_level: Mapped[int] = mapped_column(Integer)
    hospital_id: Mapped[int] = mapped_column(Integer, ForeignKey("hospitals.id"))

    hospital: Mapped["Hospital"] = relationship(back_populates="equipments")
    work_orders: Mapped[list["Work_Order"]] = relationship(back_populates="equipment")
    workers: Mapped[list["Worker"]] = relationship(back_populates="equipment")