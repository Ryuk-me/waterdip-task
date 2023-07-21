from fastapi import FastAPI, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from server.Config import configs
from server.utils.uptime import getUptime
from server.database import is_db_connected, get_db
from server.routes.api.router import routers
import time
from server.utils import custom_handler
from fastapi.responses import JSONResponse


startTime = time.time()

app = FastAPI(
    title=configs.APP_NAME,
    version=configs.APP_VERSION,
    description="Manage all your tasks at one place.",
    docs_url="/api/docs" if configs.DOCS_ENABLED else None,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_db_client():
    if is_db_connected():
        print(f"🚀 @{configs.APP_NAME} v{configs.APP_VERSION} [{configs.PYTHON_ENV}]")
        print("🍀 Database Connected.")
    else:
        print("❌ Database not Connected - Please check MONGO_DB_URI env.")


@app.on_event("shutdown")
def shutdown_db_client():
    db = get_db()
    db.close()


@app.get("/health", status_code=status.HTTP_200_OK, tags=["Health Route"])
async def health_route(req: Request):
    """
    Health Route : Returns App details.
    """
    return JSONResponse(
        {
            "app": configs.APP_NAME,
            "version": "v" + configs.APP_VERSION,
            "ip": req.client.host,
            "uptime": getUptime(startTime),
            "database": "connected" if is_db_connected() else "disconnected",
            "mode": configs.PYTHON_ENV,
        }
    )


app.include_router(routers)


@app.exception_handler(custom_handler.CustomException)
async def handle_custom_exception(request, exc: custom_handler.CustomException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.msg})
