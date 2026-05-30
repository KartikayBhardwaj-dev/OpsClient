from app.integrations.manager import (IntegrationManager)
from app.integrations.gmail.client import (GmailClient)
from app.integrations.slack.client import (SlackClient)
from app.integrations.notion.client import (NotionClient)
from app.integrations.types import (IntegrationProvider)
from app.core.config import settings
class IntegrationService:
    def __init__(self):
        self.manager = IntegrationManager()
        # self.manager.register(
        #     IntegrationProvider.GMAIL,
        #     GmailClient()
        # )
        self.manager.register(
            IntegrationProvider.SLACK,
            SlackClient(
                bot_token=settings.SLACK_BOT_TOKEN
            )
        )
        self.manager.register(
            IntegrationProvider.NOTION,
            NotionClient()
        )
    def get_client(self, provider: IntegrationProvider):
        return self.manager.get_provider(provider)