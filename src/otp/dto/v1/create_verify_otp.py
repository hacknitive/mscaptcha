from pydantic import (
    constr,
    BaseModel,
)

from src.utility.dto.constance import *


class ModelCreateVerifyOtpRequest(BaseModel):  # This model is useful for inheritance
    code: constr(
        strip_whitespace=True,
        # min_length=VARIABLE_OTP_NUMBER_OF_CHARACTERS, # These three items are commented because  of safety issues
        # max_length=VARIABLE_OTP_NUMBER_OF_CHARACTERS,
        # pattern=VARIABLE_OTP_REGEX_PATTERN,
    ) # type: ignore
