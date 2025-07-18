import json


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

def get_post_information(postId : str):
    return json
def get_user_information(userId : str):
    return json
def issue_comment(userId, postId, content):
    return json
def delete_comment(userId, postId, commentId):
    return json
def like_comment(userId, postId,) :
    return json
def unlike_comment(userId, postId, ):
    return json


