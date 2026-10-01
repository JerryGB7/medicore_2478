from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.schemas.equipment import EquipmentCreate, EquipmentRead
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

@router.post("/", response_model=EquipmentRead, status_code=status.HTTP_201_CREATED)
async def create_equipment(
    payload: EquipmentCreate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(require_role(RBAC.CLINICAL_ADMIN))
):
    equipment = Equipment(**payload.model_dump())
    db.add(equipment)
    await db.commit()
    await db.refresh(equipment)
    return equipment

@router.delete("/{equipment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_equipment(
    equipment_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(require_role(RBAC.CLINICAL_ADMIN))
):
    equipment = await db.get(Equipment, equipment_id)
    if equipment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")
    await db.delete(equipment)
    await db.commit()