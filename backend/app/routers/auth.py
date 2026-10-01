from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.dependencies import get_db, require_role
from app.models import User, RBAC
from app.schemas.user import Token, UserCreate, UserRead
from app.security import create_access_token, verify_password, hash_password

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/token", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
)-> Token:
    result = await db.execute(select(User).where(User.username == form_data.username.lower()))
    user = result.scalar_one_or_none()
    if user is None or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": user.username, "role": user.role.value})
    return Token(access_token = access_token, token_type="Bearer")