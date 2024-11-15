from typing import (
    Annotated,
    Optional,
)

from pydantic import (
    BaseModel,
    AwareDatetime,
    Field,
)
from utilsweb.fastapi.response.response_schema import ResponseSchema

from src.setting import SETTINGS


class ModelCreateRequest(BaseModel):
    allowable_charachters: str = SETTINGS.CAPTCHA.DEFAULT_ALLOWABLE_CHARACHTERS
    number_of_charachters: int = SETTINGS.CAPTCHA.DEFAULT_NUMBER_OF_CHARACHTERS
    validity_period_in_seconds: Annotated[int, Field(strict=True, gt=0)] | None = (
        SETTINGS.CAPTCHA.DEFAULT_VALIDITY_PERIOD_IN_SECONDS
    )
    description: Optional[str] = None


class ModelCreateResponse(BaseModel):
    code_image: Optional[str] = None
    code_pid: Optional[str] = None

    allowable_charachters: Optional[str] = None
    number_of_charachters: Optional[int] = None
    validity_period_in_seconds: Optional[int] = None
    expiration_time: Optional[AwareDatetime] = None
    description: Optional[str] = None


class ModelCreateResponseWithSchema(ResponseSchema):
    data: Optional[ModelCreateResponse] = None
