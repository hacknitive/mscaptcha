from utilsweb.fastapi.adapter.call_url import call_url
from utilscommon import enum

from ...setting import RUN_MODE
from ...utility.dto.constance import *
from ...utility.message import messages


if RUN_MODE in {
    enum.EnumRunMode.production,
    enum.EnumRunMode.development,
}:
    async def send_otp_code(
            phone_number: str,
            code: str,
    ) -> dict:
        return await call_url(
            method='POST',
            url=f'https://api.kavenegar.com/v1/{VARIABLE_KAVEH_NEGAR_API_KEY}/verify/lookup.json',
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
                'charset': 'utf-8',
            },
            json=None,
            data={
                'receptor': phone_number,
                'template': VARIABLE_KAVEH_NEGAR_TEMPLATE_NAME,
                'token': code,
            },
            raise_=True,
            error_message=messages.service_unavailable(service='سرویس ارسال پیام کوتاه'),
            run_mode=RUN_MODE,
            verify_ssl=False,
            read_text=False,
        )

else:
    async def send_otp_code(
            phone_number: str,
            code: str,
    ) -> dict:
        return dict()
