from fastapi import APIRouter
from app.schemas.hitl import ApprovalRequest
from app.schemas.hitl import ApprovalWorkflowRequest

from app.services.hitl_service import HITLService

router = APIRouter(
    prefix="/hitl",
    tags=["HITL"]
)


@router.post("/review")
async def review_workflow(
    request: ApprovalRequest
):
    result = await HITLService.request_review(
        request.user_input
    )

    return {
        "selected_agent": result["selected_agent"],
        "research": result["research"],
        "approval_required": result["approval_required"]
    }


@router.post("/approve")

async def approve_workflow(

    request: ApprovalWorkflowRequest

):
    result = await HITLService.approve_workflow(
        user_input=request.user_input,
        selected_agent=request.selected_agent,
        research=request.research
    )
    return {
        "summary": result["summary"]
    }