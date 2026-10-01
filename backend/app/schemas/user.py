from pydantic import BaseModel, ConfigDict, Field
from app.models import RBAC

class UserBase(BaseModel):
    username: str = Field(min_length=5, max_length=50)
    role: RBAC

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"