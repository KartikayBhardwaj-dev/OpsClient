from fastapi import APIRouter

from app.integrations.notion.client import NotionClient
from app.integrations.notion.service import NotionService

router = APIRouter(
    prefix="/notion",
    tags=["Notion"]
)


@router.post("/page")
async def create_page(
    title: str,
    content: str
):

    notion_client = NotionClient()

    result = NotionService.create_page(
        notion_client,
        title,
        content
    )

    return {
        "message": "Page created",
        "page": result
    }