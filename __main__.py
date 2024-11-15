from uvicorn import run
from src.setting import SETTINGS

if __name__ == "__main__":
    run(
        app=SETTINGS.UVICORN_SERVER.APP,
        host=SETTINGS.UVICORN_SERVER.HOST,
        port=SETTINGS.UVICORN_SERVER.PORT,
        log_level=SETTINGS.UVICORN_SERVER.LOG_LEVEL.lower(),
        proxy_headers=SETTINGS.UVICORN_SERVER.PROXY_HEADERS,
        forwarded_allow_ips=SETTINGS.UVICORN_SERVER.FORWARDED_ALLOW_IPS,
        reload=SETTINGS.UVICORN_SERVER.RELOAD,
        loop=SETTINGS.UVICORN_SERVER.LOOP,
        workers=SETTINGS.UVICORN_SERVER.WORKERS,
        server_header=SETTINGS.UVICORN_SERVER.SERVER_HEADER,
    )
