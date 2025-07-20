from services.classes.row_to_class import row_to_post, row_to_topic, row_to_activity, row_to_user
from services.connection.connection import get_database_connection
from services.connection.connection import handle_db_error
from services.classes.post import post
from services.classes.activity import activity
from services.classes.topic import topic
from services.classes.users import user
from datetime import datetime


class activity_service:
    def __init__(self):
        self.connection = get_database_connection()

    def __del__(self):
        if self.connection:
            self.connection.close()

    # 添加新活动
    # 参数列表：
    """
    new_activity : 活动对象
    """
    # 返回值：
    """
    当新增成功时：
    {
        'success': True,
        'message': '新增活动成功！',
        'activity_id': int          # 活动id
    }
    当失败时：
    {
        'success': False,
        'message': ?                # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def add_activity(self, new_activity: activity):
        cursor = self.connection.cursor()
        try:
            query = """
            INSERT INTO activities 
            (title, date, location, calorie, duration, weather, 
             start_place, end_place, time, difficulty, type, image, star_count)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                new_activity.title,
                new_activity.data,
                new_activity.location,
                new_activity.calorie or 0,  # 默认卡路里0
                new_activity.duration or 30,  # 默认时长30分钟
                new_activity.weather or 1,  # 默认天气晴
                new_activity.start_place,
                new_activity.end_place,
                new_activity.time or new_activity.data,  # 默认使用活动日期
                new_activity.difficulty or "中等",  # 默认难度
                new_activity.type or "其他",  # 默认类型
                new_activity.image,
                new_activity.star_count or 0
            ))
            activity_id = cursor.lastrowid
            self.connection.commit()
            return {
                'success': True,
                'message': '新增活动成功！',
                'activity_id': activity_id
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 删除活动
    # 参数列表：
    """
    activity_id : 表示被删除的活动id
    """
    # 返回值
    """
    当删除成功时：
    {
        'success': True,
        'message': '删除成功',
        'data' : {
            'activity_id': activity_id
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?                # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def remove_activity(self, activity_id: int):
        cursor = self.connection.cursor()
        try:
            # 外键约束会自动删除关联数据
            query = "DELETE FROM activities WHERE activity_id = %s"
            cursor.execute(query, (activity_id,))
            self.connection.commit()
            if cursor.rowcount == 0:
                return {
                    'success': False,
                    'message': '删除失败',
                    'detail': '数据库中不存在该活动的记录'
                }
            else:
                return {
                    'success': True,
                    'message': '删除成功',
                    'data' : {
                        'activity_id': activity_id
                    }
                }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 获取分页的数据
    # 参数列表
    """
    page : 第几页
    size : 获取的个数
    """
    # 返回值：
    """
    当查询成功时：
    {
        'success': True,
        'message': '获取成功',
        'data': {
            'activities': [                 # 活动数组
                {
                    'id': int,              # 活动id
                    'activity': activity,   # 活动对象
                    'enroll_count': int     # 报名人数  
                },
                ...
            ]
            'pagination': {                 # 页码相关
                'total': total,             # 总数
                'page': page,               # 哪一页
                'size': size,               # 有多少
                'pages': (total + size - 1) 
            }
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?                # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def get_all_activities(self, page: int = 1, size: int = 10):
        cursor = self.connection.cursor(dictionary=True)
        try:
            # 获取活动总数
            count_query = "SELECT COUNT(*) as total FROM activities"
            cursor.execute(count_query)
            total = cursor.fetchone()['total']

            # 获取分页数据
            query = """
            SELECT a.*, 
                   (SELECT COUNT(*) FROM enroll WHERE activity_id = a.activity_id) as enroll_count
            FROM activities a
            ORDER BY a.date DESC
            LIMIT %s OFFSET %s
            """
            offset = (page - 1) * size
            cursor.execute(query, (size, offset))

            activities = []
            for row in cursor:
                activity_obj = row_to_activity(row)
                activities.append({
                    'id': row['activity_id'],  # 新增返回ID
                    'activity': activity_obj,
                    'enroll_count': row['enroll_count']
                })

            return {
                'success': True,
                'message': '获取成功',
                'data': {
                    'activities': activities,
                    'pagination': {
                        'total': total,
                        'page': page,
                        'size': size,
                        'pages': (total + size - 1) // size
                    }
                }
            }
        except Exception as e:
            return handle_db_error(e)
        finally:
            cursor.close()
    # 获取活动的详细信息
    # 参数列表：
    """
    activity_id : 通过活动id获取详细信息
    """
    # 返回值：
    """
    当查询成功时：
    {
        'success': True,
        'message': '查询成功！',
        'data': {
            'id': int,                      # 帖子id
            'activity': activity,           # 活动对象
            'enroll_count': int,            # 报名人数
            'labels': [                     # 标签数组
                {
                    'id': int,              # 标签id
                    'name': str             # 标签名称
                },
                ...
            ], 
            'related_posts': [              # 关联的帖子数组
                {
                    'id': int,              # 帖子id
                    'title': str,           # 帖子标题
                    'time': str,            # 发布时间
                    'author': str,          # 发布者
                    'author_id': int        # 发布者id
                },
                ...
            ]
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?                # 各种可能的错误信息
        'detail' : ?                # 详细情况
    } 
    """
    def get_detail_activity(self, activity_id: int):
        cursor = self.connection.cursor(dictionary=True)
        try:
            # 获取活动基本信息
            query = """
            SELECT a.*, 
                   (SELECT COUNT(*) FROM enroll WHERE activity_id = a.activity_id) as enroll_count
            FROM activities a
            WHERE a.activity_id = %s
            """
            cursor.execute(query, (activity_id,))
            row = cursor.fetchone()
            if not row:
                return None

            # 获取关联的标签
            label_query = """
            SELECT l.content 
            FROM labels l
            JOIN activity_label al ON l.label_id = al.label_id
            WHERE al.activity_id = %s
            """
            cursor.execute(label_query, (activity_id,))

            # 获取关联的帖子
            post_query = """
            SELECT b.blog_id, b.title, b.post_time, u.name as author_name
            FROM blogs b
            JOIN blog_activity ba ON b.blog_id = ba.blog_id
            JOIN users u ON b.user_id = u.id
            WHERE ba.activity_id = %s
            ORDER BY b.post_time DESC
            LIMIT 5
            """
            cursor.execute(post_query, (activity_id,))

            return {
                'success': True,
                'message': '查询成功！',
                'data': {
                    'id': activity_id,  # 明确返回活动ID
                    'activity': row_to_activity(row),
                    'enroll_count': row['enroll_count'],
                    'labels': [{'id': label['label_id'], 'name': label['content']} for label in cursor],  # 标签增加ID
                    'related_posts': [{
                        'id': post['blog_id'],
                        'title': post['title'],
                        'time': post['post_time'],
                        'author': post['author_name'],
                        'author_id': post['user_id']  # 新增作者ID
                    } for post in cursor]
                }
            }
        except Exception as e:
            return handle_db_error(e)
        finally:
            cursor.close()

    # 修改活动信息
    # 参数列表：
    """
    activity_id : 表示被删除的活动id
    """
    # 返回值：bool类型
    """
    当修改成功时：
    {
        'success': True,
        'message': '修改成功!',
        'data': {
            'activity_id': int      # 返回用户id
        }
    } 
    当失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    } 
    """
    def modify_activity(self, activity_id: int, **kwargs):
        if not kwargs:
            return False

        cursor = self.connection.cursor()
        try:
            # 构建动态更新语句
            set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
            query = f"UPDATE activities SET {set_clause} WHERE activity_id = %s"

            # 执行更新
            values = list(kwargs.values()) + [activity_id]
            cursor.execute(query, values)

            self.connection.commit()
            if cursor.rowcount == 0:
                return {
                    'success': False,
                    'message': '活动不存在',
                    'detail': '数据库中不存在活动相关的记录'
                }
            else:
                return {
                    'success': True,
                    'message': "修改成功",
                    'data': {
                        'activity_id' : activity_id,
                    }
                }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

