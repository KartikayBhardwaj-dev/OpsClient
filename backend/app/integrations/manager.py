from app.integrations.types import (
    IntegrationProvider
)


class IntegrationManager:

    def __init__(self):
        self.providers = {}

    def register(
        self,
        provider: IntegrationProvider,
        client
    ):

        self.providers[provider] = client

    def get_provider(
        self,
        provider: IntegrationProvider
    ):

        return self.providers.get(provider)