from app.workflows.state import GraphState
from app.core.llm import get_llm

llm = get_llm()
async def planner_node(
        state: GraphState
):
    prompt = f"""
    Create a Research Plan for:
    {state["user_input"]}"""
    response = await llm.ainvoke(prompt)
    return {
        "plan": response.content
    }