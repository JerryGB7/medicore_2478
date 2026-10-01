from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.schemas.equipment import EquipmentCreate, EquipmentRead, EquipmentBase
from app.models import Equipment, User, RBAC, Worker
from app.dependencies import get_db, get_current_user, require_role
from app.models.enum import equipment_status

router = APIRouter(prefix="/equipment", tags=["Equipment"])

@router.get("/", response_model=list[EquipmentRead])
async def get_all_equipment(
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_user)
):
    statement = select(Equipment)
    result = await db.execute(statement)
    return list(result.scalars().all())

@router.get("/{equipment_id}", response_model=EquipmentRead)
async def get_equipment_by_id(
    equipment_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_user)
) -> Equipment:
    equipment = await db.get(Equipment, equipment_id)

    if equipment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")
    return equipment

