from fastapi import APIRouter
from services.activity_service import *

router = APIRouter()


@router.get("/")
def get_activities():
    activities = get_activities()

    if not activities:
        return {"success": False, "message": "Activities not found"}

    return {"success": True, "data": activities}

@router.get("/{activity_id}")
def get_activity(activity_id: int):
    activity = get_activity_by_id(activity_id)

    if not activity:
        return {"success": False, "message": "Activity not found"}

    return {"success": True, "data": activity}

#需要请求头
@router.post("/{activity_id}/enroll")
def enroll_activity( activity_id: int):

    return {"success": True}

@router.get("/banners")
def get_banners():
    banners= get_banners()

    return {"success": True, "data": banners}

