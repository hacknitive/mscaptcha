from redis import Redis
from fastapi import Depends
from utilsweb.fastapi.response.custom_orjson_response import (
    ProjectJSONResponse as JsonResponse,
)
from utilsweb.fastapi.router import convert_module_name_to_route_name

from src.utility.database.get_redis_client import get_redis_client
from src.utility.dependency import check_service_auth
from ... import LOWER_SNAKE_CASE_NAME
from ...dto.v1 import ModelVerifyRequest as RequestModel
from ...dto.v1 import ModelVerifyResponseWithSchema as ResponseModel
from ...service.v1 import verify as service

from .router import router

ROUTE_NAME = convert_module_name_to_route_name(
    entity_name=LOWER_SNAKE_CASE_NAME,
    module_name=__file__,
)


@router.post(
    path="/verify",
    name=ROUTE_NAME,
    summary="summary",
    description="description",
    response_description="response_description",
    openapi_extra=None,
    response_model=ResponseModel,
    dependencies=[Depends(check_service_auth)],
)
async def router(
    model: RequestModel,
    redis: Redis = Depends(get_redis_client),
) -> JsonResponse:

    data = await service(
        model=model,
        redis=redis,
    )
    return JsonResponse(**data.model_dump())
