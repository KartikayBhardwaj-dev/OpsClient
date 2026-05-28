from app.agents.base_agent import BaseAgent

class AnalyticsAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Business Analytics Agent"
        )