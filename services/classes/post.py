class post:
    def __init__(self,user_id : int, post_time : str, title : str, content : str, activity : list, topics : list,
                 like_count : int, star_count : int):
        self.user_id = user_id      # 发布者
        self.post_time = post_time  # 发布时间
        self.title = title          # 标题
        self.content = content      # 内容
        self.activity = activity    # 关联活动的数组
        self.topics = topics        # 关联话题的数组
        self.like_count = like_count# 点赞数
        self.star_count = star_count# 收藏数
