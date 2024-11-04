from datetime import datetime
from typing import Optional

from utilsweb.fastapi.response.response_schema import ResponseSchema
from pydantic import (
    BaseModel,
    AwareDatetime,
    field_serializer,
)

from utilsweb.fastapi.dto.make_datetime_aware import make_datetime_aware


class ModelCreateSendOtpResponse(BaseModel):
    def __init__(self, **kwargs):
        output = make_datetime_aware(
            inputs=kwargs,
            datetime_field_names=(
                'expire_at',
                'unlock_resend_at',
                'created_at',
            )
        )
        super().__init__(**output)

    phone_number: Optional[str] = None

    expire_at: Optional[AwareDatetime] = None
    unlock_resend_at: Optional[AwareDatetime] = None

    created_at: Optional[AwareDatetime] = None

    @field_serializer(
        'expire_at',
        'unlock_resend_at',
        'created_at',
    )
    def serialize_dt(self, v: Optional[datetime], _info):
        if v:
            return v.strftime("%Y-%m-%dT%H:%M:%S+00:00")


class ModelCreateSendOtpResponseWithSchema(ResponseSchema):
    data: Optional[ModelCreateSendOtpResponse] = None
