from pydantic import BaseModel


class WorkflowRequest(BaseModel):
    user_input: str


class WorkflowResponse(BaseModel):
    summary: str