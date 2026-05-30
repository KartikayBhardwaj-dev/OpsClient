from pydantic import BaseModel

class SlackMessageRequest(
    BaseModel
):
    channel: str
    text: str


class SlackMessageResponse(
    BaseModel
):
    success: bool
    channel: str