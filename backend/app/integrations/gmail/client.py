from app.integrations.base import (BaseIntegrationClient)
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build



class GmailClient(BaseIntegrationClient):
    def __init__(
            self,
            access_token: str,
            refresh_token: str,
            client_id: str,
            client_secret: str
    ):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.service = None

    async def connect(self):
        credentials = Credentials(
            token=self.access_token,
            refresh_token=self.refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        self.service = build(
            "gmail",
            "v1",
            credentials=credentials
        )

        return self.service
    
    async def health_check(self):

        if self.service is None:
            await self.connect()

        try:
            profile = (
                self.service
                .users()
                .getProfile(userId="me")
                .execute()
                )

            return {
                "provider": "gmail",
                "status": "healthy",
                "email": profile.get("emailAddress")
            }

        except Exception as e:
            return {
                "provider": "gmail",
                "status": "unhealthy",
                "error": str(e)
            }
