from app.workflows.state import GraphState

async def human_review_node(
        state: GraphState
):
    return {
        "approval_required": True
    }