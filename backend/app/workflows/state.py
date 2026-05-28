from typing import TypedDict
from typing import List

class GraphState(TypedDict):
    user_input: str
    selected_agent: str
    research: str
    summary: str
    messages: List[str]