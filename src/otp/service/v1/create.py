from datetime import timedelta, datetime

from ....utility.dto.constance import *
from ...database.action import (
    fetch_one_by_filter,
    insert_one,
    delete_one_by_filter,
)
from ...adapter.send_otp_code import send_otp_code
from ...utility.random_code_generator import random_code_generator
from ...dto.v1.create_send_otp import ModelCreateSendOtpResponse

VALIDITY_PERIOD_IN_SECOND_TIMEDELTA = timedelta(seconds=SETTINGS.OTP.VALIDITY_PERIOD_IN_SECONDS)
RESEND_LOCK_DURATION_IN_SECOND_TIMEDELTA = timedelta(seconds=SETTINGS.OTP.RESEND_LOCK_DURATION_IN_SECOND)

TIME_LIMIT_OTP_EXCEPTION = ProjectBaseException(
    status_code=HTTP_403_FORBIDDEN,
    success=False,
    data=None,
    error=messages.time_limit_otp(),
    message=messages.time_limit_otp(),
)


async def create(
        phone_number: str,
        who_send: str,  # forgot_password, register_user or ...
) -> dict:
    filter_ = {
        "phone_number": phone_number,
        "who_send": who_send,
    }
    otp_code_obj = await fetch_one_by_filter(
        filter_=filter_,
        sort=VARIABLE_SORT_DIRECTION_BY_CREATED_AT_DESCENDING,
    )

    now = datetime.utcnow()
    if otp_code_obj is not None:
        resend_unlock_time = otp_code_obj.created_at + RESEND_LOCK_DURATION_IN_SECOND_TIMEDELTA
        if now < resend_unlock_time:
            raise ProjectBaseException(
                status_code=HTTP_403_FORBIDDEN,
                success=False,
                data=ModelCreateSendOtpResponse(**{
                    **otp_code_obj.model_dump(),
                    'expire_at': otp_code_obj.created_at + VALIDITY_PERIOD_IN_SECOND_TIMEDELTA,
                    'unlock_resend_at': otp_code_obj.created_at + RESEND_LOCK_DURATION_IN_SECOND_TIMEDELTA,
                }),
                error=messages.time_limit_otp(),
                message=messages.time_limit_otp(),
            )

    otp_random_code = await random_code_generator()

    otp_code_obj = await insert_one(
        inputs={
            'phone_number': phone_number,
            'code': otp_random_code,
            'who_send': who_send,
        }
    )

    try:
        await send_otp_code(
            phone_number=phone_number,
            code=str(otp_random_code),
        )
    except Exception:
        await delete_one_by_filter(
            filter_={
                'phone_number': otp_code_obj.phone_number,
                'code': otp_code_obj.code,
            }
        )
        raise

    return {
        **otp_code_obj.model_dump(),
        'expire_at': otp_code_obj.created_at + VALIDITY_PERIOD_IN_SECOND_TIMEDELTA,
        'unlock_resend_at': otp_code_obj.created_at + RESEND_LOCK_DURATION_IN_SECOND_TIMEDELTA,
    }
