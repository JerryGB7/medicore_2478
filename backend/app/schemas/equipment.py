from pydantic import BaseModel, ConfigDict, Field
from app.models.equipment import equipment_status

class EquipmentBase(BaseModel):
    serial_number: int
    model: str = Field(ge=0, le=50)
    status: equipment_status = equipment_status.AVAILABLE
    charge_level: int = 100
    hospital_id: int

class EquipmentCreate(EquipmentBase):
    pass

class EquipmentRead(EquipmentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)