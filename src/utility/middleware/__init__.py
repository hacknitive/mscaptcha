# from fastapi import Request, Response

from utilsweb.fastapi.middleware import (
    prepare_cors_middleware,
    prepare_gzip_middleware,
    prepare_process_time_header,
)

from ...fast_api_pre_setup import app
from ...setting import SETTINGS

# @app.middleware("http")
# async def tus_options_middleware(request: Request, call_next):
#     # Check if it's an OPTIONS request to the TUS upload endpoint
#     print(
#         "===================================================== OPTION ROUTE ==============================================")
#     if request.method == "OPTIONS" and request.url.path.startswith("/api/v1/video/") and request.url.path.endswith(
#             "/upload"):
#         headers = {
#             # TUS-specific headers
#             "Tus-Resumable": "1.0.0",
#             "Tus-Version": "1.0.0",
#             "Tus-Extension": "creation,termination",
#             "Tus-Max-Size": str(20 * 1024 * 1024 * 1024),  # 20GB max file size
#
#             # CORS headers (manually added for the OPTIONS response)
#             "Access-Control-Allow-Origin": "*",  # Adjust to your frontend
#             "Access-Control-Allow-Methods": "*",  # Allowed methods
#             "Access-Control-Allow-Headers": "*",
#             # Allowed headers in requests
#             "Access-Control-Allow-Credentials": "true",  # If credentials (cookies, tokens) are allowed
#             "Access-Control-Max-Age": "600",  # Cache the preflight response for 600 seconds
#             "Access-Control-Expose-Headers": "x-user-token,Tus-Resumable,Tus-Version,Tus-Extension,Tus-Max-Size,Location,Upload-Offset,Upload-Length",  # Cache the preflight response for 600 seconds
#         }
#
#         return Response(status_code=200, headers=headers)
#
#     # If not TUS OPTIONS request, proceed with the request
#     response = await call_next(request)
#     return response

prepare_gzip_middleware(
    app=app,
    minimum_size=SETTINGS.GZIP_MIDDLEWARE.MINIMUM_SIZE_IN_BYTE
)

prepare_cors_middleware(
    app=app,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=[
        "Tus-Resumable",
        "Tus-Version",
        "Tus-Extension",
        "Tus-Max-Size",
        "Location",
        "Upload-Offset",
        "Upload-Length",
    ]
)

prepare_process_time_header(app=app)
