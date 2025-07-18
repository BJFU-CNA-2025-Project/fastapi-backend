from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_user():
    return {"message": "User endpoint"}

@router.get("/profile")
def get_user_profile(authorization: Annotated[str | None, Header()] = None,response = Response):
    """
    处理获取用户信息的请求
    """
    if not authorization or not authorization.startswith("Bearer ") :
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"success": False}    #检查是否携带请求头Authorization: Bearer {token}
    token = authorization.split("Bearer ")[1]
    data = user_profile_by_id(token)       #分离token并用token获取用户信息
    if not data:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"success": False}
    return {"success": True, "data": data}

@router.get("/activities/")
def get_users_activities(authorization: Annotated[str | None, Header()] = None,response = Response):
    """
    处理获取用户活动的请求
    """
    if not authorization or not authorization.startswith("Bearer ") :
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"success": False}    #检查是否携带请求头Authorization: Bearer {token}
    token = authorization.split("Bearer ")[1]
    data = user_activities_by_id(token) #分离token并用token获取用户活动列表
    if not data:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"success": False}
    return {"success": True, "data": data}


@router.get("/favorites/")
def get_users_favorites(authorization: Annotated[str | None, Header()] = None,response = Response):
    """
    处理获取用户收藏的请求
    """
    if not authorization or not authorization.startswith("Bearer ") :
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"success": False}    #检查是否携带请求头Authorization: Bearer {token}
    token = authorization.split("Bearer ")[1]
    data = user_favorites_by_id(token)    #分离token并用token获取用户收藏
    if not data:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"success": False}
    return {"success": True, "data": data}