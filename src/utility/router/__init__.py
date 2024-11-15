from src.fast_api_pre_setup import app
from src.image_captcha.router.v1.router import router as image_captch_router

list_of_all_routers = (image_captch_router,)

for router in list_of_all_routers:
    app.include_router(router=router)
