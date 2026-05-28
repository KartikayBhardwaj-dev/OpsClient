from pydantic import BaseModel

class ApprovalRequest(BaseModel):
    user_input: str


class ApprovalWorkflowRequest(BaseModel):
    user_input: str
    selected_agent: str
    research: str

    