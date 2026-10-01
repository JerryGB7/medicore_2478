from pydantic import BaseModel, Field, ConfigDict

class HospitalBase(BaseModel):
    name: str = Field(ge=0, le=50)
    location_region: str = Field(ge=0, le=50)
    capacity: int
    supervisor_id: int

class HospitalCreate(HospitalBase):
    pass

class HospitalRead(HospitalBase):
    id: int
    model_config = ConfigDict(from_attributes=True)