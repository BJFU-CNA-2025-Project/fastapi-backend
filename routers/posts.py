from fastapi import APIRouter
from starlette import status

router = APIRouter()

# 用于用户点赞和收藏状态的内存字典
like_status = {}  # {(user_id, post_id): bool}
star_status = {}  # {(user_id, post_id): bool}


@router.get("/")
def get_posts():
    return {"message": "Posts endpoint"}


@router.post("/{id}/star")
def star_post(id: int):
    postId = 1  # 假设
    key = (postId, id)
    # 切换状态
    current = star_status.get(key, False)
    star_status[key] = not current
    return {
        "post_id": postId,
        "user_id": id,
        "isStarred": star_status[key],
        "message": f"{id} 收藏{'成功' if star_status[key] else '已取消'}"
    }


@router.post("/{id}/like")
def like_post(id: int):
    postId = 1  # 假设
    key = (postId, id)
    # 切换状态
    current = like_status.get(key, False)
    like_status[key] = not current
    return {
        "post_id": postId,
        "user_id": id,
        "isLiked": like_status[key],
        "message": f"{id} 点赞{'成功' if like_status[key] else '已取消'}"
    }

