from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, require_role, get_current_user
from app.models import Hospital, User
from app.schemas.hospital import HospitalCreate, HospitalRead
from backend.app.models.enum import RBAC

router = APIRouter(prefix="/hospitals", tags=["Hospitals"])

@router.get("/", response_model=list[HospitalRead])
async def get_all_hospitals(
    db = Depends(get_db)
):
    statement = select(Hospital)
    result = await db.execute(statement)
    return list(result.scalars().all())

@router.get("/{hospital_id}", response_model=HospitalRead)
async def get_hospital_by_id(
    hospital_id: int,
    db = Depends(get_db)
):
    hospital = await db.get(Hospital, hospital_id)
    if hospital is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hospital not found")
    return hospital

@router.post("/", response_model=HospitalRead, status_code=status.HTTP_201_CREATED)
async def create_hospital(
    payload: HospitalCreate,
    db = Depends(get_db),
    _: User = Depends(require_role(RBAC.CLINICAL_ADMIN))
):
    hospital = Hospital(**payload.model_dump())
    db.add(hospital)
    await db.commit()
    await db.refresh(hospital)
    return hospital