from fastapi import APIRouter

from app.services.integration_service import (
    IntegrationService
)

from app.integrations.types import (
    IntegrationProvider
)

router = APIRouter(
    prefix="/integrations",
    tags=["Integrations"]
)

service = IntegrationService()


@router.get("/health")

async def integrations_health():

    # gmail = await service.get_client(
    #     IntegrationProvider.GMAIL
    # ).health_check()

    slack = await service.get_client(
        IntegrationProvider.SLACK
    ).health_check()

    notion = await service.get_client(
        IntegrationProvider.NOTION
    ).health_check()

    return {
        # "gmail": gmail,
        "slack": slack,
        "notion": notion
    }