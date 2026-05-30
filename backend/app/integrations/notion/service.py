from app.core.config import settings
from app.integrations.notion.client import NotionClient

class NotionService:
    @staticmethod
    def create_page(
        notion_client: NotionClient,
        title: str,
        content: str
    ):
        page = notion_client.client.pages.create(
            parent={
                "page_id": settings.NOTION_PARENT_PAGE_ID
            },
            properties={
                "title": {
                    "title": [
                        {
                            "text": {
                                "content": title
                            }
                        }
                    ]
                }
            },
            children=[
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": content
                                }
                            }
                        ]
                    }
                }
            ]
        )
        return page