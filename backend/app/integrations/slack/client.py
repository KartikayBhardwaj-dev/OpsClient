from app.integrations.base import (
    BaseIntegrationClient
)
import requests


class SlackClient(
    BaseIntegrationClient
):
    def __init__(
            self,
            bot_token: str
    ):
        self.bot_token = bot_token

    async def connect(self):

        response = requests.post(
            "https://slack.com/api/auth.test",
            headers={
                "Authorization": f"Bearer {self.bot_token}"
            }
        )

        data = response.json()
        return data.get("ok", False)
    
    async def health_check(self):
        connected = await self.connect()
        return {
            "provider": "slack",
            "status": (
                "healthy"
                if connected
                else "unhealthy"
            )
        }
    
    def send_message(
            self,
            channel: str,
            text: str
    ):
        response = requests.post(
            "https://slack.com/api/chat.postMessage",
            headers={
                "Authorization": f"Bearer {self.bot_token}",
                "Content-Type": "application/json"
            },
            json={
                "channel": channel,
                "text": text
            }
        )


        return response.json()