# 项目目录结构：
```
services/
│
├── classes/
│   ├── __init__.py
│   ├── activity.py
│   ├── post.py
│   ├── row_to_class.py
│   ├── topic.py
│   └── users.py
│
├── connection/
│   ├── __init__.py
│   ├── connection.py
│   └── DatabaseConfig.py
│
├── sql/
│   └── sql.sql
│
├── __init__.py
├── activity_service.py
├── post_service.py
├── tag_service.py
├── topic_service.py
└── user_service.py
```

## 主要模块说明

1. **数据模型(classes/)**
   - 定义应用核心数据结构的Python类
   - 包含活动、帖子、话题、用户等模型定义
   - `row_to_class.py`提供数据库行到Python对象的转换功能

2. **数据库连接(connection/)**
   - 封装所有数据库连接相关逻辑
   - 包含连接池管理和配置加载

3. **服务模块**
   - 提供各类业务服务接口
   - 每个服务对应一个核心业务领域
   - 遵循统一的API设计规范

4. **SQL脚本(sql/)**
   - 数据库初始化脚本
   - 表结构和基础数据定义

# 目录：

* [1. 返回值格式规范](#1返回值格式规范)
* [2. 数据模型定义](#2数据模型定义)
    * [2.1 活动模型](#21-活动模型)
    * [2.2 用户模型](#22-用户模型)
    * [2.3 帖子模型](#23-帖子模型)
    * [2.4 话题模型](#24-话题模型)
* [3. 数据库模型](#3数据库模型)
    * [3.1 核心数据表](#31-核心数据表)
        * [3.1.1 用户表](#311-用户表)
        * [3.1.2 活动表](#312-活动表)
        * [3.1.3 帖子表](#313-帖子表)
        * [3.1.4 话题表](#314-话题表)
        * [3.1.5 标签表](#315-标签表)
    * [3.2 关联关系表](#32-关联关系表)
        * [3.2.1 用户活动表](#321-用户活动表)
        * [3.2.2 收藏关系表](#322-收藏关系表)
        * [3.2.3 内容关联表](#323-内容关联表)
        * [3.2.4 标签关联表](#324-标签关联表)
        * [3.2.5 点赞关联表](#325-点赞关联表)
    * [3.3 辅助数据表](#33-辅助数据表)
        * [3.3.1 评论表](#331-评论表)
        * [3.3.2 运动数据表](#332-运动数据表)
* [4. 数据库API接口](#4数据库api接口)
    * [4.1 活动服务](#41-活动服务)
        * [4.1.1 添加新活动](#411-添加新活动)
        * [4.1.2 删除活动](#412-删除活动)
        * [4.1.3 获取分页活动数据](#413-获取分页活动数据)
        * [4.1.4 获取活动详情](#414-获取活动详情)
        * [4.1.5 修改活动信息](#415-修改活动信息)
    * [4.2 帖子服务](#42-帖子服务)
        * [4.2.1 添加新帖子](#421-添加新帖子)
        * [4.2.2 删除帖子](#422-删除帖子)
        * [4.2.3 获取所有帖子](#423-获取所有帖子)
        * [4.2.4 获取帖子详情](#424-获取帖子详情)
        * [4.2.5 获取帖子评论](#425-获取帖子评论)
        * [4.2.6 发表评论](#426-发表评论)
        * [4.2.7 删除评论](#427-删除评论)
        * [4.2.8 点赞帖子](#428-点赞帖子)
        * [4.2.9 取消点赞](#429-取消点赞)
        * [4.2.10 收藏帖子](#4210-收藏帖子)
        * [4.2.11 取消收藏](#4211-取消收藏)
    * [4.3 标签服务](#43-标签服务)
        * [4.3.1 创建新标签](#431-创建新标签)
        * [4.3.2 为帖子关联标签](#432-为帖子关联标签)
        * [4.3.3 为活动关联标签](#433-为活动关联标签)
    * [4.4 话题服务](#44-话题服务)
        * [4.4.1 添加新话题](#441-添加新话题)
        * [4.4.2 删除话题](#442-删除话题)
        * [4.4.3 获取热门话题](#443-获取热门话题)
        * [4.4.4 获取话题关联帖子](#444-获取话题关联帖子)
    * [4.5 用户服务](#45-用户服务)
        * [4.5.1 添加新用户](#451-添加新用户)
        * [4.5.2 删除用户](#452-删除用户)
        * [4.5.3 获取用户信息](#453-获取用户信息)
        * [4.5.4 更新用户信息](#454-更新用户信息)
        * [4.5.5 报名活动](#455-报名活动)
        * [4.5.6 取消报名](#456-取消报名)
        * [4.5.7 收藏活动](#457-收藏活动)
        * [4.5.8 获取用户参与活动](#458-获取用户参与活动)
        * [4.5.9 获取用户收藏帖子](#459-获取用户收藏帖子)
        * [4.5.10 获取用户收藏活动](#4510-获取用户收藏活动)
        * [4.5.11 取消收藏活动](#4511-取消收藏活动)
        * [4.5.12 获取用户发布帖子](#4512-获取用户发布帖子)
        * [4.5.13 获取用户报名活动](#4513-获取用户报名活动)
        * [4.5.14 记录运动数据](#4514-记录运动数据)
        * [4.5.15 获取运动数据](#4515-获取运动数据)

# 1.返回值格式规范

**当查询成功时：**
```json
{
    "success": true,
    "message": "查询成功！",
    "data": "返回数据内容"
}
```
**当查询失败时：**
```json
{
    "success": false,
    "message": "查询失败！",
    "detail": "错误详情信息"
}
```

**字段说明**
* ```success```: 布尔值，标识操作是否成功
* ```message```: 操作结果的状态信息
* ```data```: 操作成功时返回的业务数据
* ```detail```: 操作失败时的详细错误说明

**错误处理说明**
当```detail```字段包含以下关键词时，表明存在系统设计问题，请及时反馈：
* 缺少必要字段
* 数据表不存在
* 字段不存在
* SQL语句错误

返回值若包含英文，则说明此时错误来自于数据库内部，可以向**AI**询问相关内容。


# 2.数据模型定义
## 2.1 活动模型
```python
class activity:
    def __init__(self, title : str, data : str, location : str, calorie : int, duration : int, weather : int, start_place : str,
                 end_place : str, time : str, difficulty : str, type : str, image : str, star_count : int):
        self.title = title                  # 标题
        self.data = data                    # 活动日期
        self.location = location            # 活动地点
        self.calorie = calorie              # 消耗卡路里
        self.duration = duration            # 时长（分钟）
        self.weather = weather              # 天气
        self.start_place = start_place      # 起点
        self.end_place = end_place          # 终点
        self.time = time                    # 活动时间
        self.difficulty = difficulty        # 难度
        self.type = type                    # 活动类型
        self.image = image                  # 图像位置
        self.star_count = star_count        # 收藏数量
```
## 2.2 用户模型
```python
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
```
## 2.3 帖子模型
```python
class post:
    def __init__(self,user_id : int, post_time : str, title : str, content : str, activity : list, topics : list,
                 like_count : int, star_count : int):
        self.user_id = user_id              # 发布者
        self.post_time = post_time          # 发布时间
        self.title = title                  # 标题
        self.content = content              # 内容
        self.activity = activity            # 关联活动的数组
        self.topics = topics                # 关联话题的数组
        self.like_count = like_count        # 点赞数
        self.star_count = star_count        # 收藏数
```
## 2.4 话题模型
```python
class topic:
    def __init__(self, title : str, description : str, color : str, icon : str, image : str):
        self.title = title                  # 标题
        self.description = description      # 描述
        self.color = color                  # 颜色
        self.icon = icon                    # 图标
        self.image = image                  # 图像地址
```
其余简单数据结构未单独建模。

# 3.数据库模型

## 3.1 核心数据表

### 3.1.1 用户表

```sql
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '用户ID(PK)',
  `name` varchar(20) DEFAULT NULL COMMENT '用户昵称',
  `avatar` varchar(100) DEFAULT NULL COMMENT '头像URL',
  `level` int DEFAULT NULL COMMENT '用户等级',
  `points` int DEFAULT NULL COMMENT '积分数量',
  `days` int DEFAULT NULL COMMENT '连续打卡数',
  `phone_number` varchar(20) DEFAULT NULL COMMENT '手机号',
  `register_time` datetime DEFAULT NULL COMMENT '注册时间',
  `account` varchar(20) DEFAULT NULL COMMENT '账号',
  `password` varchar(20) DEFAULT NULL COMMENT '密码',
  `open_id` varchar(30) DEFAULT NULL COMMENT '微信openId',
  `union_id` varchar(30) DEFAULT NULL COMMENT '微信unionId',
  PRIMARY KEY (`id`)
) COMMENT='用户表';
```

### 3.1.2 活动表
```sql
CREATE TABLE `activities` (
  `activity_id` int NOT NULL AUTO_INCREMENT COMMENT '活动ID(PK)',
  `title` varchar(30) DEFAULT NULL COMMENT '标题',
  `date` date DEFAULT NULL COMMENT '活动日期',
  `location` varchar(60) DEFAULT NULL COMMENT '活动地点',
  `calorie` int DEFAULT NULL COMMENT '消耗卡路里',
  `duration` int DEFAULT NULL COMMENT '时长(分钟)',
  `weather` int DEFAULT NULL COMMENT '天气',
  `start_place` varchar(60) DEFAULT NULL COMMENT '起点',
  `end_place` varchar(60) DEFAULT NULL COMMENT '终点',
  `time` time DEFAULT NULL COMMENT '活动时间',
  `difficulty` varchar(10) DEFAULT NULL COMMENT '难度',
  `type` varchar(15) DEFAULT NULL COMMENT '活动类型',
  `image` varchar(150) DEFAULT NULL COMMENT '活动图片URL',
  `star_count` int DEFAULT NULL COMMENT '收藏数',
  PRIMARY KEY (`activity_id`)
) COMMENT='活动表';
```

### 3.1.3 帖子表
```sql
CREATE TABLE `blogs` (
  `blog_id` int NOT NULL AUTO_INCREMENT COMMENT '帖子ID(PK)',
  `user_id` int DEFAULT NULL COMMENT '用户ID(FK)',
  `activity_id` int DEFAULT NULL COMMENT '活动ID(FK)',
  `post_time` datetime DEFAULT NULL COMMENT '发送时间',
  `title` varchar(50) DEFAULT NULL COMMENT '标题',
  `content` varchar(1024) DEFAULT NULL COMMENT '内容',
  `like_count` int DEFAULT NULL COMMENT '点赞数',
  `star_count` int DEFAULT NULL COMMENT '收藏数量',
  PRIMARY KEY (`blog_id`),
  KEY `activity_id` (`activity_id`),
  KEY `blogs_ibfk_1` (`user_id`),
  CONSTRAINT `blogs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `blogs_ibfk_2` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) COMMENT='帖子表';
```

### 3.1.4 话题表
```sql
CREATE TABLE `topic` (
  `topic_id` int NOT NULL AUTO_INCREMENT COMMENT '话题ID(PK)',
  `title` varchar(50) DEFAULT NULL COMMENT '标题',
  `description` varchar(255) DEFAULT NULL COMMENT '话题描述',
  `color` varchar(20) DEFAULT NULL COMMENT '主题色',
  `icon` varchar(150) DEFAULT NULL COMMENT '图标',
  `image` varchar(150) DEFAULT NULL COMMENT '封面图片',
  PRIMARY KEY (`topic_id`)
) COMMENT='话题表';
```
### 3.1.5 标签表
```sql
CREATE TABLE `labels` (
  `label_id` int NOT NULL AUTO_INCREMENT COMMENT '标签ID(PK)',
  `content` varchar(30) DEFAULT NULL COMMENT '内容',
  PRIMARY KEY (`label_id`)
) COMMENT='标签表';
```
## 3.2 关联关系表
### 3.2.1 用户活动表
```sql
CREATE TABLE `enroll` (
  `user_id` int NOT NULL COMMENT '用户ID(FK)',
  `activity_id` int NOT NULL COMMENT '活动ID(FK)',
  `enroll_time` datetime DEFAULT NULL COMMENT '报名时间',
  PRIMARY KEY (`user_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) COMMENT='用户报名活动表';

CREATE TABLE `user_activity` (
  `user_id` int NOT NULL COMMENT '用户ID(FK)',
  `activity_id` int NOT NULL COMMENT '活动ID(FK)',
  `status` varchar(20) DEFAULT NULL COMMENT '活动状态',
  PRIMARY KEY (`user_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) COMMENT='用户关联活动表';
```
### 3.2.2 收藏关系表
```sql
CREATE TABLE `star_activities` (
  `user_id` int NOT NULL COMMENT '用户ID(FK)',
  `activity_id` int NOT NULL COMMENT '活动ID(FK)',
  PRIMARY KEY (`user_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) COMMENT='用户收藏活动表';

CREATE TABLE `user_star_blogs` (
  `user_id` int NOT NULL COMMENT '用户ID(FK)',
  `blog_id` int NOT NULL COMMENT '帖子ID(FK)',
  PRIMARY KEY (`user_id`,`blog_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) COMMENT='用户收藏帖子表';
```
### 3.2.3 内容关联表
```sql
CREATE TABLE `blog_activity` (
  `blog_id` int NOT NULL COMMENT '帖子ID(FK)',
  `activity_id` int NOT NULL COMMENT '活动ID(FK)',
  PRIMARY KEY (`blog_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) COMMENT='帖子关联活动表';

CREATE TABLE `topic_blog` (
  `topic_id` int NOT NULL COMMENT '话题ID(FK)',
  `blog_id` int NOT NULL COMMENT '帖子ID(FK)',
  PRIMARY KEY (`topic_id`,`blog_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT FOREIGN KEY (`topic_id`) REFERENCES `topic` (`topic_id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) COMMENT='话题关联帖子表';
```

### 3.2.4 标签关联表
```sql
CREATE TABLE `activity_label` (
  `label_id` int NOT NULL COMMENT '标签ID(FK)',
  `activity_id` int NOT NULL COMMENT '活动ID(FK)',
  PRIMARY KEY (`label_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT FOREIGN KEY (`label_id`) REFERENCES `labels` (`label_id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) COMMENT='活动拥有标签表';

CREATE TABLE `blog_label` (
  `label_id` int NOT NULL COMMENT '标签ID(FK)',
  `blog_id` int NOT NULL COMMENT '帖子ID(FK)',
  PRIMARY KEY (`label_id`,`blog_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT FOREIGN KEY (`label_id`) REFERENCES `labels` (`label_id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) COMMENT='帖子拥有标签表';
```

### 3.2.5 点赞关联表
```sql
CREATE TABLE `user_like_blog` (
  `like_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL COMMENT '用户ID(FK)',
  `blog_id` int DEFAULT NULL COMMENT '帖子ID(FK)',
  `content` varchar(255) DEFAULT NULL COMMENT '评论内容',
  PRIMARY KEY (`like_id`),
  KEY `user_id` (`user_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) COMMENT='用户点赞帖子表';
```

## 3.3 辅助数据表

### 3.3.1 评论表
```sql
CREATE TABLE `comment` (
  `comment_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL COMMENT '用户ID(FK)',
  `blog_id` int DEFAULT NULL COMMENT '帖子ID(FK)',
  `content` varchar(255) DEFAULT NULL COMMENT '评论内容',
  `commentTime` datetime DEFAULT NULL COMMENT '评论时间',
  PRIMARY KEY (`comment_id`),
  KEY `user_id` (`user_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) COMMENT='评论表';
```

### 3.3.2 运动数据表
```sql
CREATE TABLE `exercise_data` (
  `exercise_id` int NOT NULL AUTO_INCREMENT COMMENT '运动数据ID(PK)',
  `user_id` int DEFAULT NULL COMMENT '用户ID(FK)',
  `time` datetime DEFAULT NULL COMMENT '记录时间',
  `step` int DEFAULT NULL COMMENT '运动步数',
  PRIMARY KEY (`exercise_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) COMMENT='运动数据表';
```

说明：

* 用户系统
用户表(users)存储用户基本信息，包括昵称、头像、等级、积分、打卡天数、联系方式等。每个用户有唯一ID作为主键，支持微信登录(open_id/union_id)和账号密码登录两种方式。

* 活动管理
活动表(activities)记录各类户外活动信息，包含标题、时间地点、运动指标(卡路里、时长)、路线信息(起终点)、难度等级等。用户可通过报名表(enroll)参与活动，还能收藏活动(star_activities)。活动状态通过用户活动关系表(user_activity)跟踪。

* 社区互动
用户可在帖子表(blogs)发布内容，帖子可关联活动(blog_activity)和话题(topic_blog)。帖子支持点赞(user_like_blog)和收藏(user_star_blogs)功能。评论系统(comment)允许用户互动，评论会记录发布时间和内容。

* 标签系统
标签表(labels)提供灵活的标签管理，通过活动标签(activity_label)和帖子标签(blog_label)实现多对多关联，支持按标签分类检索内容。

* 话题功能
话题表(topic)包含话题标题、描述及样式配置(颜色/图标)，通过话题帖子关系表(topic_blog)关联相关内容，形成话题聚合页。

* 健康数据
运动数据表(exercise_data)记录用户每日步数等健康指标，按时间排序可生成运动趋势分析。

所有关联表均采用级联删除设计，确保数据完整性。例如，当删除某个帖子时，其下所有的评论也会自动被删除。

# 4.数据库API接口

## 4.1 活动服务
`activity_service.py` 提供活动相关的增删改查功能，包括活动创建、删除、查询和修改等操作。

### 4.1.1 添加新活动
* 函数体：
```python
def add_activity(self, new_activity: activity):
```
* 参数：
```
new_activity : 活动对象
```
* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "新增活动成功！",
        "activity_id": "int"            // 活动id
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",               // 各种可能的错误信息
        "detail" : "str"                // 详细情况
    }
    ```

### 4.1.1 添加新活动
* 函数体：
```python
def add_activity(self, new_activity: activity):
```
* 参数：
```
new_activity : 活动对象
```
* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "新增活动成功！",
        "activity_id": "int"            // 活动id
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",               // 各种可能的错误信息
        "detail" : "str"                // 详细情况
    }
    ```

### 4.1.2 删除活动
* 函数体：
```python
def remove_activity(self, activity_id: int):
```
* 参数：
```
activity_id : 表示被删除的活动id
```
* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "删除成功",
        "data": {
            "activity_id": "int"
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",               // 各种可能的错误信息
        "detail" : "str"                // 详细情况
    }
    ```

### 4.1.3 获取分页的活动数据
* 函数体：
```python
def get_all_activities(self, page: int = 1, size: int = 10):
```
* 参数：
```
page : 第几页
size : 获取的个数
```
* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "获取成功",
        "data": {
            "activities": [
                {
                    "id": "int",              // 活动id
                    "activity": "activity",   // 活动对象
                    "enroll_count": "int"     // 报名人数  
                }
            ],
            "pagination": {
                "total": "int",             // 总数
                "page": "int",               // 哪一页
                "size": "int",               // 有多少
                "pages": "int" 
            }
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",               // 各种可能的错误信息
        "detail" : "str"                // 详细情况
    }
    ```

### 4.1.4 获取活动详细信息
* 函数体：
```python
def get_detail_activity(self, activity_id: int):
```
* 参数：
```
activity_id : 通过活动id获取详细信息
```
* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "查询成功！",
        "data": {
            "id": "int",                      // 活动id
            "activity": "activity",           // 活动对象
            "enroll_count": "int",            // 报名人数
            "labels": [                     
                {
                    "id": "int",              // 标签id
                    "name": "str"             // 标签名称
                }
            ], 
            "related_posts": [              
                {
                    "id": "int",              // 帖子id
                    "title": "str",           // 帖子标题
                    "time": "str",            // 发布时间
                    "author": "str",          // 发布者
                    "author_id": "int"        // 发布者id
                }
            ]
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",               // 各种可能的错误信息
        "detail" : "str"                // 详细情况
    }
    ```
### 4.1.5 修改活动信息
* 函数体：
```python
def modify_activity(self, activity_id: int, **kwargs):
```
* 参数：
```
activity_id : 表示被修改的活动id
kwargs : 需要修改的字段键值对
```
* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "修改成功!",
        "data": {
            "activity_id": "int"      // 返回活动id
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",               // 各种可能的错误信息
        "detail" : "str"                // 详细情况
    }
    ```

## 4.2 帖子服务
`post_service.py` 提供帖子相关的增删改查功能，包括帖子创建、删除、查询和互动等操作。

### 4.2.1 添加新帖子

* 函数体：

```python
def add_post(self, new_post: post):
```

* 参数：
```
new_post : 帖子对象
```

* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "添加成功",
        "data": {
            "post_id": "int"        // 帖子id
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",           // 错误信息
        "detail": "str"            // 详细情况
    }
    ```

### 4.2.2 删除帖子

* 函数体：

```python
def remove_post(self, post_id: int):
```

* 参数：
```
post_id : 被删除的帖子id
```

* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "删除成功",
        "data": {
            "post_id": "int"       // 被删除的帖子id
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```

### 4.2.3 获取所有帖子

* 函数体：

```python
def get_all_posts(self):
```

* 参数：
```
new_post : 帖子对象
```

* 返回值：
    * 当查询成功时：
    ```json
    {
        "success": true,
        "message": "查询成功！",
        "data": [
            {
                "id": "int",       // 帖子id
                "user_id": "int",  // 发布者id
                "post": "post"     // 帖子对象
            }
        ]
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```

### 4.2.4 获取帖子详情

* 函数体：

```python
def get_post(self, post_id: int):
```

* 参数：
```
post_id : 帖子id
```

* 返回值：
    * 当查询成功时：
    ```json
    {
        "success": true,
        "message": "查询成功",
        "data": {
            "id": "int",           // 帖子id
            "post": "post",        // 帖子对象
            "user_info": {         // 用户信息
                "id": "int",       // 用户id
                "name": "str",     // 用户名
                "avatar": "str"    // 用户头像
            },
            "activities": "list",  // 关联活动
            "topics": "list"       // 关联话题
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",           // 错误信息
        "detail": "str"            // 详细情况
    }
    ```

### 4.2.5 获取帖子评论

* 函数体：

```python
def get_all_comments(self, post_id: int):
```

* 参数：
```
post_id : 帖子id
```

* 返回值：
    * 当查询成功时：
    ```json
    {
        "success": true,
        "message": "查询成功",
        "data": [
            {
                "comment_id": "int",       // 评论id
                "user_id": "int",         // 用户id
                "blog_id": "int",         // 帖子id
                "content": "str",         // 评论内容
                "comment_time": "str",    // 评论时间
                "user_info": {            // 用户信息
                    "name": "str",        // 用户名
                    "avatar": "str"      // 用户头像
                }
            }
        ]
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",           // 错误信息
        "detail": "str"            // 详细情况
    }
    ```

### 4.2.6 发表评论

* 函数体：

```python
def leave_comment(self, user_id: int, post_id: int, content: str):
```

* 参数：
```
user_id : 用户id
post_id : 帖子id
content : 评论内容
```

* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "查询成功",
        "data": {
            "id": "int",           // 评论id
            "user_id": "int",      // 用户id
            "blog_id": "int",      // 帖子id
            "content": "str",      // 评论内容
            "comment_time": "str", // 评论时间
            "user_info": {         // 用户信息
                "id": "int",       // 用户id
                "name": "str",     // 用户名
                "avatar": "str"    // 用户头像
            }
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",           // 错误信息
        "detail": "str"            // 详细情况
    }
    ```

### 4.2.7 删除评论

* 函数体：

```python
def delete_comment(self, comment_id: int):
```

* 参数：
```
comment_id : 评论id
```

* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "删除成功!",
        "data": {
            "comment_id": "int"    // 被删除的评论id
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",           // 错误信息
        "detail": "str"            // 详细情况
    }
    ```

### 4.2.8 点赞帖子

* 函数体：

```python
def like(self, user_id: int, post_id: int):
```

* 参数：
```
new_post : 帖子对象
```

* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "点赞成功!",
        "data": {
            "user_id": "int",      // 用户id
            "post_id": "int"       // 帖子id
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```

### 4.2.9 取消点赞

* 函数体：

```python
def dislike(self, user_id: int, post_id: int):
```

* 参数：
```
user_id : 用户id
post_id : 帖子id
```

* 返回值：
    * 当成功时：
    ```json
    {
        "success": true,
        "message": "取消点赞成功!",
        "data": {
            "user_id": "int",      // 用户id
            "post_id": "int"       // 帖子id
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",           // 错误信息
        "detail": "str"            // 详细情况
    }
    ```

### 4.2.10 收藏帖子

* 函数体：

```python
def bookmark(self, user_id: int, post_id: int):
```

* 参数：
```
user_id : 用户id
post_id : 帖子id
```

* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "收藏成功!",
        "data": {
            "user_id": "int",      // 用户id
            "post_id": "int"       // 帖子id
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```

### 4.2.11 取消收藏

* 函数体：

```python
def unbookmark(self, user_id: int, post_id: int):
```

* 参数：
```
user_id : 用户id
post_id : 帖子id
```

* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "取消收藏成功!",
        "data": {
            "user_id": "int",      // 用户id
            "post_id": "int"       // 帖子id
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```

## 4.3 标签服务
`tag_service.py` 提供标签相关的创建和关联功能，包括标签创建、标签与帖子/活动的关联等操作。

### 4.3.1 创建新标签

* 函数体：

```python
def add_tag(self, tag_content: str):
```

* 参数：
```
tag_content : 标签内容（需唯一）
```

* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "创建成功",
        "data": {
            "tag_id": "int"       // 新增标签的id
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.3.2 为帖子关联标签

* 函数体：

```python
def add_tag_to_post(self, post_id: int, tag_id: int):
```

* 参数：
```
post_id : 帖子ID
tag_id : 标签ID
```

* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "添加成功",
        "data": {
            "tag_id": "int",      // 标签ID
            "post_id": "int"      // 帖子ID
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.3.3 为活动关联标签

* 函数体：

```python
def add_tag_to_activity(self, activity_id: int, tag_id: int):
```

* 参数：
```
activity_id : 活动ID
tag_id : 标签ID
```

* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "添加成功",
        "data": {
            "tag_id": "int",      // 标签ID
            "activity_id": "int"  // 活动ID
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
## 4.4 话题服务
`topic_service.py` 提供话题相关的增删改查功能，包括话题创建、删除、查询和关联帖子等操作。
### 4.4.1 添加新话题

* 函数体：

```python
def add_topic(self, new_topic: topic):
```

* 参数：
```
activity_id : 活动ID
tag_id : 标签ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "话题创建成功",
        "data": {
            "topic_id": "int"
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.4.3 为活动关联标签

* 函数体：

```python
def remove_topic(self, topic_id: int):
```

* 参数：
```
topic_id : 话题ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "删除成功！",
        "detail": {
            "topic_id": "int"
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.4.3 获取热门话题

* 函数体：

```python
def get_hot_topics(self, limit: int = 10):
```

* 参数：
```
limit : 返回数量限制（默认10）
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "获取成功",
        "data": [
            {
                "id": "int",
                "topic": "话题对象",
                "post_count": "int"
            }
        ]
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "错误信息",
        "detail": "详细情况"
    }
    ```
### 4.4.4 获取话题关联帖子

* 函数体：

```python
def get_posts_by_topic(self, topic_id: int, page: int = 1, page_size: int = 10):
```

* 参数：
```
topic_id : 话题ID
page : 页码（默认1）
page_size : 每页数量（默认10）
```

* 返回值：
    * 当新增成功时：
    ```json
    {
        "success": true,
        "message": "查询成功！",
        "data": {
            "topic_info": {
                "id": "int",
                "title": "str",
                "description": "str"
            },
            "posts": [
                {
                    "id": "int",
                    "title": "str",
                    "content": "str",
                    "post_time": "datetime",
                    "author": {
                        "id": "int",
                        "name": "str"
                    }
                }
            ],
            "pagination": {
                "total": "int",
                "page": "int",
                "page_size": "int",
                "total_pages": "int"
            }
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```

## 4.5 用户服务
`user_service.py` 提供用户相关的增删改查功能，包括用户管理、活动报名、收藏管理等操作。
### 4.5.1 添加新用户

* 函数体：

```python
def add_user(self, new_user: user):
```

* 参数：
```
new_user : 用户对象
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "用户创建成功",
        "data": {
            "user_id": "int"
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.2 删除用户

* 函数体：

```python
def remove_user(self, user_id: int):
```

* 参数：
```
user_id : 用户ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "用户删除成功！",
        "data": {
            "user_id": "int"
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.3 获取用户信息

* 函数体：

```python
def get_message(self, user_id: int):
```

* 参数：
```
user_id : 用户ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "用户信息查询成功",
        "data": {
            "id": "int",
            "user": "用户对象",
            "stats": {
                "post_count": "int",
                "activity_count": "int",
                "bookmark_count": "int"
            }
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.4 更新用户信息

* 函数体：

```python
def update_user(self, user_id: int, name: str, avatar: str):
```

* 参数：
```
user_id : 用户ID
name : 用户名
avatar : 头像URL
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "用户信息更新成功成功！",
        "data": {
            "user_id": "int"
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.5 报名活动

* 函数体：

```python
def register_activity(self, user_id: int, activity_id: int):
```

* 参数：
```
user_id : 用户ID
activity_id : 活动ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "用户报名成功！",
        "data": {
            "user_id": "int",
            "activity_id": "int",
            "enroll_time": "str"
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.6 取消报名

* 函数体：

```python
def cancel_registration(self, user_id: int, activity_id: int):
```

* 参数：
```
user_id : 用户ID
activity_id : 活动ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "取消报名成功",
        "data": {
            "user_id": "int",
            "activity_id": "int"
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.7 收藏活动

* 函数体：

```python
def bookmark_activity(self, user_id: int, activity_id: int):
```

* 参数：
```
user_id : 用户ID
activity_id : 活动ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "活动收藏成功",
        "data": {
            "user_id": "int",
            "activity_id": "int"
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.8 获取用户参与的活动

* 函数体：

```python
def get_activities(self, user_id: int):
```

* 参数：
```
user_id : 用户ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "成功获取活动!",
        "data": [
            {
                "id": "int",
                "activity": "活动对象",
                "status": "str"
            }
        ]
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.9 获取用户收藏的帖子

* 函数体：

```python
def get_bookmark_posts(self, user_id: int):
```

* 参数：
```
topic_id : 话题ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "",
        "data": [
            {
                "id": "int",
                "post": "帖子对象"
            }
        ]
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.10 获取用户收藏的活动

* 函数体：

```python
def get_bookmark_activities(self, user_id: int):
```

* 参数：
```
user_id : 用户ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "活动查询成功",
        "data": [
            {
                "id": "int",
                "activity": "活动对象"
            }
        ]
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.11 取消收藏活动

* 函数体：

```python
def unbookmark_activity(self, user_id: int, activity_id: int):
```

* 参数：
```
user_id : 用户ID
activity_id : 活动ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "已取消收藏活动",
        "data": {
            "user_id": "int",
            "activity_id": "int"
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.12 获取用户发布的帖子

* 函数体：

```python
def get_publish_posts(self, user_id: int):
```

* 参数：
```
user_id : 用户ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "获取帖子成功！",
        "data": [
            {
                "id": "int",
                "post": "帖子对象",
                "author_info": {
                    "id": "int",
                    "name": "str"
                }
            }
        ]
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.13 获取用户报名的活动

* 函数体：

```python
def get_register_activity(self, user_id: int):
```

* 参数：
```
user_id : 用户ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "查询活动成功",
        "data": [
            {
                "id": "int",
                "activity": "活动对象",
                "time": "str"
            }
        ]
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.14 记录运动数据

* 函数体：

```python
def add_exercise_data(self, user_id: int, steps: int, time: str = datetime.now()):
```

* 参数：
```
user_id : 用户ID
steps : 步数
time : 时间(可选)
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "运动数据记录成功",
        "data": {
            "exercise_id": "int"
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```
### 4.5.15 获取运动数据

* 函数体：

```python
def get_exercise_data(self, user_id: int, limit: int = 30):
```

* 参数：
```
topic_id : 话题ID
```

* 返回值：
    * 成功时：
    ```json
    {
        "success": true,
        "message": "运动数据查询成功！",
        "data": {
            "user_id": "int",
            "recent_data": [
                {
                    "id": "int",
                    "date": "str",
                    "steps": "int"
                }
            ],
            "total_steps": "int",
            "avg_daily_steps": "int"
        }
    }
    ```
    * 当失败时：
    ```json
    {
        "success": false,
        "message": "str",          // 错误信息
        "detail": "str"           // 详细情况
    }
    ```