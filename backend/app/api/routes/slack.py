from fastapi import APIRouter

from app.core.config import settings

from app.integrations.slack.client import (
    SlackClient
)

from app.integrations.slack.service import (
    SlackService
)

router = APIRouter(
    prefix="/slack",
    tags=["Slack"]
)


@router.post("/send")
async def send_slack_message(
    message: str
):

    slack_client = SlackClient(
        settings.SLACK_BOT_TOKEN
    )

    result = SlackService.send_message(
        slack_client,
        settings.SLACK_DEFAULT_CHANNEL,
        message
    )

    return result


@router.post("/workflow-test")
async def workflow_test():

    slack_client = SlackClient(
        settings.SLACK_BOT_TOKEN
    )

    result = (
        SlackService
        .send_workflow_notification(
            slack_client,
            "Research Workflow"
        )
    )

    return result


@router.post("/agent-test")
async def agent_test():

    slack_client = SlackClient(
        settings.SLACK_BOT_TOKEN
    )

    result = (
        SlackService
        .send_agent_notification(
            slack_client,
            "Supervisor Agent",
            "Completed"
        )
    )

    return result