from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.utility.database.redis_client import AsyncRedisClient
from src.setting import (
    SETTINGS,
    VERSION,
    logger,
)


# =========================================================================================================== lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize Redis client
    redis_client = AsyncRedisClient(
        host=SETTINGS.REDIS.HOST,
        port=SETTINGS.REDIS.PORT,
        db=SETTINGS.REDIS.DATABASE,
        password=SETTINGS.REDIS.PASSWORD,
        max_connections=10,
        decode_responses=True,
        logger=logger,
    )

    # Connect to Redis
    connected = await redis_client.connect()
    if not connected:
        raise RuntimeError("Failed to connect to Redis.")

    # Store in app state
    app.state.redis_client = redis_client
    yield
    # Close Redis client on shutdown
    await redis_client.close()


# =========================================================================================================== inputs
inputs = {
    "title": SETTINGS.GENERAL.APPLICATION_NAME,
    "description": SETTINGS.GENERAL.APPLICATION_DESCRIPTION,
    "version": VERSION,
    "lifespan": lifespan,
    "docs_url": SETTINGS.GENERAL.DOCS_URL,
    "redoc_url": SETTINGS.GENERAL.REDOCS_URL,
    "openapi_url": SETTINGS.GENERAL.DOCS_URL + "/openapi.json",
}

print(f"{SETTINGS.GENERAL.HOST}{SETTINGS.GENERAL.DOCS_URL[1:]}")

# ========================================================================================================= create app
app = FastAPI(**inputs)
