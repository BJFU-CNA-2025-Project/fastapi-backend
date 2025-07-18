from email.policy import default
from idlelib.query import Query
from typing import Union, Annotated
from fastapi import APIRouter
from services.activity_service import get_post_information, get_user_information,issue_comment,delete_comment,like_comment,unlike_comment
from pydantic import BaseModel

router = APIRouter()
class COMMENT(BaseModel):
    content: str
    parentId: str | None = None
@router.get("/{postId}/comments")
def get_posts(postId: Annotated[str , Query(min_length = 3,max_length = 100)]):
    post_information = get_post_information(postId)
    return {
        "success": True,
        "data":{
            "list": [
                {
                    "id" : post_information["id"],
                    "user": {
                        "id" : post_information["author"]["id"],
                        "name" : post_information["author"]["name"],
                        "avatar" : post_information["author"]["avatar"],
                    },
                    "content" : post_information["content"],
                    "createTime" : post_information["createTime"],
                    "likeCount" : post_information["likeCount"],
                    "isLiked" : post_information["isLiked"],
                }
            ],
            "total": post_information["total"],
            "hasmore": post_information["hasmore"],
        }
    }

@router.post("/{postId}{userId}/comments")
def issue_comment(postId:str, userId:str, commnet: COMMENT):
    user_information = get_user_information(userId)
    post_information = get_post_information(postId)
    issue_comment(user_information, post_information, commnet)
    # post_information["content"]+=commnet.content
    # post_information["isLiked"]=1
    # post_information["commentCount"]+=1
    # post_information["user"] += user_information
    # db.add(post_information)
    return {
        "success": True,
        "comment": {
            "postId": postId,
            "content": commnet.content,
            "parentId": commnet.parentId,
        },
        "author": {
            "userId": user_information["user"]["id"],
            "avatar": user_information["user"]["avatar"],
            "name": user_information["user"]["name"],
        }

    }
@router.get("/{postId}{userId}/comments")
def handle_like(postId:str, userId:str, isLike:bool):
    post_information = get_post_information(postId)
    userId = get_user_information(userId)
    isLike = 1 if post_information["postId"]["isLike"] else 0
    if isLike:
        return {
            "success": False,
            "content": "You have already liked this post.",
        }
    else :
        post_information["likeCount"] += 1
        post_information["isLiked"] = 1
        like_comment(userId, post_information)

        return {
            "success": True,
            "content": "You have liked this post.",
        }


