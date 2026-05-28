from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.user import router as users_router
from app.api.routes.workflows import router as workflow_router
from app.api.routes.multi_agent import router as multi_agent_router


api_router = APIRouter()

api_router.include_router(health_router)

api_router.include_router(users_router)

api_router.include_router(workflow_router)
api_router.include_router(multi_agent_router)