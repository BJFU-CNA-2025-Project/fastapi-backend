



def get_activities():
    """
    获取活动列表
    """
    # 从数据库获取活动数据


    return {"message": "Activities endpoint"}


def get_activity_by_id(activity_id: int):
    """
    根据活动ID获取活动详情
    """
    # 从数据库获取活动数据

    return {"message": f"Activity {activity_id} endpoint"}

def get_postsInformation_by_postsId(postId:str):
    """
    根据帖子ID获取帖子详情
    """

    json={
    "success": True,
    "data": {
        "list": [
        {
            "id": "评论ID",
            "user": {
            "id": "用户ID",
            "name": "用户名",
            "avatar": "头像URL"
            },
            "content": "评论内容",
            "createTime": "发布时间",
            "likeCount": bool,
            "isLiked": bool
        },
        ],
            "total":int,
            "hasMore": bool
        }
    }
    return json