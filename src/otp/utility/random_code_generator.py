from random import choices

from utilscommon.setting.enum import EnumRunMode

from src.setting import (
    SETTINGS,
    RUN_MODE,
)

POPULATION = SETTINGS.OTP.ALLOWED_CHARACTER
K = SETTINGS.OTP.NUMBER_OF_CHARACTERS

if RUN_MODE in {
    EnumRunMode.production,
    EnumRunMode.development,
}:
    async def random_code_generator():
        return ''.join(choices(
            population=POPULATION,
            k=K,
        ))

else:

    async def random_code_generator():
        return "1" * K
