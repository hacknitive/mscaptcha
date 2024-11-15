from uuid import uuid4

from redis import Redis

from src.utility.service.random_code_generator import random_code_generator
from src.utility.dto.constance import *
from ...dto.v1 import ModelCreateRequest as RequestModel
from ...dto.v1 import ModelCreateResponseWithSchema as ResponseModel
from ...utility import create_captcha_image


async def create(model: RequestModel, redis: Redis) -> ResponseModel:
    code_pid = str(uuid4())
    code = await random_code_generator(
        allowable_charachters=model.allowable_charachters,
        number_of_charachters=model.number_of_charachters,
    )

    code_image = create_captcha_image(code)

    await redis.set(
        key=code_pid,
        value=code,
        ex=model.validity_period_in_seconds,
    )

    return ResponseModel(
        status_code=HTTP_200_OK,
        success=True,
        message=MESSAGE_SUCCESS,
        error=None,
        data={
            "code_image": code_image,
            "code_pid": code_pid,
            "allowable_charachters": model.allowable_charachters,
            "number_of_charachters": model.number_of_charachters,
            "validity_period_in_seconds": model.validity_period_in_seconds,
            "expiration_time": None,
            "description": model.description,
        },
    )
