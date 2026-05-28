from app.workflows.state import GraphState
from app.core.llm import get_llm

llm = get_llm()

async def summarizer_node(state: GraphState):
    prompt = f"""
Summarize this research:
{state["research"]}"""
    response = await llm.ainvoke(prompt)
    return {
        "summary": response.content
    }