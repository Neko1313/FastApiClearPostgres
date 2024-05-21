from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html

from conf import API_V1
from src.routers.all_routers import all_routers

app = FastAPI()

appv1 = FastAPI(title="API", description="API", version="0.0.1")

for router in all_routers:
    appv1.include_router(router)

app.mount(API_V1, appv1)
