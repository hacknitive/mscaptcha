from typing import Optional

from pydantic import BaseModel, AwareDatetime
from utilsweb.fastapi.response.response_schema import ResponseSchema


class ModelVerifyRequest(BaseModel):
    user_input: str
    code_pid: str
    case_sensitive: bool = True


class ModelVerifyResponse(BaseModel):
    user_input: Optional[str] = None
    code_pid: Optional[str] = None
    case_sensitive: Optional[bool] = None

class ModelVerifyResponseWithSchema(ResponseSchema):
    data: Optional[ModelVerifyResponse] = None
