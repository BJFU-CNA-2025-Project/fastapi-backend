from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    name : str
    avatar : str

class SportData(BaseModel):
    period : str
    start : str
    end : str

@router.get("/")
def get_user():
    user_message = get_user_message()
    if not user_message:
        return {"message": "User not found"}
    return {"message": user_message}

@router.put("/profile")
def put_user(user_id: int, user: User):
    user_old = get_user_message(user_id)
    if user.name != user_old['name'] or user.avatar != user_old['avatar']:
        success = update_message({'id': user_id, 'name': user.name, 'avatar': user.avatar})
        if success:
            return {"message": "User updated successfully"}
        else:
            return {"message": "Failed to update user"}
    else:
        return {"message": "No changes made"}

@router.get("/data/")
def get_data(user_id : str):
    data = get_sport_data(user_id)
    if not data:
        return {"message": "User not found"}
    return {"success": True, "data": data}

@router.get("/activities")
def get_activity(user_id : str):
    activities = get_my_activities(user_id)
    if not activities:
        return {"message": "User not found"}
    return {"activity":activities}

@router.get("/favorites")
def get_favorites(user_id: int, type: str):
    favorites = get_favorites(user_id)
    if not favorites:
        return {"message":"not found"} # type: ignore
    filtered_favorites = [favorite for favorite in favorites if favorite.type == type]
    return {"favorites": filtered_favorites}
