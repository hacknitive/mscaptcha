from utilsweb.fastapi.exception_handling import (
    prepare_handler_for_project_base_exception_function,
    prepare_handler_for_http_exception_function,
    prepare_handler_for_5xx_creator_function,
)

from src.fast_api_pre_setup import app
from src.setting import (
    RUN_MODE,
    logger,
    SETTINGS
)
from ...utility.message import messages
from ..dto.constance import MESSAGE_FAILURE

prepare_handler_for_project_base_exception_function(
    fast_api_app=app,
    logger=logger,
    run_mode=RUN_MODE,
)

prepare_handler_for_http_exception_function(
    fast_api_app=app,
    logger=logger,
    prepared_message=messages,
    error_language=SETTINGS.GENERAL.LANGUAGE,
)

prepare_handler_for_5xx_creator_function(
    fast_api_app=app,
    logger=logger,
    run_mode=RUN_MODE,
    error_text=MESSAGE_FAILURE,
)
