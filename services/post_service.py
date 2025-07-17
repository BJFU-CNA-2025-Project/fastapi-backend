from routers.posts import Item


def get_posts():
    """
    获取帖子列表
    """
    #从数据库获取帖子数据
    return {"message": "Posts endpoint"}

def add_newpost(new_post:Item):
    """
    添加新帖子
    """
    # 帖子内容添加进入数据库
    return {"message": "add new post,Success"}

def delete_post(post_id:int,user_id:int)-> bool:
    """
    检查帖子是否属于该用户，若是则删除并返回True，否则则返回False
    """
    #将该用户的帖子内容从数据库删除


def get_topics():
    """"
    获取热门话题
    """
    #从数据库里获取话题数据
    return {"message": "topics endpoint"}


