from fastapi import APIRouter

from apis.v1 import route_user


api_router = APIRouter()
api_router.include_router(route_user.router,prefix="",tags=["users"])