from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from uvicorn.config import LOGGING_CONFIG

from routers.api import api_router

app = FastAPI(
    title="health management",
    description="health management FastAPI backend",
)

# 添加CORS中间件，允许所有来源的请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LOGGING_CONFIG["formatters"]["access"]["fmt"] = "%(levelprefix)s %(asctime)s - %(message)s"

# 添加API路由
app.include_router(api_router, prefix="/api")
