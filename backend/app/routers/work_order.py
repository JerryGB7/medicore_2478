from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.schemas.work_order import WorkOrderCreate, WorkOrderRead
from app.models import Work_Order, User, RBAC
from app.dependencies import get_db, get_current_user, require_role
from app.models.enum import work_order_status, work_order_priority

router = APIRouter(prefix="/work_orders", tags=["Work Orders"])

@router.get("/", response_model=list[WorkOrderRead])
async def get_all_work_orders(
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_user)
):
    statement = select(Work_Order)
    result = await db.execute(statement)
    return list(result.scalars().all())

@router.get("/{work_order_id}", response_model=WorkOrderRead)
async def get_work_order_by_id(
    work_order_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_user)
) -> Work_Order:
    work_order = await db.get(Work_Order, work_order_id)

    if work_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work Order not found")
    return work_order

@router.post("/", response_model=WorkOrderRead, status_code=status.HTTP_201_CREATED)
async def create_work_order(
    payload: WorkOrderCreate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(require_role(RBAC.CLINICAL_ADMIN))
):
    work_order = Work_Order(**payload.model_dump())
    db.add(work_order)
    await db.commit()
    await db.refresh(work_order)
    return work_order

@router.delete("/{work_order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_work_order(
    work_order_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(require_role(RBAC.CLINICAL_ADMIN))
):
    work_order = await db.get(Work_Order, work_order_id)
    if work_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work Order not found")
    await db.delete(work_order)
    await db.commit()