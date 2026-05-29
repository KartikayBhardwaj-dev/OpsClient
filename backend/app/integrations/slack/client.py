from app.integrations.base import (
    BaseIntegrationClient
)


class SlackClient(
    BaseIntegrationClient
):

    async def connect(self):

        return True

    async def health_check(self):

        return {
            "provider": "slack",
            "status": "healthy"
        }