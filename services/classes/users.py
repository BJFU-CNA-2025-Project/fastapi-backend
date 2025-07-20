class user:
    def __init__(self, name : str, avatar : str, level : int, points : int, days : int, phone_number : str,
                 register_time : str, account : str, password : str, open_id : str, union_id : str):
        self.name = name                    # 昵称
        self.avatar = avatar                # 头像URL
        self.level = level                  # 等级
        self.points = points                # 积分数量
        self.days = days                    # 打卡数
        self.phone_number = phone_number    # 手机号
        self.register_time = register_time  # 注册时间
        self.account = account              # 账号
        self.password = password            # 密码
        self.open_id = open_id              # 微信open_id
        self.union_id = union_id            # 微信union_id