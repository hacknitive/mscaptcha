from utilsweb.fastapi.dependency.custom_api_key_header import CustomAPIKeyHeader

from ...setting import SETTINGS
from ..dto.constance.exception import EXCEPTION_UNAUTHORIZED_SERVICE

X_SERVICE_TOKEN = CustomAPIKeyHeader(
    name=SETTINGS.API_KEY.HEADER_NAME,
    auto_error=True,
    scheme_name=SETTINGS.API_KEY.HEADER_NAME,
    exception=EXCEPTION_UNAUTHORIZED_SERVICE,
)
