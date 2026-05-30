from app.integrations.slack.client import (SlackClient)

class SlackService:
    @staticmethod
    def send_message(
        slack_client: SlackClient,
        channel: str,
        text: str
    ):
        return slack_client.send_message(
            channel=channel,
            text=text
        )
    
    @staticmethod
    def send_workflow_notification(
        slack_client: SlackClient,
        workflow_name: str
    ):
        return slack_client.send_message(
            channel="#all-testing",
            text=(
                f"Workflow Completed: "
                f"{workflow_name}"
            )
        )
    
    @staticmethod
    def send_agent_notification(
        slack_client: SlackClient,
        agent_name: str,
        status: str
    ):
        return slack_client.send_message(
            channel="all-testing",
            text=(
                f"Agent {agent_name} "
                f"Status: {status}"
            )
        )