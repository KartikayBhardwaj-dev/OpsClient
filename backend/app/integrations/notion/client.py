from app.integrations.base import (
    BaseIntegrationClient
)



class NotionClient(
    BaseIntegrationClient
):

    async def connect(self):

        return True

    async def health_check(self):

        return {
            "provider": "notion",
            "status": "healthy"
        }