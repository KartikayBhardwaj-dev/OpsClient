from typing import TypedDict
from typing import List

class GraphState(TypedDict):
    user_input: str
    plan: str
    research: str
    summary: str
    messages: List[str]
    