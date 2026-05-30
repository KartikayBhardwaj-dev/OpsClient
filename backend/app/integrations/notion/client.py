from app.integrations.base import (
    BaseIntegrationClient
)
from notion_client import Client

from app.core.config import settings

class NotionClient(
    BaseIntegrationClient
):
    def __init__(self):
        self.client = Client(auth=settings.NOTION_TOKEN)

    async def connect(self):

        return True

    async def health_check(self):

        return {
            "provider": "notion",
            "status": "healthy"
        }