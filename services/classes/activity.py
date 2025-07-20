class activity:
    def __init__(self, title : str, data : str, location : str, calorie : int, duration : int, weather : int, start_place : str,
                 end_place : str, time : str, difficulty : str, type : str, image : str, star_count : int):
        self.title = title              # 标题
        self.data = data                # 活动日期
        self.location = location        # 活动地点
        self.calorie = calorie          # 消耗卡路里
        self.duration = duration        # 时长（分钟）
        self.weather = weather          # 天气
        self.start_place = start_place  # 起点
        self.end_place = end_place      # 终点
        self.time = time                # 活动时间
        self.difficulty = difficulty    # 难度
        self.type = type                # 活动类型
        self.image = image              # 图像位置
        self.star_count = star_count    # 收藏数量