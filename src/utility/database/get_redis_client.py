from fastapi import Request

from .redis_client import AsyncRedisClient


async def get_redis_client(request: Request) -> AsyncRedisClient:
    return request.app.state.redis_client
