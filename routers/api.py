from fastapi import APIRouter

from routers.activities import router as activity_router
from routers.posts import router as post_router
from routers.user import router as user_router

api_router = APIRouter()

# 添加子路由
api_router.include_router(activity_router, prefix="/activities", tags=["activities"])
api_router.include_router(post_router, prefix="/posts", tags=["posts"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
