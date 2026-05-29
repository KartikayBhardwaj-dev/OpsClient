from abc import ABC, abstractmethod
import httpx

class BaseIntegrationClient(ABC):
    def __init__(
            self,
            access_token: str | None = None
    ):
        self.access_token = access_token

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def health_check(self):
        pass

    async def get(
            self,
            url: str,
            headers: dict | None = None
    ):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=headers
            )
            return response.json()
        
    async def post(
            self,
            url: str,
            json_data: dict,
            headers: dict | None = None
    ):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json=json_data,
                headers=headers
            )

            return response.json()