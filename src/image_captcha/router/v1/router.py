from fastapi import APIRouter

from ....utility.dto.constance import VARIABLE_PATH_V1_PREFIX
from ... import (
    CAMEL_CASE_NAME,
    PASCAL_CASE_WITH_SPACE_NAME,
)

router = APIRouter(
    prefix=VARIABLE_PATH_V1_PREFIX + CAMEL_CASE_NAME,
    tags=[PASCAL_CASE_WITH_SPACE_NAME],
)