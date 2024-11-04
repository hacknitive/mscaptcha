from datetime import (
    datetime,
    timedelta,
)

from fastapi import status
from utilscommon.exception import ProjectBaseException

from src.setting import SETTINGS
from ...utility.message import messages
from ...utility.dto.constance import VARIABLE_SORT_DIRECTION_BY_CREATED_AT_DESCENDING
from src.otp.database.action import (
    fetch_one_by_filter,
    delete_list_by_filter,
)

MESSAGE_INVALID_OTP = messages.invalid_otp()
EXCEPTION_INVALID_OTP = ProjectBaseException(
    status_code=status.HTTP_400_BAD_REQUEST,
    success=False,
    data=None,
    error=MESSAGE_INVALID_OTP,
    message=MESSAGE_INVALID_OTP,
)

MESSAGE_OTP_EXPIRED = messages.otp_expired()
EXCEPTION_OTP_EXPIRED = ProjectBaseException(
    status_code=status.HTTP_400_BAD_REQUEST,
    success=False,
    data=None,
    error=MESSAGE_OTP_EXPIRED,
    message=MESSAGE_OTP_EXPIRED,
)

VALIDITY_PERIOD_IN_SECOND_TIMEDELTA = timedelta(seconds=SETTINGS.OTP.VALIDITY_PERIOD_IN_SECONDS)


async def is_otp_valid(
        phone_number: str,
        code: str,
        who_send: str,
) -> bool:
    filter_ = {
        "phone_number": phone_number,
        "code": code,
        'who_send': who_send,
    }

    obj = await fetch_one_by_filter(
        filter_=filter_,
        sort=VARIABLE_SORT_DIRECTION_BY_CREATED_AT_DESCENDING,
    )

    if not obj:
        raise EXCEPTION_INVALID_OTP

    is_otp_expired = False
    otp_expire_at = obj.created_at + VALIDITY_PERIOD_IN_SECOND_TIMEDELTA
    if datetime.utcnow() > otp_expire_at:
        is_otp_expired = True

    await delete_list_by_filter(filter_={
        "phone_number": phone_number,
        'who_send': who_send,
    })

    if is_otp_expired:
        raise EXCEPTION_OTP_EXPIRED

    return True
