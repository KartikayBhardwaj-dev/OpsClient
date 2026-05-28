from fastapi import APIRouter
from app.schemas.workflow import WorkflowRequest
from app.services.workflow_service import WorkflowService

router = APIRouter(
    prefix="/workflows",
    tags=["Workflows"]
)

@router.post("/research")
async def execute_research_workflow(request: WorkflowRequest):
    result = await WorkflowService.execute_workflow(request.user_input)
    return {
        "summary": result["summary"]
    }