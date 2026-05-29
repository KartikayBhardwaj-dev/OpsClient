from fastapi import APIRouter
from fastapi import Request
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.jwt_handler import create_access_token
from app.auth.google_oauth import oauth
from app.core.database import get_db
from app.services.user_service import UserService
from app.auth.dependencies import get_current_user


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.get("/google/login")
async def google_login(
    request: Request
):

    redirect_url = (
        "http://127.0.0.1:8000/auth/google/callback"
    )

    return await oauth.google.authorize_redirect(
        request,
        redirect_url
    )


@router.get("/google/callback")
async def google_callback(
    request: Request,
    db: AsyncSession = Depends(get_db)
):

    token = await oauth.google.authorize_access_token(
        request
    )

    user_info = token.get("userinfo")

    email = user_info["email"]

    existing_user = await UserService.get_user_by_email(
        db,
        email
    )

    if existing_user:

        user = existing_user

    else:

        user = await UserService.create_google_user(
            db=db,
            name=user_info["name"],
            email=email,
            google_id=user_info["sub"],
            profile_picture=user_info.get("picture")
        )

    access_token = create_access_token({
        "user_id": user.id,
        "email": user.email
    })

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "picture": user.profile_picture
        }
    }


@router.get("/me")
async def get_me(
    current_user=Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }