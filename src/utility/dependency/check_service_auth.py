from fastapi import Depends

from src.setting import SETTINGS

from ..dto.constance import EXCEPTION_UNAUTHORIZED_SERVICE
from .x_service_token import X_SERVICE_TOKEN

async def check_service_auth(
        token: str = Depends(X_SERVICE_TOKEN),
) -> None:
    if token != SETTINGS.API_KEY.SECRET_KEY:
        raise EXCEPTION_UNAUTHORIZED_SERVICE
