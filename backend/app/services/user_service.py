from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


class UserService:

    @staticmethod
    async def create_user(
        db: AsyncSession,
        name: str,
        email: str
    ):

        user = User(
            name=name,
            email=email
        )

        db.add(user)

        await db.commit()
        await db.refresh(user)

        return user

    @staticmethod
    async def get_user_by_email(
        db: AsyncSession,
        email: str
    ):

        result = await db.execute(
            select(User).where(
                User.email == email
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def create_google_user(
    db: AsyncSession,
    name: str,
    email: str,
    google_id: str,
    profile_picture: str | None = None,
    gmail_access_token: str | None = None,
    gmail_refresh_token: str | None = None
    ):

        user = User(
            name=name,
            email=email,
            google_id=google_id,
            profile_picture=profile_picture,
            gmail_access_token=gmail_access_token,
            gmail_refresh_token=gmail_refresh_token
        )

        db.add(user)

        await db.commit()

        await db.refresh(user)

        return user