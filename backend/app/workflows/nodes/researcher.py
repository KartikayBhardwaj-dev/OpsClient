from app.workflows.state import GraphState
from app.core.llm import get_llm

llm = get_llm()

async def researcher_node(state: GraphState):
    prompt = f"""
Execute this research plan:
{state["plan"]}"""
    response = await llm.ainvoke(prompt)
    return {
        "research": response.content
    }