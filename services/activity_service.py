



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

def get_header(activity_id: int):
    """
    获取用户的access_token
    """
    # 从数据库获取header数据

    return{"Authorization": f"Bearer {"token"}"}

def get_banner():
    """
    获取banner数据
    """
    # 从数据库获取banner数据

    return{"message": "Banner endpoint"}

