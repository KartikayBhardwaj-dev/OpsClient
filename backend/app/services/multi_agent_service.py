from app.workflows.multi_agent_graph import graph

class MultiAgentService:
    @staticmethod
    async def execute(user_input: str):
        result = await graph.ainvoke(
            {
                "user_input": user_input,
                "messages": []
            }
        )
        return result