from app.core.llm import get_llm

class BaseAgent:
    def __init__(
            self,
            role: str
    ):
        self.role = role
        self.llm = get_llm()

    async def run(
            self,
            task: str
    ):
        prompt = f"""
You are a {self.role}.
Execute this task:
{task}"""
        response = await self.llm.ainvoke(prompt)
        return response.content