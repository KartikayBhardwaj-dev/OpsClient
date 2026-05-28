from app.agents.base_agent import BaseAgent

class SummaryAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Executive Report Summarizer"
        )
        