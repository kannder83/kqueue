# Logs
import logging


# Libraries
from fastapi import FastAPI
from config.conf import settings


# Routes
from app.client.routes import router as client_router
from app.tasks.routes import router as task_router


api_conf: dict = {
    "title": "DEV: KQueue",
    "description": "DEV: KQueue - To wait for",
    "docs_url": settings.dev_url
}

if settings.mode_prod:
    api_conf: dict = {
        "title": "KQueue",
        "description": "KQueue",
        "docs_url": settings.prod_url
    }

app: FastAPI = FastAPI(
    title=api_conf["title"],
    description=api_conf["description"],
    docs_url=api_conf["docs_url"],
    # root_path="/api/v1"
)

# Routes to publish
app.include_router(client_router)
app.include_router(task_router)
