from services.connection.connection import get_database_connection
from services.connection.connection import handle_db_error
from services.classes.post import post
from services.classes.activity import activity
from services.classes.topic import topic
from services.classes.users import user
from services.classes.row_to_class import row_to_post, row_to_topic, row_to_activity, row_to_user
from datetime import datetime
import mysql.connector

class user_service:
    def __init__(self):
        self.connection = get_database_connection()

    def __del__(self):
        if self.connection:
            self.connection.close()

    # 添加新用户
    # 参数：
    """
    new_user : 一个user对象
    """
    # 返回值：
    """
    当新增用户成功时：
    {
        'success': True,
        'message': '用户创建成功',
        'data': {
            'user_id': user_id      # 新创建的用户的id
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?                # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def add_user(self, new_user: user):
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
            INSERT INTO users 
            (name, avatar, level, points, days, phone_number, 
             register_time, account, password, open_id, union_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                new_user.name,
                new_user.avatar,
                new_user.level or 1,
                new_user.points or 0,
                new_user.days or 0,
                new_user.phone_number,
                new_user.register_time or datetime.now(),
                new_user.account,
                new_user.password,
                new_user.open_id,
                new_user.union_id
            ))
            user_id = cursor.lastrowid
            self.connection.commit()
            return {
                'success': True,
                'message': '用户创建成功',
                'data': {'user_id': user_id}
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()


    # 移除用户
    # 参数列表：
    """
    user_id : 被删除的用户的id
    """
    # 返回值：
    """
    当新增用户成功时：
    {
        'success': True,
        'message': '用户删除成功',
        'data': {
            'user_id': int          # 被删除的用户的id
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?                # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def remove_user(self, user_id: int):
        cursor = self.connection.cursor()
        try:
            # 外键约束会自动删除关联数据
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            self.connection.commit()
            if cursor.rowcount == 0:
                return {
                    'success': False,
                    'message': '用户不存在！',
                    'detail' : '数据库中未查找到该用户'
                }
            else:
                return {
                    'success': True,
                    'message': '用户删除成功！',
                    'data': {'user_id': user_id}
                }
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            cursor.close()

    # 获取用户的完整信息
    # 参数列表：
    """
    user_id : 需要获取信息的用户的id
    """
    # 返回值：
    """
    成功获取用户信息时：
    {
        'success': True,
        'message': '用户信息查询成功',
        'data': {
            'id' : int,                 # 用户id
            'user': user,               # 用户对象
            'stats': {
                'post_count': int,      # 发帖数
                'activity_count': int,  # 参与活动数
                'bookmark_count': int   # 收藏数
            }
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?                    # 各种可能的错误信息
        'detail' : ?                    # 详细情况
    }
    """
    def get_message(self, user_id: int):
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            row = cursor.fetchone()

            if not row:
                return {'success': False, 'message': '用户不存在', 'detail': '数据库中未查找到相关用户'}

            stats = {
                'post_count': self._get_user_post_count(user_id),
                'activity_count': self._get_user_activity_count(user_id),
                'bookmark_count': self._get_user_bookmark_count(user_id)
            }

            return {
                'success': True,
                'message': '用户信息查询成功',
                'data': {
                    'id' : user_id,
                    'user': row_to_user(row),
                    'stats': stats
                }
            }
        except Exception as e:
            return handle_db_error(e)
        finally:
            cursor.close()

    # 更新用户信息
    # 参数列表：
    """
    user_id : 需要获取信息的用户的id
    name : 用户的新名字
    avatar ： 新头像的地址
    """
    # 返回值：
    """
    当新增用户成功时：
    {
        'success': True,
        'message': '用户删除成功',
        'data': {
            'user_id': int          # 被更新的用户的id
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?                # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def update_user(self, user_id: int, name: str, avatar: str):
        cursor = self.connection.cursor()
        try:
            query = "UPDATE users SET name = %s, avatar = %s WHERE id = %s"
            cursor.execute(query, (name, avatar, user_id))
            self.connection.commit()
            if cursor.rowcount == 0:
                return {
                    'success': False,
                    'message': '用户不存在！',
                    'detail': '数据库中未查找到相关用户'
                }
            else:
                return {
                    'success': True,
                    'message': '用户信息更新成功成功！',
                    'data': {'user_id': user_id}
                }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 用户报名活动
    # 参数列表：
    """
    user_id : 用户id
    activity_id : 活动id
    """
    # 返回值：
    """
    当用户报名成功时：
    {
        'success': True,
        'message': '用户删除成功',
        'data': {
            'user_id': int,         # 用户id
            'activity_id': int,     # 活动id
            'enroll_time': str      # 报名时间
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?                # 各种可能的错误信息
        'detail': ?                 # 详细情况
    }
    """
    def register_activity(self, user_id: int, activity_id: int):
        cursor = self.connection.cursor()
        try:
            # 检查是否已报名
            check_query = """
            SELECT 1 FROM enroll 
            WHERE user_id = %s AND activity_id = %s
            """
            cursor.execute(check_query, (user_id, activity_id))
            if cursor.fetchone():
                return {
                'success': False,
                'message': '用户已经报名！',
                'detail' : '数据库中已经存在报名记录！'
            }
            time = datetime.now()
            # 报名活动
            enroll_query = """
            INSERT INTO enroll 
            (user_id, activity_id, enroll_time)
            VALUES (%s, %s, %s)
            """
            cursor.execute(enroll_query, (user_id, activity_id, time))

            # 添加到用户活动关联表
            user_activity_query = """
            INSERT INTO user_activity 
            (user_id, activity_id, status)
            VALUES (%s, %s, '未开始')
            ON DUPLICATE KEY UPDATE status = '未开始'
            """
            cursor.execute(user_activity_query, (user_id, activity_id))

            self.connection.commit()
            return {
                'success': True,
                'message': '用户报名成功！',
                'data' : {'user_id': user_id, 'activity_id': activity_id, 'enroll_time' : time}
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 取消报名
    # 参数列表：
    """
    user_id : 用户id
    activity_id : 活动id
    """
    # 返回值：
    """
    当成功取消报名时：
    {
        'success': True,
        'message': '取消报名成功',
        'data' : {
            'user_id': int          # 用户id
            'activity_id': int      # 活动id
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误
        'detail': ?                 # 详细信息
    }
    """
    def cancel_registration(self, user_id: int, activity_id: int):
        cursor = self.connection.cursor()
        try:
            # 1. 检查是否已报名
            check_query = """
            SELECT 1 FROM enroll 
            WHERE user_id = %s AND activity_id = %s
            """
            cursor.execute(check_query, (user_id, activity_id))
            if not cursor.fetchone():
                return {
                    'success': False,
                    'message': '用户未报名该活动',
                    'detail': '数据库中未查找到报名记录'
                }

            # 2. 从报名表中删除记录
            delete_enroll_query = """
            DELETE FROM enroll 
            WHERE user_id = %s AND activity_id = %s
            """
            cursor.execute(delete_enroll_query, (user_id, activity_id))

            # 3. 更新用户活动状态
            update_status_query = """
            UPDATE user_activity
            SET status = '已取消'
            WHERE user_id = %s AND activity_id = %s
            """
            cursor.execute(update_status_query, (user_id, activity_id))

            self.connection.commit()

            return {
                'success': True,
                'message': '取消报名成功',
                'data' : {
                    'user_id': user_id,
                    'activity_id': activity_id      # 活动id
                }
            }

        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 收藏活动
    # 参数：
    """
    user_id : 用户id
    activity_id : 活动id
    """
    # 返回值：
    """
    当收藏成功时：
    {
        'success': True,
        'message': '活动收藏成功',
        'data' : {
            'user_id': user_id,         # 用户id
            'activity_id': activity_id  # 活动id
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误
        'detail': ?                 # 详细信息
    }
    """
    def bookmark_activity(self, user_id: int, activity_id: int):
        cursor = self.connection.cursor(dictionary=True)
        try:
            # 1. 检查是否已收藏
            check_query = """
            SELECT * FROM star_activities 
            WHERE user_id = %s AND activity_id = %s
            """
            cursor.execute(check_query, (user_id, activity_id))
            existing = cursor.fetchone()

            if existing:
                return {
                    'success': False,
                    'message': '该活动已被收藏',
                    'detail': '数据库中已查找到相关的收藏记录！'
                }

            # 2. 添加收藏记录
            insert_query = """
            INSERT INTO star_activities 
            (user_id, activity_id)
            VALUES (%s, %s)
            """
            cursor.execute(insert_query, (user_id, activity_id))

            # 3. 更新活动收藏数
            update_query = """
            UPDATE activities 
            SET star_count = star_count + 1 
            WHERE activity_id = %s
            """
            cursor.execute(update_query, (activity_id,))

            self.connection.commit()

            return {
                'success': True,
                'message': '活动收藏成功',
                'data' : {
                    'user_id': user_id,
                    'activity_id': activity_id
                }
            }

        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 获取用户参与的所有活动
    # 参数列表：
    """
    user_id : 需要获取信息的用户的id
    """
    # 返回值：
    """
    当查询成功时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误
        'data' : [
            {
                'id': int,              # 活动id
                'activity': activity,   # 活动对象
                'status': str           # 状态
            },
            ...
        ]
    }
    当查询失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误
        'detail': ?                 # 详细信息
    }
    """
    def get_activities(self, user_id: int):
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
            SELECT a.*, ua.status 
            FROM activities a
            JOIN user_activity ua ON a.activity_id = ua.activity_id
            WHERE ua.user_id = %s
            ORDER BY a.date DESC
            """
            cursor.execute(query, (user_id,))
            return {
                'success': True,
                'message': "成功获取活动!",
                'data' : [{
                    'id': row['activity_id'],
                    'activity': row_to_activity(row),
                    'status': row['status']
                } for row in cursor]
            }
        except Exception as e:
            return handle_db_error(e)
        finally:
            cursor.close()

    # 获取用户收藏的帖子
    # 参数列表：
    """
    user_id : 需要获取信息的用户的id
    """
    # 返回值：list类型
    """
    当查询成功时：
    {
        'success': True,
        'message': '',
        'data' : [
            {
                'id': int,      # 帖子id
                'post': post    # 帖子对象
            },
            ...
        ]
    }
    当失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误
        'detail': ?                 # 详细信息
    }
    """
    def get_bookmark_posts(self, user_id: int):
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
            SELECT b.*
            FROM blogs b
            JOIN user_star_blogs usb ON b.blog_id = usb.blog_id
            WHERE usb.user_id = %s
            ORDER BY b.post_time DESC
            """
            cursor.execute(query, (user_id,))
            return {
                'success': True,
                'message': '',
                'data' : [{
                    'id': row['blog_id'],  # 帖子ID
                    'post': row_to_post(row)
                } for row in cursor]
            }
        except Exception as e:
            return handle_db_error(e)
        finally:
            cursor.close()

    # 获取用户收藏的活动
    # 参数列表：
    """
    user_id : 需要获取信息的用户的id
    """
    # 返回值：list类型
    """
    当查询成功时：
    {
        'success': True,
        'message': '活动查询成功',
        'data' : [
            {
                'id': int,              # 用户id
                'activity': activity    # 活动id
            },
            ...
        ]
    }
    当失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误
        'detail': ?                 # 详细信息
    }
    """
    def get_bookmark_activities(self, user_id: int):
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
            SELECT a.*
            FROM activities a
            JOIN star_activities sa ON a.activity_id = sa.activity_id
            WHERE sa.user_id = %s
            ORDER BY a.date DESC
            """
            cursor.execute(query, (user_id,))
            return {
                'success': True,
                'message': '活动查询成功',
                'data' : [{
                    'id': row['activity_id'],
                    'activity': row_to_activity(row)
                } for row in cursor]
            }
        except Exception as e:
            return handle_db_error(e)
        finally:
            cursor.close()

    # 取消收藏活动
    # 参数:
    """
        user_id: 用户ID
        activity_id: 活动ID
    """
    # 返回值:
    """
    当操作成功时：
    {
        'success': True,
        'message': '已取消收藏活动',
        'data' : {
            'user_id': user_id,
            'activity_id': activity_id
        }
    }
    当操作失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误
        'detail': ?                 # 详细信息
    }
    """
    def unbookmark_activity(self, user_id: int, activity_id: int):
        cursor = self.connection.cursor()
        try:
            # 1. 检查是否已收藏
            check_query = """
            SELECT * FROM star_activities 
            WHERE user_id = %s AND activity_id = %s
            """
            cursor.execute(check_query, (user_id, activity_id))
            if not cursor.fetchone():
                return {
                    'success': False,
                    'message': '该活动未被收藏',
                    'detail': '数据库中未找到活动被该用户收藏的记录'
                }

            # 2. 移除收藏记录
            delete_query = """
            DELETE FROM star_activities 
            WHERE user_id = %s AND activity_id = %s
            """
            cursor.execute(delete_query, (user_id, activity_id))

            # 3. 更新活动收藏数
            update_query = """
            UPDATE activities 
            SET star_count = GREATEST(0, star_count - 1) 
            WHERE activity_id = %s
            """
            cursor.execute(update_query, (activity_id,))

            self.connection.commit()

            return {
                'success': True,
                'message': '已取消收藏活动',
                'data' : {
                    'user_id': user_id,
                    'activity_id': activity_id
                }
            }

        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 获取用户发布的贴子
    # 参数列表：
    """
    user_id : 需要获取信息的用户的id
    """
    # 返回值：
    """
    当操作成功时：
    {
        'success': True,
        'message': '获取帖子成功！',
        'data' : [
            {
                'id': int,          # 帖子id
                'post': post,       # 帖子对象
                'author_info': {    # 发布者信息
                    'id': int,      # 发布者id
                    'name': str     # 发布者昵称
                }
            },
            ...
        ]
    }
    当操作失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误
        'detail': ?                 # 详细信息
    }
    """
    def get_publish_posts(self, user_id: int):
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
            SELECT b.*, u.name as author_name
            FROM blogs b
            LEFT JOIN users u ON b.user_id = u.id
            WHERE b.user_id = %s
            ORDER BY b.post_time DESC
            """
            cursor.execute(query, (user_id,))
            return {
                'success': True,
                'message': '获取帖子成功！',
                'data' : [{
                    'id': row['blog_id'],  # 帖子ID
                    'post': row_to_post(row),
                    'author_info': {
                        'id': row['user_id'],  # 作者ID
                        'name': row['author_name']
                    }
                } for row in cursor]
            }
        except Exception as e:
            return handle_db_error(e)
        finally:
            cursor.close()

    # 获取用户报名的活动
    # 参数列表：
    """
    user_id : 需要获取信息的用户的id
    """
    # 返回值：
    """
    当查询成功时：
    {
        'success': True,
        'message' : '查询活动成功',
        'data' : [
            {
                'id': int,              # 用户id
                'activity': activity,   # 活动id
                'time' : str            # 报名时间
            },
            ...
        ]
    }
    当失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误
        'detail': ?                 # 详细信息
    }
    """
    def get_register_activity(self, user_id: int):
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
            SELECT a.*, e.enroll_id, e.enroll_time 
            FROM activities a
            JOIN enroll e ON a.activity_id = e.activity_id
            WHERE e.user_id = %s
            ORDER BY e.enroll_time DESC
            """
            cursor.execute(query, (user_id,))
            return {
                'success': True,
                'message' : '查询活动成功',
                'data' : [{
                    'id': row['activity_id'],  # 活动ID
                    'activity': row_to_activity(row),
                    'time': row['enroll_time']
                } for row in cursor]
            }
        except Exception as e:
            return handle_db_error(e)
        finally:
            cursor.close()

    # 记录用户运动数据
    # 参数:
    """
    user_id: 用户ID
    steps: 运动步数
    time : 运动时间
    """
    # 返回值：
    """
    当添加成功时：
    {
        'success': True,
        'message': '运动数据记录成功',
        'data' : {
            'exercise_id': exercise_id, # 运动数据记录id
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误
        'detail': ?                 # 详细信息
    }   
    """
    def add_exercise_data( self, user_id: int, steps: int, time : str = datetime.now()):

        cursor = self.connection.cursor(dictionary=True)
        try:
            insert_query = """
            INSERT INTO exercise_data 
            (user_id, time, step)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (
                user_id,
                time,
                steps,
            ))
            exercise_id = cursor.lastrowid

            self.connection.commit()

            return {
                'success': True,
                'message': '运动数据记录成功',
                'data' : {
                    'exercise_id': exercise_id,
                }
            }

        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 获取用户的运动数据统计
    # 参数列表：
    """
    user_id : 需要获取信息的用户的id
    limit : 获取用户最近limit天的运动数据
    """
    # 返回值：
    """
    当查询成功时：
    {
        'success': True,
        'message': '运动数据查询成功！',
        'data': {
            'user_id': int,         # 用户id
            'recent_data': [        # 用户的运动数据
                {
                    'id': int,      # 运动数据id
                    'date': str,    # 日期
                    'steps': int    # 步数
                },
                ...
            ]
            'total_steps': int,     # 总运动步数
            'avg_daily_steps': int  # 平均运动步数
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误
        'detail': ?                 # 详细信息
    }   
    """
    def get_exercise_data(self, user_id: int, limit: int = 30):
        cursor = self.connection.cursor(dictionary=True)
        try:
            # 获取最近limit天数据
            query = """
            SELECT exercise_id, time, step 
            FROM exercise_data 
            WHERE user_id = %s 
            ORDER BY time DESC 
            LIMIT %s
            """
            cursor.execute(query, (user_id, limit))
            recent_data = [{
                'id': row['exercise_id'],  # 运动记录ID
                'date': row['time'],
                'steps': row['step']
            } for row in cursor]

            # 获取总步数
            query = "SELECT SUM(step) as total_steps FROM exercise_data WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            total = cursor.fetchone()
            total_steps = total['total_steps'] or 0 if total else 0

            return {
                'success': True,
                'message': '运动数据查询成功！',
                'data': {
                    'user_id': user_id,  # 用户ID
                    'recent_data': recent_data,
                    'total_steps': total_steps,
                    'avg_daily_steps': total_steps // limit if recent_data else 0
                }
            }
        except Exception as e:
            return handle_db_error(e)
        finally:
            cursor.close()

    # 获取用户发帖数
    def _get_user_post_count(self, user_id: int) -> int:
        cursor = self.connection.cursor()
        try:
            query = "SELECT COUNT(*) FROM blogs WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            return cursor.fetchone()[0]
        finally:
            cursor.close()

    # 获取用户关联活动数
    def _get_user_activity_count(self, user_id: int) -> int:
        cursor = self.connection.cursor()
        try:
            query = "SELECT COUNT(*) FROM user_activity WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            return cursor.fetchone()[0]
        finally:
            cursor.close()

    # 获取用户收藏数
    def _get_user_bookmark_count(self, user_id: int) -> int:
        cursor = self.connection.cursor()
        try:
            query = """
            SELECT (
                (SELECT COUNT(*) FROM user_star_blogs WHERE user_id = %s) +
                (SELECT COUNT(*) FROM star_activities WHERE user_id = %s)
            ) AS total
            """
            cursor.execute(query, (user_id, user_id))
            return cursor.fetchone()[0]
        finally:
            cursor.close()