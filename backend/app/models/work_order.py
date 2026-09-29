from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy import Enum as sqlenum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .enum import work_order_priority, work_order_status

if TYPE_CHECKING:
    from .equipment import Equipment
    from .hospital import Hospital

class Work_Order(Base):
    __tablename__ = "work-orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    priority: Mapped[work_order_priority] = mapped_column(sqlenum(work_order_priority, name="work_order_priority", 
                                                                  callable_values=lambda enum_cls: [member.value for member in enum_cls]), 
                                                                  default=work_order_priority.LOW)
    status: Mapped[work_order_status] = mapped_column(sqlenum(work_order_status, name="work_order_status",
                                                              callable_values= lambda enum_cls: [member.value for member in enum_cls]),
                                                              default=work_order_status.PENDING)
    equipment_id: Mapped[int] = mapped_column(Integer)
    hospital_id: Mapped[int] = mapped_column(Integer)

