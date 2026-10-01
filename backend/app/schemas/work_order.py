from pydantic import BaseModel, Field, ConfigDict
from app.models.work_order import work_order_priority, work_order_status

class WorkOrderBase(BaseModel):
    title: str
    priority: work_order_priority = work_order_priority.LOW
    status: work_order_status = work_order_status.PENDING
    equipment_id: int
    hospital_id: int

class WorkOrderCreate(WorkOrderBase):
    pass

class WorkOrderRead(WorkOrderBase):
    id: int
    model_config = ConfigDict(from_attributes=True)