from app.agents.base_agent import BaseAgent

class SupportAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Customer Support Specialist"
        )