from app.workflows.multi_agent_graph import graph

class HITLService:
    @staticmethod
    async def request_review(
        user_input: str
    ):
        result = await graph.ainvoke(
            {
                "user_input": user_input,
                "messages": [],
                "approved": False
            }
        )

        return result
    
    @staticmethod
    async def approve_workflow(
        user_input: str,
        selected_agent: str,
        research: str
    ):
        result = await graph.ainvoke(
            {
                "user_input": user_input,
                "selected_agent": selected_agent,
                "research": research,
                "approved": True,
                "messages": []
            }
        )
        return result