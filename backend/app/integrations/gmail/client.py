from app.integrations.base import (BaseIntegrationClient)

class GmailClient(BaseIntegrationClient):
    async def connect(self):
        return True
    async def health_check(self):
        return {
            "provider": "gmail",
            "status": "healthy"
        }