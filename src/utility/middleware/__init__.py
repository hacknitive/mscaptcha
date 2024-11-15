from utilsweb.fastapi.middleware import (
    prepare_cors_middleware,
    prepare_process_time_header,
)

from src.fast_api_pre_setup import app
from src.setting import SETTINGS

prepare_cors_middleware(
    app=app,
    allow_origins=SETTINGS.CORS_MIDDLEWARE.ALLOW_ORIGINS,
    allow_credentials=SETTINGS.CORS_MIDDLEWARE.ALLOW_CREDENTIALS,
    allow_methods=SETTINGS.CORS_MIDDLEWARE.ALLOW_METHODS,
    allow_headers=SETTINGS.CORS_MIDDLEWARE.ALLOW_HEADERS,
    expose_headers=SETTINGS.CORS_MIDDLEWARE.EXPOSE_HEADERS,
    allow_origin_regex=SETTINGS.CORS_MIDDLEWARE.ALLOW_ORIGIN_REGEX,
    max_age=SETTINGS.CORS_MIDDLEWARE.MAX_AGE,
)

if SETTINGS.PROCESS_TIME_MIDDLEWARE.ACTIVE:
    prepare_process_time_header(app=app)
