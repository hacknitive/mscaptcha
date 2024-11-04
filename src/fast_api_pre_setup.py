from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.setting import (
    SETTINGS,
    VERSION,
)

from src.utility.database.mongodb_engine import init_beanie


# =========================================================================================================== lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_beanie()
    yield


# =========================================================================================================== inputs
inputs = {
    "title": SETTINGS.GENERAL.APPLICATION_NAME,
    "description": SETTINGS.GENERAL.APPLICATION_DESCRIPTION,
    "version": VERSION,
    'lifespan': lifespan,
    "docs_url": SETTINGS.GENERAL.DOCS_URL,
    "redoc_url": SETTINGS.GENERAL.REDOCS_URL,
}

print(f"http://127.0.0.1:{SETTINGS.UVICORN_SERVER.PORT}{SETTINGS.GENERAL.DOCS_URL}")

# ========================================================================================================= create app
app = FastAPI(**inputs)
