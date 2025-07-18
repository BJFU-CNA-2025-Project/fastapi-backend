from pydantic import BaseModel





def user_profile_by_id(token: str):
    """
    获取用户信息
    """
    class ProfileData(BaseModel):
        id: str
        name: str
        avatar: str
        level: int
        points: int
        completedActivities: int
        days: int
    # 从数据库获取用户信息

    return ProfileData()


def user_activities_by_id(token:str):
    """
    获取用户正在进行的活动
    """
    class ActivitiesData(BaseModel):
        id : int
        title : str
        date : int
        location : str
        distance : int
        calorie : int
        duration : int
        weather : str
        startPlace : str
        endPlace : str
        time : int
        difficulty : int
        type : str
        enrolledCount : int
        image : str
    # 从数据库获取用户正在进行的活动

    return ActivitiesData()

def user_favorites_by_id(token:str):
    """
    获取用户正在进行的活动
    """
    class FavoritesData(BaseModel):
        data : list

    # 从数据库获取用户正在进行的活动

    return FavoritesData()