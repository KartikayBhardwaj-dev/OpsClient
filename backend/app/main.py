from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.api.routes import api_router
from app.core.config import settings
from app.core.logging import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Starting OpsClient...")
    yield
    print("Shutting down OpsClient...")


setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

# IMPORTANT
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY
)

app.include_router(api_router)


@app.get("/")
async def root():

    return {
        "message": "welcome to OpsClient"
    }