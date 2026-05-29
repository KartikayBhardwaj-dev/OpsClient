from app.integrations.manager import (IntegrationManager)
from app.integrations.gmail.client import (GmailClient)
from app.integrations.slack.client import (SlackClient)
from app.integrations.notion.client import (NotionClient)
from app.integrations.types import (IntegrationProvider)

class IntegrationService:
    def __init__(self):
        self.manager = IntegrationManager()
        self.manager.register(
            IntegrationProvider.GMAIL,
            GmailClient()
        )
        self.manager.register(
            IntegrationProvider.SLACK,
            SlackClient()
        )
        self.manager.register(
            IntegrationProvider.NOTION,
            NotionClient()
        )
    def get_client(self, provider: IntegrationProvider):
        return self.manager.get_provider(provider)