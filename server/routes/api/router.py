from server.routes.api.v1.task_routes import router as task_router
from fastapi import APIRouter


routers = APIRouter()
routers.include_router(task_router, tags=["task"], prefix="/api/v1/tasks")
