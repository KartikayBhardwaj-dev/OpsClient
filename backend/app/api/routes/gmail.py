from fastapi import APIRouter
from fastapi import Depends

from app.auth.dependencies import get_current_user
from app.core.config import settings
from app.integrations.gmail.client import GmailClient
from app.integrations.gmail.service import GmailService

router = APIRouter(
    prefix="/gmail",
    tags=["Gmail"]
)

@router.get("/unread")
async def get_unread_emails(
    current_user=Depends(get_current_user)
):
    gmail_client = GmailClient(
    access_token=current_user.gmail_access_token,
    refresh_token=current_user.gmail_refresh_token,
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET
)

    await gmail_client.connect()

    emails = GmailService.get_unread_emails(gmail_client)
    return {
        "emails": emails
    }

@router.post("/send")
async def send_email(
    to: str,
    subject: str,
    body: str,
    current_user=Depends(get_current_user)
):
    gmail_client = GmailClient(
        access_token=current_user.gmail_access_token,
        refresh_token=current_user.gmail_refresh_token,
        client_id=settings.GOOGLE_CLIENT_ID,
        client_secret=settings.GOOGLE_CLIENT_SECRET
    )
    await gmail_client.connect()
    result = GmailService.send_email(
        gmail_client,
        to,
        subject,
        body
    )

    return {
        "message": "Email sent",
        "gmail_response": result
    }