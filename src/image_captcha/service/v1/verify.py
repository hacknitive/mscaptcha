from redis import Redis

from src.utility.dto.constance import *
from ...dto.v1 import ModelVerifyRequest as RequestModel
from ...dto.v1 import ModelVerifyResponseWithSchema as ResponseModel


async def verify(
    model: RequestModel,
    redis: Redis,
) -> ResponseModel:
    code = await redis.get(model.code_pid)
    if not code:
        return ResponseModel(
            status_code=HTTP_404_NOT_FOUND,
            success=False,
            message=MESSAGE_FAILURE,
            error=MESSAGE_INVALID_OR_EXPIRED_CAPTCHA,
            data={
                "user_input": model.user_input,
                "code_pid": model.code_pid,
                "case_sensitive": model.case_sensitive,
            },
        )

    await redis.delete(model.code_pid)  # Prevent replay attacks
    if model.case_sensitive:
        code = code
        user_input = model.user_input
    else:
        code = code.lower()
        user_input = model.user_input.lower()

    if code == user_input:
        return ResponseModel(
            status_code=200,
            success=True,
            message=MESSAGE_CAPTCHA_SUCCEDED,
            error=None,
            data={
                "user_input": model.user_input,
                "code_pid": model.code_pid,
                "case_sensitive": model.case_sensitive,
            },
        )

    else:
        return ResponseModel(
            status_code=400,
            success=False,
            message=MESSAGE_FAILURE,
            error=MESSAGE_CAPTCHA_FAILED,
            data={
                "user_input": model.user_input,
                "code_pid": model.code_pid,
                "case_sensitive": model.case_sensitive,
            },
        )
