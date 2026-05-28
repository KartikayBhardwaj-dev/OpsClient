from app.core.llm import get_llm

class SupervisorAgent:
    def __init__(self):
        self.llm = get_llm()

    async def decide_agent(
            self,
            user_input: str
    ):
        prompt = f"""
Decide which agent should handle this task.
Available Agents:
    -research
    -analytics
    -support
User request:
{user_input}
Return Only the Agent name."""
        response = await self.llm.ainvoke(prompt)
        return response.content.strip().lower()