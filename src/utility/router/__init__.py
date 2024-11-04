from ...fast_api_pre_setup import app

from ...user.router.v1.router import router as user_router
from ...session.router.v1.router import router as session_router
from ...history.router.v1.router import router as history_router
from ...video.router.v1.router import router as video_router
from ...report.router.v1.router import router as report_router

list_of_all_routers = (
    user_router,
    session_router,
    history_router,
    video_router,
    report_router,
)

for router in list_of_all_routers:
    app.include_router(router=router)
