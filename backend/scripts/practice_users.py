import asyncio
from app.database import LocalSession
from app.models import User, RBAC
from app.security import hash_password

async def seed_users() -> None:
    async with LocalSession() as session:
        # Create practice users
        practice_users = [
            User(username="admin", hashed_password=hash_password("adminpass"), role=RBAC.CLINICAL_ADMIN),
            User(username="technician", hashed_password=hash_password("techpass"), role=RBAC.FIELD_TECHNICIAN),
            User(username="auditor", hashed_password=hash_password("auditorpass"), role=RBAC.AUDITOR),
        ]

        session.add_all(practice_users)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(seed_users())