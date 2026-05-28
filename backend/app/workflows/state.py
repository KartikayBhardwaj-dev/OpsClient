from typing import TypedDict
from typing import List
from typing import Optional

class GraphState(TypedDict):
    user_input: str
    selected_agent: str
    research: str
    summary: str
    messages: List[str]
    approval_required: bool
    approved: bool
    human_feedback: Optional[str]
    