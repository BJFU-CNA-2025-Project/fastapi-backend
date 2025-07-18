from fastapi import APIRouter
from pydantic import BaseModel

from services.post_service import get_posts
from services.post_service import add_newpost
from services.post_service import delete_post
from services.post_service import get_topics

class Item(BaseModel):
    title: str
    content: str
    image: list
    tags: list
    activityId: str


router = APIRouter()


@router.get("/")
def get_posts():
    posts = get_posts()
    return {"success": True, "data": posts}


@router.post("/new_post")
def put_posts(new_post: Item):
    add_newpost(new_post)
    return {"success": True,"message": "New post added"}


@router.delete("/delete_post/{post_id}")
def delete_post(post_id: int):
    user_id=...#从token中解析出用户id
    success = delete_post(post_id, user_id)
    if not success:
        return {"success": False, "message": "post not found"}
    return {"success": True, "message": "Post deleted"}


@router.get("/topics")
def get_topics():
    topics = get_topics()
    return {"success": True, "data": topics}
