from app.workflows.research_graph import graph

class WorkflowService:
    @staticmethod
    async def execute_workflow(user_input: str):
        result = await graph.ainvoke(
            {
                "user_input": user_input,
                "messages": []
            }
        )

        return result