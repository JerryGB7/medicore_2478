import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from fastapi.middleware.cors import CORSMiddleware

from app.routers import work_order, equipment, auth, hospital
from app.config import settings

FRONTEND_ORIGIN = settings.FRONTEND_ORIGIN

app = FastAPI(title="Medical Equipment Management System", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(hospital.router)
app.include_router(equipment.router)
app.include_router(work_order.router)

@app.get("/health", tags=["Health"])
async def health_check() -> dict[str,str]:
    return {"status": "ok"}

@app.get("/version", tags=["Health"])
async def version_check() -> dict[str,str]:
    return {"version": app.version}

@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"detail": "Integrity error occurred. Please check your input data."},
    )