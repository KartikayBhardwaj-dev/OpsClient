from fastapi import APIRouter

from app.schemas.workflow import WorkflowRequest

from app.services.multi_agent_service import MultiAgentService


router = APIRouter(
    prefix="/multi-agent",
    tags=["Multi-Agent"]
)


@router.post("/execute")
async def execute_multi_agent(
    request: WorkflowRequest
):

    result = await MultiAgentService.execute(
        request.user_input
    )

    return {
        "selected_agent": result["selected_agent"],
        "summary": result["summary"]
    }